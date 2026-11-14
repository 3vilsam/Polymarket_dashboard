# PAPER league — 100 virtual USDC perp books + 16.24 virtual USDC spot books

Updated 2026-11-15T07:52:02+08:00 MYT | tick 462 | 125 books (107 perp @100 USDC, 18 spot @16.24 USDC; incl. 9 v4 research-sweep books registered 12 Nov 2026) | public reads only

Spot research books use 5m/15m/1h timeframes. Do not compare raw Net MTM USDC across the 100-USDC and 16.24-USDC tables. An 'Early read (not evidence)' table lists fast books with >=10 closed trades; it is not the promotion bar. Ranks use net MTM (open exit cost not deducted). Gate comparisons use same-start indicative exit equity: perp books deduct taker+2bp; spot books deduct official tier-0 spot taker 0.070%+2bp. Official promotion controls remain the BTC-perp hold and random-entry books.

## Controls / luck benchmarks (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | c1-random15m-v1 | 3 | +1.8610 | 66.6667 | 40.9013 | 0.6560 | 0.4906 | 0.1342 | +0.0006 | +15.0901 | +0.0000 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); CONTROL |
| 2 | b0-btc-1x-hold-control-v1 | 0 | -13.2360 | — | — | 15.3211 | — | 0.0450 | -0.0662 | +0.0000 | -15.0901 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); CONTROL; NONTRADABLE risk-exempt |

