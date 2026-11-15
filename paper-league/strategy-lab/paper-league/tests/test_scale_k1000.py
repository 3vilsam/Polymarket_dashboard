import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import scale_k1000 as K


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

    def test_apply_does_not_rewrite_parent_fingerprint_helper(self):
        books = {'a': parent('a', sha='1')}
        first = K._fingerprint(books)
        books['a']['cash'] = 1000
        self.assertNotEqual(first, K._fingerprint(books))


if __name__ == '__main__':
    unittest.main()
