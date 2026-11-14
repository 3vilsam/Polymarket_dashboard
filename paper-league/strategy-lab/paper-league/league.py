#!/usr/bin/env python3
"""Isolated forward PAPER league. Public /info reads only, no trading interface.
Reuses the existing simulator's data transport, sizing, accounting primitives and
stop-fill function without writing to its original book or modifying its PASS gate.
"""
import argparse
import copy
import fcntl
import gzip
import hashlib
import importlib.metadata
import json
import math
import os
from pathlib import Path
import signal as signals
import sys
import time
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
ENGINE = ROOT.parent/'paper-trading'
sys.path.insert(0, str(ENGINE))
import simcore as sc
from shadow_exchange import size_order
from sentinel import stop_fill, hit_adverse
from strategies import COINS, MINUTE, HOUR, DAY, signal

CFG = dict(sc.DEFAULT_CONFIG, max_positions=2, cluster_max=1, stop_slippage_bps=5.,
           entry_slippage_bps=2., funding_reserve_hours=24, maker_fee=.00015)
RUNNING = True

def utc(t):
    return datetime.fromtimestamp(t/1000, timezone.utc).isoformat(timespec='milliseconds').replace('+00:00','Z')

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def atomic(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix+'.tmp')
    with tmp.open('w') as f:
        json.dump(data, f, indent=2, allow_nan=False)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)
    fd = os.open(str(path.parent), os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)

def read_json(path):
    return json.loads(Path(path).read_text())

def registration(root=ROOT):
    m = read_json(root/'registry/manifest.json')
    if m.get('mode') != 'PAPER_ONLY' or len(m['strategies']) != 5:
        raise ValueError('five PAPER_ONLY registrations required')
    for name, version in m.get('dependencies',{}).items():
        if importlib.metadata.version(name) != version:
            raise ValueError(f'frozen dependency version changed: {name}')
    for name, digest in m['implementation_sha256'].items():
        if sha(root/name) != digest:
            raise ValueError(f'frozen implementation changed: {name}; new registration required')
    for s in m['strategies']:
        if sha(root/'registry'/f"{s['id']}.md") != s['sha256']:
            raise ValueError(f"frozen rules changed: {s['id']}")
    return m

def event(book, typ, t, **fields):
    rec = dict(seq=len(book['events'])+1, event=typ, ts_ms=t, ts_utc=utc(t), ts_myt=sc.myt(t), **fields)
    book['events'].append(rec)
    return rec

