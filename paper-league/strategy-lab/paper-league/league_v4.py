#!/usr/bin/env python3
"""Append-only v4 research-sweep PAPER expansion (9 books). v1/v2/v3 files, rules and running books
stay byte-identical and execute their own frozen code. Same public /info collector as v3 (no new
request types). No wallet, key, order, signing, testnet or exchange write.
"""
import argparse
import copy
import fcntl
import json
import os
import resource
import signal as signals
import time
import league as L
import league_v2 as V
import league_v3 as V3
import strategies as S
import strategies_v3 as S3
import strategies_v4 as S4
import evaluation_v3 as E

ROOT = L.ROOT
RUNNING = True
V4_BOOKS = 9
TOTAL_BOOKS = 125

def registration(root=ROOT):
    old, ext, spot = V3.registration(root)
    v4 = L.read_json(root/'registry/extension-v4.json')
    if v4.get('mode') != 'PAPER_ONLY' or len(v4['strategies']) != V4_BOOKS:
        raise ValueError('9 append-only PAPER v4 registrations required')
    if v4['spot_extension_v3_sha256'] != L.sha(root/'registry/spot-extension-v3.json'):
        raise ValueError('v3 spot extension changed')
    if v4['extension_v2_sha256'] != L.sha(root/'registry/extension-v2.json'):
        raise ValueError('v2 extension changed')
    if v4['original_manifest_sha256'] != L.sha(root/'registry/manifest.json'):
        raise ValueError('original registration changed')
    for n, d in v4['implementation_sha256'].items():
        if L.sha(root/n) != d: raise ValueError(f'frozen v4 implementation changed: {n}')
    for s in v4['strategies']:
        if L.sha(root/'registry'/f"{s['id']}.md") != s['sha256']:
            raise ValueError(f"frozen v4 rules changed: {s['id']}")
    ids = {s['id'] for s in old['strategies']+ext['strategies']+spot['strategies']+v4['strategies']}
    if len(ids) != TOTAL_BOOKS: raise ValueError('duplicate or missing book id')
    return old, ext, spot, v4

def strip(s):
    return {k: v for k, v in s.items() if k != 'sha256'}

def new_book(s, now):
    if s['market'] == 'spot':
        cfg = dict(L.CFG, starting_equity=S4.SPOT_START, taker_fee=S3.SPOT_TAKER, max_leverage=1.0)
        b = L.sc.new_state(cfg)
        b.update(id=s['id'], owner=s['owner'], kind=s['kind'], lane=s['lane'], events=[], peak=S4.SPOT_START,
                 max_drawdown_pct=0., decisions={}, stopped_sides={}, day_date=L.sc.myt_date(now),
                 last_tick_myt=None, spot4_spec=s, activation_ms=now, market='spot', leverage=1,
                 starting_equity=S4.SPOT_START)
        L.event(b, 'registered', now, rules_sha256=s['sha256'], status='UNPROVEN_PAPER_ONLY', starting_equity=S4.SPOT_START,
                market='spot', leverage=1, long_only=True, no_funding=True, spot_pair=s['spot_pair'], api_coin=s['api_coin'])
        return b
    b = L.new_state(dict(strategies=[s]), now)['books'][s['id']]
    b.update(lane=s['lane'], spec4=s, activation_ms=now, market='perp')
    return b

def extend(st, old, ext, spot, v4, now, v2digest, v3digest, v4digest):
    ids4 = {s['id'] for s in v4['strategies']}
    held = {k: st['books'].pop(k) for k in list(st['books']) if k in ids4}
    V3.extend(st, old, ext, spot, now, v2digest, v3digest)
    if st.get('v4_extension_registration_sha256', v4digest) != v4digest:
        raise ValueError('persisted v4 extension registry mismatch')
    if 'v4_extension_registration_sha256' not in st:
        if held: raise ValueError('unexpected v4 books before v4 migration')
        for s in v4['strategies']: held[s['id']] = new_book(s, now)
        st.update(v4_extension_registration_sha256=v4digest, v4_extension_created_ms=now, version=4)
    if set(held) != ids4: raise ValueError('missing/unregistered v4 book')
    for s in v4['strategies']:
        key = 'spot4_spec' if s['market'] == 'spot' else 'spec4'
        if held[s['id']].get(key) != s: raise ValueError('persisted v4 spec changed')
    st['books'].update(held)
    return st

