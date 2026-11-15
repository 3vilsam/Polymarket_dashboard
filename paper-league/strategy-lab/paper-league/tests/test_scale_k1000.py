import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import league_v3 as V3
import scale_k1000 as K
import strategies as S
import strategies_v3 as S3


def parent(bid, kind='vwap', halted=False, retired=False, sha='abc'):
    book = dict(id=bid, kind=kind, owner='desk', lane='fast', market='perp', halted=halted, retired=retired,
                spec=dict(kind=kind, coins=['BTC'], interval=300000, sha256=sha, params={}))
    return book


class ScaleTwins(unittest.TestCase):
    def test_skips_halted_and_retired(self):
        books = {
            'a': parent('a'),
            'b': parent('b', halted=True),
            'c': parent('c', retired=True),
        }
        chosen = [b['id'] for b in books.values() if K.is_active(b)]
        self.assertEqual(chosen, ['a'])

    def test_twin_bankroll_and_parent_untouched(self):
        src = parent('f1-vwap5m-v1', sha='323d')
        before = copy.deepcopy(src)
        twin = K.make_twin(src, 1_700_000_000_000, '323d')
        self.assertEqual(src, before)
        self.assertEqual(twin['id'], 'f1-vwap5m-v1-k1000')
        self.assertEqual(twin['cash'], 1000)
        self.assertEqual(twin['starting_equity'], 1000)
        self.assertEqual(twin['rules_sha256'], '323d')
        self.assertEqual(twin['spec']['sha256'], '323d')
        self.assertEqual(twin['events'][0]['event'], 'registered')
        self.assertEqual(twin['events'][0]['trial_count_delta'], 0)
        self.assertEqual(twin['positions'], {})

    def test_missing_ueth_does_not_crash_spot_twins(self):
        """Reproduce the Actions KeyError: UETH absent, another spot twin still runnable."""
        ubtc = dict(id='sp-ema15m-ubtc-v1-k1000', kind='spot_ema', market='spot', cash=1000,
                    spot_spec=dict(kind='spot_ema', coins=['UBTC'], interval=900000, params={}),
                    events=[], positions={}, decisions={})
        ueth = dict(id='sp-ema15m-ueth-v1-k1000', kind='spot_ema', market='spot', cash=1000,
                    spot_spec=dict(kind='spot_ema', coins=['UETH'], interval=900000, params={}),
                    events=[], positions={}, decisions={})
        books = {ubtc['id']: ubtc, ueth['id']: ueth}
        before = copy.deepcopy(ueth)
        now = 1_700_000_000_000
        end = now // S.MINUTE * S.MINUTE
        data = dict(
            failed={'UETH': "ValueError('UETH spot 1m warmup/continuity missing')"},
            observed_ms=now, mids={'UBTC': 100.0, 'HYPE': 10.0, 'BTC': 1.0, 'ETH': 1.0, 'SOL': 1.0},
            minutes={c: [] for c in S.COINS}, spot_minutes={'UBTC': [], 'HYPE': []},
        )

        def fake_apply(st, _data, _now, _start):
            if 'UETH' in S3.SPOT_COINS:
                raise KeyError('UETH')
            fake_apply.called = True
        fake_apply.called = False

        with patch.object(V3, 'apply_spot', fake_apply):
            skipped, missing = K._apply(books, data, now, end, {'USOL'})
        self.assertTrue(fake_apply.called)
        self.assertIn('UETH', missing)
        self.assertIn(ueth['id'], skipped)
        self.assertEqual(books[ueth['id']]['cash'], before['cash'])

    def test_lost_tick_record_is_written_once(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            K.record_lost_ticks(root)
            K.record_lost_ticks(root)
            lines = [json.loads(x) for x in (root / 'data-gaps.jsonl').read_text().splitlines()]
            self.assertEqual(len(lines), 1)
            self.assertEqual(lines[0]['ticks_lost'], 11)
            self.assertFalse(lines[0]['double_counted'])

    def test_apply_does_not_rewrite_parent_fingerprint_helper(self):
        books = {'a': parent('a', sha='1')}
        first = K._fingerprint(books)
        books['a']['cash'] = 1000
        self.assertNotEqual(first, K._fingerprint(books))


if __name__ == '__main__':
    unittest.main()
