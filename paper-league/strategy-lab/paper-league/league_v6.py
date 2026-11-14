#!/usr/bin/env python3
"""USOL retirement wrapper over data-isolation v1 (league_v5). Retires the four USOL/USDC spot books
(RETIRED_DATA_QUALITY): history preserved, kept in the DSR trial count (434), no further ticks, USOL
removed from the data checks. Open virtual positions are closed once at the last valid observed mark
(reason logged), or marked UNRESOLVED if that mark is stale. No price is invented. SOL perps unaffected.
Public /info reads only; no wallet, key, order, signing, testnet or exchange write.
"""
import argparse
import contextlib
import copy
import fcntl
import json
import os
import signal as signals
import time
import league as L
import league_v3 as V3
import league_v4 as V4
import league_v5 as V5
import strategies_v3 as S3
import evaluation_v3 as E

ROOT = L.ROOT
RUNNING = True
STALE_MS = 5*60000

def registration(root=ROOT):
    old, ext, spot, v4, di = V5.registration(root)
    r = L.read_json(root/'registry/retirement-usol-v1.json')
    if r.get('status') != 'RETIRED_DATA_QUALITY' or r.get('mode') != 'PAPER_ONLY': raise ValueError('retirement manifest invalid')
    if L.sha(root/'registry/retirement-usol-v1.md') != r['note_sha256']: raise ValueError('retirement note changed')
    if r['data_isolation_v1_sha256'] != L.sha(root/'registry/data-isolation-v1.json'): raise ValueError('data-isolation manifest changed')
    for n, d in r['implementation_sha256'].items():
        if L.sha(root/n) != d: raise ValueError(f'frozen retirement implementation changed: {n}')
    by_id = {s['id']: s for s in spot['strategies']}
    for bid, digest in r['books'].items():
        if by_id[bid]['sha256'] != digest or L.sha(root/'registry'/f'{bid}.md') != digest: raise ValueError(f'retired book rules changed {bid}')
    return old, ext, spot, v4, di, r

@contextlib.contextmanager
def without(symbols):
    saved = (S3.SPOT_MARKETS, S3.SPOT_COINS)
    try:
        S3.SPOT_MARKETS = {k: v for k, v in saved[0].items() if k not in symbols}
        S3.SPOT_COINS = tuple(c for c in saved[1] if c not in symbols)
        yield
    finally:
        S3.SPOT_MARKETS, S3.SPOT_COINS = saved

def retire(st, r, now):
    """One-time, inside the tick transaction, before any fetch: uses only marks already observed."""
    if st.get('retirement_usol_v1_applied_ms'): return []
    last = st.get('last_tick_ms'); out = []
    for bid in r['books']:
        b = st['books'][bid]
        fresh = last is not None and now-last <= STALE_MS and 'di_cursor' not in b and b.get('last_tick_myt') == L.sc.myt(last)
        for p in list(b['positions'].values()):
            mark = b['marks'].get(p['coin'])
            if fresh and mark and mark > 0:
                px = mark*(1-S3.SLIP_FLOOR_BPS/1e4)
                V3.spot_close(b, p, px, now, 'retired_data_quality_close_at_last_valid_mark', last_valid_mark=mark,
                              mark_observed_utc=L.utc(last), fill_source='last_observed_mid_minus_2bp_plus_spot_taker')
                out.append(dict(book=bid, trade_id=p['id'], status='CLOSED', price=px, mark=mark, mark_observed_utc=L.utc(last)))
            else:
                p['unresolved'] = True
                L.event(b, 'unresolved_position', now, trade_id=p['id'], coin=p['coin'],
                        reason='retired_data_quality_last_mark_stale_no_price_invented', last_mark=mark,
                        last_tick_utc=L.utc(last) if last else None)
                out.append(dict(book=bid, trade_id=p['id'], status='UNRESOLVED', last_mark=mark))
        b.update(retired=True, retired_status='RETIRED_DATA_QUALITY', retired_ms=now, retired_utc=L.utc(now),
                 retirement_note_sha256=r['note_sha256'])
        L.event(b, 'retired', now, status='RETIRED_DATA_QUALITY', note_sha256=r['note_sha256'],
                reason=r['reason'], history_preserved=True, kept_in_dsr_trial_count=True)
    st['retirement_usol_v1_applied_ms'] = now
    return out

def apply_tick(cand, data, now, old, retired, symbols):
    with without(symbols):
        view = dict(cand, books={k: b for k, b in cand['books'].items() if k not in retired})
        counts, summary = V5.apply_tick(view, data, now, old)
    cand['books'].update(view['books'])  # V5 writes processed copies into the view's dict
    for k in ('next_minute', 'last_tick_ms', 'ticks', 'data_isolation'): cand[k] = view[k]
    E.update(cand, now)  # full book set: DSR trial count stays 434, retired books keep their history
    return counts, summary

