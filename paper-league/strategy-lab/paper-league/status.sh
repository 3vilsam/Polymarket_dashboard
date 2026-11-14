#!/usr/bin/env bash
set -eu
cd -- "$(dirname -- "$(readlink -f -- "$0")")"
python3 - "$@" <<'PY'
import json,os,time,sys
from pathlib import Path
import league as L
try:
    import labels as LB; LBM=LB.load()
except Exception: LBM=None
def tg(bid):
    if not LBM: return ''
    t=LB.tags(LBM,bid)
    return (' ['+', '.join(t)+']') if t else ''
full='--full' in sys.argv
for label,file,needle in [('supervisor','supervisor.pid','supervise.sh'),('engine','engine.pid','league_v8.py')]:
    try:
        pid=int(Path(file).read_text()); os.kill(pid,0)
        command=Path(f'/proc/{pid}/cmdline').read_bytes().decode().replace('\0',' ')
        print(f'{label}: PID {pid} '+('RUNNING' if needle in command else 'STALE PID / legacy engine'))
    except Exception: print(label+': NOT RUNNING')
try:
    hb=L.read_json('heartbeat.json'); age=time.time()-hb['ts_ms']/1000
    print(f"Heartbeat: {hb['ts_myt']} MYT; age {age:.1f}s; {hb['status']}"+(' STALE' if age>180 else ''))
    if hb.get('error'): print('ERROR:',hb['error'])
    if hb.get('load'): print('Last successful load:',json.dumps(hb['load'],sort_keys=True))
except FileNotFoundError: print('Heartbeat unavailable')
try:
    st=L.read_json('league_state.json'); age=time.time()-st['last_tick_ms']/1000
    print(f"Successful data: {age:.1f}s ago; ticks={st['ticks']}; books={len(st['books'])}; known DSR trials={309+len(st['books'])}"+(' STALE DATA' if age>180 else ''))
    bs=list(st['books'].values())
    print(f"Open virtual positions={sum(len(b['positions']) for b in bs)}; closed episodes={sum(len(b['closed_trades']) for b in bs)}; halted books={sum(b['halted'] for b in bs)}")
    print('Risk-review candidates:',', '.join(b['id'] for b in bs if b.get('evaluation',{}).get('status')=='CANDIDATE_REVIEW_ONLY') or 'none')
    def net(b):
        return L.sc.equity(b)-float(b.get('starting_equity',100.))
    def lane_of(b):
        if 'spot_spec' in b or b.get('market')=='spot': return b.get('lane','spot_slow')
        return 'control' if b['kind'] in ('benchmark','random') else b.get('lane','slow')
    if not full:
        for lane in ('control','fast','slow','spot_control','spot_fast','spot_slow'):
            group=[b for b in bs if lane_of(b)==lane]
            if not group: continue
            print(f'\n{lane.upper()} ({len(group)} books), highest current net MTM, NOT a profitability verdict:')
            for b in sorted(group,key=net,reverse=True)[:(2 if 'control' in lane else 3)]:
                e=b.get('evaluation',{}); m=L.metrics(b)
                print(f" {b['id']}{tg(b['id'])}{' (RETIRED_DATA_QUALITY)' if b.get('retired') else ''}: net={net(b):+.4f}; start={float(b.get('starting_equity',100.)):.2f}; closed={m['trades']}; open={len(b['positions'])}; DSR={e.get('dsr_probability')}; gate={e.get('status','legacy')}"+('; NOT SIGNIFICANT' if m['trades']<30 else ''))
        early=[b for b in bs if b.get('lane') in ('fast','spot_fast') and len(b.get('closed_trades',[]))>=10]
        print('\nEARLY READ (not evidence) — fast books with >=10 closed trades, ranked by trade count then net after costs. NOT significance, NOT a PASS, does not change the promotion bar, not a CANDIDATE:')
        if not early:
            print(' none yet')
        else:
            early=sorted(early,key=lambda b:(-len(b['closed_trades']), -net(b)))
            for b in early[:8]:
                e=b.get('evaluation',{}); m=L.metrics(b)
                print(f" {b['id']}{tg(b['id'])}: closed={m['trades']}; net={net(b):+.4f}; start={float(b.get('starting_equity',100.)):.2f}; gate={e.get('status','legacy')}"+('; NOT SIGNIFICANT' if m['trades']<30 else ''))
    if LBM:
        print('\nLABELS (registry/labels-v1, append-only):')
        for bid,lab in LBM['labels'].items():
            print(f" {bid}: {lab['label']}"+(' — PROMOTION-INELIGIBLE' if lab.get('promotion_eligible') is False else '')+f"; gate={st['books'][bid].get('evaluation',{}).get('status')}")
        print(' Clusters (each = ONE effective trial in promotion review; DSR count stays 434): '+'; '.join(f"{c}={len(v)} books" for c,v in LBM['clusters'].items()))
except FileNotFoundError: print('No successful tick')
if full: print('\n'+(Path('leaderboard.md').read_text() if Path('leaderboard.md').exists() else 'Leaderboard unavailable'))
else: print('\nFull tables: leaderboard.md or ./status.sh --full; paper only, no automatic promotion. Early-read (>=10 trades) is not the promotion bar.')
PY
