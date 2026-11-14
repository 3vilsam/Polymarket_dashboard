# Registry labels v4 — 2026-11-12T12:05Z (Skippy, per Risk Manager daily FLAG, reviews/risk-daily-2026-11-12.md)
Append-only. Adds to labels-v1..v3; changes no engine code, sizing or limits.

1. NON_V1_RESEARCH, promotion-ineligible: every all-in spot book —
   sp-hold-{hype,ubtc,ueth,usol}-v1, sp-donchian5m-{hype,ubtc,ueth,usol}-v1, sp-ema15m-{hype,ubtc,ueth,usol}-v1, sp-rsi1h-{hype,ubtc,ueth,usol}-v1 (sp4-* already labelled in labels-v1).
   Reason: full-cash sizing above v1 0.5%/trade; spot/HYPE not named in v1; exchange spot stops unverified; spot_hold books carry no stop and are exempt from the -2% halt in the engine.
2. sp-hold-* are BENCHMARK CONTROLS only (buy-and-hold reference). Their -2% breaches are expected and are not v1 halt events.
3. sp-donchian5m 24h stop losses (0.109–0.113 vs 0.081 cap) are recorded as a spot-stop realism finding; no fix in place.
4. No formal halt exemption is granted. That needs an owner rewrite of risk-limits.md. Re-entry to eligibility requires new book ids with v1 sizing, or an owner-confirmed spot addendum.
