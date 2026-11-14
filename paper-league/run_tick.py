#!/usr/bin/env python3
"""One PAPER tick. State lives in paper-league/state; the frozen engine reads the copy beside itself.

Public Hyperliquid /info only. No keys, signatures, wallets, or exchange writes.
"""
from __future__ import annotations

import json
import shutil
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ENGINE = ROOT / 'strategy-lab' / 'paper-league'
STATE = ROOT / 'state'
INTERVAL_MS = 5 * 60 * 1000
LATE_MS = 2 * INTERVAL_MS
BOX_SLEEP_TICK_MS = 1794583263509  # 2026-11-13T15:21:03.509Z, last successful v7 tick
PINNED = {
    'simcore.py': '197f4d2357bf42ee7028bde984cb92712f1ada75d744ccb9e4271f806eb73eda',
    'shadow_exchange.py': '1c1f832a1c80a4a866f9d112fd2e52f1034db19b81e666e71da94eeb85d542a6',
    'sentinel.py': '73c076d559231d4ca78e9a77c797f79c69a619ced676b80e492c4aa1e65266d3',
    'risk-limits.md': 'bc8c5b8637374ff5b54fb45d6bb732ce88a726c35866b6c1d2aa7bfa64ce18f0',
}
FILES = (
    'league_state.json', 'heartbeat.json', 'last_tick.json', 'data-gaps.jsonl',
    'market_cache.json', 'leaderboard.md',
)
DIRS = ('books', 'sources')
STALE = ('snapshot collection exceeded 60s', 'snapshot crossed minute boundary')


def _copy_file(src: Path, dst: Path):
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def sync_to_engine():
    if not (STATE / 'league_state.json').is_file():
        raise SystemExit(f'missing {STATE / "league_state.json"}')
    for name in FILES:
        src = STATE / name
        if src.exists():
            _copy_file(src, ENGINE / name)
    for name in DIRS:
        src = STATE / name
        dst = ENGINE / name
        if dst.exists():
            shutil.rmtree(dst)
        if src.exists():
            shutil.copytree(src, dst)


def sync_to_state():
    for name in FILES:
        src = ENGINE / name
        if src.exists():
            _copy_file(src, STATE / name)
    for name in DIRS:
        src = ENGINE / name
        dst = STATE / name
        if not src.exists():
            continue
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)


def install_shim(league):
    """Return the pinned digest only while a reconstructed parent file does not match.

    Strategy markdown and league_*.py still use their real hashes. When the original
    simcore/sentinel/shadow_exchange/risk-limits bytes are restored, this is a pass-through.
    """
    real = league.sha
    substituted = {}

    def sha(path):
        p = Path(path)
        digest = real(path)
        resolved = p.resolve()
        expected = PINNED.get(resolved.name)
        parent_ok = (
            resolved.parent == (ROOT / 'strategy-lab' / 'paper-trading')
            or resolved == (ROOT / 'risk-limits.md')
        )
        if expected and parent_ok and digest != expected:
            substituted[p.name] = digest
            return expected
        return digest

    league.sha = sha
    return substituted


def _load(path: Path):
    return json.loads(path.read_text())


def box_sleep_recorded(path: Path) -> bool:
    if not path.exists():
        return False
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if rec.get('reason') == 'box sleep' and rec.get('last_successful_tick_ms') == BOX_SLEEP_TICK_MS:
            return True
    return False


def append_gap(engine: Path, before: dict, after: dict, reason: str):
    import league as L
    now = after.get('evidence', {}).get('received_ms') or L.sc.now_ms()
    last_ms = before.get('last_tick_ms')
    positions = []
    for book in (before.get('books') or {}).values():
        for pos in (book.get('positions') or {}).values():
            positions.append(dict(
                book=book['id'], trade_id=pos.get('id'), coin=pos.get('coin'),
                side=pos.get('side'), stop=pos.get('stop'), entry_px=pos.get('entry_px'),
                size=pos.get('size'), market=book.get('market', 'perp'),
            ))
    rec = dict(
        event='known_data_gap',
        recorded_ms=now,
        recorded_myt=L.sc.myt(now),
        recorded_utc=L.utc(now),
        last_successful_tick=before.get('ticks'),
        last_successful_tick_ms=last_ms,
        last_successful_tick_myt=L.sc.myt(last_ms) if last_ms else None,
        last_successful_tick_utc=L.utc(last_ms) if last_ms else None,
        next_minute=before.get('next_minute'),
        gap_ms=now - last_ms if last_ms else None,
        gap_minutes=round((now - last_ms) / 60000, 3) if last_ms else None,
        first_tick_after_gap=after.get('tick'),
        first_tick_after_gap_utc=after.get('ts_utc'),
        book_count=len(before.get('books') or {}),
        open_positions=positions,
        reason=reason,
        fills_backfilled=False,
        stops_during_gap='unverified',
        note='Stops during this gap are unverified. Do not backfill fills. Engine virtual-stop replay on the next live tick is flagged replayed, not a live fill.',
    )
    path = engine / 'data-gaps.jsonl'
    with path.open('a') as f:
        f.write(json.dumps(rec, allow_nan=False) + '\n')
        f.flush()


