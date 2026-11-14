# PAPER league — 100 virtual USDC perp books + 16.24 virtual USDC spot books

Updated 2026-11-13T23:21:03+08:00 MYT | tick 351 | 125 books (107 perp @100 USDC, 18 spot @16.24 USDC; incl. 9 v4 research-sweep books registered 12 Nov 2026) | public reads only

Spot research books use 5m/15m/1h timeframes. Do not compare raw Net MTM USDC across the 100-USDC and 16.24-USDC tables. An 'Early read (not evidence)' table lists fast books with >=10 closed trades; it is not the promotion bar. Ranks use net MTM (open exit cost not deducted). Gate comparisons use same-start indicative exit equity: perp books deduct taker+2bp; spot books deduct official tier-0 spot taker 0.070%+2bp. Official promotion controls remain the BTC-perp hold and random-entry books.

## Controls / luck benchmarks (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | c1-random15m-v1 | 3 | +1.4717 | 66.6667 | 40.9013 | 0.5462 | 0.4906 | 0.1148 | +0.0006 | +8.4451 | +0.0000 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); CONTROL |
| 2 | b0-btc-1x-hold-control-v1 | 0 | -6.9505 | — | — | 9.1161 | — | 0.0450 | -0.0488 | +0.0000 | -8.4451 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); CONTROL; NONTRADABLE risk-exempt |

