#!/usr/bin/env python3
"""Append-only SPOT PAPER expansion. Frozen v1 and v2 implementations stay byte-identical.
Public /info reads only; no wallet, key, order, signing, testnet or exchange write.
"""
import argparse
import copy
import fcntl
import gzip
import json
import math
import os
import resource
from pathlib import Path
import signal as signals
import time
from collections import Counter
import league as L
import league_v2 as V
import strategies as S  # BTC/ETH/SOL constants only; v2 frozen signals stay in strategies_v2
import strategies_v3 as S3
import evaluation_v3 as E

ROOT=L.ROOT
RUNNING=True
STARTING=S3.STARTING_EQUITY
SPOT_TAKER=S3.SPOT_TAKER

def registration(root=ROOT):
    old,ext=V.registration(root)
    spot=L.read_json(root/'registry/spot-extension-v3.json')
    if spot.get('mode')!='PAPER_ONLY' or len(spot['strategies'])!=16:
        raise ValueError('16 append-only PAPER spot registrations required')
    if spot['original_manifest_sha256']!=L.sha(root/'registry/manifest.json'):
        raise ValueError('original registration changed')
    if spot['extension_v2_sha256']!=L.sha(root/'registry/extension-v2.json'):
        raise ValueError('v2 extension changed')
    for n,d in spot['implementation_sha256'].items():
        if L.sha(root/n)!=d: raise ValueError(f'frozen spot implementation changed: {n}')
    for s in spot['strategies']:
        if L.sha(root/'registry'/f"{s['id']}.md")!=s['sha256']:
            raise ValueError(f"frozen spot rules changed: {s['id']}")
    ids={s['id'] for s in old['strategies']+ext['strategies']+spot['strategies']}
    if len(ids)!=116: raise ValueError('duplicate or missing book id')
    return old,ext,spot

def new_spot_book(s, now):
    cfg=dict(L.CFG, starting_equity=STARTING, taker_fee=SPOT_TAKER, max_leverage=1.0)
    b=L.sc.new_state(cfg)
    b.update(id=s['id'], owner=s['owner'], kind=s['kind'], lane=s['lane'], events=[],
             peak=STARTING, max_drawdown_pct=0., decisions={}, stopped_sides={},
             day_date=L.sc.myt_date(now), last_tick_myt=None, spot_spec=s,
             activation_ms=now, market='spot', leverage=1, starting_equity=STARTING)
    L.event(b,'registered',now,rules_sha256=s['sha256'],status='UNPROVEN_PAPER_ONLY',
            starting_equity=STARTING,market='spot',leverage=1,long_only=True,
            no_liquidation=True,no_funding=True,price_source=s['price_source'],
            spot_pair=s['spot_pair'],api_coin=s['api_coin'])
    return b

def extend(st, old, ext, spot, now, v2digest, v3digest):
    if st.get('registration_sha256',L.sha(ROOT/'registry/manifest.json'))!=ext['original_manifest_sha256']:
        raise ValueError('persisted original registry mismatch')
    expected_v2={s['id'] for s in old['strategies']+ext['strategies']}
    if 'extension_registration_sha256' not in st:
        if set(st['books'])-expected_v2:
            raise ValueError('unexpected extra books before v2 extend')
        V.extend(st,old,ext,now,v2digest)
    else:
        if st['extension_registration_sha256']!=v2digest:
            raise ValueError('persisted extension registry mismatch')
        if not expected_v2.issubset(st['books']):
            raise ValueError('missing v2 book')
        for s in ext['strategies']:
            if st['books'][s['id']].get('spec')!=s: raise ValueError('persisted spec changed')
    if st.get('spot_extension_registration_sha256',v3digest)!=v3digest:
        raise ValueError('persisted spot extension registry mismatch')
    if 'spot_extension_registration_sha256' not in st:
        if set(st['books'])!=expected_v2:
            raise ValueError('unexpected books at spot migration')
        for s in spot['strategies']:
            st['books'][s['id']]=new_spot_book(s,now)
        st.update(spot_extension_registration_sha256=v3digest,spot_extension_created_ms=now,version=3)
    expected=expected_v2|{s['id'] for s in spot['strategies']}
    if set(st['books'])!=expected: raise ValueError('missing/unregistered book')
    for s in spot['strategies']:
        if st['books'][s['id']].get('spot_spec')!=s: raise ValueError('persisted spot spec changed')
        if abs(st['books'][s['id']].get('starting_equity',0)-STARTING)>1e-12:
            raise ValueError('spot starting equity changed')
    return st

def walk_notional(levels, notional):
    acc_nt=0.; acc_sz=0.
    for px,sz in levels:
        remain=notional-acc_nt
        if remain<=0: break
        use=min(sz, remain/px)
        acc_sz+=use; acc_nt+=use*px
    if acc_sz<=0 or acc_nt<notional-1e-8: return None
    return acc_nt/acc_sz