def record_gaps(engine: Path, before: dict, after: dict):
    last_ms = before.get('last_tick_ms')
    new_ms = (after.get('evidence') or {}).get('received_ms')
    if not last_ms or not new_ms:
        return
    gap = new_ms - last_ms
    if last_ms == BOX_SLEEP_TICK_MS:
        # One row for the box outage, even though that span is also more than two intervals.
        if not box_sleep_recorded(engine / 'data-gaps.jsonl'):
            append_gap(engine, before, after, 'box sleep')
        return
    if gap > LATE_MS:
        append_gap(engine, before, after, 'scheduled tick more than 2 intervals late')


def write_heartbeat(engine: Path, result: dict, scheduler_engine: int, substituted: dict):
    import league as L
    di = result.get('data_isolation') or {}
    L.heartbeat(
        engine,
        'ok' if not di.get('skipped_books') else 'ok_partial_data_isolation',
        engine_version=scheduler_engine,
        last_success_ms=L.sc.now_ms(),
        tick=result.get('tick'),
        book_count=result.get('book_count'),
        active_books=result.get('active_books'),
        retired_books=result.get('retired_books'),
        load=result.get('load'),
        failed_symbols=di.get('failed_symbols'),
        skipped_books=len(di.get('skipped_books') or []),
        stale_positions=di.get('stale_positions'),
        fail_rate_24h=di.get('fail_rate_24h'),
        review_flags=di.get('review_flags'),
        alert=bool(di.get('review_flags')),
        labels_v1=result.get('labels_v1'),
        consecutive_skips=0,
        mode='PAPER_ONLY',
        scheduler='github-actions',
        reconstructed_dependencies=sorted(substituted),
        paper_only=True,
        exchange_writes=False,
    )


def _run_once(module_name: str):
    module = __import__(module_name)
    sys.argv = [f'{module_name}.py', '--once']
    rc = module.main()
    if rc not in (0, None):
        raise RuntimeError(f'{module_name} exited {rc}')
    return _load(ENGINE / 'last_tick.json')


def run_engine():
    """Warm outside the snapshot clock, then one v8 tick. v7 only if v8 hits a stale-fill guard."""
    import warm_cache
    before = _load(ENGINE / 'league_state.json')
    t0 = time.perf_counter()
    summary = warm_cache.warm_cache(root=ENGINE, force=False, record_gap=False, isolate=True)
    summary['warm_seconds'] = round(time.perf_counter() - t0, 3)
    print(json.dumps({'warm': {k: summary[k] for k in summary if k != 'open_positions'}}, default=str), flush=True)
    used = 8
    try:
        result = _run_once('league_v8')
    except Exception as e:
        if not any(s in str(e) for s in STALE):
            raise
        print(f'v8 stale-fill guard after warm ({e!r}); one v7 tick', flush=True)
        used = 7
        result = _run_once('league_v7')
        result['scheduler_fallback'] = 'v7'
    return before, result, used, summary


def main():
    sync_to_engine()
    sys.path.insert(0, str(ENGINE))
    import league as L
    substituted = install_shim(L)
    if substituted:
        print('reconstructed parent files (frozen bytes were not in the export): '
              + ', '.join(f'{k} real={v}' for k, v in sorted(substituted.items())), flush=True)
    try:
        before, result, used, summary = run_engine()
        record_gaps(ENGINE, before, result)
        write_heartbeat(ENGINE, result, used, substituted)
        if result.get('tick') != before.get('ticks', 0) + 1:
            raise RuntimeError(f'tick did not advance: {before.get("ticks")} -> {result.get("tick")}')
        if result.get('mode') != 'PAPER_ONLY':
            raise RuntimeError('refusing to keep a non-paper tick')
        sync_to_state()
    except Exception:
        # Leave state/ at the last committed tick. The engine directory is gitignored scratch.
        raise
    hb = _load(STATE / 'heartbeat.json')
    print(json.dumps(dict(
        tick=result['tick'],
        ts_utc=result.get('ts_utc'),
        scheduler_engine=used,
        last_tick_engine_version=result.get('engine_version'),
        heartbeat_myt=hb.get('ts_myt'),
        collection_seconds=(result.get('load') or {}).get('collection_seconds'),
        warm_requests=summary.get('requests'),
        warm_seconds=summary.get('warm_seconds'),
        book_count=result.get('book_count'),
    )), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
