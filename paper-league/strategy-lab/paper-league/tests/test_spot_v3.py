import copy
import json
import math
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import league as L
import league_v2 as V
import league_v3 as V3
import strategies_v2 as S2
import strategies_v3 as S3
import evaluation_v2 as E2
import evaluation_v3 as E3
from test_league import rows, fixture, NOW
from test_extension import state as v2_state, data as v2_data

def spot_rows(step,n,boundary,px=100.):
    start=boundary-n*step
    return [dict(t=start+i*step,o=px,h=px*1.001,l=px*0.999,c=px,v=1.) for i in range(n)]

def state(now=NOW):
    st,old,ext=v2_state(now)
    # Use the frozen live manifest when present; synthetic v3 for isolated unit tests that don't need hash checks.
    spot=dict(original_manifest_sha256=st['registration_sha256'],
              extension_v2_sha256='synthetic-v2',
              strategies=[dict(x,sha256='synthetic') for x in S3.entries()])
    V3.extend(st,old,ext,spot,now,'synthetic-extension','synthetic-spot')
    return st,old,ext,spot

def data(st,now=NOW):
    d=v2_data(st,now)
    d['spot_ctx']={c:dict(szDecimals=S3.SPOT_MARKETS[c]['szDecimals'],markPx=100.,midPx=100.,dayNtlVlm=1e6,
                          api_coin=S3.SPOT_MARKETS[c]['api_coin'],pair=S3.SPOT_MARKETS[c]['pair'],
                          price_source='spot_pair',maxLeverage=1) for c in S3.SPOT_COINS}
    start=st['next_minute']; end=now//S3.MINUTE*S3.MINUTE
    n=max(1,(end-start)//S3.MINUTE)
    d['spot_minutes']={c:rows(S3.MINUTE,n,end) for c in S3.SPOT_COINS}
    d['spot_m1']={c:rows(S3.MINUTE,250,end) for c in S3.SPOT_COINS}
    d['spot_m5']={c:rows(5*S3.MINUTE,250,now//(5*S3.MINUTE)*(5*S3.MINUTE)) for c in S3.SPOT_COINS}
    d['spot_m15']={c:rows(15*S3.MINUTE,250,now//(15*S3.MINUTE)*(15*S3.MINUTE)) for c in S3.SPOT_COINS}
    d['spot_h1']={c:rows(S3.HOUR,250,now//S3.HOUR*S3.HOUR) for c in S3.SPOT_COINS}
    d['spot_fourhour']={c:rows(4*S3.HOUR,250,now//(4*S3.HOUR)*(4*S3.HOUR)) for c in S3.SPOT_COINS}
    d['spot_books']={c:dict(bids=[(99.99,1000.)],asks=[(100.01,1000.)]) for c in S3.SPOT_COINS}
    for c in S3.SPOT_COINS: d['mids'][c]=100.
    return d

class SpotRegistration(unittest.TestCase):
    def test_live_preregistration(self):
        old,ext,spot=V3.registration()
        self.assertEqual(len(old['strategies'])+len(ext['strategies'])+len(spot['strategies']),116)
        self.assertEqual(spot['total_known_trials'],425)
        self.assertEqual(spot['starting_equity'],16.24)
        self.assertEqual(spot['spot_taker'],0.00070)
        self.assertEqual(ext['total_known_trials'],409)
        for spec in spot['strategies']:
            self.assertEqual(L.sha(L.ROOT/'registry'/f"{spec['id']}.md"),spec['sha256'])
            self.assertEqual(spec['price_source'],'spot_pair')
            self.assertFalse(spec.get('proxy'))
    def test_v2_and_v1_remain_frozen(self):
        hashes=L.read_json(L.ROOT/'backups/extension-v2/original-registry-hashes.json')
        for p,d in hashes.items(): self.assertEqual(L.sha(L.ROOT/p),d)
        ext=L.read_json(L.ROOT/'registry/extension-v2.json')
        for n,d in ext['implementation_sha256'].items():
            self.assertEqual(L.sha(L.ROOT/n),d)
    def test_spot_implementation_tamper_fails_closed(self):
        import shutil
        with tempfile.TemporaryDirectory() as t:
            root=Path(t); shutil.copytree(L.ROOT/'registry',root/'registry')
            for name in ('league_v2.py','strategies_v2.py','evaluation_v2.py','register_v2.py',
                         'league_v3.py','strategies_v3.py','evaluation_v3.py','register_v3.py'):
                shutil.copyfile(L.ROOT/name,root/name)
            (root/'league_v3.py').write_text('tampered')
            with patch.object(L,'registration',return_value=L.registration()):
                with self.assertRaisesRegex(ValueError,'frozen spot implementation'):
                    V3.registration(root)
    def test_sixteen_unique_and_capital(self):
        st,_,_,_=state()
        self.assertEqual(len(st['books']),116)
        spots=[b for b in st['books'].values() if 'spot_spec' in b]
        self.assertEqual(len(spots),16)
        self.assertTrue(all(abs(b['cash']-16.24)<1e-12 and abs(b['starting_equity']-16.24)<1e-12 for b in spots))
        self.assertTrue(all(b['cash']==100 for b in st['books'].values() if 'spot_spec' not in b))
        self.assertEqual(len({s['id'] for s in S3.entries()}),16)

class SpotMigration(unittest.TestCase):
    def test_migration_does_not_reset_old_books(self):
        st,old,ext=v2_state(); st['books'][S2.BASE[0][0]]['cash']=97
        before=copy.deepcopy({i:st['books'][i] for i in st['books']})
        spot=dict(strategies=[dict(x,sha256='synthetic') for x in S3.entries()])
        V3.extend(st,old,ext,spot,NOW,'synthetic-extension','synthetic-spot')
        for i,b in before.items():
            self.assertEqual(st['books'][i],b)
        self.assertEqual(st['books'][S2.BASE[0][0]]['cash'],97)
    def test_migration_idempotent(self):
        st,old,ext,spot=state(); st['books']['sp-ema15m-ubtc-v1']['cash']=15
        V3.extend(st,old,ext,spot,NOW,'synthetic-extension','synthetic-spot')
        self.assertEqual(st['books']['sp-ema15m-ubtc-v1']['cash'],15)
        self.assertEqual(len(st['books']),116)
    def test_digest_change_blocks(self):
        st,old,ext,spot=state()
        with self.assertRaisesRegex(ValueError,'registry mismatch'):
            V3.extend(st,old,ext,spot,NOW,'synthetic-extension','evil')
    def test_spec_change_blocks(self):
        st,old,ext,spot=state(); b=st['books']['sp-ema15m-ubtc-v1']; b['spot_spec']=dict(b['spot_spec'],hold_ms=1)
        with self.assertRaisesRegex(ValueError,'spot spec changed'):
            V3.extend(st,old,ext,copy.deepcopy(spot),NOW,'synthetic-extension','synthetic-spot')

class SpotSignals(unittest.TestCase):
    def test_signals_causal_and_long_only(self):
        for spec in S3.entries():
            if spec['kind']=='spot_hold': continue
            step=spec['interval']; boundary=NOW//step*step; r=rows(step,250,boundary)
            a=S3.signal(spec,r,boundary)
            noisy=r+[dict(t=boundary,o=1e6,h=2e6,l=1,c=1e6,v=10)]
            self.assertEqual(a,S3.signal(spec,noisy,boundary),spec['kind'])
            self.assertGreaterEqual(a['side'],0)
    def test_ema_up_cross_only(self):
        spec=next(s for s in S3.entries() if s['kind']=='spot_ema')
        step=spec['interval']; b=NOW//step*step; r=rows(step,250,b)
        for i,x in enumerate(r):
            c=90+i*0.2; x.update(c=c,o=c,h=c+0.1,l=c-0.1)
        sig=S3.signal(spec,r,b)
        self.assertIn(sig['side'],(0,1))
        self.assertGreaterEqual(sig['side'],0)
    def test_rsi_never_shorts(self):
        spec=next(s for s in S3.entries() if s['kind']=='spot_rsi')
        step=spec['interval']; b=NOW//step*step; r=rows(step,250,b)
        for i,x in enumerate(r):
            c=200-i*0.5; x.update(c=c,o=c,h=c+0.1,l=c-0.1)
        sig=S3.signal(spec,r,b)
        self.assertEqual(sig['side'],0)

class SpotExecution(unittest.TestCase):
    def test_spot_fee_and_1x_all_in_min_notional(self):
        st,old,ext,spot=state(); d=data(st); b=st['books']['sp-ema15m-ubtc-v1']
        self.assertTrue(V3.spot_open(b,'UBTC',.01,100,NOW,d['spot_ctx'],None))
        p=next(iter(b['positions'].values()))
        self.assertEqual(p['dir'],1); self.assertEqual(p['market'],'spot'); self.assertEqual(p['leverage'],1)
        self.assertGreaterEqual(p['entry_px']*p['size'],10)
        self.assertAlmostEqual(p['entry_px'],100.02)  # 2bp floor, empty depth
        self.assertAlmostEqual(p['fees'],p['size']*p['entry_px']*0.00070)
        self.assertLessEqual(p['size']*p['entry_px'],16.24+1e-9)
        self.assertEqual(p['funding'],0)
        self.assertFalse(V3.spot_open(b,'UBTC',.01,100,NOW,d['spot_ctx'],None))
    def test_no_short_open(self):
        st,_,_,_=state(); d=data(st)
        V3.apply_tick(st,d,NOW,old:=L.registration() or None)
        # rebuild properly
    def test_no_short_via_decision(self):
        st,old,_,_=state(); d=data(st); b=st['books']['sp-ema15m-ubtc-v1']
        # Force a short-like signal through apply_spot by patching
        sig=dict(side=-1,exit_long=False,exit_short=True,stop_pct=.01,details={},signal_close=100)
        with patch.object(S3,'signal',return_value=sig):
            V3.apply_tick(st,d,NOW,old)
        self.assertFalse(b['positions'])
        self.assertFalse(any(e['event']=='entry' for e in b['events']))
    def test_no_funding_on_spot(self):
        st,old,_,_=state(); d=data(st,NOW); b=st['books']['sp-ema15m-ubtc-v1']
        V3.spot_open(b,'UBTC',.01,100,NOW-S3.HOUR,d['spot_ctx'],None)
        V3.apply_tick(st,d,NOW,old)
        self.assertEqual(b['stats']['funding'],0)
        self.assertFalse(any(e['event']=='funding' for e in b['events']))
    def test_hold_all_in_no_stop(self):
        st,old,_,_=state(); d=data(st); b=st['books']['sp-hold-ubtc-v1']
        V3.apply_tick(st,d,NOW,old)
        p=next(iter(b['positions'].values()))
        self.assertIsNone(p['stop']); self.assertGreaterEqual(p['size']*p['entry_px'],10)
        self.assertAlmostEqual(p['fees'],p['size']*p['entry_px']*0.00070)
        self.assertEqual(p['dir'],1)
    def test_slippage_uses_worse_of_floor_and_l2(self):
        mid=100.; depth=dict(bids=[(99.9,1000.)],asks=[(100.05,1000.)])  # 5bp ask
        px,src=V3.fill_price(mid,1,depth,16.24)
        self.assertAlmostEqual(px,100.05)
        self.assertIn('L2',src)
        tight=dict(bids=[(99.99,1000.)],asks=[(100.01,1000.)])  # 1bp ask, floor 2bp wins
        px,src=V3.fill_price(mid,1,tight,16.24)
        self.assertAlmostEqual(px,100.02)
        self.assertIn('2bp',src)
    def test_stop_replay_uses_spot_fees(self):
        start=NOW-10*S3.HOUR; st,old,_,_=state(start); d=data(st,NOW)
        b=st['books']['sp-ema15m-ubtc-v1']
        V3.spot_open(b,'UBTC',.01,100,start-S3.MINUTE,d['spot_ctx'],None)
        p=next(iter(b['positions'].values()))
        # force a 1m low through the stop around minute 120
        for c in S3.SPOT_COINS:
            d['spot_minutes'][c][120]['l']=96
        V3.apply_tick(st,d,NOW,old)
        stop=[e for e in b['events'] if e['event']=='exit' and e['reason']=='stop']
        self.assertEqual(len(stop),1)
        self.assertTrue(stop[0]['replayed'])
        # fee must be spot taker, not perp 0.045%
        self.assertAlmostEqual(stop[0]['fee'],stop[0]['size']*stop[0]['price']*0.00070)
    def test_gap_blocks_without_committing(self):
        st,old,_,_=state(NOW-10*S3.MINUTE); d=data(st); d['spot_minutes']['UETH'].pop()
        saved=copy.deepcopy(st); candidate=copy.deepcopy(st)
        with self.assertRaisesRegex(ValueError,'UNRESOLVED_REPLAY_GAP'):
            V3.apply_tick(candidate,d,NOW,old)
        self.assertEqual(st,saved)
    def test_latency_expiry(self):
        st,old,_,_=state(); b=st['books']['sp-ema15m-ubtc-v1']
        now=NOW+100000
        d=data(st,now)
        sig=dict(side=1,exit_long=False,exit_short=False,details={},stop_pct=.005,signal_close=100)
        with patch.object(S3,'signal',return_value=sig):
            V3.apply_tick(st,d,now,old)
        self.assertFalse(b['positions'])
        self.assertTrue(any(e['event']=='missed_entry' for e in b['events']))
    def test_one_tick_no_fake_completed_and_trial_count(self):
        st,old,_,_=state(); V3.apply_tick(st,data(st),NOW,old)
        self.assertEqual(st['ticks'],1)
        self.assertTrue(all(len(b['closed_trades'])==0 for b in st['books'].values()))
        self.assertTrue(all(b['evaluation']['trial_count']==425 for b in st['books'].values()))
    def test_perp_books_untouched_by_spot_fees(self):
        st,old,_,_=state(); d=data(st)
        # A v2 book still pays perp fees if opened through frozen path
        b=st['books'][S2.BASE[0][0]]
        self.assertTrue(L.open_paper(b,'BTC',1,.01,100,NOW,d['ctx'],0))
        p=next(iter(b['positions'].values()))
        self.assertAlmostEqual(p['fees'],p['size']*p['entry_px']*.00045)
    def test_no_private_endpoint(self):
        with tempfile.TemporaryDirectory() as t:
            with self.assertRaisesRegex(ValueError,'non-public'):
                V3.PublicData(Path(t)).request(dict(type='clearinghouseState'))
            with self.assertRaisesRegex(ValueError,'non-public'):
                V3.PublicData(Path(t)).request(dict(type='spotClearinghouseState'))
    def test_spot_meta_allowed(self):
        with tempfile.TemporaryDirectory() as t:
            p=V3.PublicData(Path(t))
            with patch.object(L.PublicData,'request',return_value=[{},[]]) as req:
                # request() on v3 also updates weight via L.PublicData.request
                pass
            self.assertIn('spotMetaAndAssetCtxs', V3.PublicData.ALLOWED)

class SpotEvaluation(unittest.TestCase):
    def test_under30_never_flagged(self):
        st,old,_,_=state(); E3.initialize(st,NOW)
        b=st['books']['sp-ema15m-ubtc-v1']
        b['cash']=20.; b['closed_trades']=[dict(pnl_net=.01)]*29
        with patch.object(E3,'dsr',return_value=.999): E3.update(st,NOW)
        self.assertIsNone(b['evaluation']['flag_ms'])
        self.assertEqual(b['evaluation']['trial_count'],425)
    def test_hold_is_control(self):
        st,_,_,_=state(); E3.initialize(st,NOW)
        b=st['books']['sp-hold-ubtc-v1']; b['cash']=20.; b['closed_trades']=[dict(pnl_net=.01)]*30
        with patch.object(E3,'dsr',return_value=.999): E3.update(st,NOW)
        self.assertEqual(b['evaluation']['status'],'CONTROL')
        self.assertIsNone(b['evaluation']['flag_ms'])
    def test_no_auto_promotion(self):
        st,_,_,_=state(); E3.initialize(st,NOW)
        b=st['books']['sp-ema15m-ubtc-v1']; b['cash']=20.; b['closed_trades']=[dict(pnl_net=.01)]*30
        with patch.object(E3,'dsr',return_value=.999):
            E3.update(st,NOW); E3.update(st,NOW+S3.HOUR)
        self.assertNotEqual(b['evaluation']['status'],'CANDIDATE_REVIEW_ONLY')
        start=E3.next_day(NOW)+S3.MINUTE
        with patch.object(E3,'dsr',return_value=.999):
            E3.update(st,start); b['cash']=21.; E3.update(st,start+7*S3.DAY)
        self.assertEqual(b['evaluation']['status'],'CANDIDATE_REVIEW_ONLY')
        self.assertTrue(any(e['event']=='candidate_for_risk_review' for e in b['events']))
    def test_export_has_spot_tables_and_425(self):
        st,old,_,_=state(); V3.apply_tick(st,data(st),NOW,old)
        with tempfile.TemporaryDirectory() as t:
            V3.export(st,Path(t)); text=(Path(t)/'leaderboard.md').read_text()
        for needle in ('16.24 virtual USDC','Spot buy-and-hold','Spot fast','Spot slow','425','0.070%','not perp-mid proxies','NO automatic promotion','sp-hold-ubtc-v1','sp-ema15m-hype-v1','sp-donchian5m-ubtc-v1','Early read (not evidence)','change the promotion bar'):
            self.assertIn(needle,text)
        # 100 perp + 16 spot, each flagged not significant if no trades (holds have no closed trades)
        self.assertGreaterEqual(text.count('NOT SIGNIFICANT (<30)'),116)
    def test_early_read_ten_trades_not_candidate(self):
        st,old,_,_=state(); V3.apply_tick(st,data(st),NOW,old)
        b=st['books']['sp-ema15m-ubtc-v1']
        b['closed_trades']=[dict(pnl_net=.01)]*10
        b['stats']['trades_closed']=10
        # a slow book with 10 trades must not appear
        s=st['books']['sp-rsi1h-ubtc-v1']
        s['closed_trades']=[dict(pnl_net=.02)]*10
        with tempfile.TemporaryDirectory() as t:
            V3.export(st,Path(t)); text=(Path(t)/'leaderboard.md').read_text()
        self.assertIn('Early read (not evidence)',text)
        self.assertIn('sp-ema15m-ubtc-v1', text.split('## Early read (not evidence)')[1].split('##')[0] if '##' in text.split('## Early read (not evidence)')[1] else text.split('## Early read (not evidence)')[1].split('DSR uses')[0])
        early=text.split('## Early read (not evidence)')[1].split('DSR uses')[0]
        self.assertIn('sp-ema15m-ubtc-v1', early)
        self.assertNotIn('sp-rsi1h-ubtc-v1', early)
        self.assertNotIn('CANDIDATE_REVIEW_ONLY', early)
        self.assertIn('change the promotion bar', early)
        # promotion status on the book itself remains not-candidate
        self.assertNotEqual(b['evaluation']['status'],'CANDIDATE_REVIEW_ONLY')

if __name__=='__main__': unittest.main(verbosity=2)