## Fast / short-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | g-vwap-eth-p0-v1 | 6 | +2.3563 | 83.3333 | 37.4804 | 1.0891 | 0.3927 | 0.3456 | +0.0053 | +9.3297 | +0.8846 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-vwap-eth-p2-v1 | 5 | +1.7454 | 80.0000 | 4.6107 | 2.4792 | 0.3491 | 0.2922 | -0.0017 | +8.7187 | +0.2736 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | g-vwap-eth-p1-v1 | 4 | +1.5788 | 75.0000 | 4.2410 | 1.5160 | 0.3947 | 0.2273 | +0.0049 | +8.5522 | +0.1071 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | g-vwap-all-p1-v1 | 14 | +0.4991 | 50.0000 | 1.2018 | 2.4279 | 0.0357 | 0.8781 | +0.0012 | +7.4725 | -0.9726 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | g-rsi2-eth-p0-v1 | 3 | +0.3097 | 66.6667 | 12.1631 | 0.4654 | 0.1032 | 0.1651 | +0.0001 | +7.2831 | -1.1620 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | g-rsi2-eth-p2-v1 | 1 | +0.2884 | 100.0000 | inf | 0.0632 | 0.2884 | 0.0469 | +0.0000 | +7.2617 | -1.1833 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | g-squeeze-sol-p2-v1 | 7 | +0.2674 | 42.8571 | 1.2909 | 1.3576 | 0.0382 | 0.4672 | -0.0003 | +7.2407 | -1.2044 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | g-rsi2-btc-p2-v1 | 2 | +0.1809 | 100.0000 | inf | 0.5796 | 0.0904 | 0.1123 | +0.0007 | +7.1543 | -1.2908 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | g-rsi2-sol-p2-v1 | 3 | +0.0976 | 66.6667 | 1.3923 | 0.6027 | 0.0325 | 0.1578 | +0.0003 | +7.0709 | -1.3741 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | g-rsi2-btc-p0-v1 | 2 | +0.0821 | 50.0000 | 2.1660 | 0.1520 | 0.0410 | 0.1220 | +0.0000 | +7.0555 | -1.3896 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | g-rsi2-sol-p0-v1 | 2 | +0.0234 | 50.0000 | 1.0942 | 0.6032 | 0.0117 | 0.1128 | +0.0003 | +6.9968 | -1.4483 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | f4-ema15m-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-ema-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-ema-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-ema-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-ema-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | n4-utc21-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.5899 | -1.4717 | 434 | — | 0 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-asia-btc-p0-v1 | 1 | -0.0076 | 0.0000 | 0.0000 | 0.2813 | -0.0076 | 0.0668 | +0.0021 | +6.9658 | -1.4793 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-asia-btc-p1-v1 | 1 | -0.0076 | 0.0000 | 0.0000 | 0.2813 | -0.0076 | 0.0668 | +0.0021 | +6.9658 | -1.4793 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-asia-btc-p2-v1 | 1 | -0.0076 | 0.0000 | 0.0000 | 0.2813 | -0.0076 | 0.0668 | +0.0021 | +6.9658 | -1.4793 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-ema-sol-p2-v1 [cluster:TREND] | 0 | -0.0978 | — | — | 1.2127 | — | 0.0195 | -0.0006 | +6.8475 | -1.5976 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | f3-rsi2-5m-v1 | 4 | -0.1176 | 50.0000 | 0.6317 | 0.7137 | -0.0294 | 0.2405 | +0.0001 | +6.8558 | -1.5893 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-asia-eth-p0-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +6.8441 | -1.6010 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-asia-eth-p1-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +6.8441 | -1.6010 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | g-asia-eth-p2-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +6.8441 | -1.6010 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-vwap-sol-p0-v1 | 7 | -0.1808 | 57.1429 | 0.8646 | 2.3469 | -0.0258 | 0.4217 | +0.0026 | +6.7926 | -1.6525 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-squeeze-eth-p2-v1 | 4 | -0.2301 | 25.0000 | 0.3911 | 0.5407 | -0.0575 | 0.2679 | +0.0000 | +6.7432 | -1.7018 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-rsi2-btc-p1-v1 | 2 | -0.2472 | 0.0000 | 0.0000 | 0.3991 | -0.1236 | 0.1336 | +0.0000 | +6.7261 | -1.7190 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | f1-vwap5m-v1 | 9 | -0.3429 | 55.5556 | 0.7748 | 2.3231 | -0.0381 | 0.5660 | +0.0003 | +6.6305 | -1.8146 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-vwap-btc-p0-v1 | 4 | -0.3483 | 50.0000 | 0.4745 | 0.9694 | -0.0871 | 0.2526 | -0.0033 | +6.6251 | -1.8200 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-rsi2-eth-p1-v1 | 3 | -0.4034 | 33.3333 | 0.2834 | 0.5118 | -0.1345 | 0.1830 | +0.0000 | +6.5699 | -1.8751 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-vwap-btc-p1-v1 | 7 | -0.4084 | 57.1429 | 0.6096 | 1.1597 | -0.0583 | 0.4292 | -0.0057 | +6.5649 | -1.8801 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-vwap-sol-p2-v1 | 8 | -0.4378 | 50.0000 | 0.7701 | 2.3942 | -0.0547 | 0.4867 | +0.0019 | +6.5356 | -1.9095 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | g-ema-btc-p1-v1 [cluster:TREND] | 1 | -0.4760 | 0.0000 | 0.0000 | 0.4978 | -0.4760 | 0.0671 | +0.0000 | +6.4974 | -1.9477 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-ema-eth-p1-v1 [cluster:TREND] | 1 | -0.4846 | 0.0000 | 0.0000 | 0.6807 | -0.4796 | 0.0781 | +0.0000 | +6.4644 | -1.9807 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | f2-asia15m-v1 | 2 | -0.4854 | 0.0000 | 0.0000 | 0.8244 | -0.2427 | 0.1140 | +0.0022 | +6.4879 | -1.9571 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 37 | g-asia-all-p1-v1 | 2 | -0.4854 | 0.0000 | 0.0000 | 0.8244 | -0.2427 | 0.1140 | +0.0022 | +6.4879 | -1.9571 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-ema-sol-p1-v1 [cluster:TREND] | 1 | -0.5038 | 0.0000 | 0.0000 | 0.8346 | -0.4779 | 0.0770 | -0.0008 | +6.4467 | -1.9984 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | g-ema-btc-p2-v1 [cluster:TREND] | 1 | -0.5433 | 0.0000 | 0.0000 | 1.2187 | -0.4791 | 0.0783 | -0.0016 | +6.4023 | -2.0428 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | g-vwap-btc-p2-v1 | 3 | -0.6223 | 0.0000 | 0.0000 | 0.9564 | -0.2074 | 0.1939 | -0.0017 | +6.3510 | -2.0940 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | g-asia-sol-p0-v1 | 2 | -0.8276 | 0.0000 | 0.0000 | 1.0277 | -0.4138 | 0.1038 | +0.0005 | +6.1458 | -2.2993 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | g-asia-sol-p1-v1 | 2 | -0.8276 | 0.0000 | 0.0000 | 1.0277 | -0.4138 | 0.1038 | +0.0005 | +6.1458 | -2.2993 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | g-asia-sol-p2-v1 | 2 | -0.8276 | 0.0000 | 0.0000 | 1.0277 | -0.4138 | 0.1038 | +0.0005 | +6.1458 | -2.2993 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | g-squeeze-btc-p1-v1 | 4 | -0.8617 | 0.0000 | 0.0000 | 0.8931 | -0.2154 | 0.2659 | -0.0001 | +6.1117 | -2.3334 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | g-rsi2-all-p1-v1 | 4 | -0.8767 | 25.0000 | 0.1535 | 0.8794 | -0.2192 | 0.2290 | +0.0003 | +6.0966 | -2.3485 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 46 | g-vwap-sol-p1-v1 | 8 | -0.9149 | 50.0000 | 0.3862 | 1.3822 | -0.1144 | 0.5051 | -0.0004 | +6.0585 | -2.3866 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | g-squeeze-sol-p0-v1 | 5 | -0.9454 | 20.0000 | 0.0399 | 1.1790 | -0.1891 | 0.3325 | +0.0000 | +6.0279 | -2.4172 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 48 | g-squeeze-sol-p1-v1 | 5 | -0.9454 | 20.0000 | 0.0399 | 1.1790 | -0.1891 | 0.3325 | +0.0000 | +6.0279 | -2.4172 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | g-ema-all-p1-v1 [cluster:TREND] | 2 | -0.9589 | 0.0000 | 0.0000 | 1.1002 | -0.4770 | 0.1451 | -0.0008 | +5.9902 | -2.4549 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 50 | g-rsi2-sol-p1-v1 | 3 | -1.0259 | 0.0000 | 0.0000 | 1.0282 | -0.3420 | 0.1800 | +0.0003 | +5.9474 | -2.4977 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 51 | g-squeeze-eth-p1-v1 | 5 | -1.1065 | 20.0000 | 0.0928 | 1.1065 | -0.2213 | 0.3338 | -0.0012 | +5.8669 | -2.5782 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 52 | g-squeeze-btc-p0-v1 | 6 | -1.1900 | 0.0000 | 0.0000 | 1.2214 | -0.1983 | 0.3982 | +0.0007 | +5.7834 | -2.6617 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 53 | g-squeeze-eth-p0-v1 | 7 | -1.1949 | 28.5714 | 0.1302 | 1.4016 | -0.1707 | 0.4674 | -0.0012 | +5.7785 | -2.6666 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 54 | g-squeeze-btc-p2-v1 | 6 | -1.6568 | 16.6667 | 0.0735 | 1.9582 | -0.2761 | 0.3978 | -0.0065 | +5.3166 | -3.1285 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 55 | f5-squeeze1m-v1 | 11 | -2.1846 | 9.0909 | 0.0292 | 2.3893 | -0.1986 | 0.7295 | +0.0016 | +4.7887 | -3.6564 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |

