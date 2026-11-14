"""v4 research-sweep PAPER families (12 Nov 2026). Rules frozen before first live tick.
Source-motivated, fixed parameters chosen from the cited papers' headline settings, never tuned on
league results. No return claim. Public Hyperliquid data only.
"""
import math
from datetime import datetime, timezone
import numpy as np
import pandas as pd
from strategies import COINS, MINUTE, HOUR, DAY
import strategies_v3 as S3

SPOT_START = S3.STARTING_EQUITY

def _perp(id, kind, coins, hold, lane, params, src):
    return dict(id=id, kind=kind, interval=HOUR, hold_ms=hold, lane=lane, coins=list(coins), params=params,
                market='perp', owner='v4 research sweep 2026-11-12; source-motivated, unvalidated', sources=src)

def _spot(id, kind, coin, hold, lane, params, src):
    m = S3.SPOT_MARKETS[coin]
    return dict(id=id, kind=kind, interval=HOUR, hold_ms=hold, lane=lane, coins=[coin], params=params,
                market='spot', leverage=1, long_only=True, sizing='all_in_cash', starting_equity=SPOT_START,
                spot_pair=m['pair'], api_coin=m['api_coin'], price_source=m['price_source'],
                taker_fee=S3.SPOT_TAKER, min_notional=S3.MIN_NOTIONAL, no_funding=True,
                slippage='max(2bp_adverse_mid, L2_notional_walk)',
                owner='v4 research sweep 2026-11-12; source-motivated spot variant, unvalidated', sources=src)

SRC = {
 'tsmom': ['https://www.nber.org/papers/w24877', 'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3309565',
           'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4675565'],
 'shock': ['https://www.tandfonline.com/doi/full/10.1080/15140326.2022.2151253',
           'https://ledgerjournal.org/ojs/ledger/article/view/213'],
 'negfund': ['https://www.aijmr.com/research-paper.php?id=1493', 'https://janorium.com/articles/funding-rate-signal-backtest'],
 'utc21': ['https://quantpedia.com/the-seasonality-of-bitcoin/', 'https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=NART98431919'],
 'weekend': ['https://quantpedia.com/how-to-profitably-trade-bitcoins-overnight-sessions/',
             'https://research.dial.uclouvain.be/server/api/core/bitstreams/e8ffcd60-cb1e-4e49-ac84-09b305474d6b/content'],
 'ratio': ['https://www.utupub.fi/items/3ae68380-4490-4f5b-ab53-55e4c1375ebe', 'https://ijsra.net/sites/default/files/fulltext_pdf/IJSRA-2026-0283.pdf'],
 'xsmom': ['https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4675565', 'https://doi.org/10.1007/s11408-025-00474-9'],
}

DESCRIPTIONS = {
 'tsmom_mh': 'Multi-horizon time-series momentum on closed 1h perp bars. r_h = ln(C_t/C_{t-h}) for h in (6,24,72). agree=+1 if all three >0, -1 if all three <0, else 0. Enter only when agree becomes nonzero (agree_t != 0 and agree_{t-1} != agree_t); never enter on an already-existing startup agreement. Exit long when r24<=0, short when r24>=0, or 72h hold cap. Stop max(0.5%, 3*ATR14/C), abstain if >4.5%.',
 'shock_reversal': 'Long-only reversal after an extreme negative 1h shock. r = 1h log return; sd = sample SD (ddof=1) of the 168 hourly returns before the current bar. Enter long when r_t/sd <= -z (z=3). No signal exit; exit by 24h hold cap, stop or halt. Stop max(1.0%, 3*ATR14/C); abstain if >4.5%.',
 'neg_funding': 'Long BTC perp when the mean of the last 8 settled real hourly Hyperliquid funding prints turns negative (mean_t<0 and the mean of the 8 prints ending one hour earlier >=0). Requires exactly one print per hour for 9 hours or the tick fails closed. No signal exit; 24h hold cap, stop or halt. Stop max(0.5%, 3*ATR14/C), abstain if >4.5%. Not a trend filter, threshold or funding-reverts exit, unlike the frozen g-funding books.',
 'hour_window': 'Calendar control-style seasonality: enter long at the first observation after the 21:00 UTC 1h boundary (bar 20:00-21:00 UTC closed). Exit by the 2h hold cap (~23:00 UTC), stop or halt. Stop max(0.5%, 2*ATR14/C), abstain if >4.5%. No price information in the entry decision except the stop width.',
 'weekend': 'Weekend effect: enter long BTC at the first observation after the Friday 20:00 UTC 1h boundary; exit by the 65h hold cap (~Monday 13:00 UTC), stop or halt. Fixed 4.0% stop. About one trade per week, so 30 trades needs ~7 months; expected to stay NOT_SIGNIFICANT inside any short window.',
 'ratio_mr': 'Single-leg ETH trade on ETH/BTC ratio mean reversion, NOT a hedged pair (engine allows one position per book). R=ln(C_ETH/C_BTC) on timestamp-aligned closed 1h bars; z=(R-mean168)/sd168 (rolling 168 including current, ddof=1). Long ETH when z crosses below -2 (z_{t-1}>=-2>z_t), short ETH when z crosses above +2. Exit long z>=0, short z<=0, or 48h hold cap. Stop max(0.5%, 3*ATR14_ETH/C), abstain if >4.5%. Misaligned/missing BTC bars fail closed.',
 'xs_momentum': 'Cross-sectional momentum over BTC/ETH/SOL perps, decided only at the 00:00 UTC boundary. r72 = ln(C_t/C_{t-72}) on aligned 1h bars. Candidates: top-ranked coin long if its r72>0; bottom-ranked coin short if its r72<0. Pick the single candidate with larger |r72| (one position per book). At 00:00 UTC the held coin exits if it is no longer the selected coin/side. 72h hold cap. Stop max(0.5%, 3*ATR14/C), abstain if >4.5%. Other hours: no entry and no signal exit.',
}

