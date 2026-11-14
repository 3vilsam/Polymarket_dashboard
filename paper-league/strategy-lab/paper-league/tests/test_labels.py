import copy
import subprocess
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import league as L
import labels as LB
import league_v7 as V7
from test_league import NOW
from test_data_isolation import init

NONV1 = ['sp4-shockrev1h-ubtc-v1', 'sp4-utc21-ubtc-v1']

class Labels(unittest.TestCase):
    def setUp(self):
        self.m = LB.load()
    def test_registered_append_only_and_frozen_rules_unchanged(self):
        (old, ext, spot, v4, di, r), m = V7.registration()  # verifies every prior rule/manifest sha
        self.assertEqual(m['dsr_trial_count_unchanged'], 434)
        for s in v4['strategies']: self.assertEqual(L.sha(L.ROOT/'registry'/f"{s['id']}.md"), s['sha256'])
        self.assertEqual(m['cluster_effective_trials'], dict(BTC_FRI21=1, SHOCKREV=1, TREND=1))
    def test_cluster_membership(self):
        c = self.m['clusters']
        self.assertEqual(set(c['BTC_FRI21']), {'n3-negfund-btc-v1', 'n4-utc21-btc-v1', 'n5-weekend-btc-v1', 'sp4-utc21-ubtc-v1'})
        self.assertEqual(set(c['SHOCKREV']), {'n2-shockrev1h-v1', 'sp4-shockrev1h-ubtc-v1'})
        for i in ('n1-tsmom-mh1h-v1', 'n7-xsmom72h-v1', 'l1-supertrend1h-v1', 'l2-macd4h-v1', 'f4-ema15m-v1', 's4-ewmac-riskcap-noadd-ablation-v1'):
            self.assertIn(i, c['TREND'])
        for i in ('n2-shockrev1h-v1', 'f1-vwap5m-v1', 'c1-random15m-v1'): self.assertNotIn(i, c['TREND'])
    def test_nonv1_never_candidate_and_n6_relabelled(self):
        st, _ = init()
        for b in NONV1: st['books'][b]['evaluation']['status'] = 'CANDIDATE_REVIEW_ONLY'
        st['books']['n1-tsmom-mh1h-v1']['evaluation']['status'] = 'CANDIDATE_REVIEW_ONLY'
        LB.apply(st, self.m, NOW)
        for b in NONV1:
            e = st['books'][b]['evaluation']
            self.assertEqual(e['status'], LB.STATUS_INELIGIBLE); self.assertEqual(e['gate_status_raw'], 'CANDIDATE_REVIEW_ONLY')
            self.assertFalse(st['books'][b]['labels_v1']['promotion_eligible'])
            self.assertEqual(st['books'][b]['events'][-1]['event'], 'promotion_ineligible')
        self.assertEqual(st['books']['n1-tsmom-mh1h-v1']['evaluation']['status'], 'CANDIDATE_REVIEW_ONLY')
        self.assertEqual(st['books']['n6-ethbtc-z1h-v1']['labels_v1']['label'], 'UNHEDGED_ETH_DIRECTIONAL')
        n = len(st['books'][NONV1[0]]['events']); LB.apply(st, self.m, NOW); self.assertEqual(len(st['books'][NONV1[0]]['events']), n)
    def test_leaderboard_annotation(self):
        text = LB.annotate_leaderboard('| 1 | sp4-utc21-ubtc-v1 | 0 |\n| 2 | n6-ethbtc-z1h-v1 | 0 |\n', self.m)
        self.assertIn('sp4-utc21-ubtc-v1 [NON_V1_RESEARCH, cluster:BTC_FRI21]', text)
        self.assertIn('n6-ethbtc-z1h-v1 [UNHEDGED_ETH_DIRECTIONAL]', text); self.assertIn('ONE effective trial', text)
    def test_status_shows_labels(self):
        out = subprocess.run(['./status.sh'], cwd=L.ROOT, capture_output=True, text=True, timeout=60).stdout
        self.assertIn('NON_V1_RESEARCH — PROMOTION-INELIGIBLE', out); self.assertIn('UNHEDGED_ETH_DIRECTIONAL', out)

if __name__ == '__main__': unittest.main()
