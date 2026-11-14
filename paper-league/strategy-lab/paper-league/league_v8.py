#!/usr/bin/env python3
"""Scheduling-only runner over league_v7 (minute-aligned ticks + boundary-skip). 2026-11-12.

Root cause fixed: the engine started each tick at an arbitrary second (restart time + 60s
cadence); with ~14-16s of public snapshot collection, any start after ~:44s crossed the
minute boundary, V5 raised 'snapshot crossed minute boundary' and v7 main() exited rc=1,
so the supervisor crash-looped with growing backoff.

This runner:
  1. starts every tick ALIGN_OFFSET_S after the top of a minute (wall clock), giving ~45s of
     slack for the snapshot; and
  2. treats the two frozen no-stale-fill guards ('snapshot crossed minute boundary',
     'snapshot collection exceeded 60s') as a SKIPPED tick: nothing is persisted (V6.tick
     raises before any state/cache/source/ledger write), no fills, no backfill; the process
     keeps running and retries at the next aligned minute. Any other error still fails
     closed (rc=1) as before.
No rule, sizing, signal, data-check, registry, label or DSR change; the 60s rule lives
unchanged in league_v5.py. Public /info reads only; no wallet, key, order or exchange write.
"""
import argparse
import fcntl
import json
import os
import signal as signals
import time
import league as L
import league_v7 as V7

ROOT = L.ROOT
RUNNING = True
ALIGN_OFFSET_S = 1.0
SKIP_ALERT_AFTER = 3  # consecutive skipped ticks before heartbeat alert=true
STALE_GUARDS = ('snapshot crossed minute boundary', 'snapshot collection exceeded 60s')

def is_stale_guard(exc):
    return isinstance(exc, ValueError) and any(g in str(exc) for g in STALE_GUARDS)

def seconds_until_aligned(now_s, offset=ALIGN_OFFSET_S, grace=1.0):
    """Seconds to wait so the tick starts `offset` s after a minute top. Start now if we are
    already within [offset, offset+grace] of the current minute."""
    into = now_s % 60.0
    if offset <= into <= offset+grace: return 0.0
    return (offset-into) % 60.0

def run_once(tick_fn, root=ROOT, skips=0, hb=L.heartbeat, log=print):
    """One aligned tick. Returns (result_or_None, consecutive_skips). Re-raises non-guard errors."""
    try:
        r = tick_fn()
    except Exception as e:
        if not is_stale_guard(e): raise
        skips += 1
        hb(root, 'skipped_stale_guard', engine_version=8, error=repr(e), consecutive_skips=skips,
           alert=skips >= SKIP_ALERT_AFTER, fills_written=False)
        log(f'{L.sc.myt()} TICK_SKIPPED_NO_FILLS {e!r} consecutive={skips}', flush=True)
        return None, skips
    di = r['data_isolation']
    hb(root, 'ok' if not di['skipped_books'] else 'ok_partial_data_isolation', engine_version=8,
       last_success_ms=L.sc.now_ms(), tick=r['tick'], book_count=r['book_count'], active_books=r['active_books'],
       retired_books=r['retired_books'], load=r['load'], failed_symbols=di['failed_symbols'],
       skipped_books=len(di['skipped_books']), stale_positions=di['stale_positions'],
       fail_rate_24h=di['fail_rate_24h'], review_flags=di['review_flags'], alert=bool(di['review_flags']),
       labels_v1=r['labels_v1'], consecutive_skips=0, skipped_since_last_ok=skips)
    log(json.dumps({k: v for k, v in r.items() if k != 'books'}), flush=True)
    return r, 0

def stop(*_):
    global RUNNING
    RUNNING = False

def sleep_until_aligned():
    end = time.monotonic()+seconds_until_aligned(time.time())
    while RUNNING and time.monotonic() < end: time.sleep(min(.25, max(0, end-time.monotonic())))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--once', action='store_true'); args = ap.parse_args()
    with open(ROOT/'.engine.lock', 'a') as lock:
        try: fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print('another league engine holds the lock', flush=True); return 0
        if args.once: sleep_until_aligned(); print(json.dumps(V7.tick(), indent=2)); return 0
        (ROOT/'engine.pid').write_text(str(os.getpid())); signals.signal(signals.SIGTERM, stop); signals.signal(signals.SIGINT, stop)
        skips = 0
        while RUNNING:
            sleep_until_aligned()
            if not RUNNING: break
            L.heartbeat(ROOT, 'fetching', engine_version=8, consecutive_skips=skips, alert=skips >= SKIP_ALERT_AFTER)
            try:
                _, skips = run_once(V7.tick, ROOT, skips)
            except Exception as e:
                L.heartbeat(ROOT, 'ERROR_NO_NEW_RISK', engine_version=8, error=repr(e)); print(f'{L.sc.myt()} ERROR_NO_NEW_RISK {e!r}', flush=True); return 1
            # never start two ticks in the same minute
            while RUNNING and time.time() % 60.0 < ALIGN_OFFSET_S+1.5: time.sleep(.25)
        L.heartbeat(ROOT, 'stopped', engine_version=8); return 0

if __name__ == '__main__': raise SystemExit(main())