def fill_price(mid, direction, depth, notional):
    """More-adverse of 2bp mid floor and L2 walk. direction +1 buy / -1 sell."""
    floor=mid*(1+direction*S3.SLIP_FLOOR_BPS/1e4)
    if not depth: return floor, 'observed_mid_plus_2bps_floor'
    levels=depth['asks' if direction>0 else 'bids']
    walked=walk_notional(levels, notional)
    if walked is None: return floor, 'observed_mid_plus_2bps_floor_insufficient_visible_depth'
    if direction>0: px,src=max(floor,walked), 'max(2bp_floor,L2_ask_walk)'
    else: px,src=min(floor,walked), 'max(2bp_floor,L2_bid_walk)'
    return px, src

def spot_close(book, p, px, t, why, qty=None, **notes):
    qty=min(p['size'], qty if qty is not None else p['size'])
    gross=p['dir']*qty*(px-p['entry_px'])
    fee=qty*px*SPOT_TAKER
    book['cash']+=gross-fee
    book['stats']['fees']+=fee
    p['realized_gross']+=gross
    p['fees']+=fee
    p['size']=max(0., round(p['size']-qty,12))
    L.event(book,'exit',t,trade_id=p['id'],coin=p['coin'],side=p['side'],
            size=qty,price=px,fee=fee,pnl_gross=gross,reason=why,market='spot',**notes)
    if p['size']<1e-10:
        net=p['realized_gross']-p['fees']+p['funding']
        del book['positions'][p['id']]
        book['stats']['trades_closed']+=1
        book['stats']['net_pnl']+=net
        book['stats']['wins' if net>0 else 'losses']+=1
        tr=dict(id=p['id'],coin=p['coin'],entry_ms=p['entry_ms'],exit_ms=t,
                pnl_net=net,fees=p['fees'],funding=p['funding'],reason=why,market='spot')
        book['closed_trades'].append(tr)
        L.event(book,'net_pnl',t,**tr)

def spot_resolve_stop(book, p, bar, observed):
    if p.get('stop') is None: return False
    if bar['t']+S3.MINUTE<=p['entry_ms']: return False
    entry_minute_ambiguous=bar['t']<p['entry_ms']
    adverse=bar['l'] if p['dir']>0 else bar['h']
    if L.hit_adverse(p, adverse):
        gap=L.hit_adverse(p, bar['o']) and not entry_minute_ambiguous
        cfg=dict(L.CFG, taker_fee=SPOT_TAKER, stop_slippage_bps=S3.STOP_SLIP_BPS)
        px=L.stop_fill(p,cfg,bar['o'] if not entry_minute_ambiguous else p['stop'])
        ts=bar['t'] if gap else bar['t']+S3.MINUTE-1
        spot_close(book,p,px,ts,'stop',bar_t=bar['t'],observed_at_utc=L.utc(observed),
                   replayed=observed-bar['t']>2*S3.MINUTE,gap_through_stop=gap,
                   stop_trigger=p['stop'],bar_resolution='1m',entry_minute_ambiguous=entry_minute_ambiguous,
                   fill_timing='bar_open_gap' if gap else 'intraminute_unknown_stop_assumed',
                   fill_source='virtual_stop_plus_5bp')
        return True
    return False