def tick(root=ROOT):
    start = time.monotonic(); old, ext, spot, v4, di, r = registration(root); began = L.sc.now_ms()
    st = L.read_json(root/'league_state.json')
    if st.get('registration_sha256') != L.sha(root/'registry/manifest.json'): raise ValueError('original state manifest digest changed')
    cand = copy.deepcopy(st)
    V4.extend(cand, old, ext, spot, v4, began, L.sha(root/'registry/extension-v2.json'),
              L.sha(root/'registry/spot-extension-v3.json'), L.sha(root/'registry/extension-v4.json'))
    if cand.get('data_isolation_rule_sha256', di['rule_sha256']) != di['rule_sha256']: raise ValueError('persisted data-isolation rule mismatch')
    cand.setdefault('data_isolation_effective_ms', began); cand.setdefault('data_isolation_rule_sha256', di['rule_sha256'])
    closes = retire(cand, r, began)
    retired = set(r['books']); symbols = set(r['symbols'])
    with without(symbols):
        data = V5.PublicData(root).fetch(cand, began); now = data['observed_ms']
        (c2, c3, c4), summary = apply_tick(cand, data, now, old, retired, symbols)
    cand['last_evidence'] = data['evidence']
    cand['last_load'] = dict(wall_seconds=round(time.monotonic()-start, 4), signal_computations=c2, spot_signal_computations=c3,
                             v4_signal_computations=c4, **{k: data['evidence'][k] for k in ('requests', 'request_types', 'estimated_weight', 'collection_seconds')})
    L.atomic(root/'league_state.json', cand); V4.export(cand, root)
    p = root/'leaderboard.md'; text = p.read_text()
    for bid in retired: text = text.replace(f'| {bid} |', f'| {bid} (RETIRED_DATA_QUALITY) |')
    tmp = root/'leaderboard.md.tmp'; tmp.write_text(text); os.replace(tmp, p)
    V5.log_skip(root, now, cand['ticks'], summary)
    if closes:
        with open(root/'data-gaps.jsonl', 'a') as f:
            f.write(json.dumps(dict(event='usol_retirement', recorded_ms=began, recorded_myt=L.sc.myt(began), recorded_utc=L.utc(began),
                    books=sorted(retired), positions=closes, note_sha256=r['note_sha256'], prices_invented=False))+'\n')
    result = dict(status='ok', mode='PAPER_ONLY', engine_version=6, tick=cand['ticks'], ts_myt=L.sc.myt(now), ts_utc=L.utc(now),
        book_count=len(cand['books']), active_books=len(cand['books'])-len(retired), retired_books=sorted(retired),
        trial_count=E.PRIOR_TRIALS+len(cand['books']), evidence=data['evidence'], load=cand['last_load'],
        data_isolation={k: v for k, v in summary.items() if k != 'skipped_detail'}, retirement_closes=closes,
        candidates=[b['id'] for b in cand['books'].values() if b['evaluation']['status'] == 'CANDIDATE_REVIEW_ONLY' and not b.get('retired')],
        books={b['id']: dict(equity=round(L.sc.equity(b), 8), positions=len(b['positions']), closed_trades=len(b['closed_trades']),
               market=b.get('market', 'perp'), retired=bool(b.get('retired'))) for b in cand['books'].values()})
    L.atomic(root/'last_tick.json', result)
    if not (root/'first-live-tick-v6.json').exists(): L.atomic(root/'first-live-tick-v6.json', result)
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
            start = time.monotonic(); L.heartbeat(ROOT, 'fetching', engine_version=6)
            try:
                r = tick(); di = r['data_isolation']
                L.heartbeat(ROOT, 'ok' if not di['skipped_books'] else 'ok_partial_data_isolation', engine_version=6,
                            last_success_ms=L.sc.now_ms(), tick=r['tick'], book_count=r['book_count'], active_books=r['active_books'],
                            retired_books=r['retired_books'], load=r['load'], failed_symbols=di['failed_symbols'],
                            skipped_books=len(di['skipped_books']), stale_positions=di['stale_positions'],
                            fail_rate_24h=di['fail_rate_24h'], review_flags=di['review_flags'], alert=bool(di['review_flags']))
                print(json.dumps({k: v for k, v in r.items() if k != 'books'}), flush=True)
            except Exception as e:
                L.heartbeat(ROOT, 'ERROR_NO_NEW_RISK', engine_version=6, error=repr(e)); print(f'{L.sc.myt()} ERROR_NO_NEW_RISK {e!r}', flush=True); return 1
            while RUNNING and time.monotonic()-start < 60: time.sleep(.5)
        L.heartbeat(ROOT, 'stopped', engine_version=6); return 0

if __name__ == '__main__': raise SystemExit(main())
