#!/usr/bin/env python3
"""One-shot append-only registry labels note (labels-v2): ABLATION_FAIL_2026-11-12 tag for three VWAP books.
Informational tag only. No rule-file edits, no hash changes, no status/engine change: books keep running."""
import json
import league as L
ROOT = L.ROOT
if (ROOT/'registry/labels-v2.json').exists(): raise SystemExit('Refusing labels-v2 overwrite')
created = L.utc(L.sc.now_ms())
st = L.read_json(ROOT/'league_state.json')
ext = L.read_json(ROOT/'registry/extension-v2.json'); by_id = {s['id']: s['sha256'] for s in ext['strategies']}
books = ['f1-vwap5m-v1', 'g-vwap-all-p1-v1', 'g-vwap-btc-p1-v1']
for b in books:
    assert b in st['books'], b
    assert L.sha(ROOT/'registry'/f'{b}.md') == by_id[b], f'rule file changed {b}'
TAG = 'ABLATION_FAIL_2026-11-12'
desc = ('Historical stepwise ablation research/ablation/2026-11-12-vwap: no edge survives costs '
        '(full frozen book PF < 1 IS and OOS on HL 5m 15.4d and on Binance 5m SUBSTITUTE 101d). Research tag only.')
labels = {b: dict(label=TAG, description=desc, rule_sha256=by_id[b], status_change=None, still_active=True) for b in books}
note = f'''# Append-only registry note: labels-v2

Recorded UTC: {created}. Decided by Skippy (desk coordinator) on 12 Nov 2026 after the VWAP-family ablation (`/workspace/trading-desk/research/ablation/2026-11-12-vwap/README.md`). Frozen rules are not altered mid-run: no rule file is edited and no registered sha256 changes. Sizing, signals, data rules, book status and the engine are unchanged. These books are NOT retired, halted or disabled; they keep running in the paper league. labels-v1 is unchanged.

1. {TAG}: {', '.join(books)}. {desc}
   Rule files and sha256 unchanged:
''' + ''.join(f'   - `{b}`: `{by_id[b]}`\n' for b in books) + '''2. DSR multiplicity: desk total 500 known trials (registry 434 + 66 fresh research trials from that ablation). No league book is added or removed (125 books).
'''
path = ROOT/'registry/labels-v2.md'
with path.open('x') as f: f.write(note)
digest = L.sha(path)
with path.with_suffix('.sha256').open('x') as f: f.write(f'{digest}  {path.name}\n')
m = dict(note_id='labels-v2', mode='PAPER_ONLY', recorded_utc=created, note_sha256=digest, labels=labels,
         books_still_active=True, engine_change=False, dsr_trial_count=500, dsr_trial_count_basis='434 registry + 66 research (2026-11-12-vwap)',
         total_league_books=125, labels_v1_sha256=L.sha(ROOT/'registry/labels-v1.json'),
         extension_v2_sha256=L.sha(ROOT/'registry/extension-v2.json'),
         implementation_sha256={'register_labels_v2.py': L.sha(ROOT/'register_labels_v2.py')},
         source_research='/workspace/trading-desk/research/ablation/2026-11-12-vwap/README.md')
with (ROOT/'registry/labels-v2.json').open('x') as f: json.dump(m, f, indent=2)
with (ROOT/'registry/labels-v2.json.sha256').open('x') as f: f.write(L.sha(ROOT/'registry/labels-v2.json')+'  labels-v2.json\n')
print('Registered labels-v2', digest)
