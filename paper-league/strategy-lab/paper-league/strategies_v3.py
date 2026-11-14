"""Spot-only, long-only, no-leverage PAPER families. Rules frozen before first live tick.
No learned/tuned parameters or return claims. Public Hyperliquid spot pairs only.
"""
from strategies import MINUTE, HOUR, DAY
import math
import pandas as pd

STARTING_EQUITY = 16.24
SPOT_TAKER = 0.00070  # official tier-0 spot taker, https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees
SPOT_MAKER = 0.00040  # official tier-0 spot maker; documented only, never charged without a resting-limit model
SLIP_FLOOR_BPS = 2.0
STOP_SLIP_BPS = 5.0
MIN_NOTIONAL = 10.0
FEE_SOURCE = 'https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees'
FEE_SOURCE_RETRIEVED_MYT = '2026-11-11'

# Live mainnet spot pairs verified 2026-11-11 via spotMeta / spotMetaAndAssetCtxs / allMids / l2Book.
# None of these four needs a perp-mid proxy.
SPOT_MARKETS = {
    'UBTC': dict(pair='UBTC/USDC', api_coin='@142', token_index=197, universe_index=142, szDecimals=5,
                 price_source='spot_pair', token_name='UBTC'),
    'UETH': dict(pair='UETH/USDC', api_coin='@151', token_index=221, universe_index=151, szDecimals=4,
                 price_source='spot_pair', token_name='UETH'),
    'USOL': dict(pair='USOL/USDC', api_coin='@156', token_index=254, universe_index=156, szDecimals=3,
                 price_source='spot_pair', token_name='USOL'),
    'HYPE': dict(pair='HYPE/USDC', api_coin='@107', token_index=150, universe_index=107, szDecimals=2,
                 price_source='spot_pair', token_name='HYPE'),
}
SPOT_COINS = tuple(SPOT_MARKETS)

DESCRIPTIONS = {
    'spot_hold': 'All-in 1x long buy-and-hold of the registered USDC spot pair at the first actually observed mid after activation, plus max(2bp, L2 walk) adverse slippage and official tier-0 spot taker 0.070%. No stop, no daily-halt flatten, no funding, no rebalance, no shorts, no leverage. Measurement control only; not a tradable strategy or risk-limits exception for live trading.',
    'spot_ema': 'Long-only EMA(fast)/EMA(slow) close-based crossover on fully closed UTC bars, adjust=False. Enter only on an up-cross (prior fast<=slow and current fast>slow). Exit on a down-cross, the fixed protective stop, the hold cap at the first later observed quote, or the daily halt. Never enter just because a startup trend already exists. Never short.',
    'spot_rsi': 'Long-only RSI14 pullback. RSI uses first-difference seed, EWM alpha=1/14 adjust=False; 100 if losses=0 and gains>0, 50 if both 0. Buy only when RSI crosses up from below the oversold threshold (prior<=threshold and current>threshold) AND close>EMA200. Exit when RSI>=70, close<EMA200, stop, hold cap, or daily halt. Never short.',
    'spot_donchian': 'Long-only Donchian breakout on fully closed UTC 5m bars. Buy when the current close crosses above the prior lookback-bar high (current bar excluded from the range). Exit when the current close is below the prior exit_lookback-bar low (current excluded), or on stop, the 4h hold cap, or daily halt. Never short.',
}

