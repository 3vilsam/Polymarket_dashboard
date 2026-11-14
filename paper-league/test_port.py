"""Checks for the reconstructed parent primitives and the scheduler's gap rule.

Does not touch league_state or the network.
"""
import json
import tempfile
import unittest
from pathlib import Path

from strategy_lab_import import add_parent

add_parent()
import simcore as sc
import sentinel
import run_tick


class Reconstruction(unittest.TestCase):
    def test_myt_matches_last_good_tick(self):
        self.assertEqual(sc.myt(1794583263509), '2026-11-13T23:21:03+08:00')
        self.assertEqual(sc.myt_date(1794583263509), '2026-11-13')

    def test_equity_is_cash_plus_dir_size_mark(self):
        book = dict(cash=99.99248185462616, marks={'SOL': 81.8915}, positions={
            'P': dict(coin='SOL', dir=-1, size=0.22, entry_px=83.1038759, stop=85.2)})
        self.assertAlmostEqual(sc.unrealized(book), 0.22 * (83.1038759 - 81.8915))
        self.assertAlmostEqual(sc.equity(book), 99.99248185462616 + 0.22 * (83.1038759 - 81.8915))

    def test_engine_rpu_matches_risk_review(self):
        entry, stop, size = 83.1038759, 85.20133895161196, 0.22
        cfg = sc.DEFAULT_CONFIG
        per = sc.entry_risk(entry, stop, 1.0, cfg)
        reserve = max(0.0000125, 0.0000125) * 24 * entry
        self.assertAlmostEqual(size * (per + reserve), 0.492961090719, places=9)

    def test_stop_fills_match_league_tests(self):
        cfg = dict(stop_slippage_bps=5.0)
        long = dict(dir=1, stop=97.0)
        self.assertAlmostEqual(sentinel.stop_fill(long, cfg, 99), 97 * (1 - 0.0005))
        self.assertFalse(sentinel.hit_adverse(long, 99))
        self.assertAlmostEqual(sentinel.stop_fill(long, cfg, 94), 94 * (1 - 0.0005))
        short = dict(dir=-1, stop=103.0)
        self.assertAlmostEqual(sentinel.stop_fill(short, cfg, 106), 106 * (1 + 0.0005))

    def test_floor_never_rounds_up(self):
        self.assertEqual(sc.floor_sz(0.221597644736, 2), 0.22)
        self.assertEqual(sc.floor_sz(0.209, 2), 0.20)

    def test_pass_gate_empty(self):
        cfg = sc.load_config()
        self.assertEqual(cfg['strategies'], [])
        self.assertFalse(sc.strategy_gate(cfg, 'donchian')[0])

    def test_info_refuses_signed_payload(self):
        with self.assertRaises(ValueError):
            sc.info(dict(type='order', signature='nope'))


class Gaps(unittest.TestCase):
    def test_box_sleep_once_then_late_interval(self):
        with tempfile.TemporaryDirectory() as tmp:
            engine = Path(tmp)
            before = dict(ticks=351, last_tick_ms=run_tick.BOX_SLEEP_TICK_MS, next_minute=1, books={})
            after = dict(tick=352, ts_utc='2026-11-14T10:40:00.000Z', evidence=dict(received_ms=run_tick.BOX_SLEEP_TICK_MS + 20 * 60 * 1000))
            run_tick.record_gaps(engine, before, after)
            run_tick.record_gaps(engine, before, after)
            lines = [json.loads(x) for x in (engine / 'data-gaps.jsonl').read_text().splitlines()]
            self.assertEqual(len(lines), 1)
            self.assertEqual(lines[0]['reason'], 'box sleep')
            self.assertFalse(lines[0]['fills_backfilled'])
            later_before = dict(ticks=352, last_tick_ms=after['evidence']['received_ms'], next_minute=1, books={})
            later_after = dict(tick=353, ts_utc='x', evidence=dict(received_ms=later_before['last_tick_ms'] + run_tick.LATE_MS + 1))
            run_tick.record_gaps(engine, later_before, later_after)
            reasons = [json.loads(x)['reason'] for x in (engine / 'data-gaps.jsonl').read_text().splitlines()]
            self.assertEqual(reasons[-1], 'scheduled tick more than 2 intervals late')
            on_time = dict(tick=354, evidence=dict(received_ms=later_after['evidence']['received_ms'] + 5 * 60 * 1000))
            run_tick.record_gaps(engine, dict(ticks=353, last_tick_ms=later_after['evidence']['received_ms'], books={}), on_time)
            self.assertEqual(len((engine / 'data-gaps.jsonl').read_text().splitlines()), 2)


if __name__ == '__main__':
    unittest.main()