def spot_open(book, coin, stop_pct, mid, now, ctx, depth):
    if book['halted'] or book['kind']=='spot_hold': return False
    if stop_pct is None or not .005<=stop_pct<=.045: return False
    if book['positions']:
        L.event(book,'reject',now,coin=coin,reason='spot_one_position_max')
        return False
    eq=L.sc.equity(book)
    if eq<=0: return False
    fill,src=fill_price(mid,1,depth,eq)
    stop=fill*(1-stop_pct)
    dec=ctx[coin]['szDecimals']
    qty=L.sc.floor_sz(eq/(fill*(1+SPOT_TAKER)),dec)
    if qty<=0 or qty*fill<S3.MIN_NOTIONAL:
        L.event(book,'reject',now,coin=coin,reason='minimum_notional_10_or_zero_lot',
                proposed_notional=qty*fill,equity=eq)
        return False
    notional=qty*fill
    if notional>eq+1e-9:
        L.event(book,'reject',now,coin=coin,reason='spot_1x_cap'); return False
    fee=notional*SPOT_TAKER
    tid=f"P{book['next_seq']:06d}"; book['next_seq']+=1
    p=dict(id=tid,coin=coin,dir=1,side='long',size=qty,size_initial=qty,
           entry_px=fill,entry_ms=now,stop=stop,fees=fee,realized_gross=0.,funding=0.,
           funding_hour=now//S3.HOUR,market='spot',leverage=1,spot=True)
    book['positions'][tid]=p
    book['cash']-=fee
    book['stats']['fees']+=fee
    L.event(book,'entry',now,trade_id=tid,coin=coin,side='long',size=qty,price=fill,
            stop=stop,fee=fee,fill_source=src,market='spot',leverage=1,fee_rate=SPOT_TAKER,
            price_source=book['spot_spec']['price_source'],spot_pair=book['spot_spec']['spot_pair'])
    return True

def start_spot_hold(book, data, now):
    if book.get('benchmark_started') or book['positions']: return
    coin=book['spot_spec']['coins'][0]
    mid=data['mids'][coin]; depth=data.get('spot_books',{}).get(coin)
    eq=L.sc.equity(book)
    fill,src=fill_price(mid,1,depth,eq)
    dec=data['spot_ctx'][coin]['szDecimals']
    qty=L.sc.floor_sz(eq/(fill*(1+SPOT_TAKER)),dec)
    if qty<=0 or qty*fill<S3.MIN_NOTIONAL:
        L.event(book,'reject',now,coin=coin,reason='hold_minimum_notional_10',proposed_notional=qty*fill)
        return
    fee=qty*fill*SPOT_TAKER
    book['cash']-=fee
    book['stats']['fees']+=fee
    book['positions']['SPOT_HOLD']=dict(id='SPOT_HOLD',coin=coin,dir=1,side='long',size=qty,
        size_initial=qty,entry_px=fill,entry_ms=now,stop=None,fees=fee,realized_gross=0.,
        funding=0.,funding_hour=now//S3.HOUR,market='spot',leverage=1,spot=True)
    book['benchmark_started']=True
    L.event(book,'entry',now,trade_id='SPOT_HOLD',coin=coin,price=fill,size=qty,fee=fee,
            reason='SPOT_1x_buy_hold_control_no_stop',risk_exception=True,market='spot',
            leverage=1,fill_source=src,price_source=book['spot_spec']['price_source'],
            spot_pair=book['spot_spec']['spot_pair'],fee_rate=SPOT_TAKER)

class PublicData(V.PublicData):
    ALLOWED=V.PublicData.ALLOWED|{'spotMetaAndAssetCtxs'}
    WEIGHT_CAP=1000
    def request(self,payload):
        if self.weight>=self.WEIGHT_CAP:
            raise ValueError('collector weight budget exhausted; retry after supervisor backoff')
        response=L.PublicData.request(self,payload)
        typ=payload['type']; cost=2 if typ in ('allMids','l2Book') else 20
        if typ=='candleSnapshot': cost+=math.ceil(len(response)/60)
        if typ=='fundingHistory': cost+=math.ceil(len(response)/20)
        self.weight+=cost
        return response
    def fetch(self,st,now):
        for key in list(V.KEYS.values())+['spot_m1','spot_m5','spot_m15','spot_h1']:
            self.cache.setdefault(key,{})
        meta,contexts=self.request(dict(type='metaAndAssetCtxs'))
        ctx={u['name']:dict(szDecimals=u['szDecimals'],maxLeverage=u['maxLeverage'],
              **{k:float(v[k]) for k in ('funding','markPx','oraclePx')})
             for u,v in zip(meta['universe'],contexts) if u['name'] in S.COINS}
        if set(ctx)!=set(S.COINS): raise ValueError('invalid context')
        # Token decimals are frozen in SPOT_MARKETS. Re-verify identity at most every 15 minutes
        # so a cold start does not spend a 20-weight call plus four L2 reads inside one minute.
        spot_ctx={}
        verify=self.cache.get('spot_meta_ms',0)==0 or now-self.cache.get('spot_meta_ms',0)>=15*S3.MINUTE
        if verify:
            spot_raw=self.request(dict(type='spotMetaAndAssetCtxs'))
            spot_meta,spot_ctxs=spot_raw[0],spot_raw[1]
            tokens={t['index']:t for t in spot_meta['tokens']}
            by_coin={c.get('coin'):c for c in spot_ctxs if isinstance(c,dict) and c.get('coin')}
            for name,mkt in S3.SPOT_MARKETS.items():
                raw=by_coin.get(mkt['api_coin'])
                if not raw: raise ValueError(f"missing spot context {name} {mkt['api_coin']}")
                token=tokens[mkt['token_index']]
                if token['name']!=mkt['token_name']: raise ValueError(f'spot token identity changed {name}')
                if int(token['szDecimals'])!=int(mkt['szDecimals']): raise ValueError(f'spot szDecimals changed {name}')
            self.cache['spot_meta_ms']=now
        for name,mkt in S3.SPOT_MARKETS.items():
            spot_ctx[name]=dict(szDecimals=int(mkt['szDecimals']),api_coin=mkt['api_coin'],pair=mkt['pair'],
                price_source='spot_pair',maxLeverage=1)
        d=dict(ctx=ctx,spot_ctx=spot_ctx,minutes={},funding={},books={},fourhour={},daily={},
               m1={},m5={},m15={},h1={},spot_books={},spot_minutes={},spot_m1={},spot_m5={},
               spot_m15={},spot_h1={})
        for c in S.COINS:
            cached=self.cache['m1'].get(c,[])
            start=min(st['next_minute'],cached[-1]['t'] if cached else now//S3.MINUTE*S3.MINUTE-250*S3.MINUTE)
            new=self.candles(c,'1m',start,now)
            merged={r['t']:r for r in cached}; merged.update({r['t']:r for r in new if r['t']+S3.MINUTE<=now})
            rows=[merged[t] for t in sorted(merged)]
            d['minutes'][c]=[r for r in rows if r['t']>=st['next_minute']]
            d['m1'][c]=rows[-512:]
            if len(d['m1'][c])<250 or any(b['t']-a['t']!=S3.MINUTE for a,b in zip(d['m1'][c],d['m1'][c][1:])) or rows[-1]['t']+S3.MINUTE!=now//S3.MINUTE*S3.MINUTE:
                raise ValueError(f'{c} 1m warmup/continuity missing')
            self.cache['m1'][c]=rows[-512:]
            for interval,key,count in [('5m','m5',250),('15m','m15',250),('1h','h1',250),('4h','fourhour',710),('1d','daily',250)]:
                d[key][c]=self.history(key,c,interval,count,now)
            d['funding'][c]=self.funding(c,min(st['next_minute']-S3.HOUR,now-48*S3.HOUR),now)
        for name,mkt in S3.SPOT_MARKETS.items():
            api=mkt['api_coin']
            cached=self.cache['spot_m1'].get(name,[])
            start=min(st['next_minute'],cached[-1]['t'] if cached else now//S3.MINUTE*S3.MINUTE-250*S3.MINUTE)
            new=self.candles(api,'1m',start,now)
            merged={r['t']:r for r in cached}; merged.update({r['t']:r for r in new if r['t']+S3.MINUTE<=now})
            rows=[merged[t] for t in sorted(merged)]
            d['spot_minutes'][name]=[r for r in rows if r['t']>=st['next_minute']]
            d['spot_m1'][name]=rows[-512:]
            if len(d['spot_m1'][name])<250 or any(b['t']-a['t']!=S3.MINUTE for a,b in zip(d['spot_m1'][name],d['spot_m1'][name][1:])) or rows[-1]['t']+S3.MINUTE!=now//S3.MINUTE*S3.MINUTE:
                raise ValueError(f'{name} spot 1m warmup/continuity missing')
            self.cache['spot_m1'][name]=rows[-512:]
            for interval,key,count in [('5m','spot_m5',250),('15m','spot_m15',250),('1h','spot_h1',250)]:
                d[key][name]=self._spot_history(key,name,api,interval,count,now)
        if now%(4*S3.HOUR)<=120000 or now%S3.DAY<=120000:
            for c in S.COINS:
                raw=self.request(dict(type='l2Book',coin=c))
                if abs(L.sc.now_ms()-int(raw['time']))>120000: raise ValueError('stale L2')
                d['books'][c]=dict(bids=[(float(x['px']),float(x['sz'])) for x in raw['levels'][0]],asks=[(float(x['px']),float(x['sz'])) for x in raw['levels'][1]])
        # Spot L2 only in a 2-minute window every 15 minutes. Other ticks use the 2bp floor,
        # which was conservative vs the 11 Nov 2026 16-USDC walks (0.07-1.03bp).
        if now%(15*S3.MINUTE)<=120000:
            for name,mkt in S3.SPOT_MARKETS.items():
                raw=self.request(dict(type='l2Book',coin=mkt['api_coin']))
                if abs(L.sc.now_ms()-int(raw['time']))>120000: raise ValueError('stale spot L2')
                d['spot_books'][name]=dict(bids=[(float(x['px']),float(x['sz'])) for x in raw['levels'][0]],asks=[(float(x['px']),float(x['sz'])) for x in raw['levels'][1]])
        raw=self.request(dict(type='allMids')); observed=L.sc.now_ms()
        d['mids']={c:float(raw[c]) for c in S.COINS}
        for name,mkt in S3.SPOT_MARKETS.items():
            px=float(raw[mkt['api_coin']])
            if px<=0 or not math.isfinite(px): raise ValueError(f'invalid spot mid {name}')
            d['mids'][name]=px
        if any(d['mids'][c]<=0 or not math.isfinite(d['mids'][c]) for c in S.COINS): raise ValueError('invalid mids')
        if observed-now>S3.MINUTE: raise ValueError('snapshot collection exceeded 60s; no stale fills')
        if now//S3.MINUTE!=observed//S3.MINUTE: raise ValueError('snapshot crossed minute boundary; retry current data, no hindsight fills')
        d['observed_ms']=observed
        source=self.root/'sources'/f'{now}.json.gz'; source.parent.mkdir(exist_ok=True)
        with gzip.open(source,'wt') as f:
            json.dump(dict(network='mainnet_public_read_only',asof_utc=L.utc(observed),requests=self.requests),f)
        L.atomic(self.path,self.cache)
        counts=Counter(r['request']['type'] for r in self.requests)
        d['evidence']=dict(path=str(source.relative_to(self.root)),sha256=L.sha(source),received_ms=observed,
             requests=len(self.requests),request_types=dict(counts),estimated_weight=self.weight,
             collection_seconds=round(time.monotonic()-self.collect_started,4))
        return d
    def _spot_history(self,key,name,api,interval,count,now):
        step=V.STEPS[interval]; rows=self.cache[key].get(name,[]); end=now//step*step
        if not rows or rows[-1]['t']+step<end:
            start=rows[-1]['t'] if rows else end-count*step
            new=self.candles(api,interval,start,now)
            merged={r['t']:r for r in rows}; merged.update({r['t']:r for r in new if r['t']+step<=now})
            rows=[merged[t] for t in sorted(merged)]
            self.cache[key][name]=rows
        if len(rows)<count or any(b['t']-a['t']!=step for a,b in zip(rows,rows[1:])) or rows[-1]['t']+step!=end:
            raise ValueError(f'{name} {interval} warmup/continuity/currentness missing')
        return rows

SPOT_KEYS={5*S3.MINUTE:'spot_m5',15*S3.MINUTE:'spot_m15',S3.HOUR:'spot_h1'}

def apply_spot(st,data,now,start):
    end=now//S3.MINUTE*S3.MINUTE
    bycoin={c:{r['t']:r for r in data['spot_minutes'][c]} for c in S3.SPOT_COINS}
    books=[b for b in st['books'].values() if 'spot_spec' in b]
    for t in range(start,end,S3.MINUTE):
        if not all(t in bycoin[c] for c in S3.SPOT_COINS): raise ValueError('UNRESOLVED_REPLAY_GAP')
        bars={c:bycoin[c][t] for c in S3.SPOT_COINS}
        for b in books:
            if t+S3.MINUTE<=b['activation_ms']: continue
            L.mark(b,{c:bars[c]['o'] for c in S3.SPOT_COINS},t)
            # No funding on spot. Never invent a zero funding print.
            for p in list(b['positions'].values()):
                if p.get('stop') is not None: spot_resolve_stop(b,p,bars[p['coin']],now)
            L.mark(b,{c:bars[c]['c'] for c in S3.SPOT_COINS},t+S3.MINUTE-1)
            if b['kind']!='spot_hold' and not b['halted'] and L.sc.equity(b)<=b['day_start_equity']*.98:
                b.update(halted=True,halt_reason='daily_loss_minus_2_percent',pending_halt_flatten=True)
                L.event(b,'halt',t+S3.MINUTE-1,equity=L.sc.equity(b),note='replayed threshold; flatten at next actually observed quote, not unseen historical close')
    cache={}
    for b in books:
        spec=b['spot_spec']; L.mark(b,{c:data['mids'][c] for c in S3.SPOT_COINS},now)
        if spec['kind']=='spot_hold':
            start_spot_hold(b,data,now); L.mark(b,{c:data['mids'][c] for c in S3.SPOT_COINS},now)
            b['last_tick_myt']=L.sc.myt(now)
            if b.get('valuation_bucket')!=now//(15*S3.MINUTE):
                L.event(b,'valuation',now,equity=L.sc.equity(b),cash=b['cash'],unrealized=L.sc.unrealized(b),
                    fees=b['stats']['fees'],funding=0.,positions=len(b['positions']),max_drawdown_pct=b['max_drawdown_pct'])
                b['valuation_bucket']=now//(15*S3.MINUTE)
            continue
        for p in list(b['positions'].values()):
            mid=data['mids'][p['coin']]; depth=data.get('spot_books',{}).get(p['coin'])
            if p.get('stop') is not None and L.hit_adverse(p,mid):
                px,_=fill_price(mid,-p['dir'],depth,p['size']*mid)
                # Stops at live mid use 5bp adverse, never a tighter L2 improvement.
                stop_px=mid*(1-p['dir']*S3.STOP_SLIP_BPS/1e4)
                px=min(px,stop_px) if p['dir']>0 else max(px,stop_px)
                spot_close(b,p,px,now,'stop',gap_through_stop=True,fill_source='first_observed_mid_adverse5bp')
            elif now-p['entry_ms']>=spec['hold_ms']:
                px,_=fill_price(mid,-p['dir'],depth,p['size']*mid)
                spot_close(b,p,px,now,'observed_time_exit',delay_ms=now-p['entry_ms']-spec['hold_ms'])
        if b.pop('pending_halt_flatten',False):
            for p in list(b['positions'].values()):
                mid=data['mids'][p['coin']]; px=mid*(1-p['dir']*S3.STOP_SLIP_BPS/1e4)
                spot_close(b,p,px,now,'daily_halt_first_observation')
        if b['kind']!='spot_hold' and not b['halted'] and L.sc.equity(b)<=b['day_start_equity']*.98:
            b.update(halted=True,halt_reason='daily_loss_minus_2_percent')
            L.event(b,'halt',now,equity=L.sc.equity(b),note='sticky: owner reset required; no automatic midnight reset')
            for p in list(b['positions'].values()):
                mid=data['mids'][p['coin']]; px=mid*(1-p['dir']*S3.STOP_SLIP_BPS/1e4)
                spot_close(b,p,px,now,'daily_halt')
        step=spec['interval']; boundary=now//step*step
        for c in spec['coins']:
            if b['decisions'].get(c,0)>=boundary: continue
            key=(spec['kind'],json.dumps(spec['params'],sort_keys=True),c,boundary)
            if key not in cache:
                rows=data[SPOT_KEYS[step]][c]
                if rows[-1]['t']+step!=boundary: raise ValueError('stale new signal')
                cache[key]=S3.signal(spec,rows,boundary)
            sig=cache[key]; allowed=now-boundary<=(45000 if step==S3.MINUTE else 90000)
            L.event(b,'signal',now,coin=c,boundary_utc=L.utc(boundary),side=sig['side'],
                    details=sig['details'],entry_window_open=allowed)
            current=next((p for p in b['positions'].values() if p['coin']==c),None)
            mid=data['mids'][c]; depth=data.get('spot_books',{}).get(c)
            if current and (sig['exit_long'] or sig['side']<0):
                px,_=fill_price(mid,-1,depth,current['size']*mid)
                spot_close(b,current,px,now,'signal_or_time_exit',signal_boundary_utc=L.utc(boundary),delay_ms=now-boundary)
                current=None
            if sig['side']==1 and current is None:
                if not allowed:
                    L.event(b,'missed_entry',now,coin=c,reason='no_hindsight_entry_signal_expired',boundary_utc=L.utc(boundary))
                else:
                    spot_open(b,c,sig['stop_pct'],mid,now,data['spot_ctx'],depth)
            b['decisions'][c]=boundary
        b['last_tick_myt']=L.sc.myt(now); L.mark(b,{c:data['mids'][c] for c in S3.SPOT_COINS},now)
        if b.get('valuation_bucket')!=now//(15*S3.MINUTE):
            L.event(b,'valuation',now,equity=L.sc.equity(b),cash=b['cash'],unrealized=L.sc.unrealized(b),
                fees=b['stats']['fees'],funding=b['stats']['funding'],positions=len(b['positions']),max_drawdown_pct=b['max_drawdown_pct'])
            b['valuation_bucket']=now//(15*S3.MINUTE)
    return len(cache)

def apply_tick(st,data,now,old):
    start=st['next_minute']
    subset=dict(st,books={s['id']:st['books'][s['id']] for s in old['strategies']})
    L.apply_tick(subset,data,now)
    E.initialize(st,now)
    computations=V.apply_new(st,data,now,start)
    spot_computations=apply_spot(st,data,now,start)
    st.update(next_minute=subset['next_minute'],last_tick_ms=now,ticks=subset['ticks'])
    E.update(st,now)
    return computations,spot_computations

def metrics(b):
    m=L.metrics(b)
    # league.metrics hardcodes equity-100; spot books start at 16.24.
    m['net_pnl']=L.sc.equity(b)-float(b.get('starting_equity',100.))
    return m

def export(st,root=ROOT):
    L.export(st,root)
    rows=[(b,metrics(b)) for b in st['books'].values()]
    n_spot=sum(1 for b,_ in rows if 'spot_spec' in b)
    n_perp=len(rows)-n_spot
    text='# PAPER league — 100 virtual USDC perp books + 16.24 virtual USDC spot books\n\n'
    text+=f"Updated {L.sc.myt(st['last_tick_ms'])} MYT | tick {st['ticks']} | {len(rows)} books ({n_perp} perp @100 USDC, {n_spot} spot @16.24 USDC) | public reads only\n\n"
    text+=("Spot research books use 5m/15m/1h timeframes. Do not compare raw Net MTM USDC across the 100-USDC and 16.24-USDC tables. An 'Early read (not evidence)' table lists fast books with >=10 closed trades; it is not the promotion bar. Ranks use net MTM (open exit cost not deducted). Gate comparisons use same-start indicative exit equity: perp books deduct taker+2bp; spot books deduct official tier-0 spot taker 0.070%+2bp. Official promotion controls remain the BTC-perp hold and random-entry books.\n\n")
    groups=[
        ('control','Controls / luck benchmarks (100 virtual USDC perp books)'),
        ('fast','Fast / short-term (100 virtual USDC perp books)'),
        ('slow','Slow / long-term (100 virtual USDC perp books)'),
        ('spot_control','Spot buy-and-hold controls (16.24 virtual USDC, 1x long, no leverage)'),
        ('spot_fast','Spot fast / 5m and 15m (16.24 virtual USDC, long-only, no leverage)'),
        ('spot_slow','Spot slow / 1h (16.24 virtual USDC, long-only, no leverage)'),
    ]
    def lane_of(b):
        if 'spot_spec' in b: return b.get('lane','spot_slow')
        return 'control' if b['kind'] in ('benchmark','random') else b.get('lane','slow')
    for lane,title in groups:
        text+=f'## {title}\n\n'
        text+='| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |\n'
        text+='|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|\n'
        group=[(b,m) for b,m in rows if lane_of(b)==lane]
        def fmt(v): return '—' if v is None else (v if isinstance(v,str) else f'{v:.4f}')
        for rank,(b,m) in enumerate(sorted(group,key=lambda x:x[1]['net_pnl'],reverse=True),1):
            e=b['evaluation']; o=e['oos']; significance='NOT SIGNIFICANT (<30)' if m['trades']<30 else 'UNPROVEN'
            fresh='not flagged' if e['flag_ms'] is None else ('wait fresh day + flat' if o is None else f"{o['status']}: {o['elapsed_days']:.2f}d/{o['trades']} trades; {(o.get('end_net_pct',o['net_pct'])):+.3f}%")
            status=f"{significance}; {e['status']}"+('; HALTED' if b['halted'] else '')
            if b['kind']=='benchmark': status+='; NONTRADABLE risk-exempt'
            if b['kind']=='spot_hold': status+='; SPOT HOLD CONTROL (no stop/halt flatten)'
            text+=f"| {rank} | {b['id']} | {m['trades']} | {m['net_pnl']:+.4f} | {fmt(m['win_rate'])} | {fmt(m['profit_factor'])} | {m['max_drawdown_pct']:.4f} | {fmt(m['expectancy'])} | {m['fees']:.4f} | {m['funding']:+.4f} | {e['excess_btc_pct']:+.4f} | {e['excess_random_pct']:+.4f} | {e['trial_count']} | {fmt(e['dsr_probability'])} | {e['days']} | {fresh} | {status} |\n"
        text+='\n'
    # Early operational look only: >=10 closed trades on fast/spot_fast books.
    early=[(b,m) for b,m in rows if b.get('lane') in ('fast','spot_fast') and m['trades']>=10]
    text+="## Early read (not evidence)\n\n"
    text+="Fast and spot_fast books with at least 10 closed trades, ranked by closed-trade count then net MTM after paid fees/funding (open exit cost not deducted). This is an operational early look so small-capital books can be watched before the 30-trade / DSR / fresh-OOS bar. It is **not** significance, **not** a PASS, and **does not** change the promotion bar. Nothing in this section is a CANDIDATE.\n\n"
    if not early:
        text+="No fast book has 10 closed trades yet.\n\n"
    else:
        text+="| Rank | Book | Lane | Closed | Net MTM USDC | Win % | Fees | Funding | Gate |\n"
        text+="|---:|---|---|---:|---:|---:|---:|---:|---|\n"
        early=sorted(early,key=lambda x:(-x[1]['trades'],-x[1]['net_pnl']))
        def fmt(v): return '—' if v is None else (v if isinstance(v,str) else f'{v:.4f}')
        for rank,(b,m) in enumerate(early,1):
            e=b.get('evaluation',{})
            text+=f"| {rank} | {b['id']} | {b.get('lane')} | {m['trades']} | {m['net_pnl']:+.4f} | {fmt(m['win_rate'])} | {m['fees']:.4f} | {m['funding']:+.4f} | {e.get('status','')} |\n"
        text+='\n'

    trials=E.PRIOR_TRIALS+len(st['books'])
    text+=f'DSR uses completed MYT daily returns, >=8 full daily observations, skew/kurtosis-adjusted normal probability, cross-book Sharpe dispersion with sampling-error floor. Trial count = 309 prior + ALL league books (perp and spot, including controls); currently {trials}. Unknown external searches are not verifiable: {trials} is the known count, not proof of complete worldwide trial history. Correlated books/time series make this an approximate conservative diagnostic, not a statistical guarantee.\n\n'
    text+='CANDIDATE_REVIEW_ONLY needs >=30 closed trades, positive costed return, outperformance vs BOTH the BTC-perp hold and random-entry controls, DSR>0.95, then a following non-overlapping fresh-MYT-day/flat-book OOS >=7 days OR >=30 new trades for fast/spot_fast books, profitable and beating both controls. First OOS endpoint is fixed PASS/FAIL. Candidate means send evidence for Risk Manager review only; NO automatic promotion.\n\n'
    text+='Spot books charge official tier-0 spot taker 0.070% (https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees, retrieved 11 Nov 2026) plus max(2bp adverse mid, L2 walk); maker 0.040% is documented and never assumed. No funding. No leverage, long only, no liquidation model. Stops are virtual candle replay with gaps+5bp, NOT exchange protection. UBTC/USDC (@142), UETH/USDC (@151), USOL/USDC (@156) and HYPE/USDC (@107) are real spot pairs, not perp-mid proxies. All families are unvalidated experiments; prior failed tests stay failed.\n'
    tmp=root/'leaderboard.md.tmp'; tmp.write_text(text); os.replace(tmp,root/'leaderboard.md')

def tick(root=ROOT):
    start=time.monotonic(); cpu=time.process_time(); old,ext,spot=registration(root); began=L.sc.now_ms()
    st=L.read_json(root/'league_state.json')
    if st.get('registration_sha256')!=L.sha(root/'registry/manifest.json'): raise ValueError('original state manifest digest changed')
    candidate=copy.deepcopy(st)
    extend(candidate,old,ext,spot,began,L.sha(root/'registry/extension-v2.json'),L.sha(root/'registry/spot-extension-v3.json'))
    data=PublicData(root).fetch(candidate,began); now=data['observed_ms']
    computations,spot_computations=apply_tick(candidate,data,now,old)
    candidate['last_evidence']=data['evidence']
    load=dict(max_rss_mb=round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,2),cpu_seconds=round(time.process_time()-cpu,4),wall_seconds=round(time.monotonic()-start,4),
              signal_computations=computations,spot_signal_computations=spot_computations,
              **{k:data['evidence'][k] for k in ('requests','request_types','estimated_weight','collection_seconds')})
    candidate['last_load']=load
    L.atomic(root/'league_state.json',candidate); export(candidate,root)
    load['wall_seconds_including_exports']=round(time.monotonic()-start,4)
    load['cpu_seconds_including_exports']=round(time.process_time()-cpu,4)
    result=dict(status='ok',mode='PAPER_ONLY',engine_version=3,tick=candidate['ticks'],ts_myt=L.sc.myt(now),ts_utc=L.utc(now),
       book_count=len(candidate['books']),trial_count=E.PRIOR_TRIALS+len(candidate['books']),evidence=data['evidence'],load=load,
       candidates=[b['id'] for b in candidate['books'].values() if b['evaluation']['status']=='CANDIDATE_REVIEW_ONLY'],
       books={b['id']:dict(equity=round(L.sc.equity(b),8),positions=len(b['positions']),closed_trades=len(b['closed_trades']),
                           starting_equity=b.get('starting_equity',100.),market=b.get('market','perp'))
              for b in candidate['books'].values()})
    L.atomic(root/'last_tick.json',result)
    if not (root/'first-live-tick-v3.json').exists(): L.atomic(root/'first-live-tick-v3.json',result)
    return result

def stop(*_):
    global RUNNING
    RUNNING=False

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--once',action='store_true'); args=ap.parse_args()
    with open(ROOT/'.engine.lock','a') as lock:
        try: fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError:
            print('another league engine holds the lock',flush=True); return 0
        if args.once: print(json.dumps(tick(),indent=2)); return 0
        (ROOT/'engine.pid').write_text(str(os.getpid())); signals.signal(signals.SIGTERM,stop); signals.signal(signals.SIGINT,stop)
        while RUNNING:
            start=time.monotonic(); L.heartbeat(ROOT,'fetching',engine_version=3)
            try:
                r=tick(); L.heartbeat(ROOT,'ok',engine_version=3,last_success_ms=L.sc.now_ms(),tick=r['tick'],book_count=r['book_count'],load=r['load'])
                print(json.dumps({k:v for k,v in r.items() if k!='books'}),flush=True)
            except Exception as e:
                L.heartbeat(ROOT,'ERROR_NO_NEW_RISK',engine_version=3,error=repr(e)); print(f'{L.sc.myt()} ERROR_NO_NEW_RISK {e!r}',flush=True); return 1
            while RUNNING and time.monotonic()-start<60: time.sleep(.5)
        L.heartbeat(ROOT,'stopped',engine_version=3); return 0

if __name__=='__main__': raise SystemExit(main())
