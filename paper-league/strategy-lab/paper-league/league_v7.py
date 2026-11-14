#!/usr/bin/env python3
"""labels-v1 overlay over league_v6: same tick, then registry labels (NON_V1_RESEARCH promotion
ineligibility, cluster tags, n6 relabel) are applied to state, exports and last_tick. No rule, sizing,
signal or data-check change. Public /info reads only; no wallet, key, order, signing or exchange write."""
import argparse
import fcntl
import json
import os
import signal as signals
import time
import league as L
import league_v4 as V4
import league_v6 as V6
import labels as LB

ROOT = L.ROOT
RUNNING = True

def registration(root=ROOT):
    out = V6.registration(root); m = LB.load(root)
    if m['retirement_usol_v1_sha256'] != L.sha(root/'registry/retirement-usol-v1.json'): raise ValueError('retirement manifest changed')
    for n, d in m['implementation_sha256'].items():
        if L.sha(root/n) != d: raise ValueError(f'frozen labels implementation changed: {n}')
    return out, m

def overlay(root, m):
    st = L.read_json(root/'league_state.json'); now = st['last_tick_ms']
    LB.apply(st, m, now)
    L.atomic(root/'league_state.json', st); V4.export(st, root)
    p = root/'leaderboard.md'; text = p.read_text()
    for bid in (st.get('retired_ids') or [k for k, b in st['books'].items() if b.get('retired')]):
        text = text.replace(f'| {bid} |', f'| {bid} (RETIRED_DATA_QUALITY) |')
    text = LB.annotate_leaderboard(text, m)
    tmp = root/'leaderboard.md.tmp'; tmp.write_text(text); os.replace(tmp, p)
    r = L.read_json(root/'last_tick.json')
    r['candidates'] = [b['id'] for b in st['books'].values() if b['evaluation']['status'] == 'CANDIDATE_REVIEW_ONLY' and not b.get('retired')]
    r['labels_v1'] = dict(note_sha256=m['note_sha256'], ineligible=sorted(k for k, v in m['labels'].items() if v.get('promotion_eligible') is False),
                          clusters={c: len(v) for c, v in m['clusters'].items()})
    r['engine_version'] = 7
    for bid, x in r.get('books', {}).items(): x['labels'] = LB.tags(m, bid)
    L.atomic(root/'last_tick.json', r)
    if not (root/'first-live-tick-v7.json').exists(): L.atomic(root/'first-live-tick-v7.json', r)
    return r

def tick(root=ROOT):
    _, m = registration(root)
    V6.tick(root)
    return overlay(root, m)

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
            start = time.monotonic(); L.heartbeat(ROOT, 'fetching', engine_version=7)
            try:
                r = tick(); di = r['data_isolation']
                L.heartbeat(ROOT, 'ok' if not di['skipped_books'] else 'ok_partial_data_isolation', engine_version=7,
                            last_success_ms=L.sc.now_ms(), tick=r['tick'], book_count=r['book_count'], active_books=r['active_books'],
                            retired_books=r['retired_books'], load=r['load'], failed_symbols=di['failed_symbols'],
                            skipped_books=len(di['skipped_books']), stale_positions=di['stale_positions'],
                            fail_rate_24h=di['fail_rate_24h'], review_flags=di['review_flags'], alert=bool(di['review_flags']),
                            labels_v1=r['labels_v1'])
                print(json.dumps({k: v for k, v in r.items() if k != 'books'}), flush=True)
            except Exception as e:
                L.heartbeat(ROOT, 'ERROR_NO_NEW_RISK', engine_version=7, error=repr(e)); print(f'{L.sc.myt()} ERROR_NO_NEW_RISK {e!r}', flush=True); return 1
            while RUNNING and time.monotonic()-start < 60: time.sleep(.5)
        L.heartbeat(ROOT, 'stopped', engine_version=7); return 0

if __name__ == '__main__': raise SystemExit(main())
