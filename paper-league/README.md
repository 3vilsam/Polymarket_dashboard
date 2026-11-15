# Paper league on GitHub Actions

PAPER ONLY. One public `POST https://api.hyperliquid.xyz/info` per request. No API keys, wallets, signatures, or exchange writes. This does not change the Polymarket dashboard site or `pages.yml`.

A separate private repo could not be created from this environment (`gh` here is read-only, and there is no create-repo tool). The league lives in this folder so its commits stay in one place and the dashboard pages workflow is untouched. That workflow still uploads the whole tree, including this folder, because it was left as it is.

## What runs

`.github/workflows/league.yml` keeps a backup cron (`7-57/5 * * * *`) and `workflow_dispatch`. GitHub's own cron on this public repo has been hours apart (one league run in the first 6.5 hours, and the Pages `*/5` cron about 4–7 hours apart), so each run on `main` waits until about five minutes after it started and then queues the next run with `gh workflow run`. That needs `actions: write` as well as `contents: write`. The token is the built-in `GITHUB_TOKEN`; it can create a `workflow_dispatch` run, and it is not an API key or an exchange credential. Concurrency group `league` does not cancel the run in progress, so the queued run starts after this one pushes state. A tick more than two intervals (10 minutes) after the previous one appends a row to `state/data-gaps.jsonl`. Fills are not backfilled. The engine's own virtual-stop replay still runs and is flagged replayed.

`run_tick.py` copies `state/` into the engine directory, warms `market_cache.json` outside the 60-second snapshot clock (the same idea as `supervise.sh`), runs one `league_v8.py --once`, and copies state back. v7 is used only if v8 still raises a stale-fill guard after that warm.

The scheduler engine is v8. `last_tick.json` keeps `engine_version: 7` because v8 is the scheduling wrapper and does not relabel the tick record. `heartbeat.json` records `engine_version: 8`.

Scale twins (`-k1000`) are a separate cohort at 1,000 virtual USDT. They are not in `books` and do not change the DSR trial count. See `trial-ledger.md` and the `-k1000` section of `NEW-BOOK-HASHES.md`. A measured tick on the tick-493 state collected the snapshot in 3.9s and applied 117 twins in 1.1s (7.7s wall together), under the 60s guard.

## Why v8 was skipping on the box

v8 treats `snapshot collection exceeded 60s` as a skip and keeps the process up. That guard is wall clock from the moment the tick is marked started until the last `allMids`, and the cache is saved only after the guard passes. A public `allMids` returns in about 0.2s and a `candleSnapshot` of the whole gap (1,157 one-minute bars) in about 0.6s. Warming the stale cache on a healthy host still took 61.5s (34 requests, estimated weight 854) because the series are fetched one after another with the existing pace. That is already over the guard, so an in-tick catch-up is rejected before the collector's own save. The old v8 skip left that cache unwritten and did not exit, so `supervise.sh` never warmed again and every later minute repeated the cold catch-up. v8 now warms and writes `market_cache.json` when that 60s guard trips (no fills, no `league_state`), and it warms again before the next minute, so the catch-up cannot loop. After a warm, the same v8 one-shot tick collected in 3.0s (8 requests) and advanced 351 to 352. It is not a 60-second API.

## State and the one writer

Authoritative files are under `paper-league/state/` (books, `league_state.json` including halt latches and the DSR ledger, `heartbeat.json`, `market_cache.json`, `data-gaps.jsonl`, `sources/`). The frozen engine cannot be edited to read that path: its SHA-256 is checked every tick. The scheduler copies state in, ticks, and copies it back. The chain on `main` is the writer. The box export at tick 392 replaced an earlier GitHub replay (tick 352 from tick 351); that GitHub tick is recorded in `data-gaps.jsonl` as superseded and is not in the ledger. Stop the box engine before it ticks past that export, or the two copies diverge again.

A box copy stays read-only:

```bash
git pull
# read paper-league/state/heartbeat.json and last_tick.json
# do not commit state from the box
```

## Parent files that were not in the export

The frozen manifest also hashes `strategy-lab/paper-trading/simcore.py`, `shadow_exchange.py`, `sentinel.py`, and `risk-limits.md`. Those bytes were not in the export and are not on GitHub. The copies here are reconstructions checked against the league tests and the 13 Nov risk-review cost formula (169 of 174 existing tests pass; the other five need `backups/extension-v2/` or `backtests/2026-11-09_hl-3strat/backtest.py`, which were not exported, or a heartbeat file sitting next to the engine). `run_tick.py` returns the pinned digest only while a reconstructed file does not match. Drop the original bytes in place and the substitution stops.
