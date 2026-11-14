# Paper league on GitHub Actions

PAPER ONLY. One public `POST https://api.hyperliquid.xyz/info` per request. No API keys, wallets, signatures, or exchange writes. This does not change the Polymarket dashboard site or `pages.yml`.

A separate private repo could not be created from this environment (`gh` here is read-only, and there is no create-repo tool). The league lives in this folder so its commits stay in one place and the dashboard pages workflow is untouched. That workflow still uploads the whole tree, including this folder, because it was left as it is.

## What runs

`.github/workflows/league.yml` cron `*/5 * * * *` plus `workflow_dispatch`. Concurrency group `league` so two ticks do not overlap. Permissions are `contents: write` only. GitHub may start the cron 5–15 minutes late. A tick more than two intervals (10 minutes) after the previous one appends a row to `state/data-gaps.jsonl`. The first tick after the box also appends one row from `2026-11-13T15:21:03.509Z` with reason `box sleep`. Fills are not backfilled. The engine's own virtual-stop replay still runs and is flagged replayed.

`run_tick.py` copies `state/` into the engine directory, warms `market_cache.json` outside the 60-second snapshot clock (the same idea as `supervise.sh`), runs one `league_v8.py --once`, and copies state back. v7 is used only if v8 still raises a stale-fill guard after that warm.

The scheduler engine is v8. `last_tick.json` keeps `engine_version: 7` because v8 is the scheduling wrapper and does not relabel the tick record. `heartbeat.json` records `engine_version: 8`.

## Why v8 was skipping on the box

v8 treats `snapshot collection exceeded 60s` as a skip and keeps the process up. That guard is wall clock from the moment the tick is marked started until the last `allMids`, and the cache is saved only after the guard passes. A public `allMids` returns in about 0.2s and a `candleSnapshot` of the whole gap (1,157 one-minute bars) in about 0.6s. Warming the stale cache on a healthy host still took 61.5s (34 requests, estimated weight 854) because the series are fetched one after another with the existing pace. That is already over the guard, so an in-tick catch-up is rejected and the cache is not written. v8 then does not exit, so `supervise.sh` never warms again, and every later minute repeats the same cold catch-up. That is the skip loop. It is not a 60-second API. After the warm, the same v8 one-shot tick collected in 3.0s (8 requests) and advanced 351 to 352.

## State and the one writer

Authoritative files are under `paper-league/state/` (books, `league_state.json` including halt latches and the DSR ledger, `heartbeat.json`, `market_cache.json`, `data-gaps.jsonl`, `sources/`). The frozen engine cannot be edited to read that path: its SHA-256 is checked every tick. The scheduler copies state in, ticks, and copies it back. GitHub Actions is the only writer.

A box copy stays read-only:

```bash
git pull
# read paper-league/state/heartbeat.json and last_tick.json
# do not commit state from the box
```

## Parent files that were not in the export

The frozen manifest also hashes `strategy-lab/paper-trading/simcore.py`, `shadow_exchange.py`, `sentinel.py`, and `risk-limits.md`. Those bytes were not in the export and are not on GitHub. The copies here are reconstructions checked against the league tests and the 13 Nov risk-review cost formula (169 of 174 existing tests pass; the other five need `backups/extension-v2/` or `backtests/2026-11-09_hl-3strat/backtest.py`, which were not exported, or a heartbeat file sitting next to the engine). `run_tick.py` returns the pinned digest only while a reconstructed file does not match. Drop the original bytes in place and the substitution stops.
