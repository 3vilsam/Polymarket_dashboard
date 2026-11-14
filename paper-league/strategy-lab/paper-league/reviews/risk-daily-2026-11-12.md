# Daily paper-league risk check — 2026-11-12
Written UTC: 2026-11-12T11:59:14.727Z (tick 164; 19:59:14+08 Asia/Kuala_Lumpur). Reviewer: Risk Manager. PAPER ONLY. I changed no keys, orders, limits or registry files.
Basis: `/workspace/trading-desk/risk-limits.md` v1. Snapshot: `league_state.json` + `last_tick.json` (same tick). SOD = MYT midnight rollover 2026-11-11T16:00:00Z. Spot addendum is a DRAFT, not used. HYPE is outside v1 (research only). Books labelled NON_V1_RESEARCH are monitored, not re-judged.

## 1. Open positions (8 books) vs v1

| Book | Side/coin | Stop | Stop % | Risk at entry | Lev | Ntl USD | Day vs SOD | Verdict | Failed gate |
|---|---|---|---|---|---|---|---|---|---|
| l1-supertrend1h-v1 | short SOL | 84.2626 | 1.865% | 0.4886 (0.489%) | 0.24× | 23.99 | +0.076% | **PASS** | — |
| g-supertrend-sol-p0-v1 | short SOL (same fill as l1) | 84.2626 | 1.865% | 0.4886 (0.489%) | 0.24× | 23.99 | +0.076% | **PASS** | — |
| n1-tsmom-mh1h-v1 | short SOL | 85.2013 | 2.524% | 0.4930 (0.492%) | 0.18× | 18.28 | +0.142% | **PASS** | — |
| c1-random15m-v1 | short ETH | 2065.4913 | 1.000% | 0.4981 (0.496%) | 0.42× | 42.54 | +0.439% | **PASS** | — |
| b0-btc-1x-hold-control-v1 | long BTC | **none** | — | unprotected mark ntl 98.71 | 1.01× | 99.96 | −1.438% | **FLAG** (documented control) | no stop; full residual risk; engine exempts `benchmark` from −2% halt |
| sp-hold-ubtc-v1 | long UBTC spot | **none** | — | unprotected ~16.03 | 1× all-in | 16.20 | −1.430% | **FLAG** | no stop; all-in; spot/UBTC not in v1; not labelled NON_V1_RESEARCH |
| sp-hold-ueth-v1 | long UETH spot | **none** | — | unprotected ~15.97 | 1× all-in | 16.23 | **−2.472%** | **FLAG** | same, plus −2% daily halt hit and `halted=False` (`spot_hold` exempt from halt/flatten in league_v3) |
| sp-hold-hype-v1 | long HYPE spot | **none** | — | unprotected ~15.56 | 1× all-in | 15.78 | **−3.370%** | **FLAG** | same, plus HYPE research-only; halt hit, not latched |

Marks: BTC 72897.5, ETH 2021.25, SOL 82.4225, UBTC 72856.5, UETH 2021.85, HYPE 70.7475. Every book has ≤1 position (v1 max 2). Open v1 perps: cost-inclusive risk ≤0.5% of equity, stop in 0.5–4.5%, ntl ≥10, lev ≤3×, sizes floored. Total open risk on each of those books is the single position (~0.49%), under the 2% cap.

## 2. Drawdown (all 125 books)

- No book is at or past −10% from peak. Worst current DD: sp-hold-hype 4.556% (max 4.909%); sp-hold-ueth 3.684%; retired sp-hold-usol 3.297%; b0 2.436%; sp-hold-ubtc 2.430%.
- Daily halt (−2% of SOD equity), hit and **not latched**:
  - sp-hold-hype-v1: eq 16.013829 / SOD 16.572299 = **−3.370%**
  - sp-hold-ueth-v1: eq 15.974967 / SOD 16.379842 = **−2.472%**
  - sp-hold-usol-v1 (RETIRED_DATA_QUALITY, flat since 2026-11-12T06:11:03.778Z): eq 16.223371 / SOD 16.590001 = **−2.210%**
  Engine code (`league.py` benchmark early-return; `league_v3.py` `kind!='spot_hold'`) exempts these controls from halt and flatten. That is a written paper-engine exception, not an owner rewrite of risk-limits.md. v1 is not met.
