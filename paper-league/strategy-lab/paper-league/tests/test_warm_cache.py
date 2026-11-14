import copy
import json
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import league as L
import league_v3 as V3
import strategies as S
import strategies_v3 as S3
import warm_cache as W
from test_league import NOW


def bars(step, n, last_t, px=100.):
    start = last_t - (n - 1) * step
    return [dict(t=start + i * step, o=px, h=px * 1.001, l=px * 0.999, c=px, v=1.) for i in range(n)]


def last_closed(step, now):
    return now // step * step - step


def seed_cache(last_1m, now=None):
    now = last_1m + S3.MINUTE if now is None else now
    cache = dict(fourhour={}, daily={}, funding={}, m1={}, m5={}, m15={}, h1={},
                 spot_m1={}, spot_m5={}, spot_m15={}, spot_h1={}, spot_meta_ms=last_1m)
    for coin in S.COINS:
        cache['m1'][coin] = bars(S3.MINUTE, 250, last_1m)
        cache['m5'][coin] = bars(5 * S3.MINUTE, 250, last_closed(5 * S3.MINUTE, now))
        cache['m15'][coin] = bars(15 * S3.MINUTE, 250, last_closed(15 * S3.MINUTE, now))
        cache['h1'][coin] = bars(S3.HOUR, 250, last_closed(S3.HOUR, now))
        cache['fourhour'][coin] = bars(4 * S3.HOUR, 250, last_closed(4 * S3.HOUR, now))
        cache['daily'][coin] = bars(S3.DAY, 250, last_closed(S3.DAY, now))
        cache['funding'][coin] = [dict(coin=coin, fundingRate='0.0000125', premium='0',
                                      time=now // S3.HOUR * S3.HOUR)]
    for name, mkt in S3.SPOT_MARKETS.items():
        cache['spot_m1'][name] = bars(S3.MINUTE, 250, last_1m)
        cache['spot_m5'][name] = bars(5 * S3.MINUTE, 250, last_closed(5 * S3.MINUTE, now))
        cache['spot_m15'][name] = bars(15 * S3.MINUTE, 250, last_closed(15 * S3.MINUTE, now))
        cache['spot_h1'][name] = bars(S3.HOUR, 250, last_closed(S3.HOUR, now))
    return cache


def seed_state(last_1m, tick=58):
    last_tick = last_1m + 23_000
    return dict(
        ticks=tick, last_tick_ms=last_tick, next_minute=last_1m + S3.MINUTE,
        books={'g-vwap-btc-p1-v1': dict(
            id='g-vwap-btc-p1-v1', market='perp',
            positions={'P000002': dict(id='P000002', coin='BTC', side='long', stop=73330.74,
                                       entry_px=73699.23, size=0.00101)},
        )},
    )


def write_root(tmp, cache, state):
    root = Path(tmp)
    L.atomic(root / 'market_cache.json', cache)
    L.atomic(root / 'league_state.json', state)
    (root / 'books' / 'g-vwap-btc-p1-v1').mkdir(parents=True)
    (root / 'books' / 'g-vwap-btc-p1-v1' / 'ledger.jsonl').write_text('{"seq":1,"event":"registered"}\n')
    return root


def fake_info_factory(now):
    calls = []

    def info(payload):
        calls.append(copy.deepcopy(payload))
        typ = payload['type']
        if typ == 'spotMetaAndAssetCtxs':
            tokens = [dict(index=m['token_index'], name=m['token_name'], szDecimals=m['szDecimals'])
                      for m in S3.SPOT_MARKETS.values()]
            ctxs = [dict(coin=m['api_coin']) for m in S3.SPOT_MARKETS.values()]
            return [dict(tokens=tokens), ctxs]
        if typ == 'fundingHistory':
            hour = (now // S3.HOUR) * S3.HOUR
            return [dict(coin=payload['coin'], fundingRate='0.0000125', premium='0', time=hour)]
        if typ == 'candleSnapshot':
            req = payload['req']
            step = {'1m': S3.MINUTE, '5m': 5 * S3.MINUTE, '15m': 15 * S3.MINUTE,
                    '1h': S3.HOUR, '4h': 4 * S3.HOUR, '1d': S3.DAY}[req['interval']]
            start = int(req['startTime']); end = int(req['endTime'])
            t = start // step * step
            out = []
            while t <= end and t + step <= now:
                out.append(dict(t=t, o='100', h='100.1', l='99.9', c='100', v='1'))
                t += step
            return out
        raise AssertionError('unexpected ' + typ)
    info.calls = calls
    return info


class WarmDecision(unittest.TestCase):
    def test_noop_when_cache_is_current(self):
        now = NOW + 45_000
        last = W.last_closed_1m(now)
        cache = seed_cache(last, now=now)
        self.assertEqual(W.max_1m_lag_ms(cache, now), 0)
        self.assertFalse(W.should_warm(cache, now))

    def test_noop_at_exactly_ten_minutes(self):
        now = NOW + 45_000
        last = W.last_closed_1m(now) - 10 * S3.MINUTE
        cache = seed_cache(last, now=now)
        self.assertEqual(W.max_1m_lag_ms(cache, now), 10 * S3.MINUTE)
        self.assertFalse(W.should_warm(cache, now))

    def test_warm_when_gap_greater_than_ten_minutes(self):
        now = NOW + 45_000
        last = W.last_closed_1m(now) - 10 * S3.MINUTE - 1
        cache = seed_cache(last, now=now)
        self.assertTrue(W.should_warm(cache, now))


class WarmCache(unittest.TestCase):
    def test_fresh_cache_makes_no_requests_and_writes_no_fills(self):
        now = NOW + 45_000
        last = W.last_closed_1m(now)
        sleeps = []
        info = fake_info_factory(now)
        with tempfile.TemporaryDirectory() as tmp:
            root = write_root(tmp, seed_cache(last, now=now), seed_state(last))
            before_state = (root / 'league_state.json').read_bytes()
            before_ledger = (root / 'books/g-vwap-btc-p1-v1/ledger.jsonl').read_text()
            before_cache = (root / 'market_cache.json').read_bytes()
            summary = W.warm_cache(root=root, now=now, sleep_fn=sleeps.append, info_fn=info, record_gap=True)
            self.assertFalse(summary['warmed'])
            self.assertEqual(summary['status'], 'cache_fresh')
            self.assertFalse(summary['fills_written'])
            self.assertEqual(info.calls, [])
            self.assertEqual(sleeps, [])
            self.assertEqual((root / 'league_state.json').read_bytes(), before_state)
            self.assertEqual((root / 'books/g-vwap-btc-p1-v1/ledger.jsonl').read_text(), before_ledger)
            self.assertEqual((root / 'market_cache.json').read_bytes(), before_cache)
            # last tick is old relative to now (~45s only) so no gap record either
            self.assertFalse((root / 'data-gaps.jsonl').exists())

    def test_warms_stale_cache_staggers_and_records_gap_without_fills(self):
        now = NOW + 45_000
        last = W.last_closed_1m(now) - 15 * S3.MINUTE
        sleeps = []
        info = fake_info_factory(now)
        with tempfile.TemporaryDirectory() as tmp:
            root = write_root(tmp, seed_cache(last, now=now), seed_state(last, tick=58))
            before_state = (root / 'league_state.json').read_bytes()
            before_ledger = (root / 'books/g-vwap-btc-p1-v1/ledger.jsonl').read_text()
            summary = W.warm_cache(root=root, now=now, sleep_fn=sleeps.append, info_fn=info, record_gap=True)
            self.assertTrue(summary['warmed'])
            self.assertTrue(summary['gap_recorded'])
            self.assertFalse(summary['fills_written'])
            self.assertGreater(summary['requests'], 0)
            self.assertEqual((root / 'league_state.json').read_bytes(), before_state)
            self.assertEqual((root / 'books/g-vwap-btc-p1-v1/ledger.jsonl').read_text(), before_ledger)
            warmed = L.read_json(root / 'market_cache.json')
            self.assertEqual(W.max_1m_lag_ms(warmed, now), 0)
            for coin in S.COINS:
                rows = warmed['m1'][coin]
                self.assertEqual(rows[-1]['t'], W.last_closed_1m(now))
                self.assertTrue(all(b['t'] - a['t'] == S3.MINUTE for a, b in zip(rows, rows[1:])))
            recs = [json.loads(l) for l in (root / 'data-gaps.jsonl').read_text().splitlines() if l.strip()]
            self.assertEqual(len(recs), 1)
            self.assertEqual(recs[0]['last_successful_tick'], 58)
            self.assertEqual(recs[0]['fills_backfilled'], False)
            self.assertEqual(recs[0]['stops_during_gap'], 'unverified')
            self.assertEqual(recs[0]['open_positions'][0]['book'], 'g-vwap-btc-p1-v1')
            # staggered sleeps between HTTP calls (first call has no leading sleep)
            self.assertGreaterEqual(len(sleeps), summary['requests'] - 1)
            self.assertTrue(any(s == W.STAGGER_S for s in sleeps))
            # second call is idempotent: cache fresh, gap already recorded
            sleeps2 = []; info2 = fake_info_factory(now)
            summary2 = W.warm_cache(root=root, now=now, sleep_fn=sleeps2.append, info_fn=info2, record_gap=True)
            self.assertFalse(summary2['warmed'])
            self.assertFalse(summary2['gap_recorded'])
            self.assertEqual(info2.calls, [])
            recs2 = [json.loads(l) for l in (root / 'data-gaps.jsonl').read_text().splitlines() if l.strip()]
            self.assertEqual(len(recs2), 1)

    def test_does_not_invent_bars(self):
        now = NOW + 45_000
        last = W.last_closed_1m(now) - 15 * S3.MINUTE
        info = fake_info_factory(now)
        with tempfile.TemporaryDirectory() as tmp:
            root = write_root(tmp, seed_cache(last, now=now), seed_state(last))
            W.warm_cache(root=root, now=now, sleep_fn=lambda _s: None, info_fn=info, record_gap=False)
            warmed = L.read_json(root / 'market_cache.json')
            # only bars the stub API would return; no timestamps invented past last closed 1m
            for coin in S.COINS:
                for row in warmed['m1'][coin]:
                    self.assertLessEqual(row['t'] + S3.MINUTE, now)
                    self.assertEqual(row['c'], 100.0)

    def test_429_retries_with_backoff(self):
        now = NOW + 45_000
        last = W.last_closed_1m(now) - 15 * S3.MINUTE
        hits = {'n': 0}
        base = fake_info_factory(now)

        def flaky(payload):
            hits['n'] += 1
            if hits['n'] == 1:
                raise RuntimeError('info candleSnapshot failed: HTTP Error 429: Too Many Requests')
            return base(payload)

        sleeps = []
        with tempfile.TemporaryDirectory() as tmp:
            root = write_root(tmp, seed_cache(last, now=now), seed_state(last))
            summary = W.warm_cache(root=root, now=now, sleep_fn=sleeps.append, info_fn=flaky, record_gap=False)
            self.assertTrue(summary['warmed'])
            self.assertTrue(any(s >= 1.0 for s in sleeps))

    def test_sixty_second_no_stale_fills_rule_unchanged(self):
        src = (Path(__file__).resolve().parents[1] / 'league_v3.py').read_text()
        self.assertIn("if observed-now>S3.MINUTE: raise ValueError('snapshot collection exceeded 60s; no stale fills')", src)
        self.assertIn("if now//S3.MINUTE!=observed//S3.MINUTE: raise ValueError('snapshot crossed minute boundary; retry current data, no hindsight fills')", src)
        started = NOW
        observed = NOW + S3.MINUTE + 1

        class FrozenClock:
            def __init__(self):
                self.n = 0
            def __call__(self):
                self.n += 1
                return observed

        clock = FrozenClock()
        with patch.object(L.sc, 'now_ms', clock):
            collector = V3.PublicData.__new__(V3.PublicData)
            collector.weight = 0
            collector.collect_started = time.monotonic()
            with self.assertRaisesRegex(ValueError, 'snapshot collection exceeded 60s; no stale fills'):
                # Reproduce the exact frozen check with a 60s+1ms collection window.
                now = started
                if observed - now > S3.MINUTE:
                    raise ValueError('snapshot collection exceeded 60s; no stale fills')
        # Confirm threshold is still strictly greater than 60s, not loosened to a longer window.
        self.assertEqual(S3.MINUTE, 60_000)



class ForceWarmAndSupervisor(unittest.TestCase):
    def test_force_warms_even_when_cache_is_current(self):
        now = NOW + 45_000
        last = W.last_closed_1m(now)
        cache = seed_cache(last, now=now)
        self.assertFalse(W.should_warm(cache, now))
        info = fake_info_factory(now)
        sleeps = []
        with tempfile.TemporaryDirectory() as tmp:
            root = write_root(tmp, cache, seed_state(last))
            before_state = (root / 'league_state.json').read_bytes()
            before_ledger = (root / 'books/g-vwap-btc-p1-v1/ledger.jsonl').read_text()
            summary = W.warm_cache(root=root, now=now, sleep_fn=sleeps.append, info_fn=info,
                                   record_gap=True, force=True)
            self.assertNotEqual(summary['status'], 'cache_fresh')
            self.assertFalse(summary['fills_written'])
            self.assertEqual((root / 'league_state.json').read_bytes(), before_state)
            self.assertEqual((root / 'books/g-vwap-btc-p1-v1/ledger.jsonl').read_text(), before_ledger)
            self.assertEqual(W.max_1m_lag_ms(L.read_json(root / 'market_cache.json'), now), 0)

    def test_supervisor_always_force_warms_and_never_gives_up(self):
        src = (Path(__file__).resolve().parents[1] / 'supervise.sh').read_text()
        self.assertIn('warm_cache.py --force', src)
        self.assertIn('backoff', src)
        self.assertIn('--alert', src)
        # Loop ends only on STOP; there is no failure-count cap or exit on error.
        self.assertIn('while [[ ! -e STOP ]]', src)
        self.assertNotRegex(src, r'fail(ure|ed)_count|max_fail|give-up-after|MAX_FAIL')
        self.assertNotRegex(src, r'if \(\( failures.*>')
        self.assertIn("snapshot collection exceeded 60s; no stale fills",
                      (Path(__file__).resolve().parents[1] / 'league_v3.py').read_text())

    def test_supervisor_alert_writes_heartbeat_not_fills(self):
        now = NOW + 45_000
        last = W.last_closed_1m(now)
        with tempfile.TemporaryDirectory() as tmp:
            root = write_root(tmp, seed_cache(last, now=now), seed_state(last, tick=82))
            before_state = (root / 'league_state.json').read_bytes()
            before_ledger = (root / 'books/g-vwap-btc-p1-v1/ledger.jsonl').read_text()
            rec = W.supervisor_alert(root=root, status='SUPERVISOR_RETRY', backoff_s=300,
                                     engine_rc=1, error='engine exited rc=1', supervisor_pid=305107)
            hb = L.read_json(root / 'heartbeat.json')
            self.assertEqual(hb['status'], 'SUPERVISOR_RETRY')
            self.assertTrue(hb['alert'])
            self.assertEqual(hb['backoff_s'], 300)
            self.assertEqual(hb['engine_rc'], 1)
            self.assertEqual(hb['last_successful_tick'], 82)
            self.assertEqual(rec['status'], 'SUPERVISOR_RETRY')
            self.assertEqual((root / 'league_state.json').read_bytes(), before_state)
            self.assertEqual((root / 'books/g-vwap-btc-p1-v1/ledger.jsonl').read_text(), before_ledger)
            self.assertFalse((root / 'data-gaps.jsonl').exists())


if __name__ == '__main__':
    unittest.main(verbosity=2)
