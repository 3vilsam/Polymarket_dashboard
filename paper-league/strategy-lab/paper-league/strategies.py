"""Frozen causal signal definitions; paper research, not validated trading advice."""
import math
import numpy as np
import pandas as pd

COINS = ('BTC', 'ETH', 'SOL')
MINUTE, HOUR, DAY = 60000, 3600000, 86400000

def indicators(rows):
    df = pd.DataFrame(rows).sort_values('t').reset_index(drop=True)
    c = df.c
    df['ema200'] = c.ewm(span=200, adjust=False).mean()
    df['ema20'] = c.ewm(span=20, adjust=False).mean()
    prev = c.shift()
    tr = np.maximum(df.h-df.l, np.maximum((df.h-prev).abs(), (df.l-prev).abs()))
    df['atr'] = tr.rolling(14).mean()
    ap = df.atr / c
    df['atr_rank'] = ap.rolling(500).apply(lambda a: (a[:-1] < a[-1]).mean(), raw=True)
    delta = c.diff()
    # Wilder-style recursion with first difference as seed; warmup 200 bars.
    gain = delta.clip(lower=0).ewm(alpha=1/14, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1/14, adjust=False).mean()
    df['rsi'] = 100 - 100/(1 + gain/loss)
    df.loc[(loss == 0) & (gain > 0), 'rsi'] = 100
    df.loc[(loss == 0) & (gain == 0), 'rsi'] = 50
    return df

def signal(kind, rows, funding, boundary):
    """Only closed candles t+interval<=boundary; caller persists the fixed seed."""
    interval = DAY if kind == 'ewmac' else 4*HOUR
    rows = [r for r in rows if r['t']+interval <= boundary]
    need = 700 if kind == 'donchian' else (200 if kind in ('bb', 'rsi') else 128)
    if len(rows) < need:
        raise ValueError(f'{kind} warmup: {len(rows)} < {need}')
    df = indicators(rows)
    i, c = len(df)-1, float(df.c.iloc[-1])
    out = dict(side=0, exit_long=False, exit_short=False, stop_pct=.03,
               signal_close=c, signal_t=int(df.t.iloc[-1]), details={})
    if kind == 'donchian':
        hh, ll = df.h.iloc[i-40:i].max(), df.l.iloc[i-40:i].min()
        hx, lx = df.h.iloc[i-20:i].max(), df.l.iloc[i-20:i].min()
        side = 1 if c > hh else (-1 if c < ll else 0)
        out.update(exit_long=bool(c < lx), exit_short=bool(c > hx))
        out['details'] = dict(prior_high=float(hh), prior_low=float(ll), atr_rank=float(df.atr_rank.iloc[-1]))
        if not df.atr_rank.iloc[-1] < .8:
            side = 0
    elif kind == 'bb':
        ma, sd = df.c.iloc[-40:].mean(), df.c.iloc[-40:].std(ddof=1)
        z = (c-ma)/sd if sd else 0
        side = 1 if z < -2 else (-1 if z > 2 else 0)
        out.update(exit_long=bool(c >= ma), exit_short=bool(c <= ma))
        out['details'] = dict(z=float(z), sma40=float(ma))
    elif kind == 'rsi':
        r, prev = float(df.rsi.iloc[-1]), float(df.rsi.iloc[-2])
        trend = c > df.ema200.iloc[-1] and df.ema20.iloc[-1] > df.ema200.iloc[-1]
        side = 1 if trend and prev < 40 <= r else 0
        out.update(exit_long=bool(c < df.ema200.iloc[-1] or r >= 60),
                   stop_pct=float(2*df.atr.iloc[-1]/c))
        if not .005 <= out['stop_pct'] <= .045:
            side = 0
        out['details'] = dict(rsi=r, prior_rsi=prev, trend=bool(trend))
    elif kind == 'ewmac':
        dp = df.c.diff().ewm(span=25, adjust=False).std().iloc[-1]
        ann = df.c.pct_change().ewm(span=25, adjust=False).std().iloc[-1]*math.sqrt(365)
        forecasts = []
        for fast, slow, scalar in ((8,32,5.3),(16,64,3.75),(32,128,2.65)):
            raw = (df.c.ewm(span=fast, adjust=False).mean().iloc[-1] - df.c.ewm(span=slow, adjust=False).mean().iloc[-1])/dp if dp > 0 else 0
            forecasts.append(float(np.clip(raw*scalar, -20, 20)))
        fc = sum(forecasts)/3
        if not np.isfinite(ann) or ann <= 0:
            fc, ann = 0., 1.
        side = int(np.sign(fc))
        out.update(stop_pct=.045, forecast=fc, vol_scale=.20/ann,
                   exit_long=bool(fc <= 0), exit_short=bool(fc >= 0))
        out['details'] = dict(forecast=fc, annualized_vol=float(ann), component_forecasts=forecasts)
        out['side'] = side
        return out
    else:
        raise ValueError(kind)
    if kind in ('donchian','bb'):
        if (side == 1 and not c > df.ema200.iloc[-1]) or (side == -1 and not c < df.ema200.iloc[-1]):
            side = 0
    if kind == 'donchian':
        # Funding rows are timestamped a few milliseconds after the hour; no look-ahead.
        f = [float(x['fundingRate']) for x in funding if boundary-24*HOUR <= x['time'] < boundary]
        buckets = {int(x['time'])//HOUR for x in funding if boundary-24*HOUR <= x['time'] < boundary}
        if len(f) != 24 or len(buckets) != 24:
            raise ValueError('Donchian needs all 24 observed hourly funding prints')
        mean = sum(f)/24
        out['details']['funding24_mean'] = mean
        if (side == 1 and mean > .000025) or (side == -1 and mean < 0):
            side = 0
    out['side'] = side
    return out