# 4 buy-and-hold controls + 4 coins x (EMA 15m, RSI 1h, Donchian 4h) = 16 books.
def entries():
    out=[]
    for coin,mkt in SPOT_MARKETS.items():
        common=dict(coins=[coin], market='spot', leverage=1, long_only=True, sizing='all_in_cash',
                    starting_equity=STARTING_EQUITY, spot_pair=mkt['pair'], api_coin=mkt['api_coin'],
                    price_source=mkt['price_source'], taker_fee=SPOT_TAKER,
                    maker_fee_documented=SPOT_MAKER, min_notional=MIN_NOTIONAL, no_funding=True,
                    slippage='max(2bp_adverse_mid, L2_notional_walk)',
                    owner='Desk-defined spot experiment at owner request; unvalidated')
        out.append(dict(common, id=f'sp-hold-{coin.lower()}-v1', kind='spot_hold', interval=MINUTE,
                        hold_ms=10*365*DAY, lane='spot_control', params={},
                        owner='Spot buy-and-hold control; not a tradable strategy'))
        out.append(dict(common, id=f'sp-ema15m-{coin.lower()}-v1', kind='spot_ema', interval=15*MINUTE,
                        hold_ms=12*HOUR, lane='spot_fast', params=dict(fast=9,slow=21)))
        out.append(dict(common, id=f'sp-rsi1h-{coin.lower()}-v1', kind='spot_rsi', interval=HOUR,
                        hold_ms=7*DAY, lane='spot_slow', params=dict(length=14,oversold=30,overbought=70)))
        out.append(dict(common, id=f'sp-donchian5m-{coin.lower()}-v1', kind='spot_donchian', interval=5*MINUTE,
                        hold_ms=4*HOUR, lane='spot_fast', params=dict(lookback=20,exit_lookback=10)))
    assert len(out)==16
    assert len({s['id'] for s in out})==16
    return out

def signal(spec, rows, boundary):
    step=spec['interval']; kind=spec['kind']; p=spec['params']
    rows=[r for r in rows if r['t']+step<=boundary]
    if kind=='spot_hold':
        return dict(side=0,exit_long=False,exit_short=False,stop_pct=None,details=dict(control='hold'),signal_close=None)
    if len(rows)<220:
        raise ValueError(f'{kind} warmup missing')
    df=pd.DataFrame(rows); c=df.c; prev=c.shift()
    tr=pd.concat([df.h-df.l,(df.h-prev).abs(),(df.l-prev).abs()],axis=1).max(axis=1)
    atr=tr.rolling(14).mean(); ema200=c.ewm(span=200,adjust=False).mean()
    price=float(c.iloc[-1]); stop=max(.005,2*float(atr.iloc[-1])/price)
    o=dict(side=0,exit_long=False,exit_short=False,stop_pct=stop,details={},signal_close=price)
    def cross(a,b):
        return 1 if a.iloc[-2]<=b.iloc[-2] and a.iloc[-1]>b.iloc[-1] else (-1 if a.iloc[-2]>=b.iloc[-2] and a.iloc[-1]<b.iloc[-1] else 0)
    if kind=='spot_ema':
        a=c.ewm(span=p['fast'],adjust=False).mean(); b=c.ewm(span=p['slow'],adjust=False).mean(); d=cross(a,b)
        # Long-only: a down-cross is an exit, never a short entry.
        o.update(side=1 if d==1 else 0, exit_long=d==-1, details=dict(fast=float(a.iloc[-1]),slow=float(b.iloc[-1]),raw_cross=d))
    elif kind=='spot_rsi':
        n=p['length']; delta=c.diff()
        gain=delta.clip(lower=0).ewm(alpha=1/n,adjust=False).mean(); loss=(-delta.clip(upper=0)).ewm(alpha=1/n,adjust=False).mean()
        r=100-100/(1+gain/loss); r[(loss==0)&(gain>0)]=100; r[(loss==0)&(gain==0)]=50
        a,b=float(r.iloc[-2]),float(r.iloc[-1]); trend=float(ema200.iloc[-1]); th=p['oversold']
        o.update(side=1 if a<=th<b and price>trend else 0,
                 exit_long=bool(b>=p['overbought'] or price<trend),
                 details=dict(rsi=b,ema200=trend))
    elif kind=='spot_donchian':
        n=p['lookback']; m=p['exit_lookback']
        hi=df.h.shift().rolling(n).max(); lo=df.l.shift().rolling(m).min()
        o.update(side=1 if c.iloc[-2]<=hi.iloc[-2] and price>hi.iloc[-1] else 0,
                 exit_long=bool(price<lo.iloc[-1]),
                 details=dict(prior_high=float(hi.iloc[-1]),prior_exit_low=float(lo.iloc[-1])))
    else:
        raise ValueError(kind)
    if o['stop_pct'] is not None and (not math.isfinite(o['stop_pct']) or o['stop_pct']>.045):
        o['side']=0
    for v in o['details'].values():
        if isinstance(v,float) and not math.isfinite(v):
            o.update(side=0,details=dict(abstain='undefined indicator')); break
    if o['side']<0:
        o['side']=0
    return o
