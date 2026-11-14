#!/usr/bin/env python3
"""Pre-warm the public candle cache outside the 60-second snapshot window.

On restart after a downtime gap greater than 10 minutes, fetch public Hyperliquid
/info candles (and funding) with staggered requests and merge them into
market_cache.json so league_v3.PublicData.fetch can finish inside the existing
60s / no-stale-fills rule. This module does not loosen that rule, does not
modify frozen v1/v2/v3 implementations, does not write fills or league_state,
and uses public reads only (no keys).
"""
from __future__ import annotations

import argparse
import os
import copy
import json
import sys
import time
from pathlib import Path

import league as L
import league_v2 as V
import strategies as S
import strategies_v3 as S3

GAP_WARM_MS = 10 * S3.MINUTE
STAGGER_S = 0.35
WEIGHT_PACE_PER_MIN = 750
MAX_429_RETRIES = 6
CANDLE_PAGE = 4000

PERP_INTERVALS = (
    ('m1', '1m', S3.MINUTE, 512),
    ('m5', '5m', 5 * S3.MINUTE, None),
    ('m15', '15m', 15 * S3.MINUTE, None),
    ('h1', '1h', S3.HOUR, None),
    ('fourhour', '4h', 4 * S3.HOUR, None),
    ('daily', '1d', S3.DAY, None),
)
SPOT_INTERVALS = (
    ('spot_m1', '1m', S3.MINUTE, 512),
    ('spot_m5', '5m', 5 * S3.MINUTE, None),
    ('spot_m15', '15m', 15 * S3.MINUTE, None),
    ('spot_h1', '1h', S3.HOUR, None),
)


def _parse_candles(raw):
    return [dict(t=int(c['t']), **{k: float(c[k]) for k in ('o', 'h', 'l', 'c', 'v')}) for c in raw]


def last_closed_1m(now):
    return now // S3.MINUTE * S3.MINUTE - S3.MINUTE


def series_last_t(cache, key, name):
    rows = (cache.get(key) or {}).get(name) or []
    return int(rows[-1]['t']) if rows else None


def max_1m_lag_ms(cache, now):
    closed = last_closed_1m(now)
    lags = []
    for coin in S.COINS:
        last = series_last_t(cache, 'm1', coin)
        lags.append(closed - last if last is not None else 10**15)
    for name in S3.SPOT_COINS:
        last = series_last_t(cache, 'spot_m1', name)
        lags.append(closed - last if last is not None else 10**15)
    return max(lags) if lags else 10**15


def should_warm(cache, now, threshold_ms=GAP_WARM_MS):
    """True when any required 1m series lags the last closed minute by more than 10 minutes."""
    return max_1m_lag_ms(cache, now) > threshold_ms


def open_positions_snapshot(state):
    """Describe open paper positions at the last committed tick. Not fills."""
    out = []
    for book in (state.get('books') or {}).values():
        for pos in (book.get('positions') or {}).values():
            out.append(dict(
                book=book['id'], trade_id=pos.get('id'), coin=pos.get('coin'),
                side=pos.get('side'), stop=pos.get('stop'), entry_px=pos.get('entry_px'),
                size=pos.get('size'), market=book.get('market', 'perp'),
            ))
    return out


def _gap_log(root):
    return Path(root) / 'data-gaps.jsonl'


def already_recorded(root, last_tick_ms):
    path = _gap_log(root)
    if not path.exists() or last_tick_ms is None:
        return False
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if rec.get('last_successful_tick_ms') == last_tick_ms:
            return True
    return False


