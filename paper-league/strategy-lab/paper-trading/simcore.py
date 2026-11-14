"""Public-data and paper-accounting primitives for the league.

The frozen manifest hashes strategy-lab/paper-trading/simcore.py, and that file was not in the
league export. This module is a reconstruction of the surface league.py, league_v3.py and the
unit tests actually call. It is paper-only: one public POST to the Hyperliquid info endpoint,
no key, signature, wallet, or exchange write.

Replace this file with the original bytes when they are available. run_tick.py stops substituting
the frozen digest as soon as the bytes match.
"""
from __future__ import annotations

import json
import math
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from decimal import Decimal, ROUND_FLOOR
from zoneinfo import ZoneInfo

INFO_URL = 'https://api.hyperliquid.xyz/info'
MYT = ZoneInfo('Asia/Kuala_Lumpur')
# Public info types the league collectors already allow. Anything else is refused here too.
PUBLIC_TYPES = {
    'allMids', 'metaAndAssetCtxs', 'spotMetaAndAssetCtxs', 'candleSnapshot',
    'fundingHistory', 'l2Book', 'spotMeta',
}

DEFAULT_CONFIG = dict(
    starting_equity=100.0,
    taker_fee=0.00045,
    maker_fee=0.00015,
    max_leverage=3.0,
    max_positions=2,
    cluster_max=1,
    stop_slippage_bps=5.0,
    entry_slippage_bps=2.0,
    funding_reserve_hours=24,
    min_notional=10.0,
    strategies=[],
)


def now_ms():
    return int(time.time() * 1000)


def myt(t=None):
    """Asia/Kuala_Lumpur wall time, seconds, no milliseconds. Matches last_tick.ts_myt."""
    if t is None:
        t = now_ms()
    dt = datetime.fromtimestamp(t / 1000, timezone.utc).astimezone(MYT)
    return dt.isoformat(timespec='seconds')


def myt_date(t):
    if t is None:
        t = now_ms()
    return datetime.fromtimestamp(t / 1000, timezone.utc).astimezone(MYT).date().isoformat()


def load_config(path=None):
    """Original PASS allowlist is empty. The path is ignored; nothing is read from disk that could enable a strategy."""
    return dict(DEFAULT_CONFIG, strategies=[])


def strategy_gate(cfg, name):
    allowed = set(cfg.get('strategies') or [])
    if name in allowed:
        return True, 'allowlisted'
    return False, 'not on the empty PASS allowlist'


def new_state(cfg):
    eq = float(cfg.get('starting_equity', 100.0))
    return dict(
        version=1,
        cash=eq,
        starting_equity=eq,
        day_start_equity=eq,
        positions={},
        closed_trades=[],
        stats=dict(trades_closed=0, wins=0, losses=0, net_pnl=0.0, fees=0.0, funding=0.0),
        marks={},
        halted=False,
        halt_reason=None,
        next_seq=1,
        peak=eq,
        max_drawdown_pct=0.0,
    )


def unrealized(book):
    total = 0.0
    marks = book.get('marks') or {}
    for p in (book.get('positions') or {}).values():
        mark = marks.get(p['coin'], p['entry_px'])
        total += p['dir'] * p['size'] * (mark - p['entry_px'])
    return total


def equity(book):
    return float(book.get('cash', 0.0)) + unrealized(book)


def floor_sz(qty, decimals):
    if qty is None or not isinstance(qty, (int, float)) or not math.isfinite(qty) or qty <= 0:
        return 0.0
    quantum = Decimal(1).scaleb(-int(decimals))
    q = Decimal(f'{qty:.12f}').quantize(quantum, rounding=ROUND_FLOOR)
    return float(q)


def _slip(cfg):
    return float(cfg.get('stop_slippage_bps', 5.0)) / 1e4


def entry_risk(px, stop, qty, cfg):
    """Per the 13 Nov risk review: distance + entry taker + stop*(taker+stop slip), times qty.

    Funding reserve is added by league.risk_per_unit, not here.
    """
    taker = float(cfg['taker_fee'])
    slip = _slip(cfg)
    per = abs(px - stop) + px * taker + abs(stop) * (taker + slip)
    return per * qty


def position_risk(p, cfg):
    """Remaining loss if the stop fills, excluding fees and funding already on the position.

    enforce_cost_risk adds p['fees'] and subtracts p['funding'] itself. A missing stop
    (benchmark / hold) contributes no stop risk.
    """
    stop = p.get('stop')
    if stop is None or not p.get('size'):
        return 0.0
    taker = float(cfg['taker_fee'])
    slip = _slip(cfg)
    per = abs(p['entry_px'] - stop) + abs(stop) * (taker + slip)
    return p['size'] * per


def open_risk(book, cfg):
    return sum(position_risk(p, cfg) for p in (book.get('positions') or {}).values())


def notional_open(book):
    marks = book.get('marks') or {}
    total = 0.0
    for p in (book.get('positions') or {}).values():
        px = marks.get(p['coin'], p['entry_px'])
        total += abs(p['size'] * px)
    return total


def walk_book(depth, direction, qty):
    """Walk asks for a long and bids for a short. Returns (vwap, filled).

    Size past the visible book stays at the worst visible price so the fill is not improved
    by inventing deeper liquidity.
    """
    if qty is None or qty <= 0:
        return None, 0.0
    levels = list(depth['asks'] if direction > 0 else depth['bids'])
    levels.sort(key=lambda level: level[0], reverse=direction < 0)
    if not levels:
        raise ValueError('empty book')
    left = float(qty)
    notional = 0.0
    filled = 0.0
    last = float(levels[0][0])
    for px, sz in levels:
        px, sz = float(px), float(sz)
        last = px
        if left <= 1e-12:
            break
        take = min(sz, left)
        notional += take * px
        filled += take
        left -= take
    if left > 1e-12:
        notional += left * last
        filled += left
    return (notional / filled if filled else last), filled


def info(payload, timeout=12, retries=1):
    """POST the public info endpoint. No API key, signature, or account field is sent."""
    if not isinstance(payload, dict):
        raise ValueError('info payload must be an object')
    typ = payload.get('type')
    if typ not in PUBLIC_TYPES:
        raise ValueError(f'non-public info type refused: {typ}')
    for forbidden in ('signature', 'privateKey', 'vaultAddress', 'nonce', 'action'):
        if forbidden in payload:
            raise ValueError('refusing signed or account payload')
    body = json.dumps(payload).encode()
    last = None
    attempts = int(retries) + 1
    for attempt in range(attempts):
        req = urllib.request.Request(
            INFO_URL, data=body, headers={'Content-Type': 'application/json'}, method='POST')
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            detail = e.read().decode('utf-8', errors='replace')[:300]
            last = RuntimeError(f'HTTP {e.code} {detail}')
            if attempt + 1 < attempts and e.code in (429, 500, 502, 503):
                time.sleep(min(2.0, 0.25 * (attempt + 1)))
                continue
            raise last
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            last = e
            if attempt + 1 < attempts:
                time.sleep(0.25)
                continue
            raise
    raise last
