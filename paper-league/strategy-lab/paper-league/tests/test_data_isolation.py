import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import league as L
import league_v4 as V4
import league_v5 as V5
import strategies as S
import strategies_v2 as S2
import strategies_v3 as S3
import evaluation_v3 as E3
import warm_cache as W
from strategies import MINUTE, HOUR
from test_league import NOW
from test_v4 import v4_state
from test_spot_v3 import data as v3_data
from test_warm_cache import fake_info_factory, seed_cache, seed_state, write_root

T1 = NOW+2*MINUTE+5000

def drop(data, syms):
    d = copy.deepcopy(data)
    for k, v in d.items():
        if isinstance(v, dict) and k not in ('mids',):
            for s in syms: v.pop(s, None)
    d['failed'] = {s: 'synthetic failure' for s in syms}
    return d

def init():
    st, old, *_ = v4_state(); E3.initialize(st, NOW); return st, old

def norm(b, ignore=()):
    b = copy.deepcopy(b); b['marks'] = {k: v for k, v in b.get('marks', {}).items() if k not in ignore}
    for x in ('trial_count', 'dsr_probability'): b['evaluation'].pop(x, None)
    return json.dumps(b, sort_keys=True)

class Registration(unittest.TestCase):
    def test_rule_registered_with_sha_and_books_untouched(self):
        old, ext, spot, v4, di = V5.registration()
        self.assertEqual(L.sha(L.ROOT/'registry/data-isolation-v1.md'), di['rule_sha256'])
        self.assertFalse(di['retroactive']); self.assertEqual(di['total_known_trials'], 434)
        self.assertEqual(len(old['strategies'])+len(ext['strategies'])+len(spot['strategies'])+len(v4['strategies']), 125)

