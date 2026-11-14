import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import league as L
import strategies as S
import numpy as np

NOW = int(__import__('datetime').datetime(2026,11,11,5,30,tzinfo=__import__('datetime').timezone.utc).timestamp()*1000)

def manifest():
    return dict(mode='PAPER_ONLY',strategies=[dict(id=f'{k}-test',kind=k,owner='test',sha256='fake') for k in ('donchian','bb','ewmac','rsi','benchmark')])

def rows(step,n,boundary):
    start=boundary-n*step
    return [dict(t=start+i*step,o=100.,h=100.1,l=99.9,c=100.,v=1.) for i in range(n)]

def fixture(st,now):
    return dict(mids={c:100. for c in S.COINS},ctx={c:dict(szDecimals=5,funding=.0000125,maxLeverage=20) for c in S.COINS},
        books={},minutes={c:rows(S.MINUTE,(now//S.MINUTE*S.MINUTE-st['next_minute'])//S.MINUTE,now//S.MINUTE*S.MINUTE) for c in S.COINS},
        fourhour={c:rows(4*S.HOUR,710,now//(4*S.HOUR)*(4*S.HOUR)) for c in S.COINS},
        daily={c:rows(S.DAY,250,now//S.DAY*S.DAY) for c in S.COINS},
        funding={c:[dict(time=t+50,fundingRate='0.0000125',coin=c,premium='0') for t in range(now//S.HOUR*S.HOUR-72*S.HOUR,now//S.HOUR*S.HOUR+1,S.HOUR)] for c in S.COINS})

def book(st,k='donchian'):
    return st['books'][k+'-test']

def position(b,entry,stop=97.,direction=1,size=.1):
    p=dict(id='P000001',coin='BTC',dir=direction,side='long' if direction>0 else 'short',size=size,size_initial=size,
        entry_px=100.,entry_ms=entry,stop=stop,fees=.0045,realized_gross=0.,funding=0.,funding_hour=entry//S.HOUR,
        risk_at_entry=.4,risk_cap_at_entry=.5)
    b['positions'][p['id']]=p
    b['cash']-=p['fees']
    b['stats']['fees']+=p['fees']
    return p

class Tests(unittest.TestCase):
    def setUp(self):
        self.st=L.new_state(manifest(),NOW)
    def test_five_isolated_starting_books(self):
        self.assertEqual(len(self.st['books']),5)
        self.assertEqual([b['cash'] for b in self.st['books'].values()],[100]*5)
        book(self.st)['cash']=1
        self.assertEqual(book(self.st,'bb')['cash'],100)
    def test_no_fake_trade_on_start(self):
        L.apply_tick(self.st,fixture(self.st,NOW),NOW)
        self.assertEqual(sum(len(b['closed_trades']) for b in self.st['books'].values()),0)
        self.assertEqual(sum(len(b['positions']) for b in self.st['books'].values()),1)
    def test_benchmark_costed_once(self):
        d=fixture(self.st,NOW)
        L.apply_tick(self.st,d,NOW)
        b=book(self.st,'benchmark')
        self.assertGreater(b['stats']['fees'],0)
        self.assertLess(L.sc.equity(b),100)
        fees=b['stats']['fees']
        L.apply_tick(self.st,d,NOW)
        self.assertEqual(b['stats']['fees'],fees)
    def test_risk_size_includes_costs_reserve(self):
        b=book(self.st)
        ok=L.open_paper(b,'BTC',1,.03,100.,NOW,fixture(self.st,NOW)['ctx'],.0000125)
        self.assertTrue(ok)
        p=next(iter(b['positions'].values()))
        self.assertLessEqual(p['risk_at_entry'],.5)
        self.assertLess(p['size'],.5/3)
        self.assertGreaterEqual(p['size']*p['entry_px'],10)
    def test_cluster_stricter_than_two_positions(self):
        b=book(self.st)
        d=fixture(self.st,NOW)
        self.assertTrue(L.open_paper(b,'BTC',1,.03,100,NOW,d['ctx'],.0000125))
        self.assertFalse(L.open_paper(b,'ETH',1,.03,100,NOW,d['ctx'],.0000125))
    def test_reject_outside_universe(self):
        self.assertFalse(L.open_paper(book(self.st),'DOGE',1,.03,100,NOW,{},0))
    def test_missing_or_wide_stop_rejected(self):
        b=book(self.st)
        for stop in (0.,.004,.05):
            self.assertFalse(L.open_paper(b,'BTC',1,stop,100,NOW,{},0))
    def test_minimum_never_rounded_up(self):
        b=book(self.st)
        b['cash']=10
        d=fixture(self.st,NOW)
        self.assertFalse(L.open_paper(b,'BTC',1,.03,100,NOW,d['ctx'],0))
    def test_halted_no_entry(self):
        b=book(self.st);b['halted']=True
        self.assertFalse(L.open_paper(b,'BTC',1,.03,100,NOW,{},0))
    def test_l2_sizing_reused(self):
        b=book(self.st);d=fixture(self.st,NOW)
        depth=dict(bids=[(99.99,100.)],asks=[(100.01,100.)])
        with patch.object(L,'size_order',wraps=L.size_order) as reused:
            self.assertTrue(L.open_paper(b,'BTC',1,.03,100,NOW,d['ctx'],.0000125,depth))
            self.assertEqual(reused.call_count,1)
        self.assertAlmostEqual(next(iter(b['positions'].values()))['entry_px'],100.01)
    def test_long_stop_touch(self):
        b=book(self.st);p=position(b,NOW-S.HOUR)
        bar=dict(t=NOW,o=99,h=100,l=96,c=98)
        self.assertTrue(L.resolve_stop(b,p,bar,NOW+S.MINUTE))
        exit=next(e for e in b['events'] if e['event']=='exit')
        self.assertAlmostEqual(exit['price'],97*(1-.0005))
        self.assertFalse(exit['gap_through_stop'])
    def test_long_gap_open(self):
        b=book(self.st);p=position(b,NOW-S.HOUR)
        self.assertTrue(L.resolve_stop(b,p,dict(t=NOW,o=94,h=95,l=93,c=94),NOW+S.HOUR))
        exit=next(e for e in b['events'] if e['event']=='exit')
        self.assertAlmostEqual(exit['price'],94*(1-.0005))
        self.assertTrue(exit['gap_through_stop'])
    def test_short_stop_gap(self):
        b=book(self.st);p=position(b,NOW-S.HOUR,103,-1)
        L.resolve_stop(b,p,dict(t=NOW,o=106,h=107,l=105,c=106),NOW+S.HOUR)
        exit=next(e for e in b['events'] if e['event']=='exit')
        self.assertAlmostEqual(exit['price'],106*(1+.0005))
    def test_entry_minute_ambiguity_conservative(self):
        b=book(self.st);p=position(b,NOW+30000)
        L.resolve_stop(b,p,dict(t=NOW,o=94,h=101,l=93,c=100),NOW+S.MINUTE)
        exit=next(e for e in b['events'] if e['event']=='exit')
        self.assertTrue(exit['entry_minute_ambiguous'])
        self.assertFalse(exit['gap_through_stop'])
        self.assertAlmostEqual(exit['price'],97*(1-.0005))
    def test_no_pre_entry_bar(self):
        b=book(self.st);p=position(b,NOW)
        self.assertFalse(L.resolve_stop(b,p,dict(t=NOW-S.MINUTE,o=94,h=101,l=93,c=100),NOW+S.MINUTE))
    def test_overnight_replay_stop_at_first_crossing(self):
        start=NOW-10*S.HOUR
        self.st=L.new_state(manifest(),start)
        b=book(self.st);position(b,start-S.MINUTE)
        d=fixture(self.st,NOW)
        d['minutes']['BTC'][120]['l']=96
        L.apply_tick(self.st,d,NOW)
        exits=[e for e in b['events'] if e['event']=='exit']
        self.assertEqual(len(exits),1)
        self.assertEqual(exits[0]['bar_t'],start+120*S.MINUTE)
        self.assertTrue(exits[0]['replayed'])
        self.assertEqual(self.st['next_minute'],NOW)
    def test_stop_closes_once_repeat_tick(self):
        b=book(self.st);p=position(b,NOW-S.HOUR)
        L.resolve_stop(b,p,dict(t=NOW,o=94,h=101,l=93,c=100),NOW+S.MINUTE)
        L.apply_tick(self.st,fixture(self.st,NOW),NOW)
        self.assertEqual(len(b['closed_trades']),1)
        self.assertEqual(sum(e['event']=='net_pnl' for e in b['events']),1)
    def test_replay_gap_blocks_before_mutation(self):
        self.st['next_minute']=NOW-2*S.MINUTE
        d=fixture(self.st,NOW);d['minutes']['ETH'].pop()
        old=copy.deepcopy(self.st)
        with self.assertRaisesRegex(ValueError,'UNRESOLVED_REPLAY_GAP'):
            L.apply_tick(self.st,d,NOW)
        self.assertEqual(self.st,old)
    def test_missing_funding_never_zero(self):
        b=book(self.st);p=position(b,NOW-S.HOUR)
        t=NOW//S.HOUR*S.HOUR
        with self.assertRaisesRegex(ValueError,'missing/duplicate funding'):
            L.funding_at(b,dict(BTC=[]),dict(BTC=dict(o=100)),t)
    def test_funding_actual_rate_price_proxy_once(self):
        b=book(self.st);p=position(b,NOW-S.HOUR)
        t=NOW//S.HOUR*S.HOUR
        f=dict(BTC=[dict(time=t+90,fundingRate='.001')]);bars=dict(BTC=dict(o=120))
        L.funding_at(b,f,bars,t);L.funding_at(b,f,bars,t)
        self.assertAlmostEqual(p['funding'],-.012)
        ev=[e for e in b['events'] if e['event']=='funding']
        self.assertEqual(len(ev),1)
        self.assertIn('proxy',ev[0]['price_source'])
    def test_short_positive_funding_receives(self):
        b=book(self.st);p=position(b,NOW-S.HOUR,103,-1)
        t=NOW//S.HOUR*S.HOUR
        L.funding_at(b,dict(BTC=[dict(time=t+90,fundingRate='.001')]),dict(BTC=dict(o=120)),t)
        self.assertAlmostEqual(p['funding'],.012)
    def test_no_funding_after_stop_close(self):
        b=book(self.st);p=position(b,NOW-S.HOUR)
        L.close(b,p,97,NOW,'stop')
        L.funding_at(b,{}, {},NOW//S.HOUR*S.HOUR)
        self.assertEqual(b['stats']['funding'],0)
    def test_risk_consumed_by_funding_closes(self):
        b=book(self.st);p=position(b,NOW-S.HOUR)
        b['marks']['BTC']=100
        p['funding']=-.3
        L.enforce_cost_risk(b,NOW)
        self.assertFalse(b['positions'])
        self.assertEqual(b['closed_trades'][0]['reason'],'funding_or_risk_budget_exhausted')
    def test_halt_sticky_across_midnight(self):
        b=book(self.st);b['cash']=97
        L.halt(b,NOW)
        self.assertTrue(b['halted'])
        L.mark(b,{},NOW+S.DAY)
        self.assertTrue(b['halted'])
    def test_no_hindsight_entry(self):
        b=book(self.st);d=fixture(self.st,NOW)
        sig=dict(side=1,exit_long=False,exit_short=False,details={},stop_pct=.03)
        L.decision(b,'BTC',sig,d,NOW,NOW-30*S.MINUTE,False)
        self.assertFalse(b['positions'])
        self.assertEqual(b['events'][-1]['event'],'missed_entry')
    def test_metrics_costed_round_trip(self):
        b=book(self.st);p=position(b,NOW-S.HOUR)
        L.close(b,p,110,NOW,'test')
        b['marks']['BTC']=110
        m=L.metrics(b)
        self.assertEqual(m['trades'],1)
        self.assertEqual(m['win_rate'],100)
        self.assertAlmostEqual(m['realized'],1-.0045-.00495)
        self.assertEqual(m['profit_factor'],'inf')
    def test_no_trades_metrics_not_invented(self):
        m=L.metrics(book(self.st))
        for k in ('profit_factor','win_rate','expectancy'):
            self.assertIsNone(m[k])
    def test_drawdown_equity_percent(self):
        b=book(self.st);b['cash']=110;L.mark(b,{},NOW)
        b['cash']=99;L.mark(b,{},NOW)
        self.assertAlmostEqual(b['max_drawdown_pct'],10)
    def test_atomic_json_valid(self):
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp)/'a.json'
            L.atomic(p,dict(a=1));L.atomic(p,dict(a=2))
            self.assertEqual(L.read_json(p),dict(a=2))
            self.assertFalse(p.with_suffix('.json.tmp').exists())
    def test_public_request_guard(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError,'non-public'):
                L.PublicData(Path(temp)).request(dict(type='order'))
    def test_registration_hash_tamper(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);(root/'registry').mkdir()
            m=manifest();m['implementation_sha256']={}
            for s in m['strategies']:
                path=root/'registry'/f"{s['id']}.md";path.write_text('frozen')
                s['sha256']=L.sha(path)
            L.atomic(root/'registry/manifest.json',m)
            self.assertEqual(len(L.registration(root)['strategies']),5)
            path.write_text('tampered')
            with self.assertRaisesRegex(ValueError,'frozen rules changed'):
                L.registration(root)
    def test_frozen_implementation_tamper(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);(root/'registry').mkdir()
            m=manifest();(root/'code.py').write_text('old')
            m['implementation_sha256']={'code.py':L.sha(root/'code.py')}
            L.atomic(root/'registry/manifest.json',m)
            (root/'code.py').write_text('new')
            with self.assertRaisesRegex(ValueError,'frozen implementation changed'):
                L.registration(root)
    def test_original_pass_gate_unchanged(self):
        cfg=L.sc.load_config()
        self.assertEqual(cfg['strategies'],[])
        self.assertFalse(L.sc.strategy_gate(cfg,'donchian')[0])
    def test_signals_only_closed_bars(self):
        d=fixture(self.st,NOW)
        rows=d['fourhour']['BTC']
        boundary=NOW//(4*S.HOUR)*(4*S.HOUR)
        for k in ('donchian','bb','rsi'):
            a=S.signal(k,rows,d['funding']['BTC'],boundary)
            noisy=rows+[dict(t=boundary,o=1e6,h=1e6,l=1,c=1e6,v=1)]
            self.assertEqual(a,S.signal(k,noisy,d['funding']['BTC'],boundary))
    def test_donchian_vs_original_final_rule(self):
        spec=importlib.util.spec_from_file_location('backtest',L.ROOT.parent/'backtests/2026-11-09_hl-3strat/backtest.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        d=fixture(self.st,NOW);rows=d['fourhour']['BTC']
        rng=np.random.default_rng(1)
        prices=100*np.exp(np.cumsum(rng.normal(0,.003,len(rows))))
        for r,c in zip(rows,prices):r.update(o=c,h=c*1.001,l=c*.999,c=c)
        df=S.indicators(rows);df['f24']=.0000125
        ent,xl,xs,_=module.sig_donchian(df,40)
        ent=module.apply_filters(df,ent,{'trend','vol','fund'})
        sig=S.signal('donchian',rows,d['funding']['BTC'],NOW//(4*S.HOUR)*(4*S.HOUR))
        self.assertEqual(sig['side'],int(ent[-1]))
        self.assertEqual(sig['exit_long'],bool(xl[-1]))
    def test_bollinger_vs_original_ema_only_rule(self):
        spec=importlib.util.spec_from_file_location('backtest',L.ROOT.parent/'backtests/2026-11-09_hl-3strat/backtest.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        d=fixture(self.st,NOW);rows=d['fourhour']['BTC']
        for i,r in enumerate(rows):
            c=100+i*.01+np.sin(i*.2)
            r.update(c=c,h=c+.1,l=c-.1,o=c)
        df=S.indicators(rows);df['f24']=.0000125
        ent,xl,xs,_=module.sig_bbz(df,40)
        ent=module.apply_filters(df,ent,{'trend'})
        sig=S.signal('bb',rows,d['funding']['BTC'],NOW//(4*S.HOUR)*(4*S.HOUR))
        self.assertEqual(sig['side'],int(ent[-1]))
        self.assertEqual(sig['exit_long'],bool(xl[-1]))
    def test_ewmac_stop_lockout(self):
        b=book(self.st,'ewmac');b['stopped_sides']['BTC']=1
        sig=dict(side=1,exit_long=False,exit_short=False,details={},stop_pct=.045,vol_scale=1,forecast=10,signal_close=100)
        L.decision(b,'BTC',sig,fixture(self.st,NOW),NOW,NOW,True)
        self.assertFalse(b['positions'])
        self.assertEqual(b['events'][-1]['reason'],'EWMAC_stopped_until_sign_change')
    def test_ewmac_forecast_known_uptrend(self):
        d=fixture(self.st,NOW);r=d['daily']['BTC']
        for i,row in enumerate(r):
            c=100+i*.2+np.sin(i*.1)
            row.update(c=c,o=c,h=c+.1,l=c-.1)
        sig=S.signal('ewmac',r,[],NOW//S.DAY*S.DAY)
        self.assertEqual(sig['side'],1)
        self.assertGreater(sig['forecast'],0)
        self.assertLessEqual(sig['forecast'],20)
        self.assertEqual(sig['stop_pct'],.045)
    def test_exports_include_significance_funding_caveat(self):
        L.apply_tick(self.st,fixture(self.st,NOW),NOW)
        with tempfile.TemporaryDirectory() as temp:
            L.export(self.st,Path(temp))
            text=(Path(temp)/'leaderboard.md').read_text()
            self.assertEqual(text.count('NOT SIGNIFICANT'),5)
            self.assertIn('proxy',text)
            self.assertEqual(len(list((Path(temp)/'books').glob('*/ledger.jsonl'))),5)
    def test_replay_funding_all_missed_hours_not_capped_at_three(self):
        start=NOW-10*S.HOUR
        self.st=L.new_state(manifest(),start)
        b=book(self.st);position(b,start-S.MINUTE,97,1,.01)
        L.apply_tick(self.st,fixture(self.st,NOW),NOW)
        self.assertEqual(sum(e['event']=='funding' for e in b['events']),10)

    def test_rsi_time_exit_not_delayed_until_next_fourhour_signal(self):
        b=book(self.st,'rsi');position(b,NOW-48*S.HOUR)
        L.apply_tick(self.st,fixture(self.st,NOW),NOW)
        self.assertFalse(b['positions'])
        self.assertEqual(b['closed_trades'][0]['reason'],'time_exit_48h')
    def test_funding_paginates_500_rows(self):
        with tempfile.TemporaryDirectory() as temp:
            client=L.PublicData(Path(temp))
            first=[dict(time=i*S.HOUR+50,fundingRate='.0001',coin='BTC') for i in range(500)]
            last=[dict(time=500*S.HOUR+50,fundingRate='.0002',coin='BTC')]
            with patch.object(client,'request',side_effect=[first,last]) as req:
                out=client.funding('BTC',0,501*S.HOUR)
            self.assertEqual(len(out),501)
            self.assertEqual(req.call_args_list[1].args[0]['startTime'],first[-1]['time']+1)
    def test_funding_conflict_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            client=L.PublicData(Path(temp))
            client.cache['funding']['BTC']=[dict(time=50,fundingRate='.0001')]
            with patch.object(client,'request',return_value=[dict(time=50,fundingRate='.0002')]):
                with self.assertRaisesRegex(ValueError,'conflicting funding'):
                    client.funding('BTC',0,2*S.HOUR)
    def test_missing_signal_candle_continuity_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            client=L.PublicData(Path(temp))
            bars=rows(4*S.HOUR,711,NOW//(4*S.HOUR)*(4*S.HOUR));bars.pop(100)
            with patch.object(client,'candles',return_value=bars):
                with self.assertRaisesRegex(ValueError,'continuity missing'):
                    client.history('fourhour','BTC','4h',710,NOW)
    def test_stop_loss_trade_statistics_include_funding(self):
        b=book(self.st);p=position(b,NOW-S.HOUR)
        p['funding']=-.01;b['cash']-=.01
        L.close(b,p,97,NOW,'stop')
        self.assertAlmostEqual(b['closed_trades'][0]['pnl_net'],-.3-.0045-.004365-.01)
        self.assertAlmostEqual(L.metrics(b)['net_pnl'],b['closed_trades'][0]['pnl_net'])
    def test_manifest_mode_not_accepted_as_live(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);(root/'registry').mkdir()
            m=manifest();m['mode']='LIVE'
            L.atomic(root/'registry/manifest.json',m)
            with self.assertRaisesRegex(ValueError,'PAPER_ONLY'):
                L.registration(root)

if __name__=='__main__':
    unittest.main(verbosity=2)
