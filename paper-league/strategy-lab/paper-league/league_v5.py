#!/usr/bin/env python3
"""data-isolation v1 engine wrapper (data-handling rule only; no risk, sizing or strategy change).
If one symbol's public snapshot fails its data check, only books that trade that symbol skip the tick:
no fills, no stop moves, cursor not advanced, skip appended to data-gaps.jsonl, open positions on the
symbol reported stale in heartbeat.json. Every other book runs its own frozen v1/v2/v3/v4 code.
No candle is fabricated or forward-filled. The 60s no-stale-fill and minute-boundary rules are unchanged.
Public /info reads only; no wallet, key, order, signing, testnet or exchange write.
"""
import argparse
import contextlib
import copy
import fcntl
import gzip
import json
import math
import os
import resource
import signal as signals
import time
from collections import Counter
import league as L
import league_v2 as V
import league_v3 as V3
import league_v4 as V4
import strategies as S
import strategies_v2 as S2
import strategies_v3 as S3
import evaluation_v3 as E

ROOT = L.ROOT
RUNNING = True
RULE_ID = 'data-isolation-v1'
FLAG_RATE = .5
FLAG_MIN_TICKS = 30
WINDOW_MS = 24*S.HOUR

def registration(root=ROOT):
    old, ext, spot, v4 = V4.registration(root)
    di = L.read_json(root/'registry/data-isolation-v1.json')
    if di.get('mode') != 'PAPER_ONLY' or di.get('rule_id') != RULE_ID: raise ValueError('data-isolation v1 registration required')
    if L.sha(root/'registry/data-isolation-v1.md') != di['rule_sha256']: raise ValueError('data-isolation v1 rule changed')
    if di['extension_v4_sha256'] != L.sha(root/'registry/extension-v4.json'): raise ValueError('v4 extension changed')
    for n, d in di['implementation_sha256'].items():
        if L.sha(root/n) != d: raise ValueError(f'frozen data-isolation implementation changed: {n}')
    return old, ext, spot, v4, di

def book_symbols(b, v1_ids):
    if b['id'] in v1_ids: return {'BTC'} if b['kind'] == 'benchmark' else set(S.COINS)
    if 'spot_spec' in b: return set(b['spot_spec']['coins'])
    if 'spot4_spec' in b: return set(b['spot4_spec']['coins'])
    if 'spec4' in b:
        s = b['spec4']; out = set(s['coins'])
        if s['kind'] == 'ratio_mr': out |= {s['params']['numerator'], s['params']['denominator']}
        if s['kind'] == 'xs_momentum': out |= set(S.COINS)
        return out
    if 'spec' in b: return set(b['spec']['coins'])
    raise ValueError(f"unknown book family {b['id']}")

@contextlib.contextmanager
def universe(perp, spot):
    """Temporarily restrict the frozen engines' symbol loops to healthy symbols (order preserved)."""
    saved = (L.COINS, S.COINS, S2.COINS, S3.SPOT_COINS)
    try:
        L.COINS = S.COINS = S2.COINS = tuple(c for c in saved[0] if c in perp)
        S3.SPOT_COINS = tuple(c for c in saved[3] if c in spot)
        yield
    finally:
        L.COINS, S.COINS, S2.COINS, S3.SPOT_COINS = saved