def entries():
    out = [
        _perp('n1-tsmom-mh1h-v1', 'tsmom_mh', COINS, 72*HOUR, 'slow', dict(horizons=[6,24,72], exit_h=24, stop_atr=3.), SRC['tsmom']),
        _perp('n2-shockrev1h-v1', 'shock_reversal', COINS, 24*HOUR, 'slow', dict(window=168, z=3., stop_atr=3., stop_floor=.01), SRC['shock']),
        _perp('n3-negfund-btc-v1', 'neg_funding', ['BTC'], 24*HOUR, 'slow', dict(hours=8, stop_atr=3.), SRC['negfund']),
        _perp('n4-utc21-btc-v1', 'hour_window', ['BTC'], 2*HOUR, 'fast', dict(entry_hour_utc=21, stop_atr=2.), SRC['utc21']),
        _perp('n5-weekend-btc-v1', 'weekend', ['BTC'], 65*HOUR, 'slow', dict(weekday_utc=4, entry_hour_utc=20, stop_pct=.04), SRC['weekend']),
        _perp('n6-ethbtc-z1h-v1', 'ratio_mr', ['ETH'], 48*HOUR, 'slow', dict(window=168, z=2., stop_atr=3., numerator='ETH', denominator='BTC'), SRC['ratio']),
        _perp('n7-xsmom72h-v1', 'xs_momentum', COINS, 72*HOUR, 'slow', dict(lookback=72, rebalance_hour_utc=0, stop_atr=3.), SRC['xsmom']),
        _spot('sp4-utc21-ubtc-v1', 'hour_window', 'UBTC', 2*HOUR, 'spot_fast', dict(entry_hour_utc=21, stop_atr=2.), SRC['utc21']),
        _spot('sp4-shockrev1h-ubtc-v1', 'shock_reversal', 'UBTC', 24*HOUR, 'spot_slow', dict(window=168, z=3., stop_atr=3., stop_floor=.01), SRC['shock']),
    ]
    assert len(out) == 9 and len({s['id'] for s in out}) == 9
    return out

def _closed(rows, step, boundary):
    return [r for r in rows if r['t']+step <= boundary]

def _frame(rows):
    df = pd.DataFrame(rows); c = df.c; prev = c.shift()
    tr = pd.concat([df.h-df.l, (df.h-prev).abs(), (df.l-prev).abs()], axis=1).max(axis=1)
    return df, c, tr.rolling(14).mean()

def _stop(p, atr, price, floor=.005):
    return max(p.get('stop_floor', floor), p['stop_atr']*float(atr.iloc[-1])/price)

def _aligned(series_rows, n):
    """Close series aligned on common timestamps; last n+1 rows required to be contiguous hourly."""
    common = set.intersection(*[{r['t'] for r in rows} for rows in series_rows.values()])
    ts = sorted(common)[-(n+1):]
    if len(ts) < n+1 or any(b-a != HOUR for a, b in zip(ts, ts[1:])):
        raise ValueError('aligned 1h bars missing')
    return ts, {k: {r['t']: r['c'] for r in rows} for k, rows in series_rows.items()}

