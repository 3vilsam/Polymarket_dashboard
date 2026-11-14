import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import league as L
import league_v5 as V5
import league_v6 as V6
import strategies as S
import strategies_v3 as S3
import evaluation_v3 as E3
import warm_cache as W
from strategies import MINUTE, HOUR
from test_league import NOW
from test_data_isolation import init, drop, T1, Collector
from test_spot_v3 import data as v3_data
from test_warm_cache import fake_info_factory, seed_cache, seed_state, write_root

IDS = ['sp-hold-usol-v1', 'sp-ema15m-usol-v1', 'sp-rsi1h-usol-v1', 'sp-donchian5m-usol-v1']
R = dict(books={b: 'x' for b in IDS}, symbols=['USOL'], note_sha256='synthetic', reason='thin pair')

def with_position(st, bid='sp-hold-usol-v1'):
    b = st['books'][bid]
    b['positions']['SPOT_HOLD'] = dict(id='SPOT_HOLD', coin='USOL', dir=1, side='long', size=.195, size_initial=.195, entry_px=82.9,
        entry_ms=NOW-HOUR, stop=None, fees=.01, realized_gross=0., funding=0., funding_hour=0, market='spot', leverage=1, spot=True)
    b['marks']['USOL'] = 83.0
    return b

class Registration(unittest.TestCase):
    def test_live_retirement_registered_rules_untouched(self):
        *_, r = V6.registration()
        self.assertEqual(r['status'], 'RETIRED_DATA_QUALITY'); self.assertEqual(sorted(r['books']), sorted(IDS))
        self.assertEqual(r['total_known_trials'], 434); self.assertEqual(L.sha(L.ROOT/'registry/retirement-usol-v1.md'), r['note_sha256'])
        spot = L.read_json(L.ROOT/'registry/spot-extension-v3.json')
        for s in spot['strategies']:
            if s['id'] in IDS: self.assertEqual(L.sha(L.ROOT/'registry'/f"{s['id']}.md"), s['sha256'])

class Retire(unittest.TestCase):
    def test_fresh_mark_closes_at_last_valid_price_with_reason(self):
        st, _ = init(); st['last_tick_ms'] = T1; b = with_position(st)
        for bid in IDS: st['books'][bid]['last_tick_myt'] = L.sc.myt(T1)
        out = V6.retire(st, R, T1+60000)
        self.assertEqual(out[0]['status'], 'CLOSED'); self.assertEqual(b['positions'], {})
        ex = [e for e in b['events'] if e['event'] == 'exit'][-1]
        self.assertEqual(ex['reason'], 'retired_data_quality_close_at_last_valid_mark')
        self.assertAlmostEqual(ex['price'], 83.0*(1-2/1e4)); self.assertEqual(ex['last_valid_mark'], 83.0)
        for bid in IDS:
            self.assertTrue(st['books'][bid]['retired']); self.assertEqual(st['books'][bid]['events'][-1]['event'], 'retired')
        self.assertEqual(V6.retire(st, R, T1+120000), [])  # one-time only

    def test_stale_mark_is_unresolved_not_invented(self):
        st, _ = init(); st['last_tick_ms'] = T1; b = with_position(st); b['last_tick_myt'] = L.sc.myt(T1)
        out = V6.retire(st, R, T1+10*60000)
        self.assertEqual(out[0]['status'], 'UNRESOLVED'); self.assertTrue(b['positions']['SPOT_HOLD']['unresolved'])
        self.assertFalse(any(e['event'] == 'exit' for e in b['events']))
        st2, _ = init(); st2['last_tick_ms'] = T1; b2 = with_position(st2); b2['last_tick_myt'] = L.sc.myt(T1); b2['di_cursor'] = NOW
        self.assertEqual(V6.retire(st2, R, T1+60000)[0]['status'], 'UNRESOLVED')

    def test_retired_books_frozen_others_tick_and_trials_stay_434(self):
        st, old = init(); st['last_tick_ms'] = T1-MINUTE; V6.retire(st, R, T1)
        before = {k: copy.deepcopy(st['books'][k]) for k in IDS}
        d = drop(v3_data(st, T1), ['USOL']); d['failed'] = {}  # USOL not collected at all, not a failure
        _, summary = V6.apply_tick(st, d, T1, old, set(IDS), {'USOL'})
        self.assertEqual(summary['skipped_books'], []); self.assertNotIn('USOL', summary['fail_rate_24h'])
        for k in IDS:
            self.assertEqual(st['books'][k]['events'], before[k]['events']); self.assertEqual(st['books'][k]['positions'], before[k]['positions'])
        self.assertEqual(len(st['books']), 125)
        for b in st['books'].values(): self.assertEqual(b['evaluation']['trial_count'], E3.PRIOR_TRIALS+125)
        self.assertEqual(st['books']['g-ema-sol-p0-v1']['last_tick_myt'], L.sc.myt(T1))
        self.assertEqual(st['books']['sp-ema15m-ubtc-v1']['last_tick_myt'], L.sc.myt(T1))
        self.assertEqual(S3.SPOT_COINS, ('UBTC', 'UETH', 'USOL', 'HYPE')); self.assertIn('USOL', S3.SPOT_MARKETS)

    def test_fetch_ignores_usol_even_with_missing_candles(self):
        now = NOW+20*MINUTE+5000
        with tempfile.TemporaryDirectory() as t, patch.object(L.sc, 'info', Collector._info(None, now)), patch.object(L.sc, 'now_ms', lambda: now+1000):
            with V6.without({'USOL'}):
                d = V5.PublicData(Path(t)).fetch(dict(next_minute=now//MINUTE*MINUTE-MINUTE), now)
        self.assertEqual(d['failed'], {}); self.assertNotIn('USOL', d['mids']); self.assertIn('SOL', d['m1'])

class Warm(unittest.TestCase):
    def test_warm_cache_skips_retired_symbol(self):
        now = NOW+45_000; last = W.last_closed_1m(now); info = fake_info_factory(now)
        with tempfile.TemporaryDirectory() as t:
            root = write_root(t, seed_cache(last-20*MINUTE, now=now), seed_state(last-20*MINUTE))
            (root/'registry').mkdir(exist_ok=True); (root/'registry/retirement-usol-v1.json').write_text(json.dumps(dict(symbols=['USOL'])))
            s = W.warm_cache(root=root, now=now, sleep_fn=lambda x: None, info_fn=info, force=True, record_gap=False, isolate=True)
            self.assertEqual(s['retired_symbols_excluded'], ['USOL'])
            self.assertFalse(any(c['type'] == 'candleSnapshot' and c['req']['coin'] == '@156' for c in info.calls))

if __name__ == '__main__': unittest.main()