## Slow / long-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | l1-supertrend1h-v1 [cluster:TREND] | 1 | +0.3643 | 100.0000 | inf | 1.1588 | 0.3643 | 0.0214 | +0.0031 | +7.3376 | -1.1075 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-supertrend-sol-p0-v1 [cluster:TREND] | 1 | +0.3643 | 100.0000 | inf | 1.1588 | 0.3643 | 0.0214 | +0.0031 | +7.3376 | -1.1075 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | n1-tsmom-mh1h-v1 [cluster:TREND] | 1 | +0.3606 | 100.0000 | inf | 0.8811 | 0.3606 | 0.0163 | +0.0022 | +6.9505 | -1.1111 | 434 | — | 0 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | s1-donchian40-ablation-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | s2-bb40-ema200-ablation-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | s4-ewmac-riskcap-noadd-ablation-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | r1-trend-rsi-pullback-market-lane-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | l2-macd4h-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | l3-funding1h-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | l4-weekly1d-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | g-supertrend-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-supertrend-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-supertrend-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-supertrend-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-supertrend-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-supertrend-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-supertrend-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-supertrend-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-macd-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-macd-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-macd-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-macd-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-macd-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-macd-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | g-macd-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-macd-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-macd-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-funding-btc-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-funding-btc-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-funding-btc-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-funding-eth-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-funding-eth-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-funding-eth-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | g-funding-sol-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-funding-sol-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | g-funding-sol-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 37 | g-weekly-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-weekly-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | g-weekly-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | g-weekly-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | g-weekly-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | g-weekly-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | g-weekly-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | g-weekly-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | g-weekly-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.9734 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 46 | n2-shockrev1h-v1 [cluster:SHOCKREV] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.5899 | -1.4717 | 434 | — | 0 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | n3-negfund-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.5899 | -1.4717 | 434 | — | 0 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 48 | n5-weekend-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.5899 | -1.4717 | 434 | — | 0 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | n6-ethbtc-z1h-v1 [UNHEDGED_ETH_DIRECTIONAL] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.5899 | -1.4717 | 434 | — | 0 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 50 | n7-xsmom72h-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.5899 | -1.4717 | 434 | — | 0 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |

