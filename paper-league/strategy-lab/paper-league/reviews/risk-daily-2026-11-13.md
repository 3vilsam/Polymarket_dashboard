# Daily paper-league risk check — 2026-11-13
Written UTC: 2026-11-13T11:55:04.800Z (tick 315; 19:55:04+08 Asia/Kuala_Lumpur). Reviewer: Risk Manager. PAPER ONLY. I changed no keys, orders, limits or registry files.
Basis: `/workspace/trading-desk/risk-limits.md` v1. Snapshot: frozen `league_state.json` + `last_tick.json` (same tick). SOD = MYT midnight rollover 2026-11-12T16:00:00Z. Spot addendum is a DRAFT, not used. HYPE is outside v1 (research only). Books labelled NON_V1_RESEARCH (registry `labels-v1.json` for sp4-*; `labels-v4.md` for all-in spot holds/donchian/ema/rsi) are monitored, not re-judged. Engine `labels_v1` still lists only the two sp4 books as ineligible and leaves the labels-v4 set `promotion_eligible=True`; I treated the registry notes as the label, and I did not edit the registry or engine.

Marks: BTC 69335.5, ETH 1959.7, SOL 80.7015, UBTC 69325.5, UETH 1959.2, HYPE 73.6785. Heartbeat status ok, engine 8, no stale positions, UETH 24h fail rate 1.94%. 125 books (121 active, 4 USOL retired).

## 1. Open positions (13 books) vs v1

| Book | Side/coin | Stop | Stop % | Risk at entry | Lev | Ntl USD | Day vs SOD | Verdict | Failed gate |
|---|---|---|---|---|---|---|---|---|---|
| l1-supertrend1h-v1 | short SOL | 84.2626 | 1.865% | 0.4886 (0.489%) | 0.24× | 23.99 | +0.299% | **PASS** | — |
| g-supertrend-sol-p0-v1 | short SOL (same fill as l1) | 84.2626 | 1.865% | 0.4886 (0.489%) | 0.24× | 23.99 | +0.299% | **PASS** | — |
| n1-tsmom-mh1h-v1 | short SOL | 85.2013 | 2.524% | 0.4930 (0.493%) | 0.18× | 18.28 | +0.227% | **PASS** | — |
| c1-random15m-v1 | long SOL | 79.2500 | 1.000% | 0.4960 (0.492%) | 0.42× | 42.43 | +0.287% | **PASS** | — |
| g-ema-sol-p2-v1 | long SOL | 79.2648 | 0.981% | 0.4973 (0.497%) | 0.43× | 43.23 | +0.295% | **PASS** | — |
| g-vwap-sol-p1-v1 | short SOL | 81.0888 | 0.500% | 0.4923 (0.496%) | 0.74× | 73.42 | −0.475% | **PASS** | — |
| g-vwap-all-p1-v1 | short SOL | 81.0888 | 0.500% | 0.5031 (0.498%) | 0.74× | 75.04 | +1.325% | **PASS** | — |
| b0-btc-1x-hold-control-v1 | long BTC | **none** | — | unprotected mark ntl 93.89 | 1.00× | 99.96 | **−3.320%** | **FLAG** (documented control) | no stop; full residual risk; day past −2% and engine exempts `benchmark` from halt |
| sp-hold-ubtc-v1 | long UBTC spot | **none** | — | unprotected ~15.25 | 1× all-in | 16.20 | **−3.257%** | monitored, NON_V1_RESEARCH | no stop; all-in; spot/UBTC not in v1; halt not latched (`spot_hold` engine exemption) |
| sp-hold-ueth-v1 | long UETH spot | **none** | — | unprotected ~15.48 | 1× all-in | 16.23 | **−2.458%** | monitored, NON_V1_RESEARCH | same |
| sp-hold-hype-v1 | long HYPE spot | **none** | — | unprotected ~16.21 | 1× all-in | 15.78 | +3.221% | monitored, NON_V1_RESEARCH | same, plus HYPE research-only; not through −2% today |
| sp-donchian5m-ubtc-v1 | long UBTC spot | 68850.35 | 0.500% | all-in, no `risk_at_entry` | 0.98× | 15.92 | +0.063% | monitored, NON_V1_RESEARCH | full-cash sizing; stop loss + costs ~0.1018 vs 0.5% cap 0.0812 (1.25×) |
| sp-donchian5m-ueth-v1 | long UETH spot | 1935.6123 | 0.500% | all-in, no `risk_at_entry` | 1.00× | 15.95 | −0.353% | monitored, NON_V1_RESEARCH | same construction; implied cost-inclusive risk ~0.1020 vs cap 0.0799 (1.28×) |