def valuation(b, now, coins, data):
    b['last_tick_myt'] = L.sc.myt(now); L.mark(b, {c: data['mids'][c] for c in coins}, now)
    if b.get('valuation_bucket') != now//(15*S.MINUTE):
        L.event(b, 'valuation', now, equity=L.sc.equity(b), cash=b['cash'], unrealized=L.sc.unrealized(b),
                fees=b['stats']['fees'], funding=b['stats']['funding'], positions=len(b['positions']),
                max_drawdown_pct=b['max_drawdown_pct'])
        b['valuation_bucket'] = now//(15*S.MINUTE)

def apply_perp4(st, data, now, start):
    """Same replay/stop/halt/time-exit/decision path as frozen V.apply_new, v4 signals only."""
    end = now//S.MINUTE*S.MINUTE; bycoin = {c: {r['t']: r for r in data['minutes'][c]} for c in S.COINS}
    books = [b for b in st['books'].values() if 'spec4' in b]
    for t in range(start, end, S.MINUTE):
        if not all(t in bycoin[c] for c in S.COINS): raise ValueError('UNRESOLVED_REPLAY_GAP')
        bars = {c: bycoin[c][t] for c in S.COINS}
        for b in books:
            if t+S.MINUTE <= b['activation_ms']: continue
            L.mark(b, {c: bars[c]['o'] for c in S.COINS}, t)
            L.funding_at(b, data['funding'], bars, t)
            for p in list(b['positions'].values()): L.resolve_stop(b, p, bars[p['coin']], now)
            L.mark(b, {c: bars[c]['c'] for c in S.COINS}, t+S.MINUTE-1)
            if not b['halted'] and L.sc.equity(b) <= b['day_start_equity']*.98:
                b.update(halted=True, halt_reason='daily_loss_minus_2_percent', pending_halt_flatten=True)
                L.event(b, 'halt', t+S.MINUTE-1, equity=L.sc.equity(b), note='replayed threshold; flatten at next actually observed quote')
    cache = {}
    for b in books:
        spec = b['spec4']; L.mark(b, data['mids'], now)
        for p in list(b['positions'].values()):
            mid = data['mids'][p['coin']]
            if L.hit_adverse(p, mid):
                L.close(b, p, mid*(1-p['dir']*.0005), now, 'stop', gap_through_stop=True, fill_source='first_observed_mid_adverse5bp')
            elif now-p['entry_ms'] >= spec['hold_ms']:
                L.close(b, p, mid*(1-p['dir']*.0002), now, 'observed_time_exit', delay_ms=now-p['entry_ms']-spec['hold_ms'])
        if b.pop('pending_halt_flatten', False):
            for p in list(b['positions'].values()):
                L.close(b, p, data['mids'][p['coin']]*(1-p['dir']*.0005), now, 'daily_halt_first_observation')
        L.halt(b, now); L.enforce_cost_risk(b, now)
        step = spec['interval']; boundary = now//step*step
        for c in spec['coins']:
            if b['decisions'].get(c, 0) >= boundary: continue
            key = (spec['kind'], json.dumps(spec['params'], sort_keys=True), c, boundary)
            if key not in cache: cache[key] = S4.signal(spec, data, boundary, c)
            sig = cache[key]; allowed = now-boundary <= 90000
            L.decision(b, c, sig, dict(data, books={}), now, boundary, allowed)  # 2bp adverse observed-mid fills
            b['decisions'][c] = boundary
        valuation(b, now, S.COINS, data)
    return len(cache)

