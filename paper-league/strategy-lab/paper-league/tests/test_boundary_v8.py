import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import league as L
import league_v5 as V5
import league_v8 as V8
from strategies import MINUTE

BOUNDARY = ValueError('snapshot crossed minute boundary; retry current data, no hindsight fills')

class Boundary(unittest.TestCase):
    def test_guard_still_raises_in_frozen_collector(self):
        src = (Path(V5.__file__)).read_text()
        self.assertIn("if now//S3.MINUTE != observed//S3.MINUTE: raise ValueError('snapshot crossed minute boundary", src)
        self.assertIn("if observed-now > S3.MINUTE: raise ValueError('snapshot collection exceeded 60s; no stale fills')", src)

    def test_boundary_crossing_skips_tick_without_crash_or_writes(self):
        hbs, logs = [], []
        def tick(): raise BOUNDARY
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            r, skips = V8.run_once(tick, root, 0, hb=lambda root, s, **k: hbs.append((s, k)), log=lambda *a, **k: logs.append(a))
            self.assertIsNone(r); self.assertEqual(skips, 1)
            self.assertEqual(list(root.iterdir()), [])  # no state, ledger, source or cache written
        self.assertEqual(hbs[-1][0], 'skipped_stale_guard'); self.assertFalse(hbs[-1][1]['alert'])
        self.assertFalse(hbs[-1][1]['fills_written'])
        for _ in range(2): r, skips = V8.run_once(tick, None, skips, hb=lambda root, s, **k: hbs.append((s, k)), log=lambda *a, **k: None)
        self.assertEqual(skips, 3); self.assertTrue(hbs[-1][1]['alert'])

    def test_sixty_second_guard_also_skips(self):
        def tick(): raise ValueError('snapshot collection exceeded 60s; no stale fills')
        r, skips = V8.run_once(tick, None, 0, hb=lambda *a, **k: None, log=lambda *a, **k: None)
        self.assertIsNone(r); self.assertEqual(skips, 1)

    def test_sixty_second_skip_persists_warmed_cache_and_no_fills(self):
        hbs = []
        def tick(): raise ValueError('snapshot collection exceeded 60s; no stale fills')
        def warm(root):
            Path(root, 'market_cache.json').write_text('{"m1":{"BTC":[]}}')
            return dict(warmed=True, fills_written=False)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            r, skips = V8.run_once(tick, root, 0, hb=lambda root, s, **k: hbs.append((s, k)), log=lambda *a, **k: None, warm_fn=warm)
            self.assertIsNone(r); self.assertEqual(skips, 1)
            self.assertEqual((root/'market_cache.json').read_text()[:4], '{"m1')
            self.assertFalse((root/'league_state.json').exists())
            self.assertFalse((root/'data-gaps.jsonl').exists())
            names = {p.name for p in root.iterdir()}
            self.assertEqual(names, {'market_cache.json'})
        self.assertFalse(hbs[-1][1]['fills_written'])
        self.assertTrue(hbs[-1][1]['cache_persisted'])

    def test_other_errors_still_fail_closed(self):
        def tick(): raise ValueError('USOL spot 1m warmup/continuity missing')
        with self.assertRaises(ValueError):
            V8.run_once(tick, None, 0, hb=lambda *a, **k: None, log=lambda *a, **k: None)

    def test_success_resets_skips_and_alert_false(self):
        hbs = []
        res = dict(tick=110, book_count=125, active_books=121, retired_books=[], load={}, labels_v1={},
                   data_isolation=dict(failed_symbols={}, skipped_books=[], stale_positions=[], fail_rate_24h={}, review_flags=[]))
        r, skips = V8.run_once(lambda: res, None, 2, hb=lambda root, s, **k: hbs.append((s, k)), log=lambda *a, **k: None)
        self.assertEqual(skips, 0); self.assertEqual(hbs[-1][0], 'ok'); self.assertFalse(hbs[-1][1]['alert'])

    def test_alignment_keeps_14s_collection_inside_minute(self):
        for sec in (0, 0.5, 1.0, 1.9, 30, 44.9, 45.5, 59.9):
            wait = V8.seconds_until_aligned(1_794_465_240.0+sec)
            start = (sec+wait) % 60
            self.assertGreaterEqual(start, V8.ALIGN_OFFSET_S-1e-3); self.assertLessEqual(start, V8.ALIGN_OFFSET_S+1.0+1e-3)
            self.assertLess(start+16.0, 60.0)  # observed collection 13.5-15.1s stays in the same minute
            self.assertLess(wait, 60.0)

    def test_late_minute_start_crossing_is_detected_by_minute_math(self):
        began = 1_794_465_240_000+46_000; observed = began+16_000  # 14:33:46 restart pattern from daemon.log
        self.assertNotEqual(began//MINUTE, observed//MINUTE)
        began = 1_794_465_240_000+1_000; observed = began+16_000
        self.assertEqual(began//MINUTE, observed//MINUTE)

if __name__ == '__main__': unittest.main()