Every book has ≤1 position (v1 max 2). Open v1 perps: cost-inclusive risk ≤0.5% of equity at entry, stop in 0.5–4.5%, ntl ≥10, lev ≤3×, sizes floored. g-vwap-all-p1 printed risk 0.5031 vs a 0.5000 cap on a 100 start, but it was inside the live budget 0.5052 (equity up; 0.498% of entry equity). Total open risk on each of those books is the single position (~0.49–0.50%), under the 2% cap. Ntl USD is entry notional; leverage is entry ntl / current equity except b0/spot holds, where lev is mark ntl / equity.

## 2. Drawdown (all 125 books)

- No book is at or past −10% from peak. Worst stored max DD: sp-hold-ueth 9.326% (current 6.718%); b0 9.116% (current 7.225%); sp-hold-ubtc 9.060% (current 7.198%). Those three are close to the −10% flag (b0 has 0.884 pp of stored max DD left). Next: sp-hold-hype max 6.220% (current 0.762%); sp-ema15m-hype 4.230%; retired sp-hold-usol 3.929%; sp-donchian5m-hype 3.772%.
- **HALT latched (v1 respected):** f5-squeeze1m-v1 `halted=True`, reason `daily_loss_minus_2_percent`. Halt event 2026-11-12T15:55:59.999Z, equity 97.898290 / Nov-12 SOD 99.945603 = **−2.048%**; flattened on first observed quote at 15:56:14.933Z (P000011 BTC long, reason `daily_halt_first_observation`) to 97.815356 (**−2.131%** vs that SOD). Rollover 2026-11-12T16:00:00Z set `halt_persists=True`. Today the book is flat, eq = SOD 97.815356, day 0.000%, current/max DD 2.389%. No new risk until the owner resets in writing. 1 book currently `halted`.
- Daily halt (−2% of SOD equity), hit today and **not latched**:
  - b0-btc-1x-hold-control-v1: eq 93.842228 / SOD 97.064660 = **−3.320%** (today's trough 93.507403 = −3.665%). Engine `benchmark` exemption. Not labelled NON_V1_RESEARCH. v1 is not met.
  - sp-hold-ubtc-v1: eq 15.272601 / SOD 15.786851 = **−3.257%** (NON_V1, monitored; `spot_hold` exemption).
  - sp-hold-ueth-v1: eq 15.471737 / SOD 15.861602 = **−2.458%** (same).
  - sp-hold-usol-v1 (RETIRED_DATA_QUALITY, flat since 2026-11-12T06:11:03.778Z): eq 16.230519 / SOD 16.590001 = **−2.167%** (same; SOD still rolls).
  Engine code (`league.py` benchmark early-return; `league_v3.py` `kind!='spot_hold'`) exempts these controls from halt and flatten. That is a written paper-engine exception, not an owner rewrite of risk-limits.md. labels-v4.md records the spot holds as benchmark controls and says their −2% prints are expected, but also that no formal halt exemption is granted without an owner rewrite.
- Closest v1-judged book still trading: g-rsi2-sol-p1-v1 eq 98.974052 / SOD 99.691083 = **−0.719%**, 1.281 pp above the halt line; `halted=False` correctly. Next: g-rsi2-all-p1 −0.560%; g-vwap-sol-p1 −0.475%.

## 3. Cluster

Majors + HYPE treated as one cluster (UBTC=BTC, UETH=ETH). Books open in the same direction:

- **Long 8:** b0 BTC, c1 SOL, g-ema-sol-p2 SOL, sp-hold-ubtc, sp-donchian5m-ubtc, sp-hold-ueth, sp-donchian5m-ueth, sp-hold-hype
- **Short 5:** l1 SOL, g-supertrend-sol-p0 SOL, n1 SOL, g-vwap-sol-p1 SOL, g-vwap-all-p1 SOL

**Pile-up (3+ same direction) both ways.** Per-book cluster cap of 1 is held (33 historical `major_cluster_max_1` rejects, 14 in the last 24h; no book has 2 positions). This is a league-evidence warning, not a single-account breach: these are separate virtual books.

Cluster tags (one effective trial each for promotion): BTC_FRI21 = 4 books, none open; SHOCKREV = 2, none open; TREND = 53, **6 open** — short SOL: l1, g-supertrend-sol-p0, n1; long SOL: g-ema-sol-p2; long spot NON_V1: sp-donchian5m-ubtc, sp-donchian5m-ueth. Count the TREND tag as one trial, not independent confirmation. Do not treat the three TREND SOL shorts as separate confirmation, and do not ignore the opposing TREND long.

## 4. Last 24h (from 2026-11-12T11:55:04.800Z)

84 entries, 79 exits, 38 books traded. Exit reasons: observed_time 31, signal_or_time 28, stop 19, daily_halt_first_observation 1. Closed pnl_net sum +3.108 across the 79 trades. Worst v1-judged closed trade −0.487 USD (g-vwap-eth-p1 P000004 ETH stop), under the 0.50 cap on a 100 book.

- Perp entries (79): stop present and inside 0.5–4.5%; cost-inclusive risk ≤ the live `risk_budget` (0.5% of equity at entry). Several fills printed 0.5005–0.5102 USD vs 0.5000 on a 100 start; all were inside a larger live budget (equity up). Ntl ≥10, lev ≤3×, sizes rounded down. No missing-stop perp entries. The only unstopped opens remain the already-open hold controls (no new hold entries in the window).
- **Monitored — v3 all-in spot (labels-v4 NON_V1_RESEARCH, not re-judged):** implied stop loss + fees still above a 0.5% cap.
  - sp-donchian5m-ubtc-v1 P000001: 0.1018 vs cap 0.0812 (1.25×)
  - sp-donchian5m-ueth-v1 P000002: 0.1429 vs 0.0806 (1.77×); P000003: 0.1020 vs 0.0799 (1.28×)
  - sp-donchian5m-hype-v1 P000002: 0.2136 vs 0.0807 (2.65×); HYPE research-only
  - sp-ema15m-hype-v1 P000001: 0.3128 vs 0.0811 (3.86×); HYPE research-only (1.85% stop on full cash)
  Same construction as previously flagged: full-cash ~16 USD.

## 5. New registry books since last Risk daily (2026-11-12T11:59:14Z)

None. No trading book was added after the v4 set (registered 2026-11-12T05:47Z / created_myt 13:51+08). After yesterday's review, registry gained only `labels-v4.md` (2026-11-12T12:02:53Z): research tags marking all-in spot books NON_V1_RESEARCH / promotion-ineligible. That is not a new book and was not ingested into engine `labels_v1` (still sha256 `18d5fbce…`, ineligible = sp4 only). Standing paper verdicts unchanged: n1–n7 **PASS** (paper); sp4-shockrev1h-ubtc-v1 and sp4-utc21-ubtc-v1 **FLAG** / NON_V1_RESEARCH, not re-judged (flat). C1/C2 are not in this league.

## Correction

1. f5 stays halted until the owner resets the daily-loss stop in writing from a trusted device. I will not unlatch it.
2. If unstopped hold controls (b0, and the spot holds) must keep running as benchmarks, the owner has to write that exemption into risk-limits.md from a trusted device. I will not invent it. Until then b0 FAILs v1 and can print daily losses past −2% with no latch. Its stored max DD (9.12%) is close to the −10% flag.
3. labels-v4.md already labels the remaining all-in spot books NON_V1_RESEARCH. The engine has not picked that up. Ingest or re-register if the desk wants the engine state to match; I will not touch the registry. Re-entry to v1 eligibility still needs new book ids with v1 sizing (qty = floor(0.005·eq / (stop+costs)), reject ntl <10) or an owner-confirmed spot addendum.
4. Do not promote more than one TREND book, or more than one same-direction majors position, into a single live account. Tags count as one trial.

PASS is paper-gate compliance only. It is not owner authorisation and not a sized live ticket.