- Closest v1-judged book: f5-squeeze1m-v1 eq 98.248971 / SOD 99.945603 = **−1.698%**, 0.302 USD (0.302 pp) above the halt line; `halted=False` correctly. b0 −1.438%; sp-hold-ubtc −1.430%. 0 books currently `halted`.

## 3. Cluster

Majors + HYPE treated as one cluster (UBTC=BTC, UETH=ETH). Books open in the same direction:

- **Long 4:** b0 BTC, sp-hold-ubtc, sp-hold-ueth, sp-hold-hype
- **Short 4:** l1 SOL, g-supertrend-sol-p0 SOL, n1 SOL, c1-random ETH

**Pile-up (3+ same direction) both ways.** Per-book cluster cap of 1 is held (19 historical `major_cluster_max_1` rejects; no book has 2 positions). This is a league-evidence warning, not a single-account breach: these are separate virtual books.

Cluster tags (one effective trial each for promotion): BTC_FRI21 = 4 books, none open; SHOCKREV = 2, none open; TREND = 53, **3 open, all short SOL** (l1, g-supertrend-sol-p0, n1). Count those three as one trial, not independent confirmation.

## 4. Last 24h (from 2026-11-11T11:59:14Z)

79 entries, 78 exits, 48 books traded. Exit reasons: signal_or_time 51, stop 17, observed_time 9, retired_data_quality 1. Closed pnl_net sum −9.947 across the 78 trades. Worst v1-perp closed trade −0.483 USD (under the 0.50 cap on a 100 book).

- Perp entries: stop present and inside 0.5–4.5%; cost-inclusive risk ≤ the live `risk_budget` (0.5% of equity at entry). Four fills printed 0.5004–0.5011 USD vs 0.5000 on a 100 start; all were inside a larger live budget (equity up). Ntl ≥10, lev ≤3×, sizes rounded down. No missing-stop entries except the already-open hold controls (no new hold entries in the window except the prior open).
- **FLAG — v3 spot donchian (all-in, not labelled NON_V1_RESEARCH):**
  - sp-donchian5m-usol-v1: stop loss −0.1128 vs 0.5% cap 0.0812 (1.39×)
  - sp-donchian5m-ueth-v1: stop loss −0.1109 vs 0.0812 (1.37×)
  - sp-donchian5m-hype-v1: stop loss −0.1086 vs 0.0812 (1.34×); HYPE research-only
  Same construction as the already-FLAG'd sp4 books: full-cash ~16 USD, 0.5% stop + ~0.21% costs ≈ 0.68% equity.

## 5. New registry books since last Risk reviews

None. Newest trading books remain the v4 set (registered 2026-11-12T05:47Z). labels-v2 (06:31:50Z) and labels-v3 (06:42:12Z) are research tags only (ABLATION_FAIL); no book added. Standing paper verdicts unchanged: n1–n7 **PASS** (paper); sp4-shockrev1h-ubtc-v1 and sp4-utc21-ubtc-v1 **FLAG** / NON_V1_RESEARCH, not re-judged (flat, 0 trades). C1/C2 are not in this league.

## Correction

1. Label the remaining v3 all-in spot books (holds, donchian, and any ema/rsi that use the same cash sizing) NON_V1_RESEARCH, **or** re-register with v1 sizing: qty = floor(0.005·eq / (stop+costs)), reject ntl <10. At 16.24 equity a 0.5% cap is untradeable once the stop is ≳0.62%.
2. If unstopped hold controls must keep running as benchmarks, the owner has to write that exemption into risk-limits.md from a trusted device. I will not invent it. Until then they FAIL v1 and can print daily losses past −2% with no latch.
3. Do not promote more than one TREND book, or more than one same-direction majors position, into a single live account. Tags count as one trial.

PASS is paper-gate compliance only. It is not owner authorisation and not a sized live ticket.
