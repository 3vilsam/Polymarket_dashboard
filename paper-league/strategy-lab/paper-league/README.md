# Forward PAPER league: 100 perp books + 16 spot books

**54 fast + 44 slow research books + BTC-hold and random-entry controls**, each100 virtual USDC. One60-second public Hyperliquid mainnet collector. No keys, accounts, orders, signing, exchange writes, testnet or real capital. These are98 correlated, unvalidated experiments, not98 profitable strategies. No LLM call per market tick.

## Run / inspect

```bash
cd /workspace/trading-desk/strategy-lab/paper-league
./start.sh                              # idempotent supervisor, preserve all capital/history
./status.sh                             # concise health, load and leading rows; not a winner claim
./status.sh --full                       # all100 rows, both controls and evidence gates
python3 -m unittest discover -s tests -v # offline/synthetic, no exchange or book writes
python3 -c 'import league_v2; league_v2.registration(); print("all frozen files verified")'
# Only when no daemon holds the singleton lock:
python3 league_v3.py --once  # or league_v2.py only if no v3 supervisor is running
```

`supervise.sh` always runs `warm_cache.py --force` before each engine start (staggered public `/info` reads into `market_cache.json`, outside the snapshot clock), including when the lag is under 10 minutes, so a short stall cannot skip warmup and then miss the 60-second snapshot budget. That keeps the existing 60-second / no-stale-fills rule intact. Known gaps are appended to `data-gaps.jsonl` (stops during a gap are unverified; fills are never backfilled). Then it runs `league_v3.py` (frozen v1/v2 books plus the 16 spot books) and restarts a failed engine with 30–300 second exponential backoff; it does not give up after N failures. Engine/supervisor each have singleton flocks; state and tick commit atomic/fsynced. `heartbeat.json` shows fetching/ok/ERROR_NO_NEW_RISK and supervisor alerts (`SUPERVISOR_WARMING` / `SUPERVISOR_RETRY` / `SUPERVISOR_WARM_FAILED`, `alert=true`) while the engine is down; stale heartbeat/data>180s is not all-clear. Logs `daemon.log`, `last_tick.json`; full archived public request/receipt evidence under `sources/`.

**No automatic whole-box reboot startup:** cron was absent; no service installed. Existing daily review routine must call `start.sh` then `status.sh`. Supervision covers engine failure, not a powered-off box. Intentional stop: create `STOP`, TERM only verified supervisor PID; it forwards TERM to its engine. Resume: remove STOP and `start.sh`. Never reset/delete `league_state.json`; no automatic halt clearing. Leave the independent old paper sentinel alone.

## Immutable originals and append-only expansion

The original **five MD registrations, sha files, registry/manifest.json, league.py and strategies.py are byte-for-byte untouched**. Their hashes and code still verify each tick. `league_v2.py` calls the frozen legacy implementation for those five only. All pre-existing capital, positions, events, cursors and hashes are preserved. Original failed historical tests stay failed. The original production paper config, empty PASS allowlist and sentinel are unchanged.

The95 new registrations have separate `registry/extension-v2.json`, its SHA, and one MD+SHA per id. `register_v2.py` refuses overwrite. On first successful v2 tick the engine appends new100-USDC books and pins the extension digest atomically in the SAME authoritative state. No new book has historical performance. Changing any frozen rule/code/dependency requires new ids/prospective registration, never a score-improving edit. The original receipt remains `registration-receipt.json`; extension receipt is `extension-registration-receipt.json`. `backups/extension-v2/` contains the untouched originals, migration-time state/cache and complete original-registry hash inventory.

### First15 core books

| ID | Lane / frozen family |
|---|---|
| s1-donchian40-ablation-v1 | original4h Donchian40/EMA200/ATR/funding; prior NO EDGE |
| s2-bb40-ema200-ablation-v1 | original4h BB40/EMA200 step2, not final filtered version |
| s4-ewmac-riskcap-noadd-ablation-v1 | original daily EWMAC with explicit new risk/no-add overlay |
| r1-trend-rsi-pullback-market-lane-v1 | original desk-defined4h RSI/trend lane; not an independently submitted bot strategy |
| b0-btc-1x-hold-control-v1 | original initial1x fixed-unit BTC PERP hold; NONTRADABLE risk exception |
| f1-vwap5m-v1 | rolling4h VWAP/ATR extreme cross mean reversion,1h time exit |
| f2-asia15m-v1 | MYT08:00–12:00 range, breakouts12:00–16:00; exit inside range/session end |
| f3-rsi2-5m-v1 | RSI2 extreme fade5/95 with EMA200 direction filter;1h cap |
| f4-ema15m-v1 | EMA9/21 cross;12h cap |
| f5-squeeze1m-v1 | Bollinger20 prior squeeze + band breakout,30m cap |
| l1-supertrend1h-v1 | ATR10 x3 Supertrend direction flip;7day cap |
| l2-macd4h-v1 | MACD12/26/9 trend cross;14day cap |
| l3-funding1h-v1 | real trailing8h funding +/-0.005%/hour contrarian, EMA20 filter;72h cap |
| l4-weekly1d-v1 | rolling7day high/low breakout, prior3day opposite exit;28day cap |
| c1-random15m-v1 | fixed seeded hash draw,1/12 chance per coin/bar, random side,1% stop,4h cap |