class PublicData(V3.PublicData):
    """Same requests and per-symbol checks as the frozen v3 collector, but a failing symbol is recorded
    in d['failed'] instead of failing every book. Global reads (contexts, allMids) and the 60s /
    minute-boundary rules still fail the whole tick."""
    def fetch(self, st, now):
        for key in list(V.KEYS.values())+['spot_m1', 'spot_m5', 'spot_m15', 'spot_h1']:
            self.cache.setdefault(key, {})
        failed = {}
        meta, contexts = self.request(dict(type='metaAndAssetCtxs'))
        ctx = {u['name']: dict(szDecimals=u['szDecimals'], maxLeverage=u['maxLeverage'],
               **{k: float(v[k]) for k in ('funding', 'markPx', 'oraclePx')})
               for u, v in zip(meta['universe'], contexts) if u['name'] in S.COINS}
        if set(ctx) != set(S.COINS): raise ValueError('invalid context')
        verify = self.cache.get('spot_meta_ms', 0) == 0 or now-self.cache.get('spot_meta_ms', 0) >= 15*S3.MINUTE
        if verify:
            spot_raw = self.request(dict(type='spotMetaAndAssetCtxs'))
            tokens = {t['index']: t for t in spot_raw[0]['tokens']}
            by_coin = {c.get('coin'): c for c in spot_raw[1] if isinstance(c, dict) and c.get('coin')}
            for name, mkt in S3.SPOT_MARKETS.items():
                raw = by_coin.get(mkt['api_coin'])
                if not raw: failed[name] = f"missing spot context {mkt['api_coin']}"; continue
                token = tokens[mkt['token_index']]
                if token['name'] != mkt['token_name'] or int(token['szDecimals']) != int(mkt['szDecimals']):
                    failed[name] = 'spot token identity changed'
            if not failed: self.cache['spot_meta_ms'] = now
        spot_ctx = {name: dict(szDecimals=int(m['szDecimals']), api_coin=m['api_coin'], pair=m['pair'], price_source='spot_pair', maxLeverage=1)
                    for name, m in S3.SPOT_MARKETS.items()}
        d = dict(ctx=ctx, spot_ctx=spot_ctx, minutes={}, funding={}, books={}, fourhour={}, daily={},
                 m1={}, m5={}, m15={}, h1={}, spot_books={}, spot_minutes={}, spot_m1={}, spot_m5={}, spot_m15={}, spot_h1={})
        last_closed = now//S3.MINUTE*S3.MINUTE
        for c in S.COINS:
            try:
                cached = self.cache['m1'].get(c, [])
                start = min(st['next_minute'], cached[-1]['t'] if cached else last_closed-250*S3.MINUTE)
                new = self.candles(c, '1m', start, now)
                merged = {r['t']: r for r in cached}; merged.update({r['t']: r for r in new if r['t']+S3.MINUTE <= now})
                rows = [merged[t] for t in sorted(merged)]; m1 = rows[-512:]
                if len(m1) < 250 or any(b['t']-a['t'] != S3.MINUTE for a, b in zip(m1, m1[1:])) or rows[-1]['t']+S3.MINUTE != last_closed:
                    raise ValueError(f'{c} 1m warmup/continuity missing')
                part = dict(minutes=[r for r in rows if r['t'] >= st['next_minute']], m1=m1)
                for interval, key, count in [('5m', 'm5', 250), ('15m', 'm15', 250), ('1h', 'h1', 250), ('4h', 'fourhour', 710), ('1d', 'daily', 250)]:
                    part[key] = self.history(key, c, interval, count, now)
                part['funding'] = self.funding(c, min(st['next_minute']-S3.HOUR, now-48*S3.HOUR), now)
                self.cache['m1'][c] = m1
                for k, v in part.items(): d[k][c] = v
            except Exception as e:
                failed[c] = repr(e)
        for name, mkt in S3.SPOT_MARKETS.items():
            if name in failed: continue
            try:
                api = mkt['api_coin']; cached = self.cache['spot_m1'].get(name, [])
                start = min(st['next_minute'], cached[-1]['t'] if cached else last_closed-250*S3.MINUTE)
                new = self.candles(api, '1m', start, now)
                merged = {r['t']: r for r in cached}; merged.update({r['t']: r for r in new if r['t']+S3.MINUTE <= now})
                rows = [merged[t] for t in sorted(merged)]; m1 = rows[-512:]
                if len(m1) < 250 or any(b['t']-a['t'] != S3.MINUTE for a, b in zip(m1, m1[1:])) or rows[-1]['t']+S3.MINUTE != last_closed:
                    raise ValueError(f'{name} spot 1m warmup/continuity missing')
                part = dict(spot_minutes=[r for r in rows if r['t'] >= st['next_minute']], spot_m1=m1)
                for interval, key, count in [('5m', 'spot_m5', 250), ('15m', 'spot_m15', 250), ('1h', 'spot_h1', 250)]:
                    part[key] = self._spot_history(key, name, api, interval, count, now)
                self.cache['spot_m1'][name] = m1
                for k, v in part.items(): d[k][name] = v
            except Exception as e:
                failed[name] = repr(e)
        if now%(4*S3.HOUR) <= 120000 or now%S3.DAY <= 120000:
            for c in S.COINS:
                if c in failed: continue
                try:
                    raw = self.request(dict(type='l2Book', coin=c))
                    if abs(L.sc.now_ms()-int(raw['time'])) > 120000: raise ValueError('stale L2')
                    d['books'][c] = dict(bids=[(float(x['px']), float(x['sz'])) for x in raw['levels'][0]], asks=[(float(x['px']), float(x['sz'])) for x in raw['levels'][1]])
                except Exception as e: failed[c] = repr(e)
        if now%(15*S3.MINUTE) <= 120000:
            for name, mkt in S3.SPOT_MARKETS.items():
                if name in failed: continue
                try:
                    raw = self.request(dict(type='l2Book', coin=mkt['api_coin']))
                    if abs(L.sc.now_ms()-int(raw['time'])) > 120000: raise ValueError('stale spot L2')
                    d['spot_books'][name] = dict(bids=[(float(x['px']), float(x['sz'])) for x in raw['levels'][0]], asks=[(float(x['px']), float(x['sz'])) for x in raw['levels'][1]])
                except Exception as e: failed[name] = repr(e)
        raw = self.request(dict(type='allMids')); observed = L.sc.now_ms()
        d['mids'] = {}
        for c in S.COINS:
            px = float(raw.get(c, 'nan'))
            if px > 0 and math.isfinite(px): d['mids'][c] = px
            else: failed.setdefault(c, 'invalid mid')
        for name, mkt in S3.SPOT_MARKETS.items():
            px = float(raw.get(mkt['api_coin'], 'nan'))
            if px > 0 and math.isfinite(px): d['mids'][name] = px
            else: failed.setdefault(name, 'invalid spot mid')
        # Unchanged global rules: no stale fills.
        if observed-now > S3.MINUTE: raise ValueError('snapshot collection exceeded 60s; no stale fills')
        if now//S3.MINUTE != observed//S3.MINUTE: raise ValueError('snapshot crossed minute boundary; retry current data, no hindsight fills')
        d['observed_ms'] = observed; d['failed'] = failed
        source = self.root/'sources'/f'{now}.json.gz'; source.parent.mkdir(exist_ok=True)
        with gzip.open(source, 'wt') as f:
            json.dump(dict(network='mainnet_public_read_only', asof_utc=L.utc(observed), failed_symbols=failed, requests=self.requests), f)
        L.atomic(self.path, self.cache)
        counts = Counter(r['request']['type'] for r in self.requests)
        d['evidence'] = dict(path=str(source.relative_to(self.root)), sha256=L.sha(source), received_ms=observed,
             requests=len(self.requests), request_types=dict(counts), estimated_weight=self.weight,
             collection_seconds=round(time.monotonic()-self.collect_started, 4), failed_symbols=sorted(failed))
        return d

