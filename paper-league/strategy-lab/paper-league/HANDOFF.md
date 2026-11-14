# Parent handoff: 100-book PAPER expansion

## Completed design / operational facts
- 100 independent100-virtual-USDC books:54 fast,44 slow,2 controls (BTC hold + random entry).98 research books are correlated/unvalidated, NOT98 proven strategies.95 added,5 existing preserved.
- The original five registrations/sha files, manifest, league.py, strategies.py and original production simulator/config/empty PASS gate are byte-identical. Frozen legacy code runs those5 only; separate league_v2.py/strategies_v2.py/evaluation_v2.py plus append-only extension manifest implement95 new books. All new rules frozen before first live tick. No keys, orders, accounts, signing, testnet or exchange writes.
- 83/83 offline tests pass, including original46,100-book isolation, all95 stop replay over10h, risk/fees, causal bars/latency, shared caches, DSR/fresh OOS and tamper fail-closed. Test record tests/extension-results.txt. Bytecode + shell syntax passed.
- Existing start.sh / supervisor remains singleton; now targets league_v2.py. status.sh defaults to concise health/load/top rows to limit routine context, --full reads100-row leaderboard. No LLM calls per tick.

## Owner steering implemented
- First15 core books: original5 plus VWAP5m,Asia15m,RSI2-5m,EMA15m,squeeze1m,Supertrend1h,MACD4h,funding1h,weekly1d,random15m.
- 85 frozen grid variants:9 families x3 individual assets x3 parameter sets=81 plus4 fast all-asset parameter1 variants. No after-results parameter selection. Full95 ids/SHA256 in NEW-BOOK-HASHES.md and registry/extension-v2.json. Some correlated/duplicate rules intentionally counted, not hidden.
- DSR trial count409=309 prior + EVERY100 league book, controls included. Actual DSR probability uses completed MYT daily returns (>=8), skew/kurtosis and expected max Sharpe, cross-book SR dispersion with sampling-error floor. Correlated/non-iid assumptions mean diagnostic approximation, not proof; unavailable at launch. External source trials remain unknown, so409 is the auditable desk count.
- >=30 completed trades + positive costed return + beats BOTH BTC/random + DSR>.95 + no halt -> FLAGGED only. Following MYT day and FLAT book starts non-overlapping OOS. First endpoint >=7 elapsed days OR >=30 NEW closed fast-book trades; require positive OOS and beat BOTH controls, freeze first PASS/FAIL. Only current gates plus OOS PASS give CANDIDATE_REVIEW_ONLY. Never automatically promote/trade/send.
- Review columns are explicit on fast/slow/control leaderboard: net/costs/DD/expectancy, both control excess returns, DSR trials/probability/full days, fresh OOS and gate. Every<30 row flagged NOT SIGNIFICANT.

## Required parent follow-up
1. Existing daily evidence/news routine should run start.sh then status.sh (compact default), inspect heartbeat ERROR/staleness>180s and load, then review leaderboard if needed. Whole-box reboot autostart remains absent: no cron/service installed. Routine or manual command must restart after reboot.
2. Do not tell owner each bot supplied/proved these strategies: these are desk-defined standard-family/grid experiments requested by owner; original failed historical tests remain failed.
3. If candidate_for_risk_review appears in a ledger / CANDIDATE_REVIEW_ONLY in status, parent sends full frozen rules, costed forward/OOS evidence and caveats to Risk Manager. This engine creates no outgoing messages/routines, and has no exchange execution path. Desk independent100+trade review/owner exact-ticket approval remain separate.
4. No promised winner by15Nov: eight FULL days plus following OOS cannot be fabricated in four days. Counts may differ across cadences and many wide-stop/$10-minimum signals can reject at100.
5. Keep news/research and bot ownership review in existing workflow, not mid-run retuning. Inspect disk/CPU in a week; losses and failed variants retained. Do not remove poor books to improve rank or reset equity/halt.