## Spot buy-and-hold controls (16.24 virtual USDC, 1x long, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-hold-hype-v1 | 0 | +0.2253 | — | — | 6.2204 | — | 0.0110 | +0.0000 | +7.9827 | -0.1733 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 2 | sp-hold-usol-v1 (RETIRED_DATA_QUALITY) | 1 | -0.0166 | 0.0000 | 0.0000 | 3.9287 | -0.0166 | 0.0226 | +0.0000 | +6.5820 | -1.5741 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 3 | sp-hold-ueth-v1 | 0 | -0.9476 | — | — | 9.3260 | — | 0.0114 | +0.0000 | +0.7647 | -7.3914 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 4 | sp-hold-ubtc-v1 | 0 | -1.0884 | — | — | 9.0595 | — | 0.0113 | +0.0000 | -0.1014 | -8.2575 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |

## Spot fast / 5m and 15m (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-ema15m-ubtc-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.6844 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-ema15m-ueth-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.6844 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-ema15m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.6844 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp4-utc21-ubtc-v1 [NON_V1_RESEARCH, cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.5899 | -1.4717 | 434 | — | 0 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH |
| 5 | sp-donchian5m-ubtc-v1 [cluster:TREND] | 1 | -0.0100 | 0.0000 | 0.0000 | 1.0251 | -0.0100 | 0.0223 | +0.0000 | +6.6226 | -1.5335 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | sp-donchian5m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 1 | -0.1128 | 0.0000 | 0.0000 | 1.0376 | -0.1128 | 0.0226 | +0.0000 | +5.9897 | -2.1663 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | sp-donchian5m-ueth-v1 [cluster:TREND] | 3 | -0.2184 | 33.3333 | 0.1658 | 1.7456 | -0.0728 | 0.0671 | +0.0000 | +5.3398 | -2.8163 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | sp-ema15m-hype-v1 [cluster:TREND] | 1 | -0.3205 | 0.0000 | 0.0000 | 4.2298 | -0.3205 | 0.0218 | +0.0000 | +4.7108 | -3.4453 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | sp-donchian5m-hype-v1 [cluster:TREND] | 2 | -0.3300 | 0.0000 | 0.0000 | 3.7718 | -0.1650 | 0.0438 | +0.0000 | +4.6525 | -3.5036 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |

## Spot slow / 1h (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-rsi1h-ubtc-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.6844 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-rsi1h-ueth-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.6844 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-rsi1h-usol-v1 (RETIRED_DATA_QUALITY) | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.6844 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-rsi1h-hype-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.6844 | -1.4717 | 434 | — | 1 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | sp4-shockrev1h-ubtc-v1 [NON_V1_RESEARCH, cluster:SHOCKREV] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +6.5899 | -1.4717 | 434 | — | 0 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH |

## Early read (not evidence)

Fast and spot_fast books with at least 10 closed trades, ranked by closed-trade count then net MTM after paid fees/funding (open exit cost not deducted). This is an operational early look so small-capital books can be watched before the 30-trade / DSR / fresh-OOS bar. It is **not** significance, **not** a PASS, and **does not** change the promotion bar. Nothing in this section is a CANDIDATE.

| Rank | Book | Lane | Closed | Net MTM USDC | Win % | Fees | Funding | Gate |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | g-vwap-all-p1-v1 | fast | 14 | +0.4991 | 50.0000 | 0.8781 | +0.0012 | NOT_SIGNIFICANT |
| 2 | f5-squeeze1m-v1 | fast | 11 | -2.1846 | 9.0909 | 0.7295 | +0.0016 | NOT_SIGNIFICANT |

DSR uses completed MYT daily returns, >=8 full daily observations, skew/kurtosis-adjusted normal probability, cross-book Sharpe dispersion with sampling-error floor. Trial count = 309 prior + ALL league books (perp and spot, including controls); currently 434. Unknown external searches are not verifiable: 434 is the known count, not proof of complete worldwide trial history. Correlated books/time series make this an approximate conservative diagnostic, not a statistical guarantee.

