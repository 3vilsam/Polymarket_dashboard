# Risk review: n1-tsmom-mh1h-v1 P000001 paper SOL short (stop 85.2013)
Written UTC: 2026-11-12T16:17:14Z (00:17:14+08 Asia/Kuala_Lumpur, 13 Nov). Reviewer: Risk Manager, independent desk review. PAPER / BACKTEST ONLY. I changed no keys, orders, limits or registry files.
Basis: `/workspace/trading-desk/risk-limits.md` v1. Cost model requested for this review: taker 0.045% × 2 + 0.10% stop slip, plus stress at 25 bp and 50 bp stop slip. Engine record (5 bp stop slip + 24h funding reserve) is shown for reconciliation, not as a substitute for the requested model. Spot addendum remains a DRAFT and was not used.
Snapshot: `strategy-lab/paper-league/league_state.json` last_tick 2026-11-12T16:16:21.130Z (2026-11-13T00:16:21+08). Entry event from the same book's ledger / events (seq 22). SOL `szDecimals=2` and `maxLeverage=20` from the league public `metaAndAssetCtxs` snapshot `sources/1794499981039.json.gz` (network: Hyperliquid mainnet public `/info` only).

The owner referred to "tonight's paper SOL short" with stop 85.24. The only open (or last-24h) SOL short whose stop is at that figure is n1-tsmom-mh1h-v1 P000001, stop 85.20133895161196 (85.24 to two decimals). Identified by grepping paper-league books/ledgers/state; no other fill carries a stop of 85.24.

