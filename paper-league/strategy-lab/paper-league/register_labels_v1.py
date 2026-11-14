#!/usr/bin/env python3
"""One-shot append-only registry labels note (labels-v1). No rule-file edits, no hash changes."""
import json
import league as L
ROOT = L.ROOT
if (ROOT/'registry/labels-v1.json').exists(): raise SystemExit('Refusing labels-v1 overwrite')
created = L.utc(L.sc.now_ms())
st = L.read_json(ROOT/'league_state.json')
trend_kinds = ('donchian', 'ewmac', 'ema', 'supertrend', 'macd', 'weekly', 'spot_ema', 'spot_donchian', 'tsmom_mh', 'xs_momentum')
trend = sorted(k for k, b in st['books'].items() if b['kind'] in trend_kinds)
desc_nonv1 = ('Full-cash spot sizing (all-in ~16.2 USDC notional, ~0.7-4.7% equity at the stop), above risk-limits v1 0.5% per trade; '
              'spot/UBTC not named in v1; exchange spot trigger stops unverified. Research only.')
labels = {
 'sp4-shockrev1h-ubtc-v1': dict(label='NON_V1_RESEARCH', description=desc_nonv1, promotion_eligible=False),
 'sp4-utc21-ubtc-v1': dict(label='NON_V1_RESEARCH', description=desc_nonv1, promotion_eligible=False),
 'n6-ethbtc-z1h-v1': dict(label='UNHEDGED_ETH_DIRECTIONAL', description='Single-leg ETH perp trade driven by the ETH/BTC ratio z-score. Exposure is ETH directional beta (ETH-BTC 1h corr 0.918), NOT a hedged or market-neutral pair.'),
}
clusters = {
 'BTC_FRI21': sorted(['n3-negfund-btc-v1', 'n4-utc21-btc-v1', 'n5-weekend-btc-v1', 'sp4-utc21-ubtc-v1']),
 'SHOCKREV': sorted(['n2-shockrev1h-v1', 'sp4-shockrev1h-ubtc-v1']),
 'TREND': trend,
}
for ids in [list(labels)]+list(clusters.values()):
    for i in ids: assert i in st['books'], i
note = f'''# Append-only registry note: labels-v1

Recorded UTC: {created}. Decided by Skippy (desk coordinator) on 12 Nov 2026 after Risk Manager review `reviews/risk-review-2026-11-12.md`. Frozen rules are not altered mid-run: no rule file is edited and no registered sha256 changes. Sizing, signals, data rules and the DSR multiplicity count (434) are unchanged.

1. NON_V1_RESEARCH, promotion-ineligible: sp4-shockrev1h-ubtc-v1, sp4-utc21-ubtc-v1. {desc_nonv1} Their evaluation status is reported as INELIGIBLE_NON_V1_RESEARCH whatever the gate computes; they can never become CANDIDATE_REVIEW_ONLY. Becoming eligible needs a new registration with v1 risk sizing or an owner-confirmed spot addendum, under new book ids.
2. Cluster tags. Each cluster counts as ONE effective trial, i.e. one piece of independent evidence, in any promotion review: several members passing is not multiple confirmations.
   - BTC_FRI21: {', '.join(clusters['BTC_FRI21'])}
   - SHOCKREV: {', '.join(clusters['SHOCKREV'])}
   - TREND ({len(trend)} books; kinds {', '.join(trend_kinds)}): {', '.join(trend)}
3. n6-ethbtc-z1h-v1 relabelled UNHEDGED_ETH_DIRECTIONAL: {labels['n6-ethbtc-z1h-v1']['description']}
'''
path = ROOT/'registry/labels-v1.md'
with path.open('x') as f: f.write(note)
digest = L.sha(path)
with path.with_suffix('.sha256').open('x') as f: f.write(f'{digest}  {path.name}\n')
impl = {p: L.sha(ROOT/p) for p in ['labels.py', 'league_v7.py', 'register_labels_v1.py']}
m = dict(note_id='labels-v1', mode='PAPER_ONLY', recorded_utc=created, note_sha256=digest, labels=labels, clusters=clusters,
         cluster_effective_trials={c: 1 for c in clusters}, dsr_trial_count_unchanged=434,
         retirement_usol_v1_sha256=L.sha(ROOT/'registry/retirement-usol-v1.json'), implementation_sha256=impl,
         source_review='reviews/risk-review-2026-11-12.md')
with (ROOT/'registry/labels-v1.json').open('x') as f: json.dump(m, f, indent=2)
with (ROOT/'registry/labels-v1.json.sha256').open('x') as f: f.write(L.sha(ROOT/'registry/labels-v1.json')+'  labels-v1.json\n')
print('Registered labels-v1', digest, 'TREND', len(trend))