def replay_data(data, start, perp, spot):
    """Real 1m candles from the (contiguity-checked) 512-bar window, from a book's own cursor."""
    d = dict(data); d['minutes'] = {}; d['spot_minutes'] = {}
    for c in perp:
        rows = data['m1'][c]
        if rows[0]['t'] > start: return None
        d['minutes'][c] = [r for r in rows if r['t'] >= start]
    for c in spot:
        rows = data['spot_m1'][c]
        if rows[0]['t'] > start: return None
        d['spot_minutes'][c] = [r for r in rows if r['t'] >= start]
    return d

def run_group(st, books, data, now, start, old_ids, perp, spot):
    view = dict(st, books={b['id']: b for b in books}, next_minute=start)
    v1 = dict(view, books={k: b for k, b in view['books'].items() if k in old_ids})
    with universe(perp, spot):
        if v1['books']: L.apply_tick(v1, data, now)
        c2 = V.apply_new(view, data, now, start)
        c3 = V3.apply_spot(view, data, now, start)
        c4 = V4.apply_perp4(view, data, now, start)+V4.apply_spot4(view, data, now, start)
    return c2, c3, c4

def apply_tick(st, data, now, old):
    start = st['next_minute']; end = now//S.MINUTE*S.MINUTE
    failed = set(data.get('failed', {}))
    perp = [c for c in S.COINS if c not in failed]; spot = [c for c in S3.SPOT_COINS if c not in failed]
    old_ids = {s['id'] for s in old['strategies']}
    E.initialize(st, now)
    groups = {}; skipped = {}
    for b in st['books'].values():
        syms = book_symbols(b, old_ids); bad = sorted(syms & failed)
        cursor = b.get('di_cursor', start)
        if bad: skipped[b['id']] = dict(symbols=bad, cursor=cursor, reason='symbol_failed_data_check'); continue
        groups.setdefault(cursor, []).append(b)
    totals = [0, 0, 0]
    for cursor in sorted(groups):
        books = groups[cursor]
        d = data if cursor == start else replay_data(data, cursor, perp, spot)
        if d is None:
            for b in books: skipped[b['id']] = dict(symbols=[], cursor=cursor, reason='replay_window_exceeded_needs_review')
            continue
        trial = copy.deepcopy(books)
        try:
            cs = run_group(st, trial, d, now, cursor, old_ids, perp, spot)
        except ValueError as e:
            if cursor == start: raise  # healthy-cursor failures still fail the tick closed, as before
            for b in books: skipped[b['id']] = dict(symbols=[], cursor=cursor, reason=f'replay_failed: {e}')
            continue
        for b in trial:
            b.pop('di_cursor', None); st['books'][b['id']] = b
        totals = [x+y for x, y in zip(totals, cs)]
    for bid, info in skipped.items():
        st['books'][bid]['di_cursor'] = info['cursor']
    st.update(next_minute=end, last_tick_ms=now, ticks=st['ticks']+1)
    E.update(st, now)
    di = st.setdefault('data_isolation', dict(rule_id=RULE_ID, history=[]))
    di['history'] = [h for h in di['history'] if h[0] > now-WINDOW_MS]+[[now, sorted(failed)]]
    stale = [dict(book=bid, trade_id=p['id'], coin=p['coin'], side=p['side'], stop=p.get('stop'),
                  last_cursor_utc=L.utc(info['cursor']), market=st['books'][bid].get('market', 'perp'))
             for bid, info in skipped.items() for p in st['books'][bid]['positions'].values()]
    n = len(di['history'])
    rates = {c: sum(c in h[1] for h in di['history'])/n for c in list(S.COINS)+list(S3.SPOT_COINS)}
    flags = [dict(symbol=c, fail_rate_24h=round(r, 4), ticks=n, note='>50% of ticks failed data check over trailing 24h; review symbol')
             for c, r in rates.items() if r > FLAG_RATE and n >= FLAG_MIN_TICKS]
    summary = dict(rule_id=RULE_ID, failed_symbols=data.get('failed', {}), skipped_books=sorted(skipped),
                   skipped_detail=skipped, stale_positions=stale, fail_rate_24h={c: round(r, 4) for c, r in rates.items()},
                   window_ticks=n, review_flags=flags)
    return tuple(totals), summary

