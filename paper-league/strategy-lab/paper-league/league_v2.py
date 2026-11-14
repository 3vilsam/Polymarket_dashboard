#!/usr/bin/env python3
"""Append-only PAPER expansion. The original five rules and implementation stay frozen.
Only a fixed public /info request allowlist is reachable; no wallet/order surface.
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
import strategies_v2 as S
import evaluation_v2 as E

ROOT=L.ROOT
RUNNING=True
STEPS={'1m':S.MINUTE,'5m':5*S.MINUTE,'15m':15*S.MINUTE,'1h':S.HOUR,'4h':4*S.HOUR,'1d':S.DAY}
KEYS={S.MINUTE:'m1',5*S.MINUTE:'m5',15*S.MINUTE:'m15',S.HOUR:'h1',4*S.HOUR:'fourhour',S.DAY:'daily'}

def registration(root=ROOT):
    old=L.registration(root)  # Verifies the ORIGINAL files and five rules unchanged.
    ext=L.read_json(root/'registry/extension-v2.json')
    if ext.get('mode')!='PAPER_ONLY' or len(ext['strategies'])!=95:
        raise ValueError('95 append-only PAPER registrations required')
    if ext['original_manifest_sha256']!=L.sha(root/'registry/manifest.json'):
        raise ValueError('original registration changed')
    for n,d in ext['implementation_sha256'].items():
        if L.sha(root/n)!=d: raise ValueError(f'frozen extension implementation changed: {n}')
    for s in ext['strategies']:
        if L.sha(root/'registry'/f"{s['id']}.md")!=s['sha256']:
            raise ValueError(f"frozen extension rules changed: {s['id']}")
    if len({s['id'] for s in old['strategies']+ext['strategies']})!=100: raise ValueError('duplicate book id')
    return old,ext

def extend(st, old, ext, now, digest):
    if st.get('registration_sha256',L.sha(ROOT/'registry/manifest.json'))!=ext['original_manifest_sha256']:
        raise ValueError('persisted original registry mismatch')
    if st.get('extension_registration_sha256',digest)!=digest:
        raise ValueError('persisted extension registry mismatch')
    if 'extension_registration_sha256' not in st:
        # Atomic first-live-tick migration, existing books never replaced/reset.
        expected={s['id'] for s in old['strategies']}
        if set(st['books'])!=expected: raise ValueError('unexpected legacy books at migration')
        for s in ext['strategies']:
            b=L.new_state(dict(strategies=[s]),now)['books'][s['id']]
            b.update(lane=s['lane'],spec=s,activation_ms=now)
            st['books'][s['id']]=b
        st.update(extension_registration_sha256=digest,extension_created_ms=now,version=2)
    expected={s['id'] for s in old['strategies']+ext['strategies']}
    if set(st['books'])!=expected: raise ValueError('missing/unregistered book')
    for s in ext['strategies']:
        if st['books'][s['id']].get('spec')!=s: raise ValueError('persisted spec changed')
    return st

class PublicData(L.PublicData):
    def __init__(self,root):
        super().__init__(root)
        for key in KEYS.values(): self.cache.setdefault(key,{})
        self.weight=0
        self.collect_started=time.monotonic()
    def request(self,payload):
        # Refuse an oversized burst before spending it; no per-book calls.
        if self.weight>=750: raise ValueError('collector weight budget exhausted; retry after supervisor backoff')
        response=super().request(payload)
        typ=payload['type']; cost=2 if typ in ('allMids','l2Book') else 20
        if typ=='candleSnapshot': cost+=math.ceil(len(response)/60)
        if typ=='fundingHistory': cost+=math.ceil(len(response)/20)
        self.weight+=cost
        return response
    def history(self,key,coin,interval,count,now):
        step=STEPS[interval]; rows=self.cache[key].get(coin,[]); end=now//step*step
        if not rows or rows[-1]['t']+step<end:
            start=rows[-1]['t'] if rows else end-count*step
            new=self.candles(coin,interval,start,now)
            merged={r['t']:r for r in rows}; merged.update({r['t']:r for r in new if r['t']+step<=now})
            rows=[merged[t] for t in sorted(merged)]
            self.cache[key][coin]=rows
        if len(rows)<count or any(b['t']-a['t']!=step for a,b in zip(rows,rows[1:])) or rows[-1]['t']+step!=end:
            raise ValueError(f'{coin} {interval} warmup/continuity/currentness missing')
        return rows
    def fetch(self,st,now):
        meta,contexts=self.request(dict(type='metaAndAssetCtxs'))
        ctx={u['name']:dict(szDecimals=u['szDecimals'],maxLeverage=u['maxLeverage'],
              **{k:float(v[k]) for k in ('funding','markPx','oraclePx')})
             for u,v in zip(meta['universe'],contexts) if u['name'] in S.COINS}
        if set(ctx)!=set(S.COINS): raise ValueError('invalid context')
        d=dict(ctx=ctx,minutes={},funding={},books={},fourhour={},daily={},m1={},m5={},m15={},h1={})
        for c in S.COINS:
            cached=self.cache['m1'].get(c,[])
            start=min(st['next_minute'],cached[-1]['t'] if cached else now//S.MINUTE*S.MINUTE-250*S.MINUTE)
            new=self.candles(c,'1m',start,now)
            merged={r['t']:r for r in cached}; merged.update({r['t']:r for r in new if r['t']+S.MINUTE<=now})
            rows=[merged[t] for t in sorted(merged)]
            d['minutes'][c]=[r for r in rows if r['t']>=st['next_minute']]
            d['m1'][c]=rows[-512:]
            if len(d['m1'][c])<250 or any(b['t']-a['t']!=S.MINUTE for a,b in zip(d['m1'][c],d['m1'][c][1:])) or rows[-1]['t']+S.MINUTE!=now//S.MINUTE*S.MINUTE:
                raise ValueError(f'{c} 1m warmup/continuity missing')
            self.cache['m1'][c]=rows[-512:] # All 1m strategies have finite <=132-bar memory; no EMA seed here.
            for interval,key,count in [('5m','m5',250),('15m','m15',250),('1h','h1',250),('4h','fourhour',710),('1d','daily',250)]:
                d[key][c]=self.history(key,c,interval,count,now)
            d['funding'][c]=self.funding(c,min(st['next_minute']-S.HOUR,now-48*S.HOUR),now)
        # Preserve old depth assumptions for the original books only; fast books
        # always pay adverse 2bp proxy + taker, never an unobserved bar-open price.
        if now%(4*S.HOUR)<=120000 or now%S.DAY<=120000:
            for c in S.COINS:
                raw=self.request(dict(type='l2Book',coin=c))
                if abs(L.sc.now_ms()-int(raw['time']))>120000: raise ValueError('stale L2')
                d['books'][c]=dict(bids=[(float(x['px']),float(x['sz'])) for x in raw['levels'][0]],asks=[(float(x['px']),float(x['sz'])) for x in raw['levels'][1]])
        # Last price is actually observed AFTER indicator reads, not before them.
        raw=self.request(dict(type='allMids')); observed=L.sc.now_ms()
        d['mids']={c:float(raw[c]) for c in S.COINS}
        if any(x<=0 or not math.isfinite(x) for x in d['mids'].values()): raise ValueError('invalid mids')
        if observed-now>S.MINUTE: raise ValueError('snapshot collection exceeded 60s; no stale fills')
        if now//S.MINUTE!=observed//S.MINUTE: raise ValueError('snapshot crossed minute boundary; retry current data, no hindsight fills')
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

def apply_new(st,data,now,start):
    end=now//S.MINUTE*S.MINUTE; bycoin={c:{r['t']:r for r in data['minutes'][c]} for c in S.COINS}
    newbooks=[b for b in st['books'].values() if 'spec' in b]
    for t in range(start,end,S.MINUTE):
        if not all(t in bycoin[c] for c in S.COINS): raise ValueError('UNRESOLVED_REPLAY_GAP')
        bars={c:bycoin[c][t] for c in S.COINS}
        for b in newbooks:
            if t+S.MINUTE<=b['activation_ms']: continue
            L.mark(b,{c:bars[c]['o'] for c in S.COINS},t)
            L.funding_at(b,data['funding'],bars,t)
            for p in list(b['positions'].values()): L.resolve_stop(b,p,bars[p['coin']],now)
            L.mark(b,{c:bars[c]['c'] for c in S.COINS},t+S.MINUTE-1)
            if not b['halted'] and L.sc.equity(b)<=b['day_start_equity']*.98:
                b.update(halted=True,halt_reason='daily_loss_minus_2_percent',pending_halt_flatten=True)
                L.event(b,'halt',t+S.MINUTE-1,equity=L.sc.equity(b),note='replayed threshold; flatten at next actually observed quote, not unseen historical close')
            # No retroactive time/signal/target fills for these fast books. Stops
            # alone are explicit candle-reconstructed virtual stop assumptions.
    cache={}
    for b in newbooks:
        spec=b['spec']; L.mark(b,data['mids'],now)
        for p in list(b['positions'].values()):
            mid=data['mids'][p['coin']]
            if L.hit_adverse(p,mid):
                L.close(b,p,mid*(1-p['dir']*.0005),now,'stop',gap_through_stop=True,fill_source='first_observed_mid_adverse5bp')
            elif now-p['entry_ms']>=spec['hold_ms']:
                L.close(b,p,mid*(1-p['dir']*.0002),now,'observed_time_exit',delay_ms=now-p['entry_ms']-spec['hold_ms'])
        if b.pop('pending_halt_flatten',False):
            for p in list(b['positions'].values()):
                L.close(b,p,data['mids'][p['coin']]*(1-p['dir']*.0005),now,'daily_halt_first_observation')
        L.halt(b,now); L.enforce_cost_risk(b,now)
        step=spec['interval']; boundary=now//step*step
        for c in spec['coins']:
            if b['decisions'].get(c,0)>=boundary: continue
            key=(spec['kind'],json.dumps(spec['params'],sort_keys=True),c,boundary)
            if key not in cache:
                rows=data[KEYS[step]][c]
                if rows[-1]['t']+step!=boundary: raise ValueError('stale new signal')
                cache[key]=S.signal(spec,rows,data['funding'][c],boundary,c)
            sig=cache[key]; allowed=now-boundary<= (45000 if step==S.MINUTE else 90000)
            # New books use 2bp adverse observed-mid fills (never zero-slip L2).
            proxy=dict(data,books={})
            L.decision(b,c,sig,proxy,now,boundary,allowed)
            b['decisions'][c]=boundary
        b['last_tick_myt']=L.sc.myt(now); L.mark(b,data['mids'],now)
        if b.get('valuation_bucket')!=now//(15*S.MINUTE):
            L.event(b,'valuation',now,equity=L.sc.equity(b),cash=b['cash'],unrealized=L.sc.unrealized(b),
                fees=b['stats']['fees'],funding=b['stats']['funding'],positions=len(b['positions']),max_drawdown_pct=b['max_drawdown_pct'])
            b['valuation_bucket']=now//(15*S.MINUTE)
    return len(cache)

def apply_tick(st,data,now,old):
    start=st['next_minute']
    # Existing books execute their exact frozen code, with shared observed data.
    subset=dict(st,books={s['id']:st['books'][s['id']] for s in old['strategies']})
    L.apply_tick(subset,data,now)
    E.initialize(st,now)
    computations=apply_new(st,data,now,start)
    st.update(next_minute=subset['next_minute'],last_tick_ms=now,ticks=subset['ticks'])
    E.update(st,now)
    return computations

def export(st,root=ROOT):
    L.export(st,root)  # Original per-book state/ledger format preserved.
    rows=[(b,L.metrics(b)) for b in st['books'].values()]
    text='# PAPER league — 100 virtual USDC per independent book\n\n'
    text+=f"Updated {L.sc.myt(st['last_tick_ms'])} MYT | tick {st['ticks']} | {len(rows)} books | public reads only\n\n"
    text+='Ranks use net MTM (open exit cost not deducted). Gate comparisons use same-start indicative liquidation equity: deduct taker+2bp exit estimate. Controls share comparison start, not mismatched inception returns.\n\n'
    for lane,title in [('control','Controls / luck benchmarks'),('fast','Fast / short-term'),('slow','Slow / long-term')]:
        text+=f'## {title}\n\n'
        text+='| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |\n'
        text+='|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|\n'
        group=[(b,m) for b,m in rows if ('control' if b['kind'] in ('benchmark','random') else b.get('lane','slow'))==lane]
        def fmt(v): return '—' if v is None else (v if isinstance(v,str) else f'{v:.4f}')
        for rank,(b,m) in enumerate(sorted(group,key=lambda x:x[1]['net_pnl'],reverse=True),1):
            e=b['evaluation']; o=e['oos']; significance='NOT SIGNIFICANT (<30)' if m['trades']<30 else 'UNPROVEN'
            fresh='not flagged' if e['flag_ms'] is None else ('wait fresh day + flat' if o is None else f"{o['status']}: {o['elapsed_days']:.2f}d/{o['trades']} trades; {(o.get('end_net_pct',o['net_pct'])):+.3f}%")
            status=f"{significance}; {e['status']}"+('; HALTED' if b['halted'] else '')
            if b['kind']=='benchmark': status+='; NONTRADABLE risk-exempt'
            text+=f"| {rank} | {b['id']} | {m['trades']} | {m['net_pnl']:+.4f} | {fmt(m['win_rate'])} | {fmt(m['profit_factor'])} | {m['max_drawdown_pct']:.4f} | {fmt(m['expectancy'])} | {m['fees']:.4f} | {m['funding']:+.4f} | {e['excess_btc_pct']:+.4f} | {e['excess_random_pct']:+.4f} | {e['trial_count']} | {fmt(e['dsr_probability'])} | {e['days']} | {fresh} | {status} |\n"
        text+='\n'
    text+='DSR uses completed MYT daily returns, >=8 full daily observations, skew/kurtosis-adjusted normal probability, cross-book Sharpe dispersion with sampling-error floor. Trial count = 309 prior + ALL league books (including controls); currently409. Unknown external searches are not verifiable:409 is the known count, not proof of complete worldwide trial history. Correlated books/time series make this an approximate conservative diagnostic, not a statistical guarantee.\n\n'
    text+='CANDIDATE_REVIEW_ONLY needs >=30 closed trades, positive costed return, outperformance vs BOTH controls, DSR>0.95, then a following non-overlapping fresh-MYT-day/flat-book OOS >=7 days OR >=30 new trades for fast books, profitable and beating both controls. First OOS endpoint is fixed PASS/FAIL. Candidate means send evidence for Risk Manager review only; NO automatic promotion.\n\n'
    text+='Funding uses actual settled hourly rates, cash amounts use minute-open oracle proxy. Stops are virtual candle replay with gaps+5bp, NOT exchange protection; signal/time exits are next actual observed prices, not historical fills. BTC control alone is an explicit NONTRADABLE stop/risk exception. All families/grid are unvalidated, correlated experiments; prior failed tests stay failed.\n'
    tmp=root/'leaderboard.md.tmp'; tmp.write_text(text); os.replace(tmp,root/'leaderboard.md')

def tick(root=ROOT):
    start=time.monotonic(); cpu=time.process_time(); old,ext=registration(root); began=L.sc.now_ms()
    st=L.read_json(root/'league_state.json')
    if st.get('registration_sha256')!=L.sha(root/'registry/manifest.json'): raise ValueError('original state manifest digest changed')
    candidate=copy.deepcopy(st)
    extend(candidate,old,ext,began,L.sha(root/'registry/extension-v2.json'))
    data=PublicData(root).fetch(candidate,began); now=data['observed_ms']
    computations=apply_tick(candidate,data,now,old)
    candidate['last_evidence']=data['evidence']
    load=dict(max_rss_mb=round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,2),cpu_seconds=round(time.process_time()-cpu,4),wall_seconds=round(time.monotonic()-start,4),
              signal_computations=computations,**{k:data['evidence'][k] for k in ('requests','request_types','estimated_weight','collection_seconds')})
    candidate['last_load']=load
    L.atomic(root/'league_state.json',candidate); export(candidate,root)
    load['wall_seconds_including_exports']=round(time.monotonic()-start,4)
    load['cpu_seconds_including_exports']=round(time.process_time()-cpu,4)
    result=dict(status='ok',mode='PAPER_ONLY',engine_version=2,tick=candidate['ticks'],ts_myt=L.sc.myt(now),ts_utc=L.utc(now),
       book_count=len(candidate['books']),trial_count=E.PRIOR_TRIALS+len(candidate['books']),evidence=data['evidence'],load=load,
       candidates=[b['id'] for b in candidate['books'].values() if b['evaluation']['status']=='CANDIDATE_REVIEW_ONLY'],
       books={b['id']:dict(equity=round(L.sc.equity(b),8),positions=len(b['positions']),closed_trades=len(b['closed_trades'])) for b in candidate['books'].values()})
    L.atomic(root/'last_tick.json',result)
    if not (root/'first-live-tick-v2.json').exists(): L.atomic(root/'first-live-tick-v2.json',result)
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
            start=time.monotonic(); L.heartbeat(ROOT,'fetching',engine_version=2)
            try:
                r=tick(); L.heartbeat(ROOT,'ok',engine_version=2,last_success_ms=L.sc.now_ms(),tick=r['tick'],book_count=r['book_count'],load=r['load'])
                # Compact daemon output; authoritative all-book result is last_tick.json.
                print(json.dumps({k:v for k,v in r.items() if k!='books'}),flush=True)
            except Exception as e:
                L.heartbeat(ROOT,'ERROR_NO_NEW_RISK',engine_version=2,error=repr(e)); print(f'{L.sc.myt()} ERROR_NO_NEW_RISK {e!r}',flush=True); return 1
            while RUNNING and time.monotonic()-start<60: time.sleep(.5)
        L.heartbeat(ROOT,'stopped',engine_version=2); return 0

if __name__=='__main__': raise SystemExit(main())
