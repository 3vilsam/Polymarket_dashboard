#!/usr/bin/env python3
"""Read-only live receipt verification for the 116-book spot expansion."""
from pathlib import Path
from datetime import datetime
import gzip,json
import league as L
import league_v3 as V3
root=L.ROOT; old,ext,spot=V3.registration(); st=L.read_json(root/'league_state.json')
if len(st['books'])!=116: raise SystemExit('116-book live tick not yet committed')
if 'spot_extension_registration_sha256' not in st: raise SystemExit('spot extension not pinned in state')
first=L.read_json(root/'first-live-tick-v3.json'); last=L.read_json(root/'last_tick.json')
# Preserve original five and the pre-spot 100-book event prefixes.
prior_v2=L.read_json(root/'backups/extension-v2/final-pre-extension-state.json') if (root/'backups/extension-v2/final-pre-extension-state.json').exists() else None
pre_spot=root/'backups/spot-v3/final-pre-spot-state.json'
if pre_spot.exists():
    prior=L.read_json(pre_spot)
    for id,b in prior['books'].items():
        if st['books'][id]['events'][:len(b['events'])]!=b['events']: raise ValueError('old event prefix changed '+id)
        if abs(st['books'][id].get('starting_equity',100)-b.get('starting_equity',100))>1e-12 and 'spot_spec' not in st['books'][id]:
            raise ValueError('perp starting equity changed '+id)
checks={}
for b in st['books'].values():
    start=float(b.get('starting_equity',100.))
    events=b['events']
    reconstructed=start+sum(e.get('pnl_gross',0) for e in events if e['event']=='exit')-sum(e.get('fee',0) for e in events if e['event'] in ('entry','exit'))+sum(e.get('payment',0) for e in events if e['event']=='funding')
    if abs(reconstructed-b['cash'])>1e-7: raise ValueError('cash accounting mismatch '+b['id'])
    if b['evaluation']['trial_count']!=425: raise ValueError('multiplicity count mismatch '+b['id'])
    export=L.read_json(root/'books'/b['id']/'state.json')
    if export!=b: raise ValueError('export mismatch '+b['id'])
    if b['kind'] not in ('benchmark','spot_hold'):
        if len(b['positions'])>1: raise ValueError('cluster/spot position cap violation '+b['id'])
        for p in b['positions'].values():
            if b.get('market')=='spot':
                if p['coin'] not in ('UBTC','UETH','USOL','HYPE') or p.get('dir',1)!=1 or p.get('leverage',1)!=1:
                    raise ValueError('spot invariant failed '+b['id'])
                if not p.get('stop'): raise ValueError('spot research book missing stop '+b['id'])
            else:
                if p['coin'] not in ('BTC','ETH','SOL') or not p['stop'] or p['risk_at_entry']>p['risk_cap_at_entry']+1e-8:
                    raise ValueError('risk invariant failed '+b['id'])
    if 'spot_spec' in b and abs(start-16.24)>1e-12: raise ValueError('spot starting equity '+b['id'])
    checks[b['id']]=dict(cash_reconciled=True,closed=len(b['closed_trades']),open=len(b['positions']),starting_equity=start)
registered=int(datetime.fromisoformat(spot['registered_utc'].replace('Z','+00:00')).timestamp()*1000)
if registered>int(datetime.fromisoformat(first['ts_utc'].replace('Z','+00:00')).timestamp()*1000): raise ValueError('late registration')
source=root/st['last_evidence']['path']
if L.sha(source)!=st['last_evidence']['sha256']: raise ValueError('source hash mismatch')
with gzip.open(source,'rt') as f: archive=json.load(f)
if any(r['request']['type'] not in V3.PublicData.ALLOWED for r in archive['requests']): raise ValueError('nonpublic source')
report=dict(verified_myt=L.sc.myt(),mode='PAPER_ONLY',book_count=116,trial_count=425,
 original_and_v2_event_prefixes_preserved=pre_spot.exists(),frozen_registration_verified=True,
 preregistered_before_first_tick=True,first_tick_myt=first['ts_myt'],last_tick_myt=last['ts_myt'],
 last_load=last.get('load'),supervisor_pid=int((root/'supervisor.pid').read_text()),
 engine_pid=int((root/'engine.pid').read_text()),engine_version=last.get('engine_version'),
 public_source_types=sorted({r['request']['type'] for r in archive['requests']}),
 spot_extension_manifest_sha256=L.sha(root/'registry/spot-extension-v3.json'),
 extension_v2_manifest_sha256=L.sha(root/'registry/extension-v2.json'),book_checks=checks)
L.atomic(root/'verification-v3.json',report)
print(json.dumps({k:v for k,v in report.items() if k!='book_checks'},indent=2))