def spot_open4(book, coin, stop_pct, mid, now, ctx, depth):
    spec = book['spot4_spec']
    if book['halted'] or stop_pct is None or not .005 <= stop_pct <= .045: return False
    if book['positions']:
        L.event(book, 'reject', now, coin=coin, reason='spot_one_position_max'); return False
    eq = L.sc.equity(book)
    if eq <= 0: return False
    fill, src = V3.fill_price(mid, 1, depth, eq)
    qty = L.sc.floor_sz(eq/(fill*(1+S3.SPOT_TAKER)), ctx[coin]['szDecimals'])
    if qty <= 0 or qty*fill < S3.MIN_NOTIONAL:
        L.event(book, 'reject', now, coin=coin, reason='minimum_notional_10_or_zero_lot', proposed_notional=qty*fill, equity=eq)
        return False
    notional = qty*fill
    if notional > eq+1e-9:
        L.event(book, 'reject', now, coin=coin, reason='spot_1x_cap'); return False
    fee = notional*S3.SPOT_TAKER; stop = fill*(1-stop_pct)
    tid = f"P{book['next_seq']:06d}"; book['next_seq'] += 1
    book['positions'][tid] = dict(id=tid, coin=coin, dir=1, side='long', size=qty, size_initial=qty, entry_px=fill,
        entry_ms=now, stop=stop, fees=fee, realized_gross=0., funding=0., funding_hour=now//S.HOUR, market='spot', leverage=1, spot=True)
    book['cash'] -= fee; book['stats']['fees'] += fee
    L.event(book, 'entry', now, trade_id=tid, coin=coin, side='long', size=qty, price=fill, stop=stop, fee=fee,
            fill_source=src, market='spot', leverage=1, fee_rate=S3.SPOT_TAKER, price_source=spec['price_source'], spot_pair=spec['spot_pair'])
    return True

def apply_spot4(st, data, now, start):
    """Same replay/stop/halt/exit path as frozen V3.apply_spot, v4 spot signals only."""
    end = now//S.MINUTE*S.MINUTE
    bycoin = {c: {r['t']: r for r in data['spot_minutes'][c]} for c in S3.SPOT_COINS}
    books = [b for b in st['books'].values() if 'spot4_spec' in b]
    for t in range(start, end, S.MINUTE):
        if not all(t in bycoin[c] for c in S3.SPOT_COINS): raise ValueError('UNRESOLVED_REPLAY_GAP')
        bars = {c: bycoin[c][t] for c in S3.SPOT_COINS}
        for b in books:
            if t+S.MINUTE <= b['activation_ms']: continue
            L.mark(b, {c: bars[c]['o'] for c in S3.SPOT_COINS}, t)
            for p in list(b['positions'].values()):
                if p.get('stop') is not None: V3.spot_resolve_stop(b, p, bars[p['coin']], now)
            L.mark(b, {c: bars[c]['c'] for c in S3.SPOT_COINS}, t+S.MINUTE-1)
            if not b['halted'] and L.sc.equity(b) <= b['day_start_equity']*.98:
                b.update(halted=True, halt_reason='daily_loss_minus_2_percent', pending_halt_flatten=True)
                L.event(b, 'halt', t+S.MINUTE-1, equity=L.sc.equity(b), note='replayed threshold; flatten at next actually observed quote')
    cache = {}
    for b in books:
        spec = b['spot4_spec']; L.mark(b, {c: data['mids'][c] for c in S3.SPOT_COINS}, now)
        for p in list(b['positions'].values()):
            mid = data['mids'][p['coin']]; depth = data.get('spot_books', {}).get(p['coin'])
            if p.get('stop') is not None and L.hit_adverse(p, mid):
                px, _ = V3.fill_price(mid, -1, depth, p['size']*mid); px = min(px, mid*(1-S3.STOP_SLIP_BPS/1e4))
                V3.spot_close(b, p, px, now, 'stop', gap_through_stop=True, fill_source='first_observed_mid_adverse5bp')
            elif now-p['entry_ms'] >= spec['hold_ms']:
                px, _ = V3.fill_price(mid, -1, depth, p['size']*mid)
                V3.spot_close(b, p, px, now, 'observed_time_exit', delay_ms=now-p['entry_ms']-spec['hold_ms'])
        if b.pop('pending_halt_flatten', False):
            for p in list(b['positions'].values()):
                V3.spot_close(b, p, data['mids'][p['coin']]*(1-S3.STOP_SLIP_BPS/1e4), now, 'daily_halt_first_observation')
        if not b['halted'] and L.sc.equity(b) <= b['day_start_equity']*.98:
            b.update(halted=True, halt_reason='daily_loss_minus_2_percent')
            L.event(b, 'halt', now, equity=L.sc.equity(b), note='sticky: owner reset required')
            for p in list(b['positions'].values()):
                V3.spot_close(b, p, data['mids'][p['coin']]*(1-S3.STOP_SLIP_BPS/1e4), now, 'daily_halt')
        boundary = now//S.HOUR*S.HOUR
        for c in spec['coins']:
            if b['decisions'].get(c, 0) >= boundary: continue
            key = (spec['kind'], json.dumps(spec['params'], sort_keys=True), c, boundary)
            if key not in cache: cache[key] = S4.spot_signal(spec, data, boundary, c)
            sig = cache[key]; allowed = now-boundary <= 90000
            L.event(b, 'signal', now, coin=c, boundary_utc=L.utc(boundary), side=sig['side'], details=sig['details'], entry_window_open=allowed)
            current = next((p for p in b['positions'].values() if p['coin'] == c), None)
            mid = data['mids'][c]; depth = data.get('spot_books', {}).get(c)
            if current and sig['exit_long']:
                px, _ = V3.fill_price(mid, -1, depth, current['size']*mid)
                V3.spot_close(b, current, px, now, 'signal_or_time_exit', signal_boundary_utc=L.utc(boundary), delay_ms=now-boundary)
                current = None
            if sig['side'] == 1 and current is None:
                if not allowed: L.event(b, 'missed_entry', now, coin=c, reason='no_hindsight_entry_signal_expired', boundary_utc=L.utc(boundary))
                else: spot_open4(b, c, sig['stop_pct'], mid, now, data['spot_ctx'], depth)
            b['decisions'][c] = boundary
        valuation(b, now, S3.SPOT_COINS, data)
    return len(cache)

def apply_tick(st, data, now, old):
    start = st['next_minute']
    subset = dict(st, books={s['id']: st['books'][s['id']] for s in old['strategies']})
    L.apply_tick(subset, data, now)
    E.initialize(st, now)
    computations = V.apply_new(st, data, now, start)
    spot_computations = V3.apply_spot(st, data, now, start)
    v4_computations = apply_perp4(st, data, now, start) + apply_spot4(st, data, now, start)
    st.update(next_minute=subset['next_minute'], last_tick_ms=now, ticks=subset['ticks'])
    E.update(st, now)
    return computations, spot_computations, v4_computations

def export(st, root=ROOT):
    V3.export(st, root)
    n_spot = sum(1 for b in st['books'].values() if b.get('market') == 'spot' or 'spot_spec' in b)
    p = root/'leaderboard.md'; text = p.read_text()
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('Updated '):
            lines[i] = line.split(' | ')[0]+f" | tick {st['ticks']} | {len(st['books'])} books ({len(st['books'])-n_spot} perp @100 USDC, {n_spot} spot @16.24 USDC; incl. 9 v4 research-sweep books registered 12 Nov 2026) | public reads only"
            break
    tmp = root/'leaderboard.md.tmp'; tmp.write_text('\n'.join(lines)); os.replace(tmp, p)

def tick(root=ROOT):
    start = time.monotonic(); cpu = time.process_time(); old, ext, spot, v4 = registration(root); began = L.sc.now_ms()
    st = L.read_json(root/'league_state.json')
    if st.get('registration_sha256') != L.sha(root/'registry/manifest.json'): raise ValueError('original state manifest digest changed')
    candidate = copy.deepcopy(st)
    extend(candidate, old, ext, spot, v4, began, L.sha(root/'registry/extension-v2.json'),
           L.sha(root/'registry/spot-extension-v3.json'), L.sha(root/'registry/extension-v4.json'))
    data = V3.PublicData(root).fetch(candidate, began); now = data['observed_ms']
    c2, c3, c4 = apply_tick(candidate, data, now, old)
    candidate['last_evidence'] = data['evidence']
    load = dict(max_rss_mb=round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2), cpu_seconds=round(time.process_time()-cpu, 4),
                wall_seconds=round(time.monotonic()-start, 4), signal_computations=c2, spot_signal_computations=c3, v4_signal_computations=c4,
                **{k: data['evidence'][k] for k in ('requests', 'request_types', 'estimated_weight', 'collection_seconds')})
    candidate['last_load'] = load
    L.atomic(root/'league_state.json', candidate); export(candidate, root)
    result = dict(status='ok', mode='PAPER_ONLY', engine_version=4, tick=candidate['ticks'], ts_myt=L.sc.myt(now), ts_utc=L.utc(now),
        book_count=len(candidate['books']), trial_count=E.PRIOR_TRIALS+len(candidate['books']), evidence=data['evidence'], load=load,
        candidates=[b['id'] for b in candidate['books'].values() if b['evaluation']['status'] == 'CANDIDATE_REVIEW_ONLY'],
        books={b['id']: dict(equity=round(L.sc.equity(b), 8), positions=len(b['positions']), closed_trades=len(b['closed_trades']),
                             starting_equity=b.get('starting_equity', 100.), market=b.get('market', 'perp')) for b in candidate['books'].values()})
    L.atomic(root/'last_tick.json', result)
    if not (root/'first-live-tick-v4.json').exists(): L.atomic(root/'first-live-tick-v4.json', result)
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
            start = time.monotonic(); L.heartbeat(ROOT, 'fetching', engine_version=4)
            try:
                r = tick(); L.heartbeat(ROOT, 'ok', engine_version=4, last_success_ms=L.sc.now_ms(), tick=r['tick'], book_count=r['book_count'], load=r['load'])
                print(json.dumps({k: v for k, v in r.items() if k != 'books'}), flush=True)
            except Exception as e:
                L.heartbeat(ROOT, 'ERROR_NO_NEW_RISK', engine_version=4, error=repr(e)); print(f'{L.sc.myt()} ERROR_NO_NEW_RISK {e!r}', flush=True); return 1
            while RUNNING and time.monotonic()-start < 60: time.sleep(.5)
        L.heartbeat(ROOT, 'stopped', engine_version=4); return 0

if __name__ == '__main__': raise SystemExit(main())
