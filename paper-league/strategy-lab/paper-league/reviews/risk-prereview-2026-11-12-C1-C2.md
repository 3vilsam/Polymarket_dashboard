# Risk pre-review — C1, C2 (Market Analyst, frozen 2026-11-12) — written 2026-11-12T06:55Z — PAPER ONLY
Checked vs risk-limits.md v1 + Skippy's 25/50 bps stop-slip scoring rule. Hashes per research/frozen-2026-11-12/SHA256SUMS.

C1-tsmom28-btc-long-v1 | PASS (paper) | BTC perp long-only, 4.0% stop at entry, 1 position, ~0.11x, −15% book stop + −2% daily halt.
 Sizing at 25 bps stop slip: 4.0 + 0.09 + 0.02 + 0.25 + 0.15 funding = 4.51% → 0.50/0.0451 = 11.09 USD → 0.00015 BTC ≈ 11.03 USD @73,563 → risk 0.497 USD (0.497%). OK.
 At 50 bps: 4.76% × 11.03 = 0.525 USD (0.525%), 5% over cap in stress.
 Correction: size off the 25 bps figure (not the spec's 5 bps); abstain if floored notional <10 USD (0.00014 BTC ≈ 10.3 USD is the last valid step). Note: in-sample E[R] negative at 25/50 bps; PASS is a risk gate, not an edge view.
C2-carry-ubtc-btc-v1 | FLAG | Failed gates: (1) spot UBTC leg is outside v1 (BTC/ETH/SOL perps); (2) no exchange stop proven for spot; (3) wrapped-asset depeg tail: the 1% ratio exit is polled, so a UBTC depeg/halt can lose up to the full spot leg (~18.4 USD ≈ 18% of a 100 book) vs 0.5% cap; (4) needs a two-leg engine that doesn't exist; (5) post-hoc design, n=3.
 Correction: may run only as NON_V1_RESEARCH once a two-leg engine exists, with depeg loss reported separately; not promotable until the owner approves spot/wrapped assets in limits directly.
binance_sim v2: not reviewed (paused; rules.md/code not changed).

## Addendum 07:00Z (Skippy decisions 4–5)
C2 extra checks: funding sign: short perp RECEIVES when funding >0 and PAYS when <0; exit (b) uses a 168h mean <0, so up to a week of negative carry can bleed before exit (reserve 1.80% covers ~60d at the floor rate, fine). Perp leg: 18.4 USD at ≤3x needs ~6.1 USD margin; liquidation is roughly +30% away, and the +4.5% reduce-only stop fires first, so liquidation risk is low if the stop is live. Spot leg then sells at the next quote (unhedged gap = leg risk). Verdict unchanged: FLAG (spot/wrapped outside v1, depeg tail ~18% of book, spot stop unproven).

binance_sim v2 | FLAG | Binance spot BTC/ETH/SOL, 20 USDT, −8% stop. Risk/trade = 20 × (8% + 0.20% fees + 0.04% slip + 0.25% stop slip) = 1.70 USDT = 1.7% of a 100 book (v1 cap 0.5%). Up to 3 concurrent positions in one 0.9-correlated cluster → ~5.1% open (v1: 2% total, 1 cluster position). Same signal family as C1, which was rejected today.
 Correction: notional = 0.50 / 8.49% ≈ 5.9 USDT (check Binance min notional, 5 USDT on these pairs, unverified this turn); max 1 position across BTC/ETH/SOL; or don't adopt, since C1's evidence applies.
