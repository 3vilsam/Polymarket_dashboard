import copy
import hashlib
import json
import math
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import league as L
import league_v2 as V
import strategies_v2 as S
import evaluation_v2 as E
from test_league import rows, fixture, position, NOW

def state(now=NOW):
    old=L.registration(); st=L.new_state(old,now)
    st['registration_sha256']=L.sha(L.ROOT/'registry/manifest.json')
    ext=dict(original_manifest_sha256=st['registration_sha256'],strategies=[dict(x,sha256='synthetic') for x in S.entries()])
    V.extend(st,old,ext,now,'synthetic-extension')
    return st,old,ext

def data(st,now=NOW):
    d=fixture(st,now)
    for step,key in V.KEYS.items():
        if key not in d: d[key]={c:rows(step,250,now//step*step) for c in S.COINS}
    return d

class Extension(unittest.TestCase):
    def test_full_extension_preregistered(self):
        old,ext=V.registration()
        self.assertEqual(len(old['strategies'])+len(ext['strategies']),100)
        self.assertEqual(ext['total_known_trials'],409)
        for spec in ext['strategies']:
            self.assertEqual(L.sha(L.ROOT/'registry'/f"{spec['id']}.md"),spec['sha256'])
    def test_extension_implementation_tamper_fails_closed(self):
        import shutil
        with tempfile.TemporaryDirectory() as t:
            root=Path(t); shutil.copytree(L.ROOT/'registry',root/'registry')
            for name in ('league_v2.py','strategies_v2.py','evaluation_v2.py','register_v2.py'):
                shutil.copyfile(L.ROOT/name,root/name)
            (root/'league_v2.py').write_text('tampered')
            with patch.object(L,'registration',return_value=L.registration()):
                with self.assertRaisesRegex(ValueError,'frozen extension implementation'):
                    V.registration(root)
    def test_extension_rule_tamper_fails_closed(self):
        import shutil
        with tempfile.TemporaryDirectory() as t:
            root=Path(t); shutil.copytree(L.ROOT/'registry',root/'registry')
            for name in ('league_v2.py','strategies_v2.py','evaluation_v2.py','register_v2.py'):
                shutil.copyfile(L.ROOT/name,root/name)
            (root/'registry'/'f1-vwap5m-v1.md').write_text('tampered')
            with patch.object(L,'registration',return_value=L.registration()):
                with self.assertRaisesRegex(ValueError,'frozen extension rules'):
                    V.registration(root)
    def test_total100_unique_base15(self):
        st,_,_=state(); self.assertEqual(len(st['books']),100)
        self.assertEqual(len(S.BASE)+5,15)
        self.assertEqual(len({s['id'] for s in S.entries()}),95)
    def test_all_independent100(self):
        st,_,_=state(); self.assertTrue(all(b['cash']==100 for b in st['books'].values()))
        st['books'][S.BASE[0][0]]['cash']=4
        self.assertEqual(st['books'][S.BASE[1][0]]['cash'],100)
    def test_original_bytes_untouched(self):
        hashes=L.read_json(L.ROOT/'backups/extension-v2/original-registry-hashes.json')
        for p,d in hashes.items(): self.assertEqual(L.sha(L.ROOT/p),d)
        self.assertEqual(L.sha(L.ROOT/'league.py'),L.sha(L.ROOT/'backups/extension-v2/league.py'))
        self.assertEqual(L.sha(L.ROOT/'strategies.py'),L.sha(L.ROOT/'backups/extension-v2/strategies.py'))
    def test_migration_no_old_reset(self):
        old=L.registration(); st=L.new_state(old,NOW); before=copy.deepcopy(st['books'])
        st['registration_sha256']=L.sha(L.ROOT/'registry/manifest.json')
        ext=dict(original_manifest_sha256=st['registration_sha256'],strategies=[dict(x,sha256='synthetic') for x in S.entries()])
        V.extend(st,old,ext,NOW,'ext')
        self.assertEqual({i:st['books'][i] for i in before},before)
    def test_migration_idempotent(self):
        st,old,ext=state(); st['books'][S.BASE[0][0]]['cash']=97
        V.extend(st,old,ext,NOW,'synthetic-extension')
        self.assertEqual(st['books'][S.BASE[0][0]]['cash'],97)
    def test_digest_change_blocks(self):
        st,old,ext=state()
        with self.assertRaisesRegex(ValueError,'registry mismatch'): V.extend(st,old,ext,NOW,'evil')
    def test_spec_change_blocks(self):
        st,old,ext=state(); st['books'][S.BASE[0][0]]['spec']['hold_ms']=1
        with self.assertRaisesRegex(ValueError,'spec changed'): V.extend(st,old,copy.deepcopy(dict(ext,strategies=[dict(x,sha256='synthetic') for x in S.entries()])),NOW,'synthetic-extension')
    def test_grid_asset_restrictions_and_variety(self):
        es=S.entries(); self.assertEqual(sum(len(s['coins'])==1 for s in es),81)
        for s in es: self.assertTrue(set(s['coins'])<=set(S.COINS))
        self.assertEqual({s['interval'] for s in es},{S.MINUTE,5*S.MINUTE,15*S.MINUTE,S.HOUR,4*S.HOUR,S.DAY})
    def test_new_signals_causal_all_families(self):
        for spec in S.entries()[:10]:
            step=spec['interval']; boundary=NOW//step*step; r=rows(step,250,boundary)
            f=[dict(time=t+50,fundingRate='.0000125') for t in range(boundary-48*S.HOUR,boundary,S.HOUR)]
            a=S.signal(spec,r,f,boundary,'BTC')
            noisy=r+[dict(t=boundary,o=1e6,h=2e6,l=1,c=1e6,v=10)]
            self.assertEqual(a,S.signal(spec,noisy,f,boundary,'BTC'),spec['kind'])
    def test_random_seed_repeatable_no_price_dependence(self):
        spec=S.entries()[9]; step=spec['interval']; b=NOW//step*step; r=rows(step,250,b)
        a=S.signal(spec,r,[],b,'BTC'); r[-1]['c']=10000
        self.assertEqual(a['side'],S.signal(spec,r,[],b,'BTC')['side'])
        self.assertEqual(a['stop_pct'],.01)
    def test_funding_requires_all_real_hours(self):
        s=S.entries()[7]; b=NOW//S.HOUR*S.HOUR
        with self.assertRaisesRegex(ValueError,'complete real hourly'): S.signal(s,rows(S.HOUR,250,b),[],b,'BTC')
    def test_funding_direction_extremes(self):
        s=S.entries()[7]; b=NOW//S.HOUR*S.HOUR; r=rows(S.HOUR,250,b)
        for i,x in enumerate(r):
            c=200-i*.1; x.update(c=c,o=c,h=c+.1,l=c-.1)
        f=[dict(time=t+50,fundingRate='.0001') for t in range(b-8*S.HOUR,b,S.HOUR)]
        self.assertEqual(S.signal(s,r,f,b,'BTC')['side'],-1)
    def test_every_book_fee_stop_risk_min_leverage(self):
        st,_,_=state(); d=data(st)
        for b in st['books'].values():
            if 'spec' not in b: continue
            self.assertTrue(L.open_paper(b,'BTC',1,.01,100,NOW,d['ctx'],.0000125),b['id'])
            p=next(iter(b['positions'].values()))
            self.assertLessEqual(p['risk_at_entry'],.5)
            self.assertGreaterEqual(p['entry_px']*p['size'],10)
            self.assertAlmostEqual(p['entry_px'],100.02)
            self.assertAlmostEqual(p['fees'],p['size']*p['entry_px']*.00045)
            self.assertLessEqual(L.sc.notional_open(b)/L.sc.equity(b),3)
            self.assertFalse(L.open_paper(b,'ETH',1,.01,100,NOW,d['ctx'],0))
    def test_all_100_one_tick_no_fake_completed(self):
        st,old,_=state(); V.apply_tick(st,data(st),NOW,old)
        self.assertEqual(st['ticks'],1)
        self.assertTrue(all(len(b['closed_trades'])==0 for b in st['books'].values()))
        self.assertTrue(all(b['evaluation']['trial_count']==409 for b in st['books'].values()))
    def test_shared_signal_cache(self):
        st,old,_=state()
        with patch.object(S,'signal',wraps=S.signal) as sig: count=V.apply_tick(st,data(st),NOW,old)
        # <= 9 families x3 params x3 coins +3 control, not95books x3coins
        self.assertEqual(count,sig.call_count); self.assertLessEqual(count,84)
        self.assertLess(count, sum(len(s['coins']) for s in S.entries()))
    def test_all_new_stop_replay10h(self):
        start=NOW-10*S.HOUR; st,old,_=state(start); d=data(st)
        for b in st['books'].values():
            if 'spec' in b: position(b,start-S.MINUTE)
        for c in S.COINS: d['minutes'][c][120]['l']=96
        V.apply_tick(st,d,NOW,old)
        for b in st['books'].values():
            if 'spec' in b:
                stop=[e for e in b['events'] if e['event']=='exit' and e['reason']=='stop']
                self.assertEqual(len(stop),1,b['id']); self.assertTrue(stop[0]['replayed'])
                self.assertEqual(stop[0]['bar_t'],start+120*S.MINUTE)
    def test_gap_blocks_transaction_candidate(self):
        st,old,_=state(NOW-10*S.MINUTE); d=data(st); d['minutes']['ETH'].pop()
        saved=copy.deepcopy(st); candidate=copy.deepcopy(st)
        with self.assertRaisesRegex(ValueError,'UNRESOLVED_REPLAY_GAP'): V.apply_tick(candidate,d,NOW,old)
        self.assertEqual(st,saved)
    def test_fast_time_exit_observed_not_historical(self):
        st,old,_=state(NOW-2*S.HOUR); b=st['books'][S.BASE[0][0]]; position(b,NOW-2*S.HOUR,size=.01)
        d=data(st); d['mids']['BTC']=102
        V.apply_tick(st,d,NOW,old)
        ex=next(e for e in b['events'] if e['event']=='exit')
        self.assertEqual(ex['ts_ms'],NOW); self.assertAlmostEqual(ex['price'],102*.9998)
        self.assertEqual(ex['reason'],'observed_time_exit')
    def test_fast_latency_expiry(self):
        st,old,_=state(); b=st['books'][S.BASE[4][0]]
        d=data(st); now=NOW+50000
        sig=dict(side=1,exit_long=False,exit_short=False,details={},stop_pct=.005)
        with patch.object(S,'signal',return_value=sig): V.apply_tick(st,d,now,old)
        self.assertFalse(b['positions'])
        self.assertTrue(any(e['event']=='missed_entry' for e in b['events']))
    def test_no_private_endpoint(self):
        with tempfile.TemporaryDirectory() as t:
            with self.assertRaisesRegex(ValueError,'non-public'): V.PublicData(Path(t)).request(dict(type='clearinghouseState'))
    def test_history_cached_no_per_book_api(self):
        with tempfile.TemporaryDirectory() as t:
            p=V.PublicData(Path(t)); b=NOW//(5*S.MINUTE)*(5*S.MINUTE); r=rows(5*S.MINUTE,250,b)
            with patch.object(p,'candles',return_value=r) as req:
                a=p.history('m5','BTC','5m',250,NOW)
                for _ in range(100): self.assertEqual(a,p.history('m5','BTC','5m',250,NOW))
                self.assertEqual(req.call_count,1)
    def test_maker_never_assumed(self):
        st,_,_=state(); b=st['books'][S.BASE[0][0]]
        L.open_paper(b,'BTC',1,.01,100,NOW,data(st)['ctx'],0)
        e=next(e for e in b['events'] if e['event']=='entry')
        self.assertEqual(e['fill_source'],'observed_mid_plus_2bps')

class Evaluation(unittest.TestCase):
    def setUp(self):
        self.st,self.old,_=state(); E.initialize(self.st,NOW)
        self.b=self.st['books'][S.BASE[0][0]]; self.e=self.b['evaluation']
    def profitable(self,n=30):
        self.b['cash']=101.; self.b['closed_trades']=[dict(pnl_net=.01) for _ in range(n)]
    def test_dsr_unavailable_small_sample(self):
        self.assertIsNone(E.dsr([.01,.02],409))
        self.assertIsNone(E.dsr([.01]*30,409))
    def test_dsr_multiplicity_penalty(self):
        r=[.003+.01*math.sin(i) for i in range(100)]
        self.assertLess(E.dsr(r,409),E.dsr(r,2))
    def test_under30_never_flagged(self):
        self.profitable(29)
        with patch.object(E,'dsr',return_value=.999): E.update(self.st,NOW)
        self.assertIsNone(self.e['flag_ms'])
    def test_controls_and_dsr_all_required(self):
        self.profitable()
        with patch.object(E,'dsr',return_value=.94): E.update(self.st,NOW)
        self.assertIsNone(self.e['flag_ms'])
        rand=self.st['books'][self.e['random_id']]; rand['cash']=102
        with patch.object(E,'dsr',return_value=.999): E.update(self.st,NOW)
        self.assertIsNone(self.e['flag_ms'])
    def test_flag_not_candidate_and_fresh_day_required(self):
        self.profitable()
        with patch.object(E,'dsr',return_value=.999):
            E.update(self.st,NOW); E.update(self.st,NOW+S.HOUR)
        self.assertIsNotNone(self.e['flag_ms']); self.assertIsNone(self.e['oos'])
        self.assertNotEqual(self.e['status'],'CANDIDATE_REVIEW_ONLY')
    def start_oos(self):
        self.profitable()
        with patch.object(E,'dsr',return_value=.999):
            E.update(self.st,NOW); start=E.next_day(NOW)+S.MINUTE; E.update(self.st,start)
        return start
    def test_oos_requires_flat_book(self):
        self.profitable(); position(self.b,NOW,size=.01); self.b['marks']['BTC']=100
        with patch.object(E,'dsr',return_value=.999):
            E.update(self.st,NOW); E.update(self.st,E.next_day(NOW)+S.MINUTE)
        self.assertIsNone(self.e['oos'])
    def test_7day_oos_candidate_only_review(self):
        start=self.start_oos(); self.b['cash']=103
        with patch.object(E,'dsr',return_value=.999): E.update(self.st,start+7*S.DAY)
        self.assertEqual(self.e['status'],'CANDIDATE_REVIEW_ONLY')
        self.assertTrue(any(e['event']=='candidate_for_risk_review' for e in self.b['events']))
    def test_fast_30_new_trades_oos_alternative(self):
        start=self.start_oos(); self.b['cash']=103; self.b['closed_trades'] += [dict(pnl_net=.01)]*30
        with patch.object(E,'dsr',return_value=.999): E.update(self.st,start+S.HOUR)
        self.assertEqual(self.e['status'],'CANDIDATE_REVIEW_ONLY')
    def test_failed_oos_cannot_extend_until_win(self):
        start=self.start_oos(); self.b['cash']=100
        with patch.object(E,'dsr',return_value=.999):
            E.update(self.st,start+7*S.DAY); self.b['cash']=110; E.update(self.st,start+8*S.DAY)
        self.assertEqual(self.e['oos']['status'],'FAIL'); self.assertEqual(self.e['status'],'OOS_FAILED')
    def test_halt_disqualifies(self):
        self.profitable(); self.b['halted']=True
        with patch.object(E,'dsr',return_value=.999): E.update(self.st,NOW)
        self.assertIsNone(self.e['flag_ms'])
    def test_partial_day_excluded_and_no_missing_day_zero_fill(self):
        E.update(self.st,NOW); E.update(self.st,NOW+S.DAY)
        self.assertEqual(self.e['daily_returns'],[])
        E.update(self.st,NOW+4*S.DAY)
        self.assertEqual(self.e['daily_returns'],[])
    def test_export_columns_controls_and_counts(self):
        V.apply_tick(self.st,data(self.st),NOW,self.old)
        with tempfile.TemporaryDirectory() as t:
            V.export(self.st,Path(t)); text=(Path(t)/'leaderboard.md').read_text()
        for needle in ('Fast / short-term','Slow / long-term','DSR trials','DSR probability','Fresh OOS','vs BTC pp','vs random pp','409'):
            self.assertIn(needle,text)
        self.assertEqual(text.count('NOT SIGNIFICANT (<30)'),100)

if __name__=='__main__': unittest.main(verbosity=2)
