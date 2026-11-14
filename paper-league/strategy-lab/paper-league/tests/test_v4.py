import copy
import json
import math
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import league as L
import league_v3 as V3
import league_v4 as V4
import strategies_v4 as S4
import evaluation_v3 as E3
from strategies import HOUR, MINUTE, COINS
from test_league import NOW
from test_spot_v3 import state as v3_state, data as v3_data

def ms(y, mo, d, h):
    return int(datetime(y, mo, d, h, tzinfo=timezone.utc).timestamp()*1000)

def bars(closes, boundary, step=HOUR):
    n = len(closes); start = boundary-n*step
    return [dict(t=start+i*step, o=c, h=c*1.001, l=c*.999, c=c, v=1.) for i, c in enumerate(closes)]

def flat(n=250, px=100.):
    return [px*(1+.0005*math.sin(i)) for i in range(n)]

def funding(boundary, rates):
    hrs = len(rates)
    return [dict(time=boundary-(hrs-i)*HOUR+50, fundingRate=str(r)) for i, r in enumerate(rates)]

def v4_state(now=NOW):
    st, old, ext, spot = v3_state(now)
    v4 = dict(strategies=[dict(x, sha256='synthetic') for x in S4.entries()])
    V4.extend(st, old, ext, spot, v4, now, 'synthetic-extension', 'synthetic-spot', 'synthetic-v4')
    return st, old, ext, spot, v4

class Registry(unittest.TestCase):
    def test_nine_unique_books_sources_and_lanes(self):
        e = S4.entries(); self.assertEqual(len(e), 9); self.assertEqual(len({s['id'] for s in e}), 9)
        for s in e:
            self.assertTrue(s['sources']); self.assertEqual(s['interval'], HOUR)
            if s['market'] == 'spot':
                self.assertTrue(s['long_only']); self.assertEqual(s['leverage'], 1); self.assertEqual(s['starting_equity'], 16.24)
            else:
                self.assertTrue(set(s['coins']) <= set(COINS))
    def test_ids_do_not_collide_with_frozen_116(self):
        old, ext, spot = V3.registration()
        prior = {s['id'] for s in old['strategies']+ext['strategies']+spot['strategies']}
        self.assertFalse(prior & {s['id'] for s in S4.entries()})
    def test_live_preregistration_and_trial_count(self):
        old, ext, spot, v4 = V4.registration()
        self.assertEqual(len(old['strategies'])+len(ext['strategies'])+len(spot['strategies'])+len(v4['strategies']), 125)
        self.assertEqual(v4['total_known_trials'], 434)
        self.assertEqual(E3.PRIOR_TRIALS+125, 434)
        for s in v4['strategies']:
            self.assertEqual(L.sha(L.ROOT/'registry'/f"{s['id']}.md"), s['sha256'])