The85 fixed-grid books are9 families x3 individual assets x3 frozen parameter sets =81, plus4 fast-family all-assets parameter1 variants. Exact ids/parameters are in `strategies_v2.entries()` and the extension manifest: `g-<family>-<btc|eth|sol>-p<0|1|2>-v1`, plus `g-<vwap|asia|rsi2|ema>-all-p1-v1`. Base and grid overlap intentionally; correlated/duplicate choices still count as trials. No selection/pruning or daily random retuning. Public L2/trade imbalance was omitted: minute polling cannot substantiate a microsecond/order-flow edge, and more streams are unnecessary for these100 books.

## Execution, risk, costs and latency

- Existing5 keep frozen execution. New books use closed1m/5m/15m/1h/4h/1d bars, actual last `allMids` observed AFTER data collection. First observed entry within45s of a1m boundary or90s of other new boundaries; missed signals expire. Never fill a signal at an unseen old candle open. A60s poller is not HFT and can miss a1m window.
- All new entries: adverse2bp observed-mid proxy PLUS taker0.045%; signal/time exits2bp; stops/halt/risk exits5bp. Maker0.015% is documented but **never charged without a real resting-limit fill model**; there are no maker books. Proxy prices are not exchange fills, depth/queue/partial fills/liquidations are not modelled.
- Per book <=0.5% intended risk including entry/exit fees,5bp stop stress and24h funding reserve; <=2% open risk, <=3x,20% margin headroom, $10 minimum and downward lot rounding. Max2 positions absolute but existing stricter major-cluster cap means **only1 position/book**. BTC/ETH/SOL only. Fixed mandatory stop=max(0.5%,2ATR14/close), abstain above4.5%, random fixed1%. No adds.
- Daily MYT -2% halt flattens and remains blocked across midnight until owner reset. The halt is not a maximum-loss guarantee; gaps/funding may exceed the sizing estimate. Actual accrued costs/remaining stop budget are checked at observed ticks. BTC hold alone remains an explicitly NONTRADABLE stop/halt/risk exception, not permission to loosen strategy or live risk.
- Every real settled hourly `fundingHistory` rate is replayed; positive long debit/short credit. No zero fill or current-rate smear. USD cashflows use settlement-minute OPEN PRICE PROXY, not historical oracle: estimated, not observed exchange payments. Missing/duplicate data blocks the tick.

### Downtime safety is simulation, not real protection

Replay every missed closed1m candle before new decisions. Touched virtual stop fills at trigger+5bp adverse; opening gap through trigger at that OPEN+5bp. Entry-minute range touch is conservative and flagged ambiguous. Store original minute, actual replay observation and gap flag; candles cannot resolve exact intrabar path. >5000-minute API retention (~3d11h20m) or any missing minute => UNRESOLVED_REPLAY_GAP, no cursor skip/new entry; recover only from genuine retained data.

**New books do not receive unseen historical signal/time/risk-budget exits.** Only explicitly candle-reconstructed virtual STOP assumptions are retrospective fills. New-book replayed daily-halt threshold latches immediately but flattening waits for the next actual observed quote. Time exits log actual observation delay. Existing five retain their original frozen replay behavior. Virtual replay is NOT exchange-side stop protection or guaranteed production uptime.

## Evidence gates and luck controls

`leaderboard.md`: separate control, fast and slow ranked tables; net MTM/realized trade statistics, win%, PF, MaxDD%, expectancy, fees/funding, same-start excess return vs BOTH controls, DSR trial count/probability/full-day observations, fresh OOS and gate. Under30 completed trades always NOT SIGNIFICANT;30+ is not PASS. Net MTM includes paid fees/funding/open PnL, not future exit. Gate comparisons deduct indicative taker+2bp liquidation cost and normalize both controls to a common comparison start.

