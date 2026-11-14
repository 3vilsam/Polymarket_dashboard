# g-vwap-btc-p1-v1

Registered UTC: 2026-11-11T06:02:16.937Z

## Frozen specification

```json
{
  "coins": [
    "BTC"
  ],
  "hold_ms": 3600000,
  "id": "g-vwap-btc-p1-v1",
  "interval": 300000,
  "kind": "vwap",
  "lane": "fast",
  "owner": "Prospective fixed grid; correlated trials",
  "params": {
    "threshold": 1.5,
    "window": 24
  }
}
```

Rolling VWAP=sum(typical_price*base_volume)/sum(base_volume), typical=(H+L+C)/3. Long z=(C-VWAP)/ATR14 crosses below -threshold; short crosses above +threshold. Exit on VWAP recross. Prior z uses prior rolling VWAP and ATR.

## Frozen common rules for this prospective extension
- PAPER only, public Hyperliquid mainnet /info reads only, no wallet/private endpoint/key/order/signing/testnet/exchange writes. These are desk-defined standard-family experiments at the owner's request, not independently supplied or proven bot strategies. No optimized parameter choice or return claim. All variants, duplicates/correlations and losses retained.
- Each book starts100 virtual USDC independently at its first live tick; BTC/ETH/SOL perps only, restricted further by registered coins. Conflict order BTC,ETH,SOL. Max2 positions absolute, stricter existing major-cluster limit1. One position per coin, no adds. <=0.5% intended risk including fees, 5bp stop slippage and24h funding reserve(max(current adverse funding,0.0000125/h)). Round DOWN to szDecimals; never round up to $10 minimum. <=2% open risk, <=3x leverage and20% margin headroom. Stop distance=max(0.5%,2*arithmeticATR14/closed close), abstain if >4.5%; random alone fixed1%. Stops fixed relative to actual entry fill.
- Signals use fully closed UTC bars only. Initial250 bars seed each new interval; existing710x4h/250xdaily seed retained. EMA/EWM adjust=False, first value/difference seed. New5m/15m/1h caches append only, no rolling EMA reseed. The1m squeeze uses finite rolling memory <=132 bars so cache retains512 closed1m bars. Arithmetic ATR14=rolling mean max(H-L,abs(H-prevC),abs(L-prevC)); first TR=H-L. All prices/volume must be real observations, missing data refuses the tick. Initial old signals do not produce entries outside their window.
- One shared60-second collector loop and per-tick cached family/parameter/coin/boundary signals. Never per-book API calls. Cache new higher-timeframe candles only at their next close. Endpoint allowlist allMids,metaAndAssetCtxs,candleSnapshot,fundingHistory,l2Book. Per-collector budget750 estimated request weight; bounded HTTP timeouts/retry, supervisor backoff on errors including429. Shared-IP traffic from other agents is outside this budget. Reject collection>60s or crossing a minute; no stale/hindsight entry. Entry time uses actual receipt of last allMids AFTER candle/funding reads. No claim of high-frequency/tick execution.
- New books always market-style observed-mid +2bp adverse entry, -/+2bp adverse observed signal/time exit, +5bp adverse stop/halt/risk exit, PLUS taker0.045% each fill. Maker0.015% documented but NEVER used without resting limit/queue evidence; no such maker books here. No historical bar-open signal/target/time fills. 1m entries within45seconds of bar close; other new signals within90seconds. Missed entries logged, never retrospectively entered. Non-stop exits/timeouts during downtime execute only at the next actual observed price and record delay. No sub-minute edge can be inferred from a60second poller.
- Real settled hourly fundingHistory rates only, no current-rate smear or invented zeros. Every held settlement is replayed chronologically; long pays positive. Dollar cashflow=-direction*units*actual_rate*settlement-minute-open PRICE PROXY, not historical oracle; simulated dollar costs are estimates. Missing/duplicate funding fails the atomic tick. Current accrued costs/remaining risk checked at actual observation; no unseen historical risk-budget fill is fabricated.
- Mandatory virtual stops: replay every missed closed1m candle before decisions. Touch=trigger+5bp adverse; gap through trigger=bar open+5bp adverse. Entry-minute touch conservatively stopped and flagged ambiguous. Record original minute and replay observation, no claim exact intrabar timing. These explicit candle-reconstructed STOP assumptions are the only new-book retrospective fills, NOT real exchange protection. >5000-minute retention or any missing replay minute blocks all new entries without advancing cursor. Never force-skip. A replayed -2% MYT day-equity threshold latches no-new-risk and flattens at NEXT actual observed quote, not an unseen close. Halt stays across midnight until owner reset. Stops still replay for every book.
- One atomic fsynced authoritative all-book state + exported ledgers, single engine/supervisor locks. Original five registration MD/sha files, manifest and league.py/strategies.py stay byte-identical and run through their original frozen implementation. This append-only extension has a separate manifest pinned in state; changes require new ids and new prospective registration. No capital reset.
- Evaluation: report completed episodes, win%, PF, expectancy, net MTM after paid fees/funding and max equity DD%. Under30 closed trades NOT SIGNIFICANT; >=30 still unproven. BTC hold and random-entry controls both shown. Gate comparisons use common-start normalized liquidation-equity returns (deduct estimated exit taker+2bp), not mismatched inception PnL. MTM leaderboard itself does not deduct hypothetical exit. BTC alone retains its explicit original NONTRADABLE no-stop/risk exception.
- Known total DSR trials=309 previous backtests + EVERY league book including both controls:409 at100 books. Do not reset count, hide failed variants or treat a rank as evidence. External source searches are unknown;409 is the known auditable total, not proof of complete worldwide search count. DSR is a Bailey-style probability using unannualized completed MYT daily returns, sample SD, population skew/full kurtosis, normal expected max Sharpe for N trials with Euler gamma, cross-book Sharpe sample SD with minimum1/sqrt(n-1) sampling-noise floor, >=8 complete daily observations. Initial partial day excluded; missing full days not zero-filled. Serial and cross-book correlation make this an approximate diagnostic, not proof; no guaranteed significance.
- Fresh-period gate: first require >=30 trades, positive costed return, beat both controls, DSR>0.95 and no halt. Only then flag discovery result. Start OOS on a FOLLOWING MYT day at first FLAT-book actual tick, so no discovery episode overlaps. OOS endpoint is first >=7 elapsed days OR >=30 newly closed trades if fast. Freeze first endpoint PASS/FAIL; never extend a losing OOS until it wins. Require positive costed OOS AND beat both controls within OOS. CANDIDATE_REVIEW_ONLY additionally requires current initial gates still pass. Parent must forward evidence to Risk Manager: no automatic messages, promotion, permission or trade. Nothing in league is Risk PASS. Independent100+trade review and exact owner trade approval remain separate desk requirements.
- Max holding times are configured per book and execute at first observable price after expiry; no fixed profit target. Stops and risk/halt exits override signal exits. First checkpoint15Nov is operational, never a profit deadline. No liquidation/queue/partial-fill/depth or true tick-path model. Virtual gap loss can exceed intended risk. No news-based unfrozen discretion or parameter retuning mid-run. Source/state archives grow; whole-box reboot still requires start.sh unless a separate routine restarts it.

## Extension implementation SHA256
- `league_v2.py`: `3c3f73a0bbf73d6c1916110e0800370fef74608b28beb4c9eee1b571699ccad4`
- `strategies_v2.py`: `2334f86247abae7b971fb11a95c064ced26ed6e2e7f905237e56eaf6967d582c`
- `evaluation_v2.py`: `af35bb00eff8b070bf1e3e66257cfb7a747f0015338b51d0bb41c2d3e0f3eac3`
- `register_v2.py`: `de63cbc951a4ae1eda13830e8e4e759c7217b721ede521fe5ce0ba503b023e3f`