class Signals(unittest.TestCase):
    def test_hour_window_only_at_21_utc(self):
        p = dict(entry_hour_utc=21, stop_atr=2.)
        for h in range(24):
            b = ms(2026, 11, 12, h)
            o = S4.core('hour_window', p, bars(flat(), b), b)
            self.assertEqual(o['side'], 1 if h == 21 else 0)
    def test_weekend_only_friday_20_utc(self):
        p = dict(weekday_utc=4, entry_hour_utc=20, stop_pct=.04)
        fri = ms(2026, 11, 13, 20); thu = ms(2026, 11, 12, 20); fri19 = ms(2026, 11, 13, 19)
        self.assertEqual(S4.core('weekend', p, bars(flat(), fri), fri)['side'], 1)
        self.assertEqual(S4.core('weekend', p, bars(flat(), thu), thu)['side'], 0)
        self.assertEqual(S4.core('weekend', p, bars(flat(), fri19), fri19)['side'], 0)
    def test_shock_reversal_long_only_on_extreme_drop(self):
        p = dict(window=168, z=3., stop_atr=3., stop_floor=.01); b = ms(2026, 11, 12, 5)
        c = flat(); self.assertEqual(S4.core('shock_reversal', p, bars(c, b), b)['side'], 0)
        c2 = c[:-1]+[c[-2]*.985]
        self.assertEqual(S4.core('shock_reversal', p, bars(c2, b), b)['side'], 1)
        c3 = c[:-1]+[c[-2]*1.015]
        self.assertEqual(S4.core('shock_reversal', p, bars(c3, b), b)['side'], 0)
    def test_negative_funding_transition_and_fail_closed(self):
        p = dict(hours=8, stop_atr=3.); b = ms(2026, 11, 12, 5); r = bars(flat(), b)
        self.assertEqual(S4.core('neg_funding', p, r, b, funding(b, [1e-5]*8+[-1e-4]))['side'], 1)
        self.assertEqual(S4.core('neg_funding', p, r, b, funding(b, [-1e-5]*9))['side'], 0)
        self.assertEqual(S4.core('neg_funding', p, r, b, funding(b, [1e-5]*9))['side'], 0)
        with self.assertRaisesRegex(ValueError, 'complete real hourly'):
            S4.core('neg_funding', p, r, b, funding(b, [1e-5]*8))
    def test_tsmom_enters_only_on_fresh_agreement(self):
        p = dict(horizons=[6, 24, 72], exit_h=24, stop_atr=3.); b = ms(2026, 11, 12, 5)
        up = [100*(1.001**i) for i in range(250)]
        self.assertEqual(S4.core('tsmom_mh', p, bars(up, b), b)['side'], 0)  # already agreeing: no startup entry
        c = [100.]*240+[99.9]+[100+0.2*i for i in range(1, 10)]
        o = S4.core('tsmom_mh', p, bars(c[:-1]+[c[-1]], b), b)
        self.assertIn(o['side'], (0, 1))
        down = [100*(0.999**i) for i in range(250)]
        o = S4.core('tsmom_mh', p, bars(down, b), b); self.assertTrue(o['exit_long']); self.assertEqual(o['side'], 0)
    def test_ratio_cross_and_alignment(self):
        p = dict(window=168, z=2., stop_atr=3., numerator='ETH', denominator='BTC'); b = ms(2026, 11, 12, 5)
        btc = bars([50000*(1+.0005*math.cos(i*1.7)) for i in range(250)], b); eth_c = flat(250, 3000.); eth_c[-1] = eth_c[-2]*.97
        eth = bars(eth_c, b)
        o = S4.core('ratio_mr', p, eth, b, others=dict(ETH=eth, BTC=btc), coin='ETH'); self.assertEqual(o['side'], 1)
        eth_c[-1] = eth_c[-2]*1.03; eth = bars(eth_c, b)
        o = S4.core('ratio_mr', p, eth, b, others=dict(ETH=eth, BTC=btc), coin='ETH'); self.assertEqual(o['side'], -1)
        with self.assertRaisesRegex(ValueError, 'aligned'):
            S4.core('ratio_mr', p, eth, b, others=dict(ETH=eth, BTC=btc[:-100:2]+btc[-50:]), coin='ETH')
    def test_xs_momentum_single_candidate_only_at_midnight(self):
        p = dict(lookback=72, rebalance_hour_utc=0, stop_atr=3.); b = ms(2026, 11, 12, 0)
        o = dict(BTC=bars([100*(1.0002**i) for i in range(250)], b), ETH=bars(flat(250, 3000.), b),
                 SOL=bars([100*(0.9995**i) for i in range(250)], b))
        sides = {c: S4.core('xs_momentum', p, o[c], b, others=o, coin=c)['side'] for c in COINS}
        self.assertEqual(sum(abs(v) for v in sides.values()), 1)
        self.assertEqual(sides['SOL'], -1)  # |r72 SOL| > |r72 BTC|
        b1 = b+HOUR; o1 = {k: bars([r['c'] for r in v], b1) for k, v in o.items()}
        for c in COINS:
            s = S4.core('xs_momentum', p, o1[c], b1, others=o1, coin=c)
            self.assertEqual(s['side'], 0); self.assertFalse(s['exit_long'] or s['exit_short'])
    def test_spot_signal_never_short(self):
        b = ms(2026, 11, 12, 5); spec = [s for s in S4.entries() if s['id'] == 'sp4-shockrev1h-ubtc-v1'][0]
        o = S4.spot_signal(spec, dict(spot_h1=dict(UBTC=bars(flat(), b))), b, 'UBTC')
        self.assertIn(o['side'], (0, 1)); self.assertFalse(o['exit_short'])
    def test_stale_or_short_history_fails_closed(self):
        b = ms(2026, 11, 12, 5); p = dict(entry_hour_utc=21, stop_atr=2.)
        with self.assertRaises(ValueError): S4.core('hour_window', p, bars(flat(100), b), b)
        with self.assertRaises(ValueError): S4.core('hour_window', p, bars(flat(), b-HOUR), b)
    def test_wide_stop_abstains(self):
        b = ms(2026, 11, 12, 21); c = [100*(1.05 if i % 2 else .95) for i in range(250)]
        self.assertEqual(S4.core('hour_window', dict(entry_hour_utc=21, stop_atr=2.), bars(c, b), b)['side'], 0)