def log_skip(root, now, tick, summary):
    if not summary['skipped_books']: return
    rec = dict(event='data_isolation_skip', rule_id=RULE_ID, recorded_ms=now, recorded_myt=L.sc.myt(now), recorded_utc=L.utc(now),
               tick=tick, failed_symbols=summary['failed_symbols'], skipped_books=summary['skipped_books'],
               skip_reasons=sorted({v['reason'] for v in summary['skipped_detail'].values()}),
               stale_positions=summary['stale_positions'], fills_backfilled=False, candles_fabricated=False,
               note='Skipped books: no fills, no stop moves, cursor not advanced. Other books ticked normally.')
    with open(root/'data-gaps.jsonl', 'a') as f: f.write(json.dumps(rec)+'\n')

def tick(root=ROOT):
    start = time.monotonic(); cpu = time.process_time(); old, ext, spot, v4, di = registration(root); began = L.sc.now_ms()
    st = L.read_json(root/'league_state.json')
    if st.get('registration_sha256') != L.sha(root/'registry/manifest.json'): raise ValueError('original state manifest digest changed')
    candidate = copy.deepcopy(st)
    V4.extend(candidate, old, ext, spot, v4, began, L.sha(root/'registry/extension-v2.json'),
              L.sha(root/'registry/spot-extension-v3.json'), L.sha(root/'registry/extension-v4.json'))
    if 'data_isolation_effective_ms' not in candidate:
        candidate.update(data_isolation_effective_ms=began, data_isolation_rule_sha256=di['rule_sha256'])
    elif candidate['data_isolation_rule_sha256'] != di['rule_sha256']: raise ValueError('persisted data-isolation rule mismatch')
    data = PublicData(root).fetch(candidate, began); now = data['observed_ms']
    (c2, c3, c4), summary = apply_tick(candidate, data, now, old)
    candidate['last_evidence'] = data['evidence']
    load = dict(max_rss_mb=round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2), cpu_seconds=round(time.process_time()-cpu, 4),
                wall_seconds=round(time.monotonic()-start, 4), signal_computations=c2, spot_signal_computations=c3, v4_signal_computations=c4,
                **{k: data['evidence'][k] for k in ('requests', 'request_types', 'estimated_weight', 'collection_seconds')})
    candidate['last_load'] = load
    L.atomic(root/'league_state.json', candidate); V4.export(candidate, root)
    log_skip(root, now, candidate['ticks'], summary)
    result = dict(status='ok', mode='PAPER_ONLY', engine_version=5, tick=candidate['ticks'], ts_myt=L.sc.myt(now), ts_utc=L.utc(now),
        book_count=len(candidate['books']), trial_count=E.PRIOR_TRIALS+len(candidate['books']), evidence=data['evidence'], load=load,
        data_isolation={k: v for k, v in summary.items() if k != 'skipped_detail'},
        candidates=[b['id'] for b in candidate['books'].values() if b['evaluation']['status'] == 'CANDIDATE_REVIEW_ONLY'],
        books={b['id']: dict(equity=round(L.sc.equity(b), 8), positions=len(b['positions']), closed_trades=len(b['closed_trades']),
                             starting_equity=b.get('starting_equity', 100.), market=b.get('market', 'perp'),
                             skipped=b['id'] in summary['skipped_books']) for b in candidate['books'].values()})
    L.atomic(root/'last_tick.json', result)
    if not (root/'first-live-tick-v5.json').exists(): L.atomic(root/'first-live-tick-v5.json', result)
    return result

