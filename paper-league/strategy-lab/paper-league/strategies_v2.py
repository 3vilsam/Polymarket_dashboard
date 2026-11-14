"""Prospective, desk-defined PAPER families. No learned/tuned parameters or claims."""
import hashlib
import math
import numpy as np
import pandas as pd
from strategies import COINS, MINUTE, HOUR, DAY

# (id, kind, interval, max holding milliseconds, lane)
BASE = [
 ('f1-vwap5m-v1','vwap',5*MINUTE,HOUR,'fast'),
 ('f2-asia15m-v1','asia',15*MINUTE,4*HOUR,'fast'),
 ('f3-rsi2-5m-v1','rsi2',5*MINUTE,HOUR,'fast'),
 ('f4-ema15m-v1','ema',15*MINUTE,12*HOUR,'fast'),
 ('f5-squeeze1m-v1','squeeze',MINUTE,30*MINUTE,'fast'),
 ('l1-supertrend1h-v1','supertrend',HOUR,7*DAY,'slow'),
 ('l2-macd4h-v1','macd',4*HOUR,14*DAY,'slow'),
 ('l3-funding1h-v1','funding',HOUR,72*HOUR,'slow'),
 ('l4-weekly1d-v1','weekly',DAY,28*DAY,'slow'),
 ('c1-random15m-v1','random',15*MINUTE,4*HOUR,'control'),
]
PARAMETERS = {
 'vwap': [dict(window=48,threshold=1.5),dict(window=24,threshold=1.5),dict(window=48,threshold=2.)],
 'asia': [dict(range_hours=4),dict(range_hours=2),dict(range_hours=3)],
 'rsi2': [dict(extreme=5),dict(extreme=10),dict(extreme=2)],
 'ema': [dict(fast=9,slow=21),dict(fast=5,slow=20),dict(fast=12,slow=26)],
 'squeeze': [dict(window=20,quantile=.20),dict(window=20,quantile=.10),dict(window=30,quantile=.20)],
 'supertrend': [dict(atr_n=10,multiplier=3.),dict(atr_n=10,multiplier=2.),dict(atr_n=14,multiplier=3.)],
 'macd': [dict(fast=12,slow=26,signal=9),dict(fast=8,slow=21,signal=9),dict(fast=16,slow=32,signal=9)],
 'funding': [dict(hours=8,threshold=.00005),dict(hours=8,threshold=.000025),dict(hours=24,threshold=.00005)],
 'weekly': [dict(lookback=7),dict(lookback=14),dict(lookback=21)],
 'random': [dict(probability_denominator=12,seed='paper-league-random-v1')],
}
DESCRIPTIONS = {
 'vwap': 'Rolling VWAP=sum(typical_price*base_volume)/sum(base_volume), typical=(H+L+C)/3. Long z=(C-VWAP)/ATR14 crosses below -threshold; short crosses above +threshold. Exit on VWAP recross. Prior z uses prior rolling VWAP and ATR.',
 'asia': 'UTC 00:00 to range_hours:00 (=MYT08:00 onward) completed 15m range. From range end through before UTC08:00 (MYT16:00), buy a close crossing above range high, short crossing below range low. Exit back inside range, opposite side, or at UTC08:00 first actual observation. Range bars must be complete.',
 'rsi2': 'RSI2 gain/loss EWM alpha=1/2 adjust=False first difference seed. Buy RSI crosses below extreme only C>EMA200; short crosses above 100-extreme only C<EMA200. Exit long RSI>=50 or C<EMA200, short RSI<=50 or C>EMA200. Flat RSI=50, positive/no losses=100.',
 'ema': 'EMA adjust=False, close-based fast/slow crossover; long on up-cross, short on down-cross. Exit reverse crossover. Never enter just because a startup trend already exists.',
 'squeeze': 'Bollinger prior bands SMA(window)+/-2 sample SD(ddof=1); width=4SD/SMA. Prior width must be <=20th/10th percentile (configured quantile) of 100 widths ending two bars before current. Buy current C>prior upper, short C<prior lower. Exit on current SMA recross. Prior bands only: no breakout look-ahead.',
 'supertrend': 'Arithmetic ATR(atr_n); basic bands=(H+L)/2 +/- multiplier*ATR. Final upper=min(basic,prior final) unless prior close>prior final upper; lower=max(basic,prior final) unless prior close<prior final lower. Initial direction +1 at first valid ATR; flip only C<final lower in +1, or C>final upper in -1. Enter only on direction change, exit opposite. Fixed protective stop, not a trailing stop.',
 'macd': 'MACD=EMA(fast)-EMA(slow), signal=EMA(signal) of MACD, adjust=False. Buy histogram crossing zero upwards AND MACD>0; short crossing down AND MACD<0. Exit histogram opposite sign. No automatic initial trend entry.',
 'funding': 'Use every settled real hourly funding print strictly before signal boundary in trailing hours; require exactly one per hour. Short mean>threshold only C<EMA20; buy mean<-threshold only C>EMA20. Exit long mean>=0 or C<EMA20; short mean<=0 or C>EMA20. This is a contrarian funding experiment, not an assumed carry edge.',
 'weekly': 'Daily close crosses above prior lookback daily highs or below prior lookback lows (current excluded); default lookback7 is a rolling weekly breakout, not a Monday-open rule. Exit long below prior3 lows, short above prior3 highs. Prior close compared to its own prior lookback range.',
 'random': 'Fixed deterministic SHA256(seed|coin|UTC boundary) interpreted as integer. Enter if value modulo probability_denominator=0; side=+1 if next quotient even else -1. New draw only each closed15m boundary. Fixed1% stop, 4h observed-time exit. Same risk/cost/funding rules; no price/news information enters the random choice.',
}