class Engine(unittest.TestCase):
    def test_extend_adds_nine_and_rejects_premature_books(self):
        st, *_ = v4_state(); self.assertEqual(len(st['books']), 125)
        self.assertEqual(sum('spec4' in b for b in st['books'].values()), 7)
        self.assertEqual(sum('spot4_spec' in b for b in st['books'].values()), 2)
        for b in st['books'].values():
            if 'spot4_spec' in b: self.assertEqual(b['starting_equity'], 16.24); self.assertEqual(b['market'], 'spot')
        st2, old, ext, spot = v3_state()
        v4 = dict(strategies=[dict(x, sha256='synthetic') for x in S4.entries()])
        st2['books']['n1-tsmom-mh1h-v1'] = {}
        with self.assertRaises(ValueError):
            V4.extend(st2, old, ext, spot, v4, NOW, 'synthetic-extension', 'synthetic-spot', 'synthetic-v4')
    def test_v4_tick_leaves_frozen_116_books_identical(self):
        st, old, ext, spot, v4 = v4_state()
        a = copy.deepcopy(st); a['books'] = {k: v for k, v in a['books'].items() if 'spec4' not in v and 'spot4_spec' not in v}
        now = NOW+2*MINUTE+5000
        V3.apply_tick(a, v3_data(a, now), now, old)
        V4.apply_tick(st, v3_data(st, now), now, old)
        for k, b in a['books'].items():
            ref = copy.deepcopy(b); got = copy.deepcopy(st['books'][k])
            for x in (ref, got): x['evaluation'].pop('trial_count', None); x['evaluation'].pop('dsr_probability', None)
            self.assertEqual(json.dumps(ref, sort_keys=True), json.dumps(got, sort_keys=True), k)
        self.assertEqual(st['books']['n1-tsmom-mh1h-v1']['evaluation']['trial_count'], E3.PRIOR_TRIALS+125)
    def test_v4_perp_entry_respects_risk_limits(self):
        st, *_ = v4_state(); b = st['books']['n4-utc21-btc-v1']
        ctx = {c: dict(szDecimals=5, funding=.0000125, maxLeverage=20) for c in COINS}
        self.assertTrue(L.open_paper(b, 'BTC', 1, .01, 100., NOW, ctx, .0000125))
        p = next(iter(b['positions'].values()))
        self.assertLessEqual(p['risk_at_entry'], 100*.005+1e-9)
        self.assertLessEqual(p['size']*p['entry_px'], 300+1e-9); self.assertIsNotNone(p['stop'])
    def test_v4_spot_open_long_only_all_in_1x(self):
        st, *_ = v4_state(); b = st['books']['sp4-utc21-ubtc-v1']
        ctx = dict(UBTC=dict(szDecimals=5)); self.assertTrue(V4.spot_open4(b, 'UBTC', .01, 100., NOW, ctx, None))
        p = next(iter(b['positions'].values()))
        self.assertEqual(p['dir'], 1); self.assertLessEqual(p['size']*p['entry_px'], 16.24)
        self.assertFalse(V4.spot_open4(b, 'UBTC', .01, 100., NOW, ctx, None))
    def test_engine_has_no_write_surface_and_same_collector(self):
        src = (Path(__file__).resolve().parents[1]/'league_v4.py').read_text()
        for bad in ('/exchange', 'private_key', 'sign_l1', 'order(', 'testnet'):
            self.assertNotIn(bad, src.replace('No wallet, key, order, signing, testnet or exchange write', ''))
        self.assertIn('V3.PublicData(root).fetch', src)

if __name__ == '__main__': unittest.main()
