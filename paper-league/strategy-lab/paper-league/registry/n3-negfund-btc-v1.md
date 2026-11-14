# n3-negfund-btc-v1

Registered UTC: 2026-11-12T05:47:18.443Z

## Frozen specification

```json
{
  "coins": [
    "BTC"
  ],
  "hold_ms": 86400000,
  "id": "n3-negfund-btc-v1",
  "interval": 3600000,
  "kind": "neg_funding",
  "lane": "slow",
  "market": "perp",
  "owner": "v4 research sweep 2026-11-12; source-motivated, unvalidated",
  "params": {
    "hours": 8,
    "stop_atr": 3.0
  },
  "sources": [
    "https://www.aijmr.com/research-paper.php?id=1493",
    "https://janorium.com/articles/funding-rate-signal-backtest"
  ]
}
```

Long BTC perp when the mean of the last 8 settled real hourly Hyperliquid funding prints turns negative (mean_t<0 and the mean of the 8 prints ending one hour earlier >=0). Requires exactly one print per hour for 9 hours or the tick fails closed. No signal exit; 24h hold cap, stop or halt. Stop max(0.5%, 3*ATR14/C), abstain if >4.5%. Not a trend filter, threshold or funding-reverts exit, unlike the frozen g-funding books.

Sources: https://www.aijmr.com/research-paper.php?id=1493, https://janorium.com/articles/funding-rate-signal-backtest

## Frozen common rules for the v4 research-sweep extension (registered before its first live tick)
- PAPER only, public Hyperliquid mainnet /info reads only through the unchanged v3 collector (no new request type). No wallet, key, private endpoint, order, signing, testnet or exchange write. Requested by the owner on 12 Nov 2026 ("go online research find more different strategy and run test"). Families are motivated by the cited public sources; parameters are the sources' headline settings or round numbers fixed here, never tuned on league results. No return claim. All variants and losses retained.
- Perp books (n1-n7): 100 virtual USDC each, BTC/ETH/SOL only, frozen risk-limits v1 sizing via the existing league.open_paper: 0.5% cost-inclusive risk per trade (including 24h funding reserve), <=3x notional, one position per book (cluster max 1, inside the 2-position desk cap), mandatory protective stop 0.5%-4.5% else abstain, sticky -2% MYT daily halt, observed-mid entry +2bp adverse, Hyperliquid perp taker fee from the existing config on every fill, hourly settled funding charged/credited, stops replayed on every closed 1m candle (touch = trigger+5bp, gap = bar open+5bp), time exits at first observed quote after the hold cap +2bp.
- Spot books (sp4-*): 16.24 virtual USDC each, UBTC/USDC (@142) spot pair only, long-only 1x all-in cash, official tier-0 spot taker 0.070% every fill (maker never assumed), max(2bp, L2 walk) slippage, 5bp on stops, $10 minimum notional, no funding, same stop replay and -2% sticky halt as the v3 spot books.
- Signals use fully closed 1h UTC bars only; entries only within 90 seconds of the bar close; missed entries are logged, never back-filled. Missing, stale or misaligned data fails the whole tick closed (no partial state).
- Frozen v1/v2/v3 registrations, implementation files and the 116 running books stay byte-identical and execute their own code first each tick; v4 books are evaluated with the same evaluation_v3 code.
- Evaluation: same bar as the league. >=30 closed trades, positive costed return, beats BOTH the BTC-perp hold and random-entry controls after costs, DSR probability >0.95, not halted, then a following non-overlapping fresh-MYT-day/flat-book OOS >=7 days (or >=30 new trades for fast/spot_fast lanes). First OOS endpoint is fixed PASS/FAIL. CANDIDATE_REVIEW_ONLY only: no automatic promotion, message, permission or trade. Known DSR trials = 425 prior + these 9 = 434 at 125 books. Low-frequency books (weekend, xs-momentum, negative-funding, shock-reversal) may never reach 30 trades in a short window; they stay NOT_SIGNIFICANT, which is not a pass.

## v4 implementation SHA256
- `league_v4.py`: `8400bbb8110d7027a68abe41971e863e5a1d39dd62b0de3b36f30dc5c0859265`
- `strategies_v4.py`: `c90e1efb2daeb797ca69f384b7ea7ccf756b9837e315340affd89d570d7c0a6d`
- `register_v4.py`: `c205ccefae0f6e5c97627992ba3b1c9f564a1063bd20b6cb2c1bcfb1c4db0b42`
