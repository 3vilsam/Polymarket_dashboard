# Append-only note: USOL/USDC spot books RETIRED_DATA_QUALITY

Recorded UTC: 2026-11-12T06:09:18.588Z. Decided by Skippy (desk coordinator) on 12 Nov 2026. Data-quality retirement, not a risk-limit change.

Books: sp-hold-usol-v1, sp-ema15m-usol-v1, sp-rsi1h-usol-v1, sp-donchian5m-usol-v1. Their original frozen rule files and sha256 are unchanged:
- `sp-hold-usol-v1`: `44b9bea590b5b50331ff5c52a4daa490fd124144efe02cbd0ee4116c97addc83`
- `sp-ema15m-usol-v1`: `c4e837f13551a4d5b22300670280d6d7e09397230cba2478ea151725fa26fda2`
- `sp-rsi1h-usol-v1`: `7857d3f0348dbe54e8d81f60999e4fc82fee86d22107b69183a92397ad0ca1db`
- `sp-donchian5m-usol-v1`: `7250eaa1556a8a0ff450d4f7ed52ac9db27b08f0514bbaf96da5d51bdea160c2`

Reason: USOL/USDC spot pair too thin: Hyperliquid omits 1m candles for no-trade minutes, so the frozen 512-bar continuity check fails for hours at a time, and real fills on a pair this thin would also be poor.

Effect (from the first engine tick after this note; not retroactive):
1. Status RETIRED_DATA_QUALITY. The books stop ticking: no new signals, entries, exits or stop checks.
2. All history (events, ledgers, closed trades, evaluation) is preserved, and the books stay in the league state and in the DSR trial count (125 books, 434 known trials).
3. Any open virtual position is closed once at the last valid observed USOL/USDC mid from the last successful engine tick (minus 2bp, plus the 0.070% spot taker fee), reason `retired_data_quality_close_at_last_valid_mark`. If that mark is older than 5 minutes or the book was skipped by data-isolation v1, the position is marked UNRESOLVED instead; no price is invented.
4. USOL is removed from the engine and warm-up data checks. SOL perp books (BTC/ETH/SOL perps) are unaffected.
5. Reinstating USOL needs a new, separately registered decision with new book ids.