## Identified trade
- Book / HG id: `n1-tsmom-mh1h-v1` / `P000001`
- Market: SOL perp, short, paper
- Entry: 2026-11-12T10:00:10.109Z (18:00:10+08), fill 83.1038759, `fill_source=observed_mid_plus_2bps`
- Stop: 85.20133895161196 (fixed vs fill; registry rule max(0.5%, 3×ATR14/C), abstain if >4.5%)
- Size: 0.22 SOL (`size_initial` 0.22)
- Entry fee recorded: 0.008227283714100002 (= 0.22 × 83.1038759 × 0.00045)
- Engine `cost_inclusive_risk` / `risk_budget` / `risk_cap_at_entry`: 0.49296109071901667 / 0.50 / 0.50
- Equity at entry: 100.00 (valuations from first live tick through 2026-11-12T07:00:58.382Z were all 100.00 cash; this is the book's first trade; `starting_equity` 100.0)
- Labels: TREND, `promotion_eligible=true`
- Still open at the snapshot. Mark SOL 81.8915, cash 99.99248185462616, unrealised 0.22 × (83.1038759 − 81.8915) = 0.266722698, equity 100.25920455262617. Net funding to date +0.000709138340284. `halted=false`. Closed trades on this book: 0.

## Arithmetic (requested cost model)

    equity_at_entry     = 100.00
    risk_usd            = 100.00 × 0.5% = 0.50
    entry               = 83.1038759
    stop                = 85.20133895161196
    size                = 0.22
    taker               = 0.00045
    stop_distance       = |83.1038759 − 85.20133895161196| = 2.09746305161196
    stop_pct            = 2.09746305161196 / 83.1038759 = 2.52390520766548%
    notional            = 0.22 × 83.1038759 = 18.282852698
    leverage            = 18.282852698 / 100.00 = 0.18282852698×

Base case — 10 bp stop slip (0.10% of entry), skill-style stressed distance:

    slip_stop           = 83.1038759 × 0.0010 = 0.0831038759
    stop_fill (short)   = 85.20133895161196 + 0.0831038759 = 85.28444282751196
    fees_per_unit       = (83.1038759 + 85.28444282751196) × 0.00045 = 0.075774743427380382
    stressed_distance   = |83.1038759 − 85.28444282751196| + 0.075774743427380382
                        = 2.256341670939340382
    risk                = 0.22 × 2.256341670939340382 = 0.496395167606654884
    raw_size            = 0.50 / 2.256341670939340382 = 0.221597644736
    size (floor, 2 dp)  = 0.22   (matches the fill; not rounded up)

Stress — 25 bp stop slip:

    slip_stop           = 83.1038759 × 0.0025 = 0.20775968975
    stop_fill           = 85.40909864136196
    fees_per_unit       = 0.075830838543612882
    stressed_distance   = 2.381053579905572882
    risk at size 0.22   = 0.523831787579226034   (exceeds 0.50)
    max floor size      = floor(0.50 / 2.381053579905572882, 2 dp) = 0.20
    risk at 0.20        = 0.476210715981114576

Stress — 50 bp stop slip:

    slip_stop           = 83.1038759 × 0.0050 = 0.4155193795
    stop_fill           = 85.61685833111196
    fees_per_unit       = 0.075924330404000382
    stressed_distance   = 2.588906761515960382
    risk at size 0.22   = 0.569559487533511284   (exceeds 0.50)
    max floor size      = floor(0.50 / 2.588906761515960382, 2 dp) = 0.19
    risk at 0.19        = 0.491892284688032473

Engine record (for reconciliation only; 5 bp stop slip + 24h funding reserve at max(adverse rate, 0.00125%/h)):

    reserve_per_unit    = 0.0000125 × 24 × 83.1038759 = 0.02493116277
    exit_cost_per_unit  = 85.20133895161196 × (0.00045 + 0.0005) = 0.080941272004031362
    engine_rpu          = 2.09746305161196 + 83.1038759×0.00045 + 0.080941272004031362 + 0.02493116277
                        = 2.240732230540991362
    engine risk         = 0.22 × 2.240732230540991362 = 0.4929610907190181
    (matches recorded cost_inclusive_risk 0.49296109071901667 within 2e-15)

## Gates versus risk-limits v1

| Gate | Result | Numbers |
|---|---|---|
| 0.5% equity risk incl. costs (10 bp slip + 2×taker) | PASS | 0.49639517 ≤ 0.50 (99.28% of cap) |
| Same at 25 bp stop slip (stress, not the v1 send-tolerance) | BREACH | 0.52383179 / 0.50 = 1.0477× |
| Same at 50 bp stop slip | BREACH | 0.56955949 / 0.50 = 1.1391× |
| Stop distance 0.5–4.5% | PASS | 2.52390521% |
| Notional ≥ 10 USD | PASS | 18.282852698 |
| Size floored to SOL szDecimals=2 | PASS | 0.22, equal to floor(0.22159764, 2) under the 10 bp model |
| Leverage ≤ 3× | PASS | 0.18282853× (exchange headline maxLeverage 20 is not the desk cap) |
| Max 2 positions / 1 per majors cluster, per book | PASS | 1 position on this book; engine `cluster_max=1` |
| 2% total open risk, this book | PASS | the single position is the open risk, 0.4964% at 10 bp |
| Daily −2% halt (MYT day starting 2026-11-12T16:00:00Z) | PASS | equity 100.25920455 / SOD 100.30982384 = −0.05046%; `halted=false` |
| Liquidation distance vs the stop | MISSING | paper book has no margin mode, `marginUsed` or `liquidationPx`. Not invented. |
| Allowed market | PASS | SOL is named in v1 |

TREND-tag concentration (not a single-book v1 breach; these are separate virtual books): at this snapshot the TREND cluster still has three open SOL shorts — l1-supertrend1h-v1, g-supertrend-sol-p0-v1 (same fill as each other, stop 84.26256088912268) and this n1 trade. Count those three as one evidence trial, not independent confirmation. Other TREND opens at the same tick (spot donchian/ema on UETH and HYPE) are already labelled NON_V1_RESEARCH in labels-v4 and are not re-judged here.

## Verdict

**PASS** (paper-gate compliance only, under the requested 10 bp cost model and v1). This is not owner authorisation and not a sized live ticket. Nothing is to be sent.

- Failure gate: none on the v1 / 10 bp model.
- Stress note, not a v1 reject: 25 bp and 50 bp stop-slip stress would put this size over the 0.5% cap. If the owner wants those stresses inside the budget, the required correction is size 0.20 (25 bp) or 0.19 (50 bp), never a round-up. I will not change paper sizing or limits without a written owner rewrite.
- Promotion note: do not treat this fill as independent of the other two TREND SOL shorts.

## New candidates / books since 2026-11-12T06:55Z

None added to the registry as trading books. The only registry files newer than the cutoff are `labels-v4.md` and `labels-v4.sha256` (mtime 2026-11-12T12:02:53Z), which tag existing all-in spot books NON_V1_RESEARCH and do not register a new book. `research/ablation/2026-11-13-l3-funding1h-v1/` is a study of already-registered `l3-funding1h-v1` (registry 2026-11-11T06:02:16Z), not a new candidate. No pre-review to issue.

Inputs: risk-limits.md v1; league_state.json last_tick 2026-11-12T16:16:21.130Z; n1 events seq 22; sources/1794499981039.json.gz meta (SOL szDecimals=2); paper-league/registry/ (mtimes vs 2026-11-12T06:55Z).
Method: manual gate arithmetic as boxed above, plus directory mtime scan of registry/ and research/.
Bot: Risk Manager
