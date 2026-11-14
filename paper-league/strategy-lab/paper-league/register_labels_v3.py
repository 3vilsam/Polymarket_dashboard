#!/usr/bin/env python3
"""One-shot append-only registry labels note (labels-v3): ABLATION_FAIL_2026-11-12 tag for n1-tsmom-mh1h-v1 and n7-xsmom72h-v1.
Informational tag only. No rule-file edits, no hash changes, no status/engine change: books keep running."""
import json
import league as L
ROOT = L.ROOT
if (ROOT/'registry/labels-v3.json').exists() or (ROOT/'registry/labels-v3.md').exists(): raise SystemExit('Refusing labels-v3 overwrite')
created = L.utc(L.sc.now_ms())
st = L.read_json(ROOT/'league_state.json')
ext = L.read_json(ROOT/'registry/extension-v4.json'); by_id = {s['id']: s['sha256'] for s in ext['strategies']}
books = ['n1-tsmom-mh1h-v1', 'n7-xsmom72h-v1']
for b in books:
    assert b in st['books'], b
    rule = ROOT/'registry'/f'{b}.md'
    assert L.sha(rule) == by_id[b], f'rule file changed vs extension-v4: {b}'
    assert (ROOT/'registry'/f'{b}.sha256').read_text().split()[0] == by_id[b], f'rule .sha256 mismatch: {b}'
TAG = 'ABLATION_FAIL_2026-11-12'
desc = ('Historical stepwise ablation research/ablation/2026-11-12-trend-n1-n7 (HL 1h, 197 tradable days): no edge after HL costs. '
        'n1 full book net PF 0.76 IS / 0.71 OOS (gross 1.03/1.00); n7 1.12 / 0.50 (gross OOS 0.67). Research tag only.')
labels = {b: dict(label=TAG, description=desc, rule_sha256=by_id[b], status_change=None, still_active=True) for b in books}
note = f'''# Append-only registry note: labels-v3

Recorded UTC: {created}. Decided by Skippy (desk coordinator) on 12 Nov 2026 after the n1/n7 ablation (`/workspace/trading-desk/research/ablation/2026-11-12-trend-n1-n7/README.md`). Frozen rules are not altered mid-run: no rule file is edited and no registered sha256 changes. Sizing, signals, data rules, book status and the engine are unchanged. These books are NOT retired, halted or disabled; they keep running in the paper league. labels-v1 and labels-v2 are unchanged.

1. {TAG}: {', '.join(books)}. {desc}
   Rule files and sha256 unchanged (as registered in extension-v4.json):
''' + ''.join(f'   - `{b}`: `{by_id[b]}`\n' for b in books) + '''2. The n7 24h-lookback leave-one-out result (OOS PF 1.59) is discovery-only, seen after the holdout was used. No rule change; it is UNTRADEABLE until a new frozen rule set under a new id passes a forward test.
3. DSR multiplicity: desk total 550 known trials (500 + 50 fresh research trials from that ablation). No league book is added or removed.
'''
path = ROOT/'registry/labels-v3.md'
with path.open('x') as f: f.write(note)
digest = L.sha(path)
with path.with_suffix('.sha256').open('x') as f: f.write(f'{digest}  {path.name}\n')
m = dict(note_id='labels-v3', mode='PAPER_ONLY', recorded_utc=created, note_sha256=digest, labels=labels,
         books_still_active=True, still_active=True, status_change=None, engine_change=False,
         dsr_trial_count=550, dsr_trial_count_basis='500 (labels-v2) + 50 research (2026-11-12-trend-n1-n7)',
         discovery_only=dict(variant='n7 lookback 24h (LOO)', oos_net_pf=1.59, status='UNTRADEABLE_DISCOVERY_ONLY', rule_change=None),
         labels_v1_sha256=L.sha(ROOT/'registry/labels-v1.json'), labels_v2_sha256=L.sha(ROOT/'registry/labels-v2.json'),
         extension_v4_sha256=L.sha(ROOT/'registry/extension-v4.json'),
         implementation_sha256={'register_labels_v3.py': L.sha(ROOT/'register_labels_v3.py')},
         source_research='/workspace/trading-desk/research/ablation/2026-11-12-trend-n1-n7/README.md')
with (ROOT/'registry/labels-v3.json').open('x') as f: json.dump(m, f, indent=2)
with (ROOT/'registry/labels-v3.json.sha256').open('x') as f: f.write(L.sha(ROOT/'registry/labels-v3.json')+'  labels-v3.json\n')
print('Registered labels-v3', digest)
