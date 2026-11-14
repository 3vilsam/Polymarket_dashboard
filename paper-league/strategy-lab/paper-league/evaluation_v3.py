"""Same promotion bar as v2; spot books use spot exit-cost estimates. Never promotion."""
import evaluation_v2 as E
import strategies_v3 as S
from statistics import stdev
from datetime import datetime
from strategies import DAY
import league as L

PRIOR_TRIALS=E.PRIOR_TRIALS  # 309
dsr=E.dsr
next_day=E.next_day

def liquidated_equity(b):
    # Indicative exit cost, not a fill. Spot books: official tier-0 spot taker + 2bp floor.
    # Perp books keep the frozen v2 estimate (perp taker + 2bp).
    if b.get('market')=='spot' or 'spot_spec' in b:
        rate=S.SPOT_TAKER+.0002
        return L.sc.equity(b)-sum(p['size']*b['marks'].get(p['coin'],p['entry_px'])*rate for p in b['positions'].values())
    return E.liquidated_equity(b)

def initialize(st, now):
    ids=list(st['books']); btc=next(i for i in ids if st['books'][i]['kind']=='benchmark')
    rand=next(i for i in ids if st['books'][i]['kind']=='random')
    for b in st['books'].values():
        if 'evaluation' not in b:
            b['evaluation']=dict(start_ms=now,start_equity=liquidated_equity(b),btc_id=btc,random_id=rand,
               btc_start=liquidated_equity(st['books'][btc]),random_start=liquidated_equity(st['books'][rand]),
               daily_returns=[],day=L.sc.myt_date(now),day_start=liquidated_equity(b),
               previous=liquidated_equity(b),skip_partial_day=True,status='NOT_SIGNIFICANT',flag_ms=None,oos=None)

def update(st, now):
    trials=PRIOR_TRIALS+len(st['books'])
    for b in st['books'].values():
        e=b['evaluation']; eq=liquidated_equity(b); day=L.sc.myt_date(now)
        if day!=e['day']:
            old_day=datetime.fromisoformat(e['day']).date(); new_day=datetime.fromisoformat(day).date()
            if (new_day-old_day).days==1 and not e['skip_partial_day']:
                e['daily_returns'].append(e['previous']/e['day_start']-1)
            e.update(day=day,day_start=eq,skip_partial_day=False)
        e['previous']=eq
    sharpes=[]
    for b in st['books'].values():
        r=b['evaluation']['daily_returns']
        if len(r)>=8 and stdev(r)>1e-14: sharpes.append(sum(r)/len(r)/stdev(r))
    sigma=stdev(sharpes) if len(sharpes)>1 else 0.
    for b in st['books'].values():
        e=b['evaluation']; eq=liquidated_equity(b)
        btc=liquidated_equity(st['books'][e['btc_id']]); rand=liquidated_equity(st['books'][e['random_id']])
        ret=eq/e['start_equity']-1
        e.update(trial_count=trials,dsr_probability=dsr(e['daily_returns'],trials,sigma),
             days=len(e['daily_returns']),return_pct=100*ret,
             excess_btc_pct=100*(ret-(btc/e['btc_start']-1)),
             excess_random_pct=100*(ret-(rand/e['random_start']-1)))
        closed=len(b['closed_trades']); control=b['kind'] in ('benchmark','random','spot_hold')
        qualified=(closed>=30 and ret>0 and e['excess_btc_pct']>0 and e['excess_random_pct']>0
                   and e['dsr_probability'] is not None and e['dsr_probability']>.95 and not b['halted'])
        if control:
            e['status']='CONTROL'; continue
        if e['flag_ms'] is None:
            e['status']='NOT_SIGNIFICANT' if closed<30 else 'UNPROVEN'
            if qualified:
                e.update(flag_ms=now,oos_earliest=next_day(now),status='FLAGGED_WAIT_FRESH_DAY')
                L.event(b,'evaluation_flag',now,trial_count=trials,dsr=e['dsr_probability'],note='not CANDIDATE; wait fresh MYT day and flat book')
        if e['flag_ms'] is not None and e['oos'] is None:
            e['status']='FLAGGED_WAIT_FRESH_DAY_FLAT'
            if now>=e['oos_earliest'] and not b['positions']:
                e['oos']=dict(start_ms=now,start_equity=eq,btc_start=btc,random_start=rand,start_closed=closed,
                              status='RUNNING',net_pct=0.,trades=0)
                L.event(b,'oos_start',now,equity=eq,note='fresh day, flat; no discovery trades in OOS')
        o=e['oos']
        if o is not None:
            nr=eq/o['start_equity']-1; nt=closed-o['start_closed']; elapsed=now-o['start_ms']
            complete=elapsed>=7*DAY or (b.get('lane') in ('fast','spot_fast') and nt>=30)
            o.update(net_pct=100*nr,trades=nt,elapsed_days=elapsed/DAY,
                     excess_btc_pct=100*(nr-(btc/o['btc_start']-1)),
                     excess_random_pct=100*(nr-(rand/o['random_start']-1)))
            if complete and o['status']=='RUNNING':
                passed=nr>0 and o['excess_btc_pct']>0 and o['excess_random_pct']>0 and not b['halted']
                o.update(status='PASS' if passed else 'FAIL',end_ms=now,end_net_pct=100*nr)
                L.event(b,'oos_end',now,verdict=o['status'],net_pct=100*nr,trades=nt)
            e['status']='CANDIDATE_REVIEW_ONLY' if o['status']=='PASS' else ('OOS_FAILED' if o['status']=='FAIL' else 'OOS_RUNNING')
            if o['status']=='PASS' and not qualified: e['status']='PAST_OOS_PASS_CURRENT_GATE_FAIL'
        if e['status']=='CANDIDATE_REVIEW_ONLY' and not e.get('review_recorded'):
            e['review_recorded']=True
            L.event(b,'candidate_for_risk_review',now,note='No auto-promotion or exchange action. Parent must send evidence for Risk Manager review.')