def record_known_gap(root, info):
    """Append one known-data-gap record. Does not write or invent fills."""
    path = _gap_log(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    rec = dict(info)
    rec.setdefault('event', 'known_data_gap')
    rec.setdefault('fills_backfilled', False)
    rec.setdefault('stops_during_gap', 'unverified')
    rec.setdefault('note', 'Stops during this gap are unverified. Do not backfill fills. Engine virtual-stop replay on the next live tick is flagged replayed, not a live fill.')
    with path.open('a') as f:
        f.write(json.dumps(rec, allow_nan=False) + '\n')
        f.flush()
    return path


class Pace:
    def __init__(self, sleep_fn=time.sleep, stagger_s=STAGGER_S, weight_cap=WEIGHT_PACE_PER_MIN):
        self.sleep_fn = sleep_fn
        self.stagger_s = stagger_s
        self.weight_cap = weight_cap
        self.window_start = time.monotonic()
        self.window_weight = 0
        self.requests = []
        self.weight = 0
        self._prior = False

    def _roll(self):
        elapsed = time.monotonic() - self.window_start
        if elapsed >= 60:
            self.window_start = time.monotonic()
            self.window_weight = 0

    def before(self):
        self._roll()
        if self._prior and self.stagger_s > 0:
            self.sleep_fn(self.stagger_s)
        if self.window_weight >= self.weight_cap:
            wait = max(0.0, 60 - (time.monotonic() - self.window_start))
            if wait > 0:
                self.sleep_fn(wait)
            self.window_start = time.monotonic()
            self.window_weight = 0
        self._prior = True

    def record(self, typ, response, cost):
        self.window_weight += cost
        self.weight += cost
        self.requests.append(dict(type=typ, cost=cost, n=len(response) if isinstance(response, list) else 1))


def _cost(typ, response):
    if typ in ('allMids', 'l2Book'):
        return 2
    cost = 20
    if typ == 'candleSnapshot' and isinstance(response, list):
        cost += (len(response) + 59) // 60
    if typ == 'fundingHistory' and isinstance(response, list):
        cost += (len(response) + 19) // 20
    return cost


def request(payload, pace, info_fn):
    typ = payload['type']
    last = None
    for attempt in range(MAX_429_RETRIES + 1):
        pace.before()
        try:
            response = info_fn(payload)
        except Exception as e:
            last = e
            text = str(e)
            if '429' in text or 'Too Many Requests' in text:
                pace.sleep_fn(min(32.0, 2.0 ** attempt))
                continue
            raise
        cost = _cost(typ, response)
        pace.record(typ, response, cost)
        return response
    raise RuntimeError(f"info {typ} failed after 429 retries: {last}")


def _merge_candles(rows, new, step, now, keep=None):
    merged = {r['t']: r for r in rows if r['t'] + step <= now}
    for r in new:
        if r['t'] + step <= now:
            merged[r['t']] = r
    out = [merged[t] for t in sorted(merged)]
    if keep is not None:
        out = out[-keep:]
    if out and any(b['t'] - a['t'] != step for a, b in zip(out, out[1:])):
        raise ValueError('cache warm-up would introduce a continuity hole; refusing to write')
    return out


def _fetch_candles(api_coin, interval, start, end, pace, info_fn):
    step = V.STEPS[interval]
    rows = []
    cursor = start
    while cursor <= end:
        page_end = min(end, cursor + CANDLE_PAGE * step)
        raw = request(dict(type='candleSnapshot', req=dict(
            coin=api_coin, interval=interval, startTime=int(cursor), endTime=int(page_end),
        )), pace, info_fn)
        chunk = _parse_candles(raw)
        if not chunk:
            break
        rows.extend(chunk)
        nxt = max(r['t'] for r in chunk) + step
        if nxt <= cursor:
            break
        cursor = nxt
        if len(chunk) < CANDLE_PAGE and page_end >= end:
            break
    return rows


def _refresh_series(cache, key, name, api_coin, interval, step, now, pace, info_fn, keep=None):
    cache.setdefault(key, {})
    rows = list(cache[key].get(name) or [])
    end = now // step * step
    if rows and rows[-1]['t'] + step >= end and (keep is None or len(rows) >= min(keep, len(rows))):
        # Already has the last closed bar; 1m still needs the bar that closes at `end`
        # (rows[-1]['t'] + step == end). If current, skip the HTTP call.
        if rows[-1]['t'] + step == end:
            return False
    start = rows[-1]['t'] if rows else end - (keep or 250) * step
    new = _fetch_candles(api_coin, interval, start, now, pace, info_fn)
    cache[key][name] = _merge_candles(rows, new, step, now, keep=keep)
    updated = cache[key][name]
    if not updated or updated[-1]['t'] + step != end:
        # Mid-minute is fine: last closed bar should equal end - step, i.e. last t + step == end.
        raise ValueError(f'{name} {interval} warm-up did not reach the last closed bar')
    return True


def _refresh_funding(cache, coin, start, now, pace, info_fn):
    rows = list((cache.get('funding') or {}).get(coin) or [])
    cursor = max(start, rows[-1]['time'] - S3.HOUR) if rows else start
    if rows and rows[-1]['time'] // S3.HOUR * S3.HOUR >= now // S3.HOUR * S3.HOUR:
        return False
    for _ in range(100):
        raw = request(dict(type='fundingHistory', coin=coin, startTime=int(cursor), endTime=int(now)), pace, info_fn)
        merged = {r['time']: r for r in rows}
        for r in raw:
            if r['time'] in merged and merged[r['time']] != r:
                raise ValueError('conflicting funding duplicate')
            merged[r['time']] = r
        rows = [merged[t] for t in sorted(merged)]
        if len(raw) < 500:
            break
        nxt = max(r['time'] for r in raw) + 1
        if nxt <= cursor:
            raise ValueError('funding pagination did not advance')
        cursor = nxt
    else:
        raise ValueError('funding page limit exceeded')
    cache.setdefault('funding', {})[coin] = rows
    return True


def warm_cache(root=None, now=None, sleep_fn=time.sleep, info_fn=None, force=False, record_gap=True, isolate=False):
    """isolate=True (data-isolation v1): a symbol whose refresh fails keeps its previous cache untouched and is
    reported in summary['isolated_failures']; other symbols still warm. Nothing is fabricated or forward-filled."""
    root = Path(root or L.ROOT)
    now = int(now if now is not None else L.sc.now_ms())
    cache_path = root / 'market_cache.json'
    state_path = root / 'league_state.json'
    cache = L.read_json(cache_path) if cache_path.exists() else {}
    state = L.read_json(state_path) if state_path.exists() else {}
    lag = max_1m_lag_ms(cache, now)
    needed = force or should_warm(cache, now)
    last_tick_ms = state.get('last_tick_ms')
    last_tick = state.get('ticks')
    summary = dict(
        warmed=False, needed=needed, lag_ms=lag, lag_minutes=round(lag / 60000, 3),
        now_myt=L.sc.myt(now), last_tick=last_tick, last_tick_myt=L.sc.myt(last_tick_ms) if last_tick_ms else None,
        requests=0, estimated_weight=0, gap_recorded=False, fills_written=False,
    )
    if record_gap and last_tick_ms and now - last_tick_ms > GAP_WARM_MS and not already_recorded(root, last_tick_ms):
        record_known_gap(root, dict(
            recorded_ms=now, recorded_myt=L.sc.myt(now), recorded_utc=L.utc(now),
            last_successful_tick=last_tick, last_successful_tick_ms=last_tick_ms,
            last_successful_tick_myt=L.sc.myt(last_tick_ms), last_successful_tick_utc=L.utc(last_tick_ms),
            next_minute=state.get('next_minute'),
            next_minute_myt=L.sc.myt(state['next_minute']) if state.get('next_minute') else None,
            gap_ms=now - last_tick_ms, gap_minutes=round((now - last_tick_ms) / 60000, 3),
            book_count=len(state.get('books') or {}),
            open_positions=open_positions_snapshot(state),
            reason='paper-league downtime gap greater than 10 minutes; cache warm-up / restart',
        ))
        summary['gap_recorded'] = True
    if not needed:
        summary['status'] = 'cache_fresh'
        return summary

    info_fn = info_fn or (lambda payload: L.sc.info(payload, timeout=12, retries=1))
    # Retired symbols (registry/retirement-usol-v1.json) are removed from the data checks entirely.
    retire_path = root / 'registry' / 'retirement-usol-v1.json'
    retired = set(L.read_json(retire_path).get('symbols', [])) if retire_path.exists() else set()
    spot_markets = {k: v for k, v in S3.SPOT_MARKETS.items() if k not in retired}
    summary['retired_symbols_excluded'] = sorted(retired)
    pace = Pace(sleep_fn=sleep_fn)
    work = copy.deepcopy(cache)
    for key, _, _, _ in PERP_INTERVALS + SPOT_INTERVALS:
        work.setdefault(key, {})

    # Identity check lives in cache only (spot_meta_ms). No fills.
    if work.get('spot_meta_ms', 0) == 0 or now - work.get('spot_meta_ms', 0) >= 15 * S3.MINUTE:
        spot_raw = request(dict(type='spotMetaAndAssetCtxs'), pace, info_fn)
        tokens = {t['index']: t for t in spot_raw[0]['tokens']}
        by_coin = {c.get('coin'): c for c in spot_raw[1] if isinstance(c, dict) and c.get('coin')}
        for name, mkt in spot_markets.items():
            raw = by_coin.get(mkt['api_coin'])
            if not raw:
                raise ValueError(f"missing spot context {name} {mkt['api_coin']}")
            token = tokens[mkt['token_index']]
            if token['name'] != mkt['token_name'] or int(token['szDecimals']) != int(mkt['szDecimals']):
                raise ValueError(f'spot token identity changed {name}')
        work['spot_meta_ms'] = now

    changed = 0
    isolated = {}
    def _restore(name, keys):
        for key in keys:
            if name in (cache.get(key) or {}):
                work[key][name] = copy.deepcopy(cache[key][name])
            else:
                work.get(key, {}).pop(name, None)
    for coin in S.COINS:
        try:
            for key, interval, step, keep in PERP_INTERVALS:
                if _refresh_series(work, key, coin, coin, interval, step, now, pace, info_fn, keep=keep):
                    changed += 1
            start = min(state.get('next_minute', now) - S3.HOUR, now - 48 * S3.HOUR)
            if _refresh_funding(work, coin, start, now, pace, info_fn):
                changed += 1
        except Exception as e:
            if not isolate:
                raise
            isolated[coin] = repr(e)
            _restore(coin, [k for k, _, _, _ in PERP_INTERVALS] + ['funding'])
    for name, mkt in spot_markets.items():
        api = mkt['api_coin']
        try:
            for key, interval, step, keep in SPOT_INTERVALS:
                if _refresh_series(work, key, name, api, interval, step, now, pace, info_fn, keep=keep):
                    changed += 1
        except Exception as e:
            if not isolate:
                raise
            isolated[name] = repr(e)
            _restore(name, [k for k, _, _, _ in SPOT_INTERVALS])
    if isolate and len(isolated) == len(S.COINS) + len(spot_markets):
        raise ValueError(f'every symbol failed warm-up: {isolated}')

    L.atomic(cache_path, work)
    summary.update(status='warmed' if not isolated else 'warmed_partial_isolated', warmed=True, series_updated=changed,
                   isolated_failures=isolated,
                   requests=len(pace.requests), estimated_weight=pace.weight)
    return summary


def supervisor_alert(root=None, status='SUPERVISOR_RETRY', backoff_s=None,
                     engine_rc=None, error=None, supervisor_pid=None, **extra):
    """Write heartbeat.json with alert=True. Does not write fills or league_state."""
    root = Path(root or L.ROOT)
    details = dict(engine_version=3, alert=True, supervisor=True)
    if supervisor_pid is not None:
        details['supervisor_pid'] = int(supervisor_pid)
    if backoff_s is not None and str(backoff_s) != '':
        details['backoff_s'] = int(backoff_s)
    if engine_rc is not None and str(engine_rc) != '':
        details['engine_rc'] = int(engine_rc)
    if error:
        details['error'] = str(error)
    state_path = root / 'league_state.json'
    if state_path.exists():
        state = L.read_json(state_path)
        if state.get('last_tick_ms'):
            details['last_successful_tick'] = state.get('ticks')
            details['last_successful_tick_ms'] = state.get('last_tick_ms')
            details['last_successful_tick_myt'] = L.sc.myt(state['last_tick_ms'])
    details.update(extra)
    L.heartbeat(root, status, **details)
    return L.read_json(root / 'heartbeat.json')


def main(argv=None):
    ap = argparse.ArgumentParser(description='Pre-warm paper-league public candle cache after a downtime gap')
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--isolate', action='store_true', help='data-isolation v1: per-symbol warm failures do not block other symbols')
    ap.add_argument('--root', default=None)
    ap.add_argument('--alert', default=None, metavar='STATUS',
                    help='Write an alert heartbeat (ENGINE_DOWN / SUPERVISOR_*) and exit; no cache writes')
    ap.add_argument('--backoff', default=None)
    ap.add_argument('--engine-rc', default=None, dest='engine_rc')
    ap.add_argument('--error', default=None)
    ap.add_argument('--supervisor-pid', default=None, dest='supervisor_pid')
    args = ap.parse_args(argv)
    if args.alert:
        rec = supervisor_alert(
            root=args.root, status=args.alert, backoff_s=args.backoff,
            engine_rc=args.engine_rc, error=args.error,
            supervisor_pid=args.supervisor_pid or os.getppid(),
        )
        print(json.dumps(rec, indent=2), flush=True)
        return 0
    summary = warm_cache(root=args.root, force=args.force, isolate=args.isolate)
    print(json.dumps(summary, indent=2), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