class Isolation(unittest.TestCase):
    def test_all_healthy_matches_frozen_v4_tick(self):
        a, old = init(); b = copy.deepcopy(a)
        V4.apply_tick(a, v3_data(a, T1), T1, old)
        _, summary = V5.apply_tick(b, dict(v3_data(b, T1), failed={}), T1, old)
        self.assertEqual(summary['skipped_books'], [])
        for k in a['books']: self.assertEqual(norm(a['books'][k]), norm(b['books'][k]), k)
        self.assertEqual(a['next_minute'], b['next_minute']); self.assertEqual(a['ticks'], b['ticks'])

    def test_usol_failure_skips_only_usol_books_others_identical(self):
        a, old = init(); b = copy.deepcopy(a)
        V4.apply_tick(a, v3_data(a, T1), T1, old)
        before = copy.deepcopy(b['books'])
        _, summary = V5.apply_tick(b, drop(v3_data(b, T1), ['USOL']), T1, old)
        usol = {k for k, x in b['books'].items() if 'spot_spec' in x and x['spot_spec']['coins'] == ['USOL']}
        self.assertEqual(len(usol), 4); self.assertEqual(set(summary['skipped_books']), usol)
        for k in usol:
            got = copy.deepcopy(b['books'][k]); cur = got.pop('di_cursor')
            self.assertEqual(cur, before[k].get('di_cursor', NOW//MINUTE*MINUTE))
            self.assertEqual(got['events'], before[k]['events']); self.assertEqual(got['positions'], before[k]['positions'])
        for k in set(b['books'])-usol: self.assertEqual(norm(a['books'][k], ('USOL',)), norm(b['books'][k], ('USOL',)), k)
        self.assertEqual((L.COINS, S.COINS, S2.COINS, S3.SPOT_COINS), (('BTC', 'ETH', 'SOL'),)*3+(('UBTC', 'UETH', 'USOL', 'HYPE'),))

    def test_skipped_open_position_gets_no_stop_move_and_is_stale(self):
        st, old = init(); bk = st['books']['sp-ema15m-usol-v1']
        bk['positions']['P1'] = dict(id='P1', coin='USOL', dir=1, side='long', size=.1, size_initial=.1, entry_px=200., entry_ms=NOW-HOUR,
                                     stop=150., fees=0., realized_gross=0., funding=0., funding_hour=0, market='spot', leverage=1, spot=True)
        snap = copy.deepcopy(bk['positions'])
        _, summary = V5.apply_tick(st, drop(v3_data(st, T1), ['USOL']), T1, old)
        self.assertEqual(st['books']['sp-ema15m-usol-v1']['positions'], snap)
        self.assertTrue(any(p['book'] == 'sp-ema15m-usol-v1' and p['coin'] == 'USOL' for p in summary['stale_positions']))

    def test_btc_failure_skips_every_book_that_needs_btc(self):
        st, old = init()
        _, summary = V5.apply_tick(st, drop(v3_data(st, T1), ['BTC']), T1, old)
        sk = set(summary['skipped_books'])
        for k in ('b0-btc-1x-hold-control-v1', 'n6-ethbtc-z1h-v1', 'n7-xsmom72h-v1', 'n4-utc21-btc-v1', 'g-ema-btc-p0-v1', 'f1-vwap5m-v1'):
            self.assertIn(k, sk)
        for k in ('g-ema-eth-p0-v1', 'sp-ema15m-ubtc-v1', 'g-vwap-sol-p1-v1'): self.assertNotIn(k, sk)

    def test_recovery_replays_real_candles_from_own_cursor(self):
        st, old = init()
        V5.apply_tick(st, drop(v3_data(st, T1), ['USOL']), T1, old)
        self.assertIn('di_cursor', st['books']['sp-hold-usol-v1'])
        T2 = T1+MINUTE; _, summary = V5.apply_tick(st, dict(v3_data(st, T2), failed={}), T2, old)
        self.assertEqual(summary['skipped_books'], [])
        self.assertNotIn('di_cursor', st['books']['sp-hold-usol-v1'])
        self.assertEqual(st['books']['sp-hold-usol-v1']['last_tick_myt'], L.sc.myt(T2))

    def test_cursor_older_than_window_stays_skipped(self):
        st, old = init()
        V5.apply_tick(st, drop(v3_data(st, T1), ['USOL']), T1, old)
        st['books']['sp-hold-usol-v1']['di_cursor'] = NOW-2000*MINUTE
        T2 = T1+MINUTE; _, summary = V5.apply_tick(st, dict(v3_data(st, T2), failed={}), T2, old)
        self.assertIn('sp-hold-usol-v1', summary['skipped_books'])
        self.assertEqual(summary['skipped_detail']['sp-hold-usol-v1']['reason'], 'replay_window_exceeded_needs_review')
        self.assertEqual(st['books']['sp-hold-usol-v1']['di_cursor'], NOW-2000*MINUTE)

    def test_review_flag_over_50_percent_in_24h(self):
        st, old = init()
        st['data_isolation'] = dict(rule_id='data-isolation-v1', history=[[T1-i*MINUTE, ['USOL'] if i % 3 else []] for i in range(1, 40)])
        _, summary = V5.apply_tick(st, drop(v3_data(st, T1), ['USOL']), T1, old)
        self.assertEqual([f['symbol'] for f in summary['review_flags']], ['USOL'])
        st2, _ = init(); st2['data_isolation'] = dict(rule_id='data-isolation-v1', history=[[T1-i*MINUTE, []] for i in range(1, 40)])
        _, s2 = V5.apply_tick(st2, drop(v3_data(st2, T1), ['USOL']), T1, old)
        self.assertEqual(s2['review_flags'], [])

    def test_skip_logged_without_fabrication(self):
        st, old = init(); _, summary = V5.apply_tick(st, drop(v3_data(st, T1), ['USOL']), T1, old)
        with tempfile.TemporaryDirectory() as t:
            V5.log_skip(Path(t), T1, 1, summary)
            rec = json.loads((Path(t)/'data-gaps.jsonl').read_text().splitlines()[-1])
        self.assertEqual(rec['event'], 'data_isolation_skip'); self.assertFalse(rec['candles_fabricated']); self.assertFalse(rec['fills_backfilled'])

    def test_healthy_group_failure_still_fails_closed(self):
        st, old = init(); d = v3_data(st, T1); d['failed'] = {}
        d['minutes']['ETH'] = d['minutes']['ETH'][:-1]
        with self.assertRaises(ValueError): V5.apply_tick(st, d, T1, old)

class Collector(unittest.TestCase):
    def _info(self, now, missing_api='@156'):
        base = fake_info_factory(now)
        def info(payload, **_):
            typ = payload['type']
            if typ == 'metaAndAssetCtxs':
                return [dict(universe=[dict(name=c, szDecimals=5, maxLeverage=40) for c in S.COINS]),
                        [dict(funding='0.0000125', markPx='100', oraclePx='100') for _ in S.COINS]]
            if typ == 'allMids':
                return {**{c: '100' for c in S.COINS}, **{m['api_coin']: '100' for m in S3.SPOT_MARKETS.values()}}
            if typ == 'l2Book':
                return dict(time=now, levels=[[dict(px='99.99', sz='100')], [dict(px='100.01', sz='100')]])
            out = base(payload)
            if typ == 'candleSnapshot' and payload['req']['coin'] == missing_api and payload['req']['interval'] == '1m':
                out = [r for r in out if r['t'] < now//MINUTE*MINUTE-3*MINUTE]  # no-trade minutes: candles absent
            return out
        return info

    def test_missing_usol_candles_fail_only_usol_and_nothing_fabricated(self):
        now = NOW+20*MINUTE+5000
        with tempfile.TemporaryDirectory() as t, patch.object(L.sc, 'info', self._info(now)), patch.object(L.sc, 'now_ms', lambda: now+1000):
            pd = V5.PublicData(Path(t)); d = pd.fetch(dict(next_minute=now//MINUTE*MINUTE-MINUTE), now)
        self.assertEqual(set(d['failed']), {'USOL'})
        self.assertNotIn('USOL', d['spot_m1']); self.assertIn('UBTC', d['spot_m1']); self.assertEqual(set(d['m1']), set(S.COINS))
        self.assertNotIn('USOL', pd.cache['spot_m1'])

    def test_sixty_second_rule_still_global(self):
        now = NOW+20*MINUTE+5000
        with tempfile.TemporaryDirectory() as t, patch.object(L.sc, 'info', self._info(now)), patch.object(L.sc, 'now_ms', lambda: now+MINUTE+1):
            with self.assertRaisesRegex(ValueError, 'no stale fills'):
                V5.PublicData(Path(t)).fetch(dict(next_minute=now//MINUTE*MINUTE-MINUTE), now)

class WarmIsolate(unittest.TestCase):
    def test_isolate_keeps_failed_symbol_cache_and_warms_others(self):
        now = NOW+45_000; last = W.last_closed_1m(now); base = fake_info_factory(now)
        def info(payload):
            if payload['type'] == 'candleSnapshot' and payload['req']['coin'] == '@156': return []
            return base(payload)
        cache = seed_cache(last-20*MINUTE, now=now)
        with tempfile.TemporaryDirectory() as t:
            root = write_root(t, cache, seed_state(last-20*MINUTE))
            with self.assertRaises(ValueError):
                W.warm_cache(root=root, now=now, sleep_fn=lambda s: None, info_fn=info, force=True, record_gap=False)
            s = W.warm_cache(root=root, now=now, sleep_fn=lambda s: None, info_fn=info, force=True, record_gap=False, isolate=True)
            self.assertIn('USOL', s['isolated_failures']); self.assertEqual(s['status'], 'warmed_partial_isolated')
            out = L.read_json(root/'market_cache.json')
            self.assertEqual(out['spot_m1']['USOL'], cache['spot_m1']['USOL'])
            self.assertEqual(out['spot_m1']['UBTC'][-1]['t']+MINUTE, now//MINUTE*MINUTE)

if __name__ == '__main__': unittest.main()