CANDIDATE_REVIEW_ONLY needs >=30 closed trades, positive costed return, outperformance vs BOTH the BTC-perp hold and random-entry controls, DSR>0.95, then a following non-overlapping fresh-MYT-day/flat-book OOS >=7 days OR >=30 new trades for fast/spot_fast books, profitable and beating both controls. First OOS endpoint is fixed PASS/FAIL. Candidate means send evidence for Risk Manager review only; NO automatic promotion.

Spot books charge official tier-0 spot taker 0.070% (https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees, retrieved 11 Nov 2026) plus max(2bp adverse mid, L2 walk); maker 0.040% is documented and never assumed. No funding. No leverage, long only, no liquidation model. Stops are virtual candle replay with gaps+5bp, NOT exchange protection. UBTC/USDC (@142), UETH/USDC (@151), USOL/USDC (@156) and HYPE/USDC (@107) are real spot pairs, not perp-mid proxies. All families are unvalidated experiments; prior failed tests stay failed.

## Labels and clusters (registry/labels-v1, append-only)

- **sp4-shockrev1h-ubtc-v1**: NON_V1_RESEARCH — Full-cash spot sizing (all-in ~16.2 USDC notional, ~0.7-4.7% equity at the stop), above risk-limits v1 0.5% per trade; spot/UBTC not named in v1; exchange spot trigger stops unverified. Research only. Promotion-ineligible.
- **sp4-utc21-ubtc-v1**: NON_V1_RESEARCH — Full-cash spot sizing (all-in ~16.2 USDC notional, ~0.7-4.7% equity at the stop), above risk-limits v1 0.5% per trade; spot/UBTC not named in v1; exchange spot trigger stops unverified. Research only. Promotion-ineligible.
- **n6-ethbtc-z1h-v1**: UNHEDGED_ETH_DIRECTIONAL — Single-leg ETH perp trade driven by the ETH/BTC ratio z-score. Exposure is ETH directional beta (ETH-BTC 1h corr 0.918), NOT a hedged or market-neutral pair.

Clusters (each cluster counts as ONE effective trial / one piece of independent evidence in any promotion review; the DSR multiplicity count stays 434, unchanged and conservative):
- BTC_FRI21 (4 books): n3-negfund-btc-v1, n4-utc21-btc-v1, n5-weekend-btc-v1, sp4-utc21-ubtc-v1
- SHOCKREV (2 books): n2-shockrev1h-v1, sp4-shockrev1h-ubtc-v1
- TREND (53 books): f4-ema15m-v1, g-ema-all-p1-v1, g-ema-btc-p0-v1, g-ema-btc-p1-v1, g-ema-btc-p2-v1, g-ema-eth-p0-v1, g-ema-eth-p1-v1, g-ema-eth-p2-v1, g-ema-sol-p0-v1, g-ema-sol-p1-v1, g-ema-sol-p2-v1, g-macd-btc-p0-v1, g-macd-btc-p1-v1, g-macd-btc-p2-v1, g-macd-eth-p0-v1, g-macd-eth-p1-v1, g-macd-eth-p2-v1, g-macd-sol-p0-v1, g-macd-sol-p1-v1, g-macd-sol-p2-v1, g-supertrend-btc-p0-v1, g-supertrend-btc-p1-v1, g-supertrend-btc-p2-v1, g-supertrend-eth-p0-v1, g-supertrend-eth-p1-v1, g-supertrend-eth-p2-v1, g-supertrend-sol-p0-v1, g-supertrend-sol-p1-v1, g-supertrend-sol-p2-v1, g-weekly-btc-p0-v1, g-weekly-btc-p1-v1, g-weekly-btc-p2-v1, g-weekly-eth-p0-v1, g-weekly-eth-p1-v1, g-weekly-eth-p2-v1, g-weekly-sol-p0-v1, g-weekly-sol-p1-v1, g-weekly-sol-p2-v1, l1-supertrend1h-v1, l2-macd4h-v1, l4-weekly1d-v1, n1-tsmom-mh1h-v1, n7-xsmom72h-v1, s1-donchian40-ablation-v1, s4-ewmac-riskcap-noadd-ablation-v1, sp-donchian5m-hype-v1, sp-donchian5m-ubtc-v1, sp-donchian5m-ueth-v1, sp-donchian5m-usol-v1, sp-ema15m-hype-v1, sp-ema15m-ubtc-v1, sp-ema15m-ueth-v1, sp-ema15m-usol-v1