## Fast / short-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | g-vwap-eth-p0-v1 | 8 | +1.3705 | 62.5000 | 2.3048 | 1.9503 | 0.1713 | 0.4395 | +0.0059 | +14.6278 | -0.4623 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-ema-sol-p1-v1 [cluster:TREND] | 2 | +1.3031 | 50.0000 | 3.7267 | 0.9790 | 0.6516 | 0.0920 | +0.0023 | +14.5604 | -0.5296 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | g-squeeze-sol-p0-v1 | 9 | +0.9626 | 33.3333 | 1.5611 | 1.4996 | 0.1070 | 0.5969 | -0.0026 | +14.2199 | -0.8702 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | g-vwap-eth-p2-v1 | 8 | +0.5882 | 50.0000 | 1.1384 | 2.6304 | 0.0339 | 0.4289 | +0.0005 | +13.8279 | -1.2622 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | g-squeeze-sol-p1-v1 | 7 | +0.4917 | 28.5714 | 1.3981 | 1.4996 | 0.0702 | 0.4652 | -0.0009 | +13.7490 | -1.3410 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | g-ema-btc-p2-v1 [cluster:TREND] | 2 | +0.3681 | 50.0000 | 1.7683 | 1.3431 | 0.1840 | 0.0970 | +0.0025 | +13.6254 | -1.4647 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | g-rsi2-eth-p0-v1 | 3 | +0.3097 | 66.6667 | 12.1631 | 0.4654 | 0.1032 | 0.1651 | +0.0001 | +13.5670 | -1.5231 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | g-rsi2-eth-p2-v1 | 1 | +0.2884 | 100.0000 | inf | 0.0632 | 0.2884 | 0.0469 | +0.0000 | +13.5457 | -1.5444 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | g-rsi2-btc-p2-v1 | 2 | +0.1809 | 100.0000 | inf | 0.5796 | 0.0904 | 0.1123 | +0.0007 | +13.4382 | -1.6519 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | g-rsi2-sol-p2-v1 | 3 | +0.0976 | 66.6667 | 1.3923 | 0.6027 | 0.0325 | 0.1578 | +0.0003 | +13.3549 | -1.7352 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | g-rsi2-btc-p0-v1 | 2 | +0.0821 | 50.0000 | 2.1660 | 0.1520 | 0.0410 | 0.1220 | +0.0000 | +13.3394 | -1.7507 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-vwap-eth-p1-v1 | 9 | +0.0411 | 44.4444 | 1.0169 | 3.4650 | 0.0046 | 0.4478 | +0.0066 | +13.2984 | -1.7917 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-ema-eth-p1-v1 [cluster:TREND] | 2 | +0.0291 | 50.0000 | 1.0608 | 0.9248 | 0.0146 | 0.0948 | +0.0004 | +13.2864 | -1.8036 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-rsi2-sol-p0-v1 | 2 | +0.0234 | 50.0000 | 1.0942 | 0.6032 | 0.0117 | 0.1128 | +0.0003 | +13.2807 | -1.8094 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | f4-ema15m-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-ema-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-ema-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-ema-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-ema-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-asia-btc-p0-v1 | 1 | -0.0076 | 0.0000 | 0.0000 | 0.2813 | -0.0076 | 0.0668 | +0.0021 | +13.2497 | -1.8404 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-asia-btc-p1-v1 | 1 | -0.0076 | 0.0000 | 0.0000 | 0.2813 | -0.0076 | 0.0668 | +0.0021 | +13.2497 | -1.8404 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-asia-btc-p2-v1 | 1 | -0.0076 | 0.0000 | 0.0000 | 0.2813 | -0.0076 | 0.0668 | +0.0021 | +13.2497 | -1.8404 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | f3-rsi2-5m-v1 | 4 | -0.1176 | 50.0000 | 0.6317 | 0.7137 | -0.0294 | 0.2405 | +0.0001 | +13.1397 | -1.9503 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-asia-eth-p0-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +13.1280 | -1.9621 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | g-asia-eth-p1-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +13.1280 | -1.9621 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-asia-eth-p2-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +13.1280 | -1.9621 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-squeeze-btc-p1-v1 | 5 | -0.1366 | 20.0000 | 0.8415 | 0.9097 | -0.0273 | 0.3320 | +0.0001 | +13.1207 | -1.9694 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-rsi2-btc-p1-v1 | 2 | -0.2472 | 0.0000 | 0.0000 | 0.3991 | -0.1236 | 0.1336 | +0.0000 | +13.0100 | -2.0800 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-rsi2-eth-p1-v1 | 4 | -0.3094 | 50.0000 | 0.4504 | 0.5330 | -0.0774 | 0.2124 | +0.0000 | +12.9479 | -2.1422 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-ema-all-p1-v1 [cluster:TREND] | 3 | -0.4478 | 33.3333 | 0.5305 | 1.3432 | -0.1493 | 0.1616 | -0.0004 | +12.8095 | -2.2806 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-ema-btc-p1-v1 [cluster:TREND] | 1 | -0.4760 | 0.0000 | 0.0000 | 0.4978 | -0.4760 | 0.0671 | +0.0000 | +12.7813 | -2.3088 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | n4-utc21-btc-v1 [cluster:BTC_FRI21] | 1 | -0.4838 | 0.0000 | 0.0000 | 0.4998 | -0.4838 | 0.0196 | +0.0000 | +12.4160 | -2.3166 | 434 | — | 2 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-ema-sol-p2-v1 [cluster:TREND] | 1 | -0.4850 | 0.0000 | 0.0000 | 1.5814 | -0.4850 | 0.0387 | -0.0006 | +12.7723 | -2.3178 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | f2-asia15m-v1 | 2 | -0.4854 | 0.0000 | 0.0000 | 0.8244 | -0.2427 | 0.1140 | +0.0022 | +12.7719 | -2.3182 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-asia-all-p1-v1 | 2 | -0.4854 | 0.0000 | 0.0000 | 0.8244 | -0.2427 | 0.1140 | +0.0022 | +12.7719 | -2.3182 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | g-squeeze-btc-p0-v1 | 8 | -0.7698 | 12.5000 | 0.4828 | 1.5361 | -0.0962 | 0.5300 | +0.0009 | +12.4875 | -2.6026 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 37 | g-rsi2-all-p1-v1 | 5 | -0.7825 | 40.0000 | 0.2444 | 0.9174 | -0.1565 | 0.2546 | +0.0003 | +12.4748 | -2.6153 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-asia-sol-p0-v1 | 2 | -0.8276 | 0.0000 | 0.0000 | 1.0277 | -0.4138 | 0.1038 | +0.0005 | +12.4297 | -2.6604 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | g-asia-sol-p1-v1 | 2 | -0.8276 | 0.0000 | 0.0000 | 1.0277 | -0.4138 | 0.1038 | +0.0005 | +12.4297 | -2.6604 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | g-asia-sol-p2-v1 | 2 | -0.8276 | 0.0000 | 0.0000 | 1.0277 | -0.4138 | 0.1038 | +0.0005 | +12.4297 | -2.6604 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | g-vwap-btc-p1-v1 | 10 | -0.8882 | 50.0000 | 0.5564 | 2.1378 | -0.0888 | 0.5757 | -0.0061 | +12.3691 | -2.7210 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | g-rsi2-sol-p1-v1 | 4 | -0.9317 | 25.0000 | 0.0918 | 1.0662 | -0.2329 | 0.2056 | +0.0003 | +12.3256 | -2.7645 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | g-vwap-btc-p0-v1 | 7 | -1.0954 | 42.8571 | 0.3234 | 1.6080 | -0.1565 | 0.4104 | -0.0037 | +12.1619 | -2.9282 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | g-squeeze-sol-p2-v1 | 10 | -1.1563 | 30.0000 | 0.5064 | 2.1547 | -0.1156 | 0.6676 | -0.0003 | +12.1010 | -2.9890 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | g-squeeze-eth-p2-v1 | 6 | -1.1797 | 16.6667 | 0.1113 | 1.2631 | -0.1966 | 0.4017 | -0.0002 | +12.0775 | -3.0125 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 46 | g-vwap-btc-p2-v1 | 5 | -1.2767 | 0.0000 | 0.0000 | 2.1272 | -0.3147 | 0.3183 | -0.0021 | +11.9526 | -3.1375 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | g-squeeze-eth-p1-v1 | 6 | -1.3394 | 16.6667 | 0.0779 | 1.3394 | -0.2232 | 0.4002 | -0.0012 | +11.9179 | -3.1722 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 48 | g-vwap-sol-p2-v1 | 12 | -1.5140 | 33.3333 | 0.4341 | 3.8965 | -0.1593 | 0.6885 | +0.0026 | +11.7251 | -3.3650 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | g-vwap-sol-p0-v1 | 11 | -1.5574 | 36.3636 | 0.3921 | 4.1466 | -0.1627 | 0.6133 | +0.0031 | +11.6789 | -3.4112 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 50 | g-vwap-all-p1-v1 | 21 | -1.5836 | 38.0952 | 0.6805 | 4.9028 | -0.0754 | 1.1979 | +0.0016 | +11.6737 | -3.4164 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 51 | g-squeeze-eth-p0-v1 | 9 | -1.8974 | 22.2222 | 0.0862 | 2.1027 | -0.2108 | 0.5997 | -0.0014 | +11.3599 | -3.7302 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 52 | g-squeeze-btc-p2-v1 | 10 | -1.9771 | 20.0000 | 0.2991 | 2.1208 | -0.1977 | 0.6605 | -0.0063 | +11.2801 | -3.8099 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 53 | f1-vwap5m-v1 | 14 | -2.1834 | 35.7143 | 0.3280 | 4.5808 | -0.1726 | 0.8356 | +0.0005 | +11.0530 | -4.0371 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 54 | f5-squeeze1m-v1 | 11 | -2.1846 | 9.0909 | 0.0292 | 2.3893 | -0.1986 | 0.7295 | +0.0016 | +11.0727 | -4.0174 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 55 | g-vwap-sol-p1-v1 | 14 | -2.4589 | 35.7143 | 0.2925 | 3.2710 | -0.1756 | 0.7592 | +0.0011 | +10.7984 | -4.2917 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |

## Slow / long-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | l1-supertrend1h-v1 [cluster:TREND] | 1 | +0.3643 | 100.0000 | inf | 1.1588 | 0.3643 | 0.0214 | +0.0031 | +13.6215 | -1.4685 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-supertrend-sol-p0-v1 [cluster:TREND] | 1 | +0.3643 | 100.0000 | inf | 1.1588 | 0.3643 | 0.0214 | +0.0031 | +13.6215 | -1.4685 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | n1-tsmom-mh1h-v1 [cluster:TREND] | 1 | +0.3606 | 100.0000 | inf | 0.8811 | 0.3606 | 0.0163 | +0.0022 | +13.2603 | -1.4722 | 434 | — | 2 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | s1-donchian40-ablation-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | s2-bb40-ema200-ablation-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | s4-ewmac-riskcap-noadd-ablation-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | r1-trend-rsi-pullback-market-lane-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | l2-macd4h-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | l3-funding1h-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | l4-weekly1d-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | g-supertrend-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-supertrend-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-supertrend-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-supertrend-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-supertrend-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-supertrend-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-supertrend-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-supertrend-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-macd-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-macd-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-macd-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-macd-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-macd-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-macd-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | g-macd-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-macd-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-macd-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-funding-btc-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-funding-btc-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-funding-btc-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-funding-eth-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-funding-eth-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-funding-eth-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | g-funding-sol-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-funding-sol-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | g-funding-sol-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 37 | g-weekly-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-weekly-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | g-weekly-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | g-weekly-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | g-weekly-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | g-weekly-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | g-weekly-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | g-weekly-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | g-weekly-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.2573 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 46 | n3-negfund-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.8998 | -1.8328 | 434 | — | 2 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | n5-weekend-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.8998 | -1.8328 | 434 | — | 2 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 48 | n6-ethbtc-z1h-v1 [UNHEDGED_ETH_DIRECTIONAL] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.8998 | -1.8328 | 434 | — | 2 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | n7-xsmom72h-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.8998 | -1.8328 | 434 | — | 2 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 50 | n2-shockrev1h-v1 [cluster:SHOCKREV] | 0 | -0.1769 | — | — | 0.3765 | — | 0.0067 | -0.0000 | +12.7133 | -2.0193 | 434 | — | 2 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |

## Spot buy-and-hold controls (16.24 virtual USDC, 1x long, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-hold-usol-v1 (RETIRED_DATA_QUALITY) | 1 | -0.0166 | 0.0000 | 0.0000 | 3.9287 | -0.0166 | 0.0226 | +0.0000 | +12.8854 | -1.9352 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 2 | sp-hold-hype-v1 | 0 | -1.6571 | — | — | 19.4142 | — | 0.0110 | +0.0000 | +2.7060 | -12.1146 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 3 | sp-hold-ubtc-v1 | 0 | -2.1048 | — | — | 15.1740 | — | 0.0113 | +0.0000 | -0.0509 | -14.8716 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 4 | sp-hold-ueth-v1 | 0 | -2.2606 | — | — | 17.2803 | — | 0.0114 | +0.0000 | -1.0094 | -15.8300 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |

## Spot fast / 5m and 15m (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-ema15m-ubtc-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9878 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-ema15m-ueth-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9878 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-ema15m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9878 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-donchian5m-ubtc-v1 [cluster:TREND] | 1 | -0.0100 | 0.0000 | 0.0000 | 1.0251 | -0.0100 | 0.0223 | +0.0000 | +12.9261 | -1.8945 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | sp-donchian5m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 1 | -0.1128 | 0.0000 | 0.0000 | 1.0376 | -0.1128 | 0.0226 | +0.0000 | +12.2932 | -2.5274 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | sp-donchian5m-ueth-v1 [cluster:TREND] | 3 | -0.2184 | 33.3333 | 0.1658 | 1.7456 | -0.0728 | 0.0671 | +0.0000 | +11.6433 | -3.1773 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | sp-ema15m-hype-v1 [cluster:TREND] | 1 | -0.3205 | 0.0000 | 0.0000 | 4.2298 | -0.3205 | 0.0218 | +0.0000 | +11.0142 | -3.8064 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | sp-donchian5m-hype-v1 [cluster:TREND] | 2 | -0.3300 | 0.0000 | 0.0000 | 3.7718 | -0.1650 | 0.0438 | +0.0000 | +10.9560 | -3.8646 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | sp4-utc21-ubtc-v1 [NON_V1_RESEARCH, cluster:BTC_FRI21] | 1 | -0.3304 | 0.0000 | 0.0000 | 2.1185 | -0.3304 | 0.0225 | +0.0000 | +10.8651 | -3.8674 | 434 | — | 2 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |

## Spot slow / 1h (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-rsi1h-ubtc-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9878 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-rsi1h-ueth-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9878 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-rsi1h-usol-v1 (RETIRED_DATA_QUALITY) | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9878 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-rsi1h-hype-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9878 | -1.8328 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | sp4-shockrev1h-ubtc-v1 [NON_V1_RESEARCH, cluster:SHOCKREV] | 1 | -0.3852 | 0.0000 | 0.0000 | 2.4557 | -0.3852 | 0.0224 | +0.0000 | +10.5276 | -4.2049 | 434 | — | 2 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |

## Early read (not evidence)

Fast and spot_fast books with at least 10 closed trades, ranked by closed-trade count then net MTM after paid fees/funding (open exit cost not deducted). This is an operational early look so small-capital books can be watched before the 30-trade / DSR / fresh-OOS bar. It is **not** significance, **not** a PASS, and **does not** change the promotion bar. Nothing in this section is a CANDIDATE.

| Rank | Book | Lane | Closed | Net MTM USDC | Win % | Fees | Funding | Gate |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | g-vwap-all-p1-v1 | fast | 21 | -1.5836 | 38.0952 | 1.1979 | +0.0016 | NOT_SIGNIFICANT |
| 2 | f1-vwap5m-v1 | fast | 14 | -2.1834 | 35.7143 | 0.8356 | +0.0005 | NOT_SIGNIFICANT |
| 3 | g-vwap-sol-p1-v1 | fast | 14 | -2.4589 | 35.7143 | 0.7592 | +0.0011 | NOT_SIGNIFICANT |
| 4 | g-vwap-sol-p2-v1 | fast | 12 | -1.5140 | 33.3333 | 0.6885 | +0.0026 | NOT_SIGNIFICANT |
| 5 | g-vwap-sol-p0-v1 | fast | 11 | -1.5574 | 36.3636 | 0.6133 | +0.0031 | NOT_SIGNIFICANT |
| 6 | f5-squeeze1m-v1 | fast | 11 | -2.1846 | 9.0909 | 0.7295 | +0.0016 | NOT_SIGNIFICANT |
| 7 | g-vwap-btc-p1-v1 | fast | 10 | -0.8882 | 50.0000 | 0.5757 | -0.0061 | NOT_SIGNIFICANT |
| 8 | g-squeeze-sol-p2-v1 | fast | 10 | -1.1563 | 30.0000 | 0.6676 | -0.0003 | NOT_SIGNIFICANT |
| 9 | g-squeeze-btc-p2-v1 | fast | 10 | -1.9771 | 20.0000 | 0.6605 | -0.0063 | NOT_SIGNIFICANT |

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