## Important limitations
- 60-second polling, not HFT.1m entries expire45s after close, other new entries90s; fills use actual post-collection mid+2bp adverse plus taker0.045%. All maker assumptions omitted (no resting-limit/queue evidence); maker0.015% merely documented.
- Only new-book virtual STOP reconstruction fills retrospectively (gap open/trigger+5bp); unseen signal/time/risk exits use next actually observed mid. Replayed daily-halt threshold latches then flattens at next observed quote. Original5 retain frozen older replay behavior. Never claim real exchange-side protection or exact stop fills.
- >5000-minute retained replay gap fails closed. Funding rates real, cash payments use settlement-minute open PRICE PROXY, not historical oracle. No tick path, partial-fill, liquidation or queue model.
- Existing stricter majors cluster cap1 applies, despite max2 position ceiling. Per-book0.5% cost-inclusive intended risk,2% total,3x,$10minimum,mandatory stops,-2% sticky MYT daily halt. BTC control alone retains explicit NONTRADABLE risk exception.
- Collector shares candles/signals, caches higher timeframes until next close. Per-collector estimated weight cap750 vs official shared-IP1200/min; other agents consume their own share. Startup can fail closed/retry if25s seed read crosses a minute. Such rejected reads do NOT create fake fills or reset state.
- Valuation ledger events every15min for new books, but minute risk/equity checks and exports; original5 minute events unchanged.1m finite squeeze cache512, other EMA caches append-only. Archives/state grow: launch CPU is not proof of indefinite capacity.

## Frozen core added ids / full SHA256
- `f1-vwap5m-v1`: `323d5941fd3373584b63b9601a481367b8a087e48de5390d8bd760269a56658c`
- `f2-asia15m-v1`: `4f8d220310240eae197319e5ac8df4575ef45cd00ef12f6c4c3deca001aee0f9`
- `f3-rsi2-5m-v1`: `bd5cec7b7dc088cefbee78a157195a1bbf3640d1a3a25825ef5d83039ac9c03a`
- `f4-ema15m-v1`: `bf67bc5d75f9cc08299e8221cad80287a36d30d34715147cf870ee9ea41a06fd`
- `f5-squeeze1m-v1`: `f1bac2bd9f5b8edf7a18fe04acb282329687ae29c8b7165e03e3e6a3099c34a1`
- `l1-supertrend1h-v1`: `e950da91f0ac71bf706e43a731435d549e2f6c511714e05452424e5a38783743`
- `l2-macd4h-v1`: `1025b2f77e2919350ee71493dc2abdc1694b1b94534f23c1f912d561e964605d`
- `l3-funding1h-v1`: `4d8d5c7c3cdc7cb5cb420e837cbcb300254d7f3f94df9edc8813ed3bfb98732e`
- `l4-weekly1d-v1`: `5156a4b0a83ffc4267a77bf03c96e9adf8965fe14db4bc7cb1ad945dfa85136c`
- `c1-random15m-v1`: `e263453d3b225c2f8d94c140019431d9f54467968404b7e3b84d7a3dec14ddd9`

Full85 grid ids/hashes: NEW-BOOK-HASHES.md.

Extension manifest SHA256: `409738ca51181d616afe106c921b7441d8cbc0624b38c2be30f03fbb4712ce92`.

Live startup/verification receipt appended below after successful commit.

## Verified live expansion receipt

- First committed100-book public tick: **2026-11-11T14:05:32+08:00 MYT**, league tick17. Source `sources/1794377105210.json.gz` SHA256 `fa7cc686bb0574f02c8dfb6c00fa00a000557c17d78e44a9b5f12b40f2f67451`. All95 new books100.000000 USDC,0 closed trades. Existing BTC control retains its original position; no invented profitable result/candidate.
- Supervisor PID**242037**, engine PID**243431** (`python3 -u league_v2.py`). Two initial startup attempts failed CLOSED at14:03:08 and14:04:04 MYT because seed collection crossed a minute boundary; supervisor retried. Neither failed attempt committed a new book/trade. Third attempt committed successfully.
- Cold-start observed load: 14public requests, estimated weight322 (<1200/min official shared-IP limit), 27.496s collection, 0.3735s CPU including100-book exports, peak RSS81.1MiB. 84shared unique signal computations, not per-book HTTP calls. Startup/import CPU is additional to tick CPU.
- `verification-v2.json`: original five event prefixes preserved, all100 exported states match authoritative state, cash reconciles to entry/exit fees+gross PnL+funding, all registration/code hashes pass, preregistration precedes first tick, public request allowlist verified. No hidden reset or duplicate position.
- Source/book/state/cache disk at first verification:592KiB/1.3MiB/384KiB/904KiB respectively, excluding backups. Long-run archive/event growth still needs weekly inspection.