def core(kind, p, rows, boundary, funding=None, others=None, coin=None):
    """rows: this coin's closed 1h bars; others: {coin: closed 1h rows} for cross-asset kinds."""
    if len(rows) < 200: raise ValueError(f'{kind} warmup missing')
    if rows[-1]['t']+HOUR != boundary: raise ValueError('stale v4 signal')
    df, c, atr = _frame(rows); price = float(c.iloc[-1]); hour = (boundary//HOUR) % 24
    o = dict(side=0, exit_long=False, exit_short=False, stop_pct=_stop(p, atr, price) if 'stop_atr' in p else p.get('stop_pct'),
             details={}, signal_close=price)
    lc = np.log(c)
    if kind == 'tsmom_mh':
        def agree(i):
            rs = [float(lc.iloc[i]-lc.iloc[i-h]) for h in p['horizons']]
            return (1 if all(r > 0 for r in rs) else (-1 if all(r < 0 for r in rs) else 0)), rs
        a_now, rs = agree(-1); a_prev, _ = agree(-2)
        r24 = float(lc.iloc[-1]-lc.iloc[-1-p['exit_h']])
        o.update(side=a_now if a_now and a_prev != a_now else 0, exit_long=r24 <= 0, exit_short=r24 >= 0,
                 details=dict(r6=rs[0], r24=rs[1], r72=rs[2], agree_prev=float(a_prev)))
    elif kind == 'shock_reversal':
        r = lc.diff(); w = p['window']; sd = float(r.iloc[-1-w:-1].std(ddof=1)); last = float(r.iloc[-1])
        z = last/sd if sd > 0 else float('nan')
        o.update(side=1 if math.isfinite(z) and z <= -p['z'] else 0, details=dict(r1h=last, sd168=sd, z=z))
    elif kind == 'neg_funding':
        n = p['hours']; f = [x for x in (funding or []) if boundary-(n+1)*HOUR <= x['time'] < boundary]
        buckets = {}
        for x in f: buckets.setdefault(int(x['time'])//HOUR, []).append(float(x['fundingRate']))
        hours = [boundary//HOUR - k for k in range(n+1, 0, -1)]
        if any(len(buckets.get(h, [])) != 1 for h in hours): raise ValueError('funding signal requires complete real hourly prints')
        vals = [buckets[h][0] for h in hours]
        now_mean = sum(vals[1:])/n; prev_mean = sum(vals[:-1])/n
        o.update(side=1 if now_mean < 0 <= prev_mean else 0, details=dict(mean8=now_mean, prior_mean8=prev_mean))
    elif kind == 'hour_window':
        o.update(side=1 if hour == p['entry_hour_utc'] else 0, details=dict(boundary_hour_utc=float(hour)))
    elif kind == 'weekend':
        wd = datetime.fromtimestamp(boundary/1000, timezone.utc).weekday()
        o.update(side=1 if wd == p['weekday_utc'] and hour == p['entry_hour_utc'] else 0,
                 details=dict(weekday_utc=float(wd), boundary_hour_utc=float(hour)))
    elif kind == 'ratio_mr':
        w = p['window']
        ts, cl = _aligned({k: others[k] for k in (p['numerator'], p['denominator'])}, w+1)
        if ts[-1] != rows[-1]['t']: raise ValueError('ratio bars not current')
        R = pd.Series([math.log(cl[p['numerator']][t]/cl[p['denominator']][t]) for t in ts])
        m = R.rolling(w).mean(); s = R.rolling(w).std(ddof=1); z = (R-m)/s
        a, b = float(z.iloc[-2]), float(z.iloc[-1]); th = p['z']
        o.update(side=1 if a >= -th > b else (-1 if a <= th < b else 0), exit_long=b >= 0, exit_short=b <= 0,
                 details=dict(z=b, prior_z=a))
    elif kind == 'xs_momentum':
        if hour != p['rebalance_hour_utc']:
            o.update(details=dict(rebalance=0.)); return _finish(o)
        n = p['lookback']; ts, cl = _aligned(others, n)
        if ts[-1] != rows[-1]['t']: raise ValueError('xs bars not current')
        r = {k: math.log(cl[k][ts[-1]]/cl[k][ts[0]]) for k in others}
        order = sorted(r, key=lambda k: r[k]); top, bot = order[-1], order[0]
        cands = []
        if r[top] > 0: cands.append((abs(r[top]), top, 1))
        if r[bot] < 0: cands.append((abs(r[bot]), bot, -1))
        sel = max(cands) if cands else None
        side = sel[2] if sel and sel[1] == coin else 0
        o.update(side=side, exit_long=not (sel and sel[1] == coin and sel[2] == 1),
                 exit_short=not (sel and sel[1] == coin and sel[2] == -1),
                 details=dict(rebalance=1., **{f'r72_{k}': float(v) for k, v in r.items()}))
    else:
        raise ValueError(kind)
    return _finish(o)

def _finish(o):
    if o['stop_pct'] is None or not math.isfinite(o['stop_pct']) or o['stop_pct'] > .045: o['side'] = 0
    for v in o['details'].values():
        if isinstance(v, float) and not math.isfinite(v):
            o.update(side=0, details=dict(abstain='undefined indicator')); break
    return o

def signal(spec, data, boundary, coin):
    """Perp books. data uses the frozen v3 collector keys: h1 rows and funding per coin."""
    step = spec['interval']; assert step == HOUR
    rows = _closed(data['h1'][coin], step, boundary)
    others = {k: _closed(data['h1'][k], step, boundary) for k in COINS} if spec['kind'] in ('ratio_mr', 'xs_momentum') else None
    return core(spec['kind'], spec['params'], rows, boundary, data['funding'].get(coin), others, coin)

def spot_signal(spec, data, boundary, coin):
    rows = _closed(data['spot_h1'][coin], HOUR, boundary)
    o = core(spec['kind'], spec['params'], rows, boundary, coin=coin)
    if o['side'] < 0: o['side'] = 0
    o['exit_short'] = False
    return o
