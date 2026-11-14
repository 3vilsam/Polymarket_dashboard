#!/usr/bin/env python3
"""Read-only live receipt verification; writes only this report on the box."""
from pathlib import Path
from datetime import datetime
import gzip,json
import league as L
import league_v2 as V
root=L.ROOT; old,ext=V.registration(); st=L.read_json(root/'league_state.json')
if len(st['books'])!=100: raise SystemExit('100-book live tick not yet committed')
first=L.read_json(root/'first-live-tick-v2.json'); last=L.read_json(root/'last_tick.json')
prior=L.read_json(root/'backups/extension-v2/final-pre-extension-state.json')
for id,b in prior['books'].items():
    if st['books'][id]['events'][:len(b['events'])]!=b['events']: raise ValueError('old event prefix changed')
checks={}
for b in st['books'].values():
    events=b['events']; reconstructed=100.+sum(e.get('pnl_gross',0) for e in events if e['event']=='exit')-sum(e.get('fee',0) for e in events if e['event'] in ('entry','exit'))+sum(e.get('payment',0) for e in events if e['event']=='funding')
    if abs(reconstructed-b['cash'])>1e-7: raise ValueError('cash accounting mismatch '+b['id'])
    if b['evaluation']['trial_count']!=409: raise ValueError('multiplicity count mismatch')
    export=L.read_json(root/'books'/b['id']/'state.json')
    if export!=b: raise ValueError('export mismatch '+b['id'])
    if b['kind']!='benchmark':
        if len(b['positions'])>1: raise ValueError('cluster risk violation')
        for p in b['positions'].values():
            if p['coin'] not in ('BTC','ETH','SOL') or not p['stop'] or p['risk_at_entry']>p['risk_cap_at_entry']+1e-8: raise ValueError('risk invariant failed')
    checks[b['id']]=dict(cash_reconciled=True,closed=len(b['closed_trades']),open=len(b['positions']))
registered=int(datetime.fromisoformat(ext['registered_utc'].replace('Z','+00:00')).timestamp()*1000)
if registered>int(datetime.fromisoformat(first['ts_utc'].replace('Z','+00:00')).timestamp()*1000): raise ValueError('late registration')
source=root/st['last_evidence']['path']
if L.sha(source)!=st['last_evidence']['sha256']: raise ValueError('source hash mismatch')
with gzip.open(source,'rt') as f: archive=json.load(f)
if any(r['request']['type'] not in V.PublicData.ALLOWED for r in archive['requests']): raise ValueError('nonpublic source')
report=dict(verified_myt=L.sc.myt(),mode='PAPER_ONLY',book_count=100,original_five_event_prefixes_preserved=True,
 frozen_registration_verified=True,preregistered_before_first_tick=True,trial_count=409,
 first_tick_myt=first['ts_myt'],last_tick_myt=last['ts_myt'],last_load=last['load'],
 supervisor_pid=int((root/'supervisor.pid').read_text()),engine_pid=int((root/'engine.pid').read_text()),
 public_source_types=sorted({r['request']['type'] for r in archive['requests']}),
 extension_manifest_sha256=L.sha(root/'registry/extension-v2.json'),book_checks=checks)
L.atomic(root/'verification-v2.json',report)
print(json.dumps({k:v for k,v in report.items() if k!='book_checks'},indent=2))