def entries():
    out=[]
    for id,kind,interval,hold,lane in BASE:
        out.append(dict(id=id,kind=kind,interval=interval,hold_ms=hold,lane=lane,
                        coins=list(COINS),params=PARAMETERS[kind][0],owner='Desk-defined experimental family' if kind!='random' else 'Luck control'))
    # 81 fixed asset/parameter variants; no result-dependent search or pruning.
    for _,kind,interval,hold,lane in BASE[:-1]:
        for coin in COINS:
            for j,p in enumerate(PARAMETERS[kind]):
                out.append(dict(id=f'g-{kind}-{coin.lower()}-p{j}-v1',kind=kind,interval=interval,
                    hold_ms=hold,lane=lane,coins=[coin],params=p,owner='Prospective fixed grid; correlated trials'))
    for _,kind,interval,hold,lane in BASE[:4]:
        out.append(dict(id=f'g-{kind}-all-p1-v1',kind=kind,interval=interval,hold_ms=hold,lane=lane,
                        coins=list(COINS),params=PARAMETERS[kind][1],owner='Prospective fixed grid; correlated trials'))
    assert len(out)==95
    return out

def signal(spec, rows, funding, boundary, coin):
    step=spec['interval']; kind=spec['kind']; p=spec['params']
    rows=[r for r in rows if r['t']+step<=boundary]
    if len(rows)<220:
        raise ValueError(f'{kind} warmup missing')
    # EMA seeds remain immutable and append-only, as in the original books.
    df=pd.DataFrame(rows); c=df.c; prev=c.shift()
    tr=pd.concat([df.h-df.l,(df.h-prev).abs(),(df.l-prev).abs()],axis=1).max(axis=1)
    atr=tr.rolling(14).mean(); ema200=c.ewm(span=200,adjust=False).mean(); ema20=c.ewm(span=20,adjust=False).mean()
    price=float(c.iloc[-1]); stop=max(.005,2*float(atr.iloc[-1])/price)
    o=dict(side=0,exit_long=False,exit_short=False,stop_pct=stop,details={},signal_close=price)
    def cross(a,b):
        return 1 if a.iloc[-2]<=b.iloc[-2] and a.iloc[-1]>b.iloc[-1] else (-1 if a.iloc[-2]>=b.iloc[-2] and a.iloc[-1]<b.iloc[-1] else 0)
    if kind=='vwap':
        w=p['window']; vw=(((df.h+df.l+c)/3*df.v).rolling(w).sum()/df.v.rolling(w).sum())
        z=(c-vw)/atr; a,b=float(z.iloc[-2]),float(z.iloc[-1]); th=p['threshold']
        o.update(side=1 if a>=-th and b<-th else (-1 if a<=th and b>th else 0),exit_long=bool(price>=vw.iloc[-1]),exit_short=bool(price<=vw.iloc[-1]),details=dict(z=b,vwap=float(vw.iloc[-1])))
    elif kind=='asia':
        day=(boundary-1)//DAY*DAY; rh=p['range_hours']; session=day+rh*HOUR
        r=df[(df.t>=day)&(df.t<session)]
        if len(r)==rh*4 and session<=boundary<day+8*HOUR:
            hi,lo=float(r.h.max()),float(r.l.min()); before=float(c.iloc[-2])
            o.update(side=1 if before<=hi<price else (-1 if before>=lo>price else 0),exit_long=bool(price<=hi),exit_short=bool(price>=lo),details=dict(range_high=hi,range_low=lo))
        else:
            o.update(exit_long=True,exit_short=True,details=dict(session='outside entry window or incomplete range'))
    elif kind=='rsi2':
        delta=c.diff(); gain=delta.clip(lower=0).ewm(alpha=.5,adjust=False).mean(); loss=(-delta.clip(upper=0)).ewm(alpha=.5,adjust=False).mean()
        r=100-100/(1+gain/loss); r[(loss==0)&(gain>0)]=100; r[(loss==0)&(gain==0)]=50
        a,b=float(r.iloc[-2]),float(r.iloc[-1]); th=p['extreme']; trend=float(ema200.iloc[-1])
        o.update(side=1 if a>=th>b and price>trend else (-1 if a<=100-th<b and price<trend else 0),exit_long=bool(b>=50 or price<trend),exit_short=bool(b<=50 or price>trend),details=dict(rsi2=b,ema200=trend))
    elif kind=='ema':
        a=c.ewm(span=p['fast'],adjust=False).mean(); b=c.ewm(span=p['slow'],adjust=False).mean(); d=cross(a,b)
        o.update(side=d,exit_long=d==-1,exit_short=d==1,details=dict(fast=float(a.iloc[-1]),slow=float(b.iloc[-1])))
    elif kind=='squeeze':
        w=p['window']; ma=c.rolling(w).mean(); sd=c.rolling(w).std(ddof=1); width=4*sd/ma
        threshold=width.iloc[-102:-2].quantile(p['quantile']); squeezed=width.iloc[-2]<=threshold
        hi,lo=float((ma+2*sd).iloc[-2]),float((ma-2*sd).iloc[-2])
        o.update(side=(1 if price>hi else (-1 if price<lo else 0)) if squeezed else 0,exit_long=bool(price<=ma.iloc[-1]),exit_short=bool(price>=ma.iloc[-1]),details=dict(squeezed=bool(squeezed),prior_upper=hi,prior_lower=lo))
    elif kind=='supertrend':
        a=tr.rolling(p['atr_n']).mean(); m=(df.h+df.l)/2; upper=m+p['multiplier']*a; lower=m-p['multiplier']*a
        start=p['atr_n']-1; fu=float(upper.iloc[start]); fl=float(lower.iloc[start]); direction=1; prior_dir=1
        for i in range(start+1,len(df)):
            u,l=float(upper.iloc[i]),float(lower.iloc[i]); pc=float(c.iloc[i-1]); prior_dir=direction
            fu=u if u<fu or pc>fu else fu; fl=l if l>fl or pc<fl else fl
            if direction==1 and c.iloc[i]<fl: direction=-1
            elif direction==-1 and c.iloc[i]>fu: direction=1
        o.update(side=direction if direction!=prior_dir else 0,exit_long=direction==-1,exit_short=direction==1,details=dict(direction=direction,upper=fu,lower=fl))
    elif kind=='macd':
        mac=c.ewm(span=p['fast'],adjust=False).mean()-c.ewm(span=p['slow'],adjust=False).mean(); hist=mac-mac.ewm(span=p['signal'],adjust=False).mean()
        a,b=float(hist.iloc[-2]),float(hist.iloc[-1]); m=float(mac.iloc[-1])
        o.update(side=1 if a<=0<b and m>0 else (-1 if a>=0>b and m<0 else 0),exit_long=b<=0,exit_short=b>=0,details=dict(macd=m,histogram=b))
    elif kind=='funding':
        f=[x for x in funding if boundary-p['hours']*HOUR<=x['time']<boundary]
        if len(f)!=p['hours'] or len({int(x['time'])//HOUR for x in f})!=p['hours']:
            raise ValueError('funding signal requires complete real hourly prints')
        mean=sum(float(x['fundingRate']) for x in f)/len(f); trend=float(ema20.iloc[-1]); th=p['threshold']
        o.update(side=-1 if mean>th and price<trend else (1 if mean<-th and price>trend else 0),exit_long=bool(mean>=0 or price<trend),exit_short=bool(mean<=0 or price>trend),details=dict(mean_hourly_funding=mean))
    elif kind=='weekly':
        n=p['lookback']; hi=df.h.shift().rolling(n).max(); lo=df.l.shift().rolling(n).min()
        o.update(side=1 if c.iloc[-2]<=hi.iloc[-2] and price>hi.iloc[-1] else (-1 if c.iloc[-2]>=lo.iloc[-2] and price<lo.iloc[-1] else 0),exit_long=bool(price<df.l.iloc[-4:-1].min()),exit_short=bool(price>df.h.iloc[-4:-1].max()),details=dict(prior_high=float(hi.iloc[-1]),prior_low=float(lo.iloc[-1])))
    elif kind=='random':
        n=int(hashlib.sha256(f"{p['seed']}|{coin}|{boundary}".encode()).hexdigest(),16); den=p['probability_denominator']
        o.update(side=(1 if (n//den)%2==0 else -1) if n%den==0 else 0,stop_pct=.01,details=dict(draw_sha256=f'{n:064x}'))
    else: raise ValueError(kind)
    if not math.isfinite(o['stop_pct']) or o['stop_pct']>.045: o['side']=0
    # Flat/zero volume VWAP has no signal, never fabricated liquidity.
    for v in o['details'].values():
        if isinstance(v,float) and not math.isfinite(v):
            o.update(side=0,details=dict(abstain='undefined indicator')); break
    return o