def stop(*_):
    global RUNNING
    RUNNING = False

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--once', action='store_true'); args = ap.parse_args()
    with open(ROOT/'.engine.lock', 'a') as lock:
        try: fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print('another league engine holds the lock', flush=True); return 0
        if args.once: print(json.dumps(tick(), indent=2)); return 0
        (ROOT/'engine.pid').write_text(str(os.getpid())); signals.signal(signals.SIGTERM, stop); signals.signal(signals.SIGINT, stop)
        while RUNNING:
            start = time.monotonic(); L.heartbeat(ROOT, 'fetching', engine_version=5)
            try:
                r = tick(); di = r['data_isolation']
                L.heartbeat(ROOT, 'ok' if not di['skipped_books'] else 'ok_partial_data_isolation', engine_version=5,
                            last_success_ms=L.sc.now_ms(), tick=r['tick'], book_count=r['book_count'], load=r['load'],
                            failed_symbols=di['failed_symbols'], skipped_books=len(di['skipped_books']),
                            stale_positions=di['stale_positions'], fail_rate_24h=di['fail_rate_24h'],
                            review_flags=di['review_flags'], alert=bool(di['review_flags']))
                print(json.dumps({k: v for k, v in r.items() if k != 'books'}), flush=True)
            except Exception as e:
                L.heartbeat(ROOT, 'ERROR_NO_NEW_RISK', engine_version=5, error=repr(e)); print(f'{L.sc.myt()} ERROR_NO_NEW_RISK {e!r}', flush=True); return 1
            while RUNNING and time.monotonic()-start < 60: time.sleep(.5)
        L.heartbeat(ROOT, 'stopped', engine_version=5); return 0

if __name__ == '__main__': raise SystemExit(main())