## Warm/steady tick verification

- Tick19 at **2026-11-11T14:07:14+08:00 MYT**, all100 books committed; engine PID243431. 5public requests, estimated weight85 per ordinary minute, CPU0.1838s including exports (~0.306% of one core averaged over60s), wall9.326s including HTTP, peak RSS83.4MiB. Higher-timeframe/hourly refreshes cause larger bursts; shared-IP budget not reserved against other bots.
- Closed episodes across all books0; candidates0. DSR is unavailable, not passed. Regular1m work is9cached shared signal computations, not100 API loops. Capacity did not require reducing the100-book count at launch.
- DSR daily equity observations are minute-poll sampled first/last daily marks, not exact exchange-midnight or continuous tick returns; combined with serial/cross-book correlation, this remains approximate and requires forensic review, not a proof statistic.


## Spot expansion (v3) — parent handoff

- 16 spot-only paper books appended, each 16.24 virtual USDC. Long-only, 1x, no leverage, no funding, no liquidation. Frozen v1/v2 implementations and the running 100 perp books were not reset.
- Pairs (all real spot, not perp proxies): UBTC/USDC @142, UETH/USDC @151, USOL/USDC @156, HYPE/USDC @107. Families: buy-and-hold control, EMA 9/21 15m, RSI14 pullback 1h, Donchian 20/10 5m, one book per coin.
- Official tier-0 spot taker 0.070% / maker 0.040% from https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees retrieved 11 Nov 2026 (Asia/Kuala_Lumpur). Maker never assumed. Slippage = max(2bp adverse mid, L2 walk). $10 minimum.
- DSR trial count **425** = 409 + 16. Same promotion bar (>=30 trades, beat both controls, DSR>0.95, fresh OOS); nothing auto-promotes. `leaderboard.md` and `status.sh` also have an **Early read (not evidence)** section for fast books with >=10 closed trades; that is not a CANDIDATE and does not change the bar.
- Engine is `league_v3.py` under the same supervisor/start/status scripts. If the box reboots, the existing daily review routine must still call `start.sh` (no cron/service).
- A 16.24 all-in book with a 0.5–2% stop can trip the -2% daily halt after one or two losing trades. That is the existing desk halt applied honestly at this capital, not a loosened rule.
- First v3 live tick receipt: `first-live-tick-v3.json` and `verification-v3.json` after a successful commit.

## Verified live spot expansion receipt

- First committed 116-book public tick: **2026-11-11T17:16:59+08:00 Asia/Kuala_Lumpur**, league tick 55. All 16 new spot books started at 16.24 virtual USDC with 0 closed trades. The previous 100 perp books and their event prefixes were preserved from the tick-54 backup; no capital reset.
- Supervisor PID **283481**, engine PID **283487** (`python3 -u league_v3.py`). Earlier v3 start attempts failed closed (minute-boundary or HTTP 429) and did not commit new books or change the running 100-book state. The cache was pre-warmed with public spot candles, then the successful start began at 17:16:05 Asia/Kuala_Lumpur.
- First-tick observed load: 28 public requests (including `spotMetaAndAssetCtxs` and 4 spot `l2Book` reads in the 15-minute window), estimated weight 491, collection 54.21s (tight against the 60s / same-minute rule), CPU 0.51s including exports, peak RSS 89.6MiB. Subsequent ordinary ticks should be lighter because spot candles are cached.
- `verification-v3.json`: original and v2 event prefixes preserved, cash reconciles, all 116 books export, trial count 425, public allowlist includes `spotMetaAndAssetCtxs`, preregistration precedes the first v3 tick. Spot hold controls are 1x long on the real USDC pairs; research books are flat at activation. Candidates 0.
- Leaderboard and `status.sh` include an **Early read (not evidence)** section for fast/spot_fast books with >=10 closed trades. The CANDIDATE promotion bar is unchanged.

desk trial total: see knowledge/trial-ledger.md (561 as of 2026-11-12)