**Known trial count409 =309 prior backtests + all100 league books, including controls.** Unknown external source searches cannot be audited;409 is the recorded desk total, not a worldwide-history guarantee. DSR is a Bailey-style skew/kurtosis-adjusted normal probability of daily Sharpe exceeding the expected best ofN trials, using cross-book Sharpe dispersion with1/sqrt(n-1) floor. At least8 completed MYT daily returns, initial partial day excluded, missing full days never zero-filled. Correlated grid/time-series and normal approximations limit this statistic; it is not proof. DSR is unavailable at launch, not invented as zero or passed.

Fresh-period sequence, frozen before performance:
1. >=30 closed trades, positive costed comparison return, beats BTC AND random controls, DSR>0.95, not halted => **FLAGGED**, not candidate.
2. On a FOLLOWING MYT day, wait until that book is flat, then pin fresh OOS equity/control baselines. No discovery trade straddles the boundary.
3. First OOS endpoint after >=7 elapsed days OR >=30 NEW closed trades for fast books. Must be positive net after costs AND beat both controls within OOS. First PASS/FAIL freezes; cannot extend a failed period until lucky.
4. With all current initial gates still passing: **CANDIDATE_REVIEW_ONLY**. Parent forwards evidence for Risk Manager review, not an automatic message/order/promotion. Desk100+trade/independent validation requirements and exact owner approval remain separate.

A15Nov checkpoint cannot manufacture8 full days or OOS evidence. No profitable candidate/strategy claim at startup. News/research remains in the parent daily workflow; this daemon does not fetch news, call bots, learn/retune or send messages.

## Resource controls and retained artifacts

One60s loop;6 candle intervals cached per coin, no per-book API calls. High-timeframe fetch only after close;1m fetched once/coin/tick for replay and all fast books.1m finite squeeze cache512, other EMA seeds append-only. Family+parameters+coin+boundary signals cached across books. Collector refuses estimated weight>=750 before further calls; official IP budget1200/min, shared with other agents. Errors/timeouts back off via supervisor, no per-book retries. New valuation ledger events sampled15min while risk/equity checks and book state remain minute cadence; original five retain minute events.

`last_tick.json`/heartbeat show API request counts/types, estimated weight, network wall time, CPU seconds and peak RSS. Source responses and all losses retained. Full-state/ledger rewrites and append-only slow caches grow with time: inspect disk/CPU after a week; short launch measurements do not prove long-run capacity. Never silently remove poor books to reduce load. If the workload exceeds budget, stop/limit new risk and report rather than claim100 healthy books.

Official rate-limit reference checked11Nov2026: https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/rate-limits-and-user-limits . Expected minute average roughly100–130 weight before other agents; startup/hourly/4h/day bursts are higher. Use measured receipts, not this estimate, for observed load. No perpetual uptime guarantee.


## 16 spot books (v3 append-only)

Owner request 11 Nov 2026 16:53 Asia/Kuala_Lumpur: paper-trade spot on BTC, ETH, SOL and HYPE with 16.24 USDC and no liquidation. Frozen v1/v2 files, the original 100 books and their capital/history are unchanged. `league_v3.py` is an append-only layer; existing books still run through their frozen implementations.

- 16 independent books start at **16.24 virtual USDC** (not 100): 4 buy-and-hold controls plus EMA 15m, RSI14 pullback 1h and Donchian 20/10 5m, one each on UBTC/USDC (`@142`), UETH/USDC (`@151`), USOL/USDC (`@156`) and HYPE/USDC (`@107`). All four are live Hyperliquid spot pairs verified from public `spotMeta` / `spotMetaAndAssetCtxs` / `allMids` / `l2Book`; none uses a perp-mid proxy.
- Long only, 1x, no leverage, no shorting, no funding, all-in cash sizing, $10 minimum, mandatory stops on research books (hold controls have no stop or daily-halt flatten). Daily MYT -2% halt still applies to research books.
- Costs: official tier-0 spot taker **0.070%** plus the more adverse of a 2bp mid floor and an L2 notional walk. Maker 0.040% is documented and never assumed. Source: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees retrieved 11 Nov 2026 (Asia/Kuala_Lumpur).
- Same promotion bar: >=30 closed trades, beat the BTC-perp hold and random-entry controls after costs, DSR probability >0.95, then a fresh out-of-sample window of >=7 days (or >=30 new trades for spot_fast). **Nothing auto-promotes.** Known DSR trial count is now **425**.
- Daily routine: `./start.sh` then `./status.sh` (default compact; `--full` includes the new spot tables). An **Early read (not evidence)** section ranks fast/spot_fast books with >=10 closed trades by trade count then net MTM after costs. It is not significance, not a PASS, and does not change the promotion bar. Do not compare raw Net MTM USDC across the 100-USDC and 16.24-USDC tables.

desk trial total: see knowledge/trial-ledger.md (561 as of 2026-11-12)
