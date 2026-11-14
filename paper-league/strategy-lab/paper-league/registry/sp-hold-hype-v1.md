# sp-hold-hype-v1

Registered UTC: 2026-11-11T09:15:30.032Z

## Frozen specification

```json
{
  "api_coin": "@107",
  "coins": [
    "HYPE"
  ],
  "hold_ms": 315360000000,
  "id": "sp-hold-hype-v1",
  "interval": 60000,
  "kind": "spot_hold",
  "lane": "spot_control",
  "leverage": 1,
  "long_only": true,
  "maker_fee_documented": 0.0004,
  "market": "spot",
  "min_notional": 10.0,
  "no_funding": true,
  "owner": "Spot buy-and-hold control; not a tradable strategy",
  "params": {},
  "price_source": "spot_pair",
  "sizing": "all_in_cash",
  "slippage": "max(2bp_adverse_mid, L2_notional_walk)",
  "spot_pair": "HYPE/USDC",
  "starting_equity": 16.24,
  "taker_fee": 0.0007
}
```

All-in 1x long buy-and-hold of the registered USDC spot pair at the first actually observed mid after activation, plus max(2bp, L2 walk) adverse slippage and official tier-0 spot taker 0.070%. No stop, no daily-halt flatten, no funding, no rebalance, no shorts, no leverage. Measurement control only; not a tradable strategy or risk-limits exception for live trading.

Price source: spot_pair (HYPE/USDC, API coin @107). Not a perp-mid proxy.

## Frozen common rules for this prospective SPOT extension
- PAPER only, public Hyperliquid mainnet /info reads only, no wallet/private endpoint/key/order/signing/testnet/exchange writes. Desk-defined spot experiments at the owner's 11 Nov 2026 request, not independently supplied or proven bot strategies. No optimized parameter choice or return claim. All variants and losses retained.
- Each spot book starts with 16.24 virtual USDC independently at its first live v3 tick (the owner's stated live cash, not the 100 USDC perp-book capital). Long-only, 1x, no leverage, no shorting, no liquidation. Sizing is all-in free cash rounded down to the base token szDecimals, never rounded up to the $10 minimum. One position per book. Mandatory protective stop on research books = max(0.5%, 2*arithmetic ATR14/close); abstain from entry if stop >4.5%. Buy-and-hold controls have no stop and no daily-halt flatten.
- Universe: live USDC spot pairs UBTC/USDC (@142), UETH/USDC (@151), USOL/USDC (@156), HYPE/USDC (@107), verified from public spotMeta / spotMetaAndAssetCtxs / allMids / l2Book on 11 Nov 2026. Price source for all four is the spot pair itself, not a perp-mid proxy. A missing mid, identity change, or failed 1m continuity fails the tick closed.
- Official tier-0 spot fees from https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees retrieved 11 Nov 2026: taker 0.070%, maker 0.040%. Every fill charges taker 0.070%. Maker 0.040% is documented and NEVER used without a resting-limit/queue model; there are no maker spot books. Slippage is the more adverse of a 2bp mid floor and an L2 walk of the intended notional; if visible depth is insufficient the 2bp floor is used and labelled. Stop/halt exits use 5bp adverse. No funding is charged or credited on spot. Minimum notional $10.
- Signals use fully closed UTC bars only. 250-bar seed on 15m/1h/4h; 1m cache retains 512 closed bars. EMA/EWM adjust=False. Missing data refuses the tick. No historical bar-open signal/time fills. 15m/1h/4h entries within 90 seconds of bar close; missed entries are logged, never entered retrospectively.
- No leverage and no funding reserve. Daily MYT -2% halt still latches on research books (not hold controls) and flattens at the next actually observed quote. Halt stays across midnight until owner reset. Virtual gap loss can exceed a tight cash buffer; this is still not liquidation.
- Mandatory virtual stops for research books: replay every missed closed 1m candle before decisions. Touch=trigger+5bp adverse; gap through trigger=bar open+5bp. Entry-minute touch conservatively stopped and flagged ambiguous. These explicit candle-reconstructed STOP assumptions are the only retrospective fills, NOT real exchange protection. >5000-minute retention or any missing replay minute blocks all new entries without advancing the cursor.
- Frozen v1 and v2 registrations, implementation files and running 100 perp-book capital/history stay byte-identical and are never reset. This append-only spot extension has a separate manifest pinned in state; changes require new ids and a new prospective registration.
- Evaluation: same promotion bar as the perp league. >=30 closed trades, positive costed return, beats BOTH the BTC-perp hold and random-entry controls after costs, DSR>0.95, not halted, then a following non-overlapping fresh-MYT-day/flat-book OOS >=7 days OR >=30 new trades for spot_fast books. First OOS endpoint is fixed PASS/FAIL. CANDIDATE_REVIEW_ONLY only. No automatic promotion, message, permission or trade. Known DSR trials = 309 prior + every league book including these 16 = 425 at 116 books. Do not hide failed variants. Spot hold controls are measurement controls, not promotion benchmarks and not live-trading permission.
- Original five, the 95 v2 books, league.py, strategies.py, league_v2.py, strategies_v2.py, evaluation_v2.py and register_v2.py remain frozen. This engine adds public endpoint spotMetaAndAssetCtxs to the allowlist. Collector estimated-weight cap 1000 vs official shared-IP 1200/min.

## Spot extension implementation SHA256
- `league_v3.py`: `ce690893f699a4233fbbd10a0599f02518f0cf6b7f47e522d745d3384338c4b1`
- `strategies_v3.py`: `0a4f70b6ea54c4a281c0ac9793b7bd5b558a71c1dc1f27ed053818937e22503b`
- `evaluation_v3.py`: `1a4937460915c9b289c4b43db225a934e1d83bdfe23c99209c37ce81dda7768e`
- `register_v3.py`: `dc4ed12e7ae0d328b15de57020cade70b7b47c9e2e6e5ec5ef690912f49faf4a`