def new_state(manifest, now):
    books = {}
    for s in manifest['strategies']:
        b = sc.new_state(CFG)
        b.update(id=s['id'], owner=s['owner'], kind=s['kind'], events=[],
                 peak=100., max_drawdown_pct=0., decisions={}, stopped_sides={},
                 day_date=sc.myt_date(now), last_tick_myt=None)
        event(b, 'registered', now, rules_sha256=s['sha256'], status='UNPROVEN_PAPER_ONLY',
              starting_equity=100., benchmark_exception=s['kind']=='benchmark')
        books[s['id']] = b
    return dict(version=1, mode='PAPER_ONLY', created_ms=now, last_tick_ms=None,
                next_minute=now//MINUTE*MINUTE, books=books, ticks=0)

def mark(book, marks, t):
    book['marks'].update(marks)
    eq = sc.equity(book)
    book['peak'] = max(book['peak'], eq)
    book['max_drawdown_pct'] = max(book['max_drawdown_pct'], (book['peak']-eq)/book['peak']*100)
    date = sc.myt_date(t)
    if date != book['day_date']:
        book.update(day_date=date, day_start_equity=eq)
        event(book, 'day_rollover', t, equity=eq, halt_persists=book['halted'])
    return eq

def close(book, p, px, t, why, qty=None, **notes):
    qty = min(p['size'], qty if qty is not None else p['size'])
    gross = p['dir']*qty*(px-p['entry_px'])
    fee = qty*px*CFG['taker_fee']
    book['cash'] += gross-fee
    book['stats']['fees'] += fee
    p['realized_gross'] += gross
    p['fees'] += fee
    p['size'] = max(0., round(p['size']-qty, 12))
    event(book, 'exit', t, trade_id=p['id'], coin=p['coin'], side=p['side'],
          size=qty, price=px, fee=fee, pnl_gross=gross, reason=why, **notes)
    if p['size'] < 1e-10:
        net = p['realized_gross'] - p['fees'] + p['funding']
        del book['positions'][p['id']]
        book['stats']['trades_closed'] += 1
        book['stats']['net_pnl'] += net
        book['stats']['wins' if net > 0 else 'losses'] += 1
        tr = dict(id=p['id'], coin=p['coin'], entry_ms=p['entry_ms'], exit_ms=t,
                  pnl_net=net, fees=p['fees'], funding=p['funding'], reason=why)
        book['closed_trades'].append(tr)
        event(book, 'net_pnl', t, **tr)
        if why == 'stop' and book['kind'] == 'ewmac':
            book['stopped_sides'][p['coin']] = p['dir']

def halt(book, t):
    if book['kind'] == 'benchmark' or book['halted']:
        return
    if sc.equity(book) <= book['day_start_equity']*.98:
        book['halted'], book['halt_reason'] = True, 'daily_loss_minus_2_percent'
        event(book, 'halt', t, equity=sc.equity(book), note='sticky: owner reset required; no automatic midnight reset')
        for p in list(book['positions'].values()):
            px = book['marks'][p['coin']]*(1-p['dir']*.0005)
            close(book, p, px, t, 'daily_halt')

def funding_at(book, rows, bars, t):
    for p in list(book['positions'].values()):
        if book['kind'] == 'benchmark' and p.get('spot',False):
            continue
        hour = t//HOUR
        if t % HOUR or p['entry_ms'] > t or p.get('funding_hour',-1) >= hour:
            continue
        found = [r for r in rows[p['coin']] if int(r['time'])//HOUR == hour]
        if len(found) != 1:
            raise ValueError(f"missing/duplicate funding {p['coin']} at {utc(t)}")
        row = found[0]
        # Real settled rate; historical oracle not in /info history. Explicit price proxy.
        px = bars[p['coin']]['o']
        payment = -p['dir']*p['size']*px*float(row['fundingRate'])
        p['funding'] += payment
        p['funding_hour'] = hour
        book['cash'] += payment
        book['stats']['funding'] += payment
        event(book, 'funding', int(row['time']), trade_id=p['id'], coin=p['coin'],
              payment=payment, rate=float(row['fundingRate']), price=px,
              price_source='1m_bar_open_proxy_NOT_historical_oracle', rate_source='HL fundingHistory',
              settlement_hour_utc=utc(t))

def enforce_cost_risk(book, t):
    if book['kind']=='benchmark':
        return
    for p in list(book['positions'].values()):
        # Remaining episode loss at the stop, including already paid fees and funding.
        cost = p['fees'] - p['funding'] - p['realized_gross'] + sc.position_risk(p, CFG)
        cap = min(p['risk_cap_at_entry'], max(0.,sc.equity(book))*.005)
        if cost > cap+1e-9:
            px = book['marks'][p['coin']]*(1-p['dir']*.0005)
            close(book,p,px,t,'funding_or_risk_budget_exhausted',estimated_stop_loss=cost,risk_budget=cap)

def risk_per_unit(px, stop, funding_rate, d):
    # Reserve 24h at the larger of current adverse rate and 0.00125%/h.
    reserve = max(d*funding_rate, .0000125)*CFG['funding_reserve_hours']*px
    return sc.entry_risk(px, stop, 1., CFG) + reserve

def open_paper(book, coin, d, stop_pct, px, t, ctx, funding_rate, depth=None, desired=None):
    if book['halted'] or coin not in COINS or not .005 <= stop_pct <= .045:
        return False
    if len(book['positions']) >= min(CFG['max_positions'], CFG['cluster_max']):
        event(book, 'reject', t, coin=coin, reason='major_cluster_max_1')
        return False
    stop = px*(1-d*stop_pct)
    eq = sc.equity(book)
    if eq <= 0:
        return False
    budget = min(eq*.005, eq*.02-sc.open_risk(book, CFG))
    rpu = risk_per_unit(px, stop, funding_rate, d)
    qty = min(budget/rpu, (eq*3-sc.notional_open(book))/px, eq*.8*3/px)
    if desired is not None:
        qty = min(qty, abs(desired))
    dec = ctx[coin]['szDecimals']
    qty = sc.floor_sz(qty, dec)
    if qty <= 0:
        return False
    if depth is not None:
        # Reuse the desk's existing risk-aware iterative L2 sizing, then apply funding reserve.
        estimate = size_order(CFG, book, coin, d, stop, depth, ctx)
        qty = min(qty, estimate['size'])
        fill, _ = sc.walk_book(depth, d, qty) if qty > 0 else (px,px)
        # Stop is a percentage of the actual fill, not of a stale quote.
        stop = fill*(1-d*stop_pct)
        qty = sc.floor_sz(min(qty, budget/risk_per_unit(fill, stop, funding_rate, d)), dec)
        fill, _ = sc.walk_book(depth, d, qty) if qty > 0 else (px,px)
        stop = fill*(1-d*stop_pct)
    else:
        fill = px*(1+d*.0002)
        stop = fill*(1-d*stop_pct)
        qty = sc.floor_sz(min(qty, budget/risk_per_unit(fill,stop,funding_rate,d)), dec)
    if qty*fill < 10:
        event(book, 'reject', t, coin=coin, reason='minimum_notional_10_vs_cost_inclusive_risk',
              proposed_notional=qty*fill, budget=budget)
        return False
    risk = qty*risk_per_unit(fill,stop,funding_rate,d)
    fee = qty*fill*CFG['taker_fee']
    if risk > budget+1e-9 or qty*fill/(eq-fee) > 3+1e-9:
        event(book,'reject',t,coin=coin,reason='final_risk_or_leverage_check')
        return False
    tid = f"P{book['next_seq']:06d}"
    book['next_seq'] += 1
    p = dict(id=tid,coin=coin,dir=d,side='long' if d>0 else 'short',size=qty,
             size_initial=qty,entry_px=fill,entry_ms=t,stop=stop,fees=fee,
             realized_gross=0.,funding=0.,risk_at_entry=risk,funding_hour=t//HOUR,
             risk_cap_at_entry=budget)
    book['positions'][tid] = p
    book['cash'] -= fee
    book['stats']['fees'] += fee
    event(book,'entry',t,trade_id=tid,coin=coin,side=p['side'],size=qty,price=fill,
          stop=stop,fee=fee,cost_inclusive_risk=risk,risk_budget=budget,
          fill_source='observed_live_L2_walk' if depth else 'observed_mid_plus_2bps')
    return True

def start_benchmark(book, data, now):
    if book.get('benchmark_started'):
        return
    px = data['mids']['BTC']*(1+.0002)
    # 1x after the entry fee, all-in control; not a risk-compliant strategy.
    qty = 100/(px*(1+CFG['taker_fee']))
    fee = qty*px*CFG['taker_fee']
    book['cash'] -= fee
    book['stats']['fees'] += fee
    book['positions']['BENCH'] = dict(id='BENCH',coin='BTC',dir=1,side='long',size=qty,
        entry_px=px,entry_ms=now,stop=None,fees=fee,realized_gross=0.,funding=0.,funding_hour=now//HOUR)
    book['benchmark_started'] = True
    event(book,'entry',now,trade_id='BENCH',coin='BTC',price=px,size=qty,fee=fee,
          reason='NONTRADABLE_1x_BTC_perp_buy_hold_control_no_stop',risk_exception=True)

def resolve_stop(book, p, bar, observed):
    """Gap-aware minute replay, using the existing sentinel's stop-fill primitive."""
    if bar['t']+MINUTE <= p['entry_ms']:
        return False
    entry_minute_ambiguous = bar['t'] < p['entry_ms']
    adverse = bar['l'] if p['dir'] > 0 else bar['h']
    if hit_adverse(p, adverse):
        gap = hit_adverse(p, bar['o']) and not entry_minute_ambiguous
        px = stop_fill(p,CFG,bar['o'] if not entry_minute_ambiguous else p['stop'])
        ts = bar['t'] if gap else bar['t']+MINUTE-1
        close(book,p,px,ts,'stop',bar_t=bar['t'],observed_at_utc=utc(observed),
              replayed=observed-bar['t']>2*MINUTE,gap_through_stop=gap,
              stop_trigger=p['stop'],bar_resolution='1m',entry_minute_ambiguous=entry_minute_ambiguous,
              fill_timing='bar_open_gap' if gap else 'intraminute_unknown_stop_assumed')
        return True
    return False

def decision(book, coin, sig, data, now, boundary, allow_entry):
    event(book,'signal',now,coin=coin,boundary_utc=utc(boundary),side=sig['side'],
          details=sig['details'],entry_window_open=allow_entry)
    d = sig['side']
    current = next((p for p in book['positions'].values() if p['coin']==coin),None)
    mid = data['mids'][coin]
    if current:
        exit_sig = sig['exit_long'] if current['dir'] > 0 else sig['exit_short']
        timed = book['kind']=='rsi' and now-current['entry_ms'] >= 48*HOUR
        if exit_sig or timed or d == -current['dir']:
            px = mid*(1-current['dir']*.0002)
            close(book,current,px,now,'signal_or_time_exit',signal_boundary_utc=utc(boundary),
                  delay_ms=now-boundary)
            current = None
    if book['kind']=='ewmac':
        stopped = book['stopped_sides'].get(coin,0)
        if stopped and d == stopped:
            event(book,'reject',now,coin=coin,reason='EWMAC_stopped_until_sign_change')
            return
        if d != stopped:
            book['stopped_sides'].pop(coin,None)
        E = sc.equity(book)
        target = E*sig['vol_scale']*sig['forecast']/10/sig['signal_close']
        buffer = .10*E*sig['vol_scale']/sig['signal_close']
        old = current['dir']*current['size'] if current else 0.
        if abs(old-target) <= buffer:
            return
        target = target+buffer if old > target+buffer else target-buffer
        if target*d <= 0:
            target = 0.
        if current:
            # Conservative overlay: never add/rebalance up inside a position episode.
            # Original Carver rebalances; new id explicitly freezes this difference.
            if abs(target) < current['size'] and (current['size']-abs(target))*mid >= 10:
                q = sc.floor_sz(current['size']-abs(target),data['ctx'][coin]['szDecimals'])
                close(book,current,mid*(1-current['dir']*.0002),now,'buffer_reduce',qty=q)
            return
        desired = abs(target)
    else:
        desired = None
    if not d or current:
        return
    if not allow_entry:
        event(book,'missed_entry',now,coin=coin,reason='no_hindsight_entry_signal_expired',boundary_utc=utc(boundary))
        return
    open_paper(book,coin,d,sig['stop_pct'],mid,now,data['ctx'],data['ctx'][coin]['funding'],
               data['books'].get(coin),desired)

def apply_tick(st, data, now):
    """Pure state mutation; caller atomically commits all books + event ledgers together."""
    end = now//MINUTE*MINUTE
    bycoin = {c:{b['t']:b for b in data['minutes'][c]} for c in COINS}
    # Check all coverage before changing any book; never skip a missing downtime candle.
    for t in range(st['next_minute'],end,MINUTE):
        if not all(t in bycoin[c] for c in COINS):
            raise ValueError(f'UNRESOLVED_REPLAY_GAP at {utc(t)}; entries blocked; cursor not advanced')
    for t in range(st['next_minute'],end,MINUTE):
        bars = {c:bycoin[c][t] for c in COINS}
        for b in st['books'].values():
            # Roll day at preceding mark/open, before this minute's costs/move.
            mark(b,{c:bars[c]['o'] for c in COINS},t)
            funding_at(b,data['funding'],bars,t)
            if b['kind']!='benchmark':
                for p in list(b['positions'].values()):
                    resolve_stop(b,p,bars[p['coin']],now)
                    if p['id'] in b['positions'] and b['kind']=='rsi' and t+MINUTE-1 >= p['entry_ms']+48*HOUR:
                        close(b,p,bars[p['coin']]['c']*(1-p['dir']*.0002),t+MINUTE-1,'time_exit_48h',replayed=now-t>2*MINUTE)
            mark(b,{c:bars[c]['c'] for c in COINS},t+MINUTE-1)
            halt(b,t+MINUTE-1)
            enforce_cost_risk(b,t+MINUTE-1)
    st['next_minute'] = end
    for b in st['books'].values():
        mark(b,data['mids'],now)
        if b['kind']=='benchmark':
            start_benchmark(b,data,now)
            mark(b,data['mids'],now)
        else:
            for p in list(b['positions'].values()):
                mid = data['mids'][p['coin']]
                if hit_adverse(p,mid):
                    close(b,p,mid*(1-p['dir']*.0005),now,'stop',gap_through_stop=True,
                          note='current observable mid through stop; no retroactive stop-price guarantee')
                elif b['kind']=='rsi' and now-p['entry_ms'] >= 48*HOUR:
                    close(b,p,mid*(1-p['dir']*.0002),now,'time_exit_48h')
            halt(b,now)
            enforce_cost_risk(b,now)
            interval = DAY if b['kind']=='ewmac' else 4*HOUR
            boundary = now//interval*interval
            for coin in COINS:  # deterministic priority BTC, ETH, SOL for cluster conflicts
                if b['decisions'].get(coin,0) >= boundary:
                    continue
                rows = data['daily'][coin] if interval == DAY else data['fourhour'][coin]
                if not rows or rows[-1]['t']+interval != boundary:
                    raise ValueError(f'stale {coin} signal candles for {b["id"]}')
                sig = signal(b['kind'],rows,data['funding'][coin],boundary)
                decision(b,coin,sig,data,now,boundary,now-boundary <= 120000)
                b['decisions'][coin] = boundary
        b['last_tick_myt'] = sc.myt(now)
        mark(b,data['mids'],now)
        event(b,'valuation',now,equity=sc.equity(b),cash=b['cash'],unrealized=sc.unrealized(b),
              fees=b['stats']['fees'],funding=b['stats']['funding'],positions=len(b['positions']),
              max_drawdown_pct=b['max_drawdown_pct'])
    st.update(last_tick_ms=now,ticks=st['ticks']+1)
    return st

class PublicData:
    ALLOWED = {'candleSnapshot','allMids','metaAndAssetCtxs','fundingHistory','l2Book'}
    def __init__(self, root):
        self.root = root
        self.path = root/'market_cache.json'
        self.cache = read_json(self.path) if self.path.exists() else dict(fourhour={},daily={},funding={})
        self.requests = []
    def request(self, payload):
        if payload.get('type') not in self.ALLOWED:
            raise ValueError('non-public request refused')
        start = sc.now_ms()
        response = sc.info(payload,timeout=12,retries=1)
        self.requests.append(dict(request=payload,request_ms=start,received_ms=sc.now_ms(),response=response))
        return response
    def candles(self, coin, interval, start, end):
        raw = self.request(dict(type='candleSnapshot',req=dict(coin=coin,interval=interval,startTime=start,endTime=end)))
        return [dict(t=int(c['t']),**{k:float(c[k]) for k in ('o','h','l','c','v')}) for c in raw]
    def history(self, key, coin, interval, count, now):
        step = DAY if interval=='1d' else 4*HOUR
        rows = self.cache[key].get(coin,[])
        closed_end = now//step*step
        if not rows or rows[-1]['t']+step < closed_end:
            start = rows[-1]['t'] if rows else closed_end-count*step
            new = self.candles(coin,interval,start,now)
            merged = {r['t']:r for r in rows}
            merged.update({r['t']:r for r in new if r['t']+step <= now})
            rows = [merged[t] for t in sorted(merged)]
            self.cache[key][coin] = rows
        if len(rows)<count or any(b['t']-a['t']!=step for a,b in zip(rows,rows[1:])):
            raise ValueError(f'{coin} {interval} warmup/continuity missing')
        return rows
    def funding(self,coin,start,now):
        rows = self.cache['funding'].get(coin,[])
        # Preserve every actual timestamp and fetch overlap. No missing hour becomes zero.
        cursor = max(start, rows[-1]['time']-HOUR) if rows else start
        latest_hour = (now//HOUR-1)*HOUR  # do not insist on a just-settling print at the current instant
        if rows and rows[-1]['time']//HOUR*HOUR >= now//HOUR*HOUR:
            return rows
        for _ in range(100):
            raw = self.request(dict(type='fundingHistory',coin=coin,startTime=cursor,endTime=now))
            merged = {r['time']:r for r in rows}
            for r in raw:
                if r['time'] in merged and merged[r['time']] != r:
                    raise ValueError('conflicting funding duplicate')
                merged[r['time']] = r
            rows = [merged[t] for t in sorted(merged)]
            if len(raw)<500:
                break
            next_cursor = max(r['time'] for r in raw)+1
            if next_cursor<=cursor:
                raise ValueError('funding pagination did not advance')
            cursor = next_cursor
        else:
            raise ValueError('funding page limit exceeded')
        self.cache['funding'][coin] = rows
        return rows
    def fetch(self, st, now):
        raw = self.request(dict(type='allMids'))
        mids = {c:float(raw[c]) for c in COINS}
        meta, contexts = self.request(dict(type='metaAndAssetCtxs'))
        ctx = {u['name']:dict(szDecimals=u['szDecimals'],maxLeverage=u['maxLeverage'],
                  **{k:float(v[k]) for k in ('funding','markPx','oraclePx')})
               for u,v in zip(meta['universe'],contexts) if u['name'] in COINS}
        if set(ctx)!=set(COINS) or any(mids[c]<=0 or not math.isfinite(mids[c]) for c in COINS):
            raise ValueError('invalid market snapshot')
        d = dict(mids=mids,ctx=ctx,minutes={},fourhour={},daily={},funding={},books={})
        for c in COINS:
            d['minutes'][c] = self.candles(c,'1m',st['next_minute'],now)
            d['fourhour'][c] = self.history('fourhour',c,'4h',710,now)
            d['daily'][c] = self.history('daily',c,'1d',250,now)
            start = min(st['next_minute']-HOUR,now-48*HOUR)
            d['funding'][c] = self.funding(c,start,now)
        # Only need depth during open entry windows; avoid unneeded API weight.
        if now%(4*HOUR) <= 120000 or now%DAY <= 120000:
            for c in COINS:
                raw = self.request(dict(type='l2Book',coin=c))
                if abs(now-int(raw['time'])) > 120000:
                    raise ValueError('stale L2')
                d['books'][c] = dict(bids=[(float(x['px']),float(x['sz'])) for x in raw['levels'][0]],
                                    asks=[(float(x['px']),float(x['sz'])) for x in raw['levels'][1]])
        received = sc.now_ms()
        if received-now > MINUTE:
            raise ValueError('snapshot collection exceeded 60s; retry without stale entries')
        source = self.root/'sources'/f'{now}.json.gz'
        source.parent.mkdir(exist_ok=True)
        with gzip.open(source,'wt') as f:
            json.dump(dict(network='mainnet_public_read_only',asof_utc=utc(now),requests=self.requests),f)
        self.requests = []
        atomic(self.path,self.cache)
        d['evidence'] = dict(path=str(source.relative_to(self.root)),sha256=sha(source),received_ms=received)
        return d

def metrics(b):
    tr = b['closed_trades']
    pnl = [t['pnl_net'] for t in tr]
    gains, losses = sum(x for x in pnl if x>0), -sum(x for x in pnl if x<0)
    return dict(trades=len(tr),win_rate=sum(x>0 for x in pnl)/len(pnl)*100 if pnl else None,
        net_pnl=sc.equity(b)-100,realized=sum(pnl),profit_factor=gains/losses if losses else ('inf' if gains else None),
        max_drawdown_pct=b['max_drawdown_pct'],expectancy=sum(pnl)/len(pnl) if pnl else None,
        equity=sc.equity(b),fees=b['stats']['fees'],funding=b['stats']['funding'])

def export(st, root):
    rows = []
    for b in st['books'].values():
        directory = root/'books'/b['id']
        directory.mkdir(parents=True,exist_ok=True)
        atomic(directory/'state.json',b)
        path = directory/'ledger.jsonl'
        tmp = path.with_suffix('.tmp')
        tmp.write_text(''.join(json.dumps(e,allow_nan=False)+'\n' for e in b['events']))
        os.replace(tmp,path)
        m = metrics(b)
        def fmt(v):
            return '—' if v is None else (v if isinstance(v,str) else f'{v:.4f}')
        rows.append((b,m))
    text = '# Forward PAPER strategy league\n\n'
    text += f"Updated: {sc.myt(st['last_tick_ms'])} MYT | tick {st['ticks']} | 100 virtual USDC/book | no keys/orders.\n\n"
    text += '| Book / idea owner | Closed trades | Win % | Net MTM PnL USDC | Realized net | PF | MaxDD % | Expectancy USDC/trade | Fees | Funding net | Status |\n'
    text += '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|\n'
    for b,m in sorted(rows,key=lambda x:x[1]['net_pnl'],reverse=True):
        status = 'NOT SIGNIFICANT (<30 trades)' if m['trades']<30 else 'UNPROVEN (30 is not a PASS; 100+ and review needed)'
        if b['halted']:
            status += '; HALTED'
        if b['kind']=='benchmark':
            status += '; NONTRADABLE CONTROL (no risk stops)'
        text += f"| {b['id']} / {b['owner']} | {m['trades']} | {fmt(m['win_rate'])} | {m['net_pnl']:+.4f} | {m['realized']:+.4f} | {fmt(m['profit_factor'])} | {m['max_drawdown_pct']:.4f} | {fmt(m['expectancy'])} | {m['fees']:.4f} | {m['funding']:+.4f} | {status} |\n"
    text += '\nNet MTM includes open PnL, all charged fees and funding. Win/PF/expectancy use completed episodes only; no closed trades means unavailable, not zero edge.\n'
    text += 'Funding rates are observed settled HL hourly rates; cash amounts use each settlement minute open as an explicitly estimated historical-oracle proxy.\n'
    text += 'MaxDD is sampled 1m-close/live-mid equity (not true tick-by-tick maximum). PnL is indicative; open liquidation fee is not deducted.\n'
    text += 'BTC control is 1x initial BTC PERP exposure, no rebalance, fees + hourly funding, no stop/halt; it is a measurement exception, never a permitted strategy.\n'
    text += 'Four research books retain previous failures/unproven status. No auto-promotion, no profit promise; prior search count 309.\n'
    tmp = root/'leaderboard.md.tmp'
    tmp.write_text(text)
    os.replace(tmp,root/'leaderboard.md')

def tick(root=ROOT):
    m = registration(root)
    now = sc.now_ms()
    path = root/'league_state.json'
    st = read_json(path) if path.exists() else new_state(m,now)
    registration_digest = sha(root/'registry/manifest.json')
    if st.get('registration_sha256',registration_digest) != registration_digest:
        raise ValueError('registration manifest changed since first tick; new league id required')
    st['registration_sha256'] = registration_digest
    # Clone transaction: a failed data/funding/signal check cannot partially change persisted books.
    candidate = copy.deepcopy(st)
    data = PublicData(root).fetch(st,now)
    apply_tick(candidate,data,now)
    candidate['last_evidence'] = data['evidence']
    atomic(path,candidate)
    export(candidate,root)
    result = dict(status='ok',mode='PAPER_ONLY',tick=candidate['ticks'],ts_myt=sc.myt(now),ts_utc=utc(now),
                  evidence=data['evidence'],books={b['id']:dict(equity=round(sc.equity(b),8),
                  positions=len(b['positions']),closed_trades=len(b['closed_trades'])) for b in candidate['books'].values()})
    atomic(root/'last_tick.json',result)
    return result

def heartbeat(root,status,**details):
    atomic(root/'heartbeat.json',dict(pid=os.getpid(),ts_ms=sc.now_ms(),ts_myt=sc.myt(),status=status,**details))

def stop(*_):
    global RUNNING
    RUNNING=False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--once',action='store_true')
    args = ap.parse_args()
    with open(ROOT/'.engine.lock','a') as lock:
        try:
            fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError:
            print('another league engine holds the lock',flush=True)
            return 0
        if args.once:
            print(json.dumps(tick(),indent=2))
            return 0
        (ROOT/'engine.pid').write_text(str(os.getpid()))
        signals.signal(signals.SIGTERM,stop)
        signals.signal(signals.SIGINT,stop)
        while RUNNING:
            start=time.monotonic()
            heartbeat(ROOT,'fetching')
            try:
                result=tick()
                heartbeat(ROOT,'ok',last_success_ms=sc.now_ms(),tick=result['tick'])
                print(json.dumps(result),flush=True)
            except Exception as e:
                heartbeat(ROOT,'ERROR_NO_NEW_RISK',error=repr(e))
                print(f'{sc.myt()} ERROR_NO_NEW_RISK {e!r}',flush=True)
                # Let the wrapper restart after backoff rather than a silent error loop.
                return 1
            while RUNNING and time.monotonic()-start < 60:
                time.sleep(.5)
        heartbeat(ROOT,'stopped')
        return 0

if __name__=='__main__':
    sys.exit(main())
