# Paper test: volatility-scaled stop / sizing flag (Carver lesson)
Written UTC: 2026-11-12T16:17:14Z. Reviewer: Risk Manager. PAPER / BACKTEST ONLY. No keys, orders, limit changes or registry edits.
Applied lesson: Carver (2020-02-06) — set the stop from volatility, then size the position; a stop inside ordinary noise is the thing to flag. Companion map: Carver (2018-12-03), daily SD ≈ 0.875 × ATR.

## Method
- Script: `/workspace/trading-desk/strategy-lab/risk-tools/vol_scaled_stop_check.py` (sha256 `973ef28372c1bff98493435d2be1f75074ea099aab5b82056e5da51766a229f9`).
- Command: `python3 /workspace/trading-desk/strategy-lab/risk-tools/vol_scaled_stop_check.py`
- State: `league_state.json` last_tick 2026-11-12T16:15:41.715Z, plus each book's `ledger.jsonl` (closed_trades in state omit stop and size).
- Candles: Hyperliquid mainnet public `POST https://api.hyperliquid.xyz/info` `candleSnapshot`, interval 1h, start 2026-10-01T00:00:00Z. Fetch window 2026-11-12T16:16:08.622Z–16:16:29.142Z. BTC, ETH, SOL, HYPE: 1025 bars each, no fetch errors. UBTC/UETH/USOL mapped to the underlying perp tape (documented in the JSON sidecar).
- ATR14: arithmetic SMA of true range, first TR = H−L (same convention as the league). Only bars with close time `T` strictly before `entry_ms` — no look-ahead.
- Flag A (`tight_stop`): stop distance < 1.0 × hourly ATR14.
- Flag B (`vol_target`): implied annualised position vol = (notional / equity_at_entry) × (0.875 × ATR14 / entry) × sqrt(24×365) > 25%. The 25% line is a Carver-style account vol target used as a research threshold, not a v1 limit. 24×365 is used because these markets trade continuously.
- Sidecar: `strategy-lab/paper-league/reviews/risk-lesson-test-2026-11-13.json`.

## Results
161 paper trades in the snapshot (22 open, 139 closed). 156 had a stop and enough pre-entry bars to score Flag A. All 161 could be scored on Flag B (the five unstopped hold controls were assessed on vol only).

- Flag A, tight stop: **130 / 156** (83.3%) would have been flagged. 10 of those were still open; 120 were already closed.
- Flag B, 25% position vol: **155 / 161** would have been flagged. That threshold does not separate these books (see failure note).
- Either flag: 155 trades. Both flags clear: 6 trades only.
- Median stop / hourly ATR14 among scored stopped trades: 0.807 (min 0.477, max 2.9997). Median implied position vol: 40.95% (min 12.60%, max 93.08%).
- 151 of 156 stopped trades had a stop tighter than 1% of entry.

Closed-trade outcomes (verified `pnl_net` only; this is a description of this sample, not a performance proof):

| Set | N with pnl | Wins | Losses | Stop exits | Sum pnl (USDT) | Mean pnl |
|---|---|---|---|---|---|---|
| Flag A tight, closed | 120 | 33 | 87 | 33 | −17.393857 | −0.144949 |
| Flag B vol, closed | 136 | 39 | 97 | 38 | −19.749969 | −0.145220 |
| Neither flag, closed | 3 | 3 | 0 | 0 | +1.384708 | +0.461569 |
| All closed | 139 | 42 | 97 | 38 | −18.365261 | −0.132124 |

The three closed trades that cleared both flags were c1-random15m-v1 P000002 (ETH short, +0.848969), g-vwap-btc-p1-v1 P000006 (BTC long, +0.267869) and g-vwap-all-p1-v1 P000009 (same BTC long construction, +0.267869). N=3 is too small to treat as evidence that the flag has edge.

Tonight's reviewed SOL short, n1-tsmom-mh1h-v1 P000001, cleared both flags: stop / hourly ATR14 = 2.9997 (the book's 3×ATR14 rule), implied position vol = 12.60% at 0.1828× leverage. The other two TREND SOL shorts (l1-supertrend1h-v1 and g-supertrend-sol-p0-v1) also cleared both (stop / ATR = 2.0006, position vol 18.31%).

Unstopped holds, Flag B only (all would be flagged): b0-btc-1x-hold-control-v1, sp-hold-ubtc-v1, sp-hold-ueth-v1, sp-hold-usol-v1, sp-hold-hype-v1. Flag A is not defined without a stop.

## Honest failure / calibration note
The script ran cleanly (public candles returned, no look-ahead, no invented fills). **Flag B at 25% annualised position vol fails as a useful additional gate on this desk.** Instrument vol on these coins is already ~42–96% annualised under the Carver ATR map, so almost any v1-sized crypto book with a tight stop (and therefore a larger notional) prints well above 25%. 155 of 161 trades flag it. I am not treating Flag B as a reason to reject n1 or to change limits. A higher research threshold, or a comparison to the book's own intended hold, would be needed before this flag is worth putting on a ticket. Flag A (stop inside 1× hourly ATR) is the part of the test that actually moves: it flags the 0.5–1% stops that dominate the league and leaves the 2–3×ATR trend stops alone.

This test does not change v1 and is not a live reject rule.

Inputs: league_state.json last_tick 2026-11-12T16:15:41.715Z; book ledgers; HL mainnet public candleSnapshot 1h from 2026-10-01, fetched 2026-11-12T16:16:08Z–16:16:29Z; Carver 2020-02-06 and 2018-12-03.
Method: python3 /workspace/trading-desk/strategy-lab/risk-tools/vol_scaled_stop_check.py (vol_scaled_stop_check.py sha256 973ef28372c1bff98493435d2be1f75074ea099aab5b82056e5da51766a229f9).
Bot: Risk Manager
