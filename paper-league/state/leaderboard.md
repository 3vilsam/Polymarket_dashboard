# PAPER league — 100 virtual USDC perp books + 16.24 virtual USDC spot books

Updated 2026-11-15T22:16:03+08:00 MYT | tick 618 | 125 books (107 perp @100 USDC, 18 spot @16.24 USDC; incl. 9 v4 research-sweep books registered 12 Nov 2026) | public reads only

Spot research books use 5m/15m/1h timeframes. Do not compare raw Net MTM USDC across the 100-USDC and 16.24-USDC tables. An 'Early read (not evidence)' table lists fast books with >=10 closed trades; it is not the promotion bar. Ranks use net MTM (open exit cost not deducted). Gate comparisons use same-start indicative exit equity: perp books deduct taker+2bp; spot books deduct official tier-0 spot taker 0.070%+2bp. Official promotion controls remain the BTC-perp hold and random-entry books.

## Controls / luck benchmarks (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | c1-random15m-v1 | 6 | +0.9829 | 50.0000 | 1.9641 | 1.7123 | 0.1638 | 0.2309 | -0.0001 | +12.7120 | +0.0000 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); CONTROL |
| 2 | b0-btc-1x-hold-control-v1 | 0 | -11.7075 | — | — | 16.9854 | — | 0.0450 | -0.0800 | +0.0000 | -12.7120 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); CONTROL; NONTRADABLE risk-exempt |

## Fast / short-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | g-ema-sol-p1-v1 [cluster:TREND] | 2 | +1.7273 | 50.0000 | 3.7267 | 0.9790 | 0.6516 | 0.1051 | +0.0018 | +13.4373 | +0.7252 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-vwap-eth-p0-v1 | 11 | +1.5286 | 63.6364 | 2.0621 | 2.2871 | 0.1490 | 0.6101 | +0.0067 | +13.2125 | +0.5004 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | g-vwap-eth-p2-v1 | 11 | +0.7218 | 54.5455 | 1.2950 | 2.6304 | 0.0656 | 0.5134 | +0.0012 | +12.4510 | -0.2610 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | g-ema-btc-p2-v1 [cluster:TREND] | 2 | +0.3524 | 50.0000 | 1.7683 | 1.3431 | 0.1840 | 0.1143 | +0.0001 | +12.0566 | -0.6554 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | g-ema-eth-p0-v1 [cluster:TREND] | 0 | +0.1415 | — | — | 0.5130 | — | 0.0162 | -0.0003 | +11.8471 | -0.8649 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | g-ema-eth-p2-v1 [cluster:TREND] | 0 | +0.1415 | — | — | 0.5130 | — | 0.0162 | -0.0003 | +11.8471 | -0.8649 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | g-vwap-eth-p1-v1 | 15 | +0.1220 | 53.3333 | 1.0417 | 3.4650 | 0.0095 | 0.7538 | +0.0072 | +11.8101 | -0.9019 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | g-ema-sol-p0-v1 [cluster:TREND] | 0 | -0.0029 | — | — | 0.3716 | — | 0.0117 | -0.0004 | +11.7094 | -1.0027 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | g-asia-btc-p0-v1 | 1 | -0.0076 | 0.0000 | 0.0000 | 0.2813 | -0.0076 | 0.0668 | +0.0021 | +11.7216 | -0.9904 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | g-asia-btc-p1-v1 | 1 | -0.0076 | 0.0000 | 0.0000 | 0.2813 | -0.0076 | 0.0668 | +0.0021 | +11.7216 | -0.9904 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | g-asia-btc-p2-v1 | 1 | -0.0076 | 0.0000 | 0.0000 | 0.2813 | -0.0076 | 0.0668 | +0.0021 | +11.7216 | -0.9904 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | f4-ema15m-v1 [cluster:TREND] | 0 | -0.0156 | — | — | 0.5311 | — | 0.0173 | -0.0024 | +11.6885 | -1.0235 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-ema-btc-p0-v1 [cluster:TREND] | 0 | -0.0156 | — | — | 0.5311 | — | 0.0173 | -0.0024 | +11.6885 | -1.0235 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-asia-eth-p0-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +11.5999 | -1.1122 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-asia-eth-p1-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +11.5999 | -1.1122 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-asia-eth-p2-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +11.5999 | -1.1122 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-squeeze-sol-p0-v1 | 18 | -0.1323 | 27.7778 | 0.9659 | 3.1837 | -0.0073 | 1.1978 | -0.0017 | +11.5969 | -1.1151 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-rsi2-eth-p2-v1 | 2 | -0.2057 | 50.0000 | 0.5837 | 0.5261 | -0.1028 | 0.0688 | +0.0000 | +11.5235 | -1.1885 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-rsi2-btc-p2-v1 | 3 | -0.3078 | 66.6667 | 0.3702 | 1.0646 | -0.1026 | 0.1389 | +0.0007 | +11.4214 | -1.2907 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-ema-eth-p1-v1 [cluster:TREND] | 3 | -0.3177 | 33.3333 | 0.5259 | 1.0838 | -0.1528 | 0.1481 | +0.0001 | +11.3880 | -1.3240 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-rsi2-sol-p2-v1 | 4 | -0.3841 | 50.0000 | 0.4742 | 1.0809 | -0.0960 | 0.1989 | +0.0003 | +11.3451 | -1.3669 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-rsi2-btc-p1-v1 | 7 | -0.4635 | 57.1429 | 0.3679 | 0.8211 | -0.0662 | 0.4173 | +0.0000 | +11.2657 | -1.4463 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | n4-utc21-btc-v1 [cluster:BTC_FRI21] | 1 | -0.4838 | 0.0000 | 0.0000 | 0.4998 | -0.4838 | 0.0196 | +0.0000 | +10.8816 | -1.4667 | 434 | — | 2 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | f2-asia15m-v1 | 2 | -0.4854 | 0.0000 | 0.0000 | 0.8244 | -0.2427 | 0.1140 | +0.0022 | +11.2437 | -1.4683 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | g-asia-all-p1-v1 | 2 | -0.4854 | 0.0000 | 0.0000 | 0.8244 | -0.2427 | 0.1140 | +0.0022 | +11.2437 | -1.4683 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-ema-sol-p2-v1 [cluster:TREND] | 1 | -0.4879 | 0.0000 | 0.0000 | 1.7949 | -0.4850 | 0.0504 | -0.0011 | +11.2244 | -1.4877 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-rsi2-eth-p0-v1 | 5 | -0.5634 | 40.0000 | 0.3746 | 1.3318 | -0.1127 | 0.2332 | +0.0001 | +11.1658 | -1.5462 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-rsi2-eth-p1-v1 | 7 | -0.7735 | 42.8571 | 0.2952 | 0.9867 | -0.1076 | 0.3938 | +0.0000 | +10.9150 | -1.7971 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-rsi2-btc-p0-v1 | 6 | -0.8124 | 33.3333 | 0.2327 | 1.0859 | -0.1354 | 0.3331 | +0.0000 | +10.9168 | -1.7952 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-asia-sol-p0-v1 | 2 | -0.8276 | 0.0000 | 0.0000 | 1.0277 | -0.4138 | 0.1038 | +0.0005 | +10.9016 | -1.8105 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-asia-sol-p1-v1 | 2 | -0.8276 | 0.0000 | 0.0000 | 1.0277 | -0.4138 | 0.1038 | +0.0005 | +10.9016 | -1.8105 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-asia-sol-p2-v1 | 2 | -0.8276 | 0.0000 | 0.0000 | 1.0277 | -0.4138 | 0.1038 | +0.0005 | +10.9016 | -1.8105 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-squeeze-btc-p2-v1 | 17 | -0.9329 | 29.4118 | 0.7848 | 2.3161 | -0.0552 | 1.1540 | -0.0054 | +10.7483 | -1.9637 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | g-ema-all-p1-v1 [cluster:TREND] | 4 | -0.9416 | 25.0000 | 0.3533 | 1.3432 | -0.2315 | 0.2183 | -0.0020 | +10.7630 | -1.9490 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-rsi2-sol-p0-v1 | 4 | -0.9681 | 25.0000 | 0.2244 | 1.6311 | -0.2351 | 0.1992 | +0.0003 | +10.7240 | -1.9880 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | g-ema-btc-p1-v1 [cluster:TREND] | 2 | -0.9697 | 0.0000 | 0.0000 | 1.0659 | -0.4772 | 0.1237 | -0.0016 | +10.7348 | -1.9772 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 37 | g-squeeze-sol-p1-v1 | 12 | -1.1833 | 16.6667 | 0.5934 | 2.8197 | -0.0986 | 0.7991 | -0.0009 | +10.5459 | -2.1662 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-squeeze-sol-p2-v1 | 14 | -1.1853 | 28.5714 | 0.5705 | 2.4338 | -0.0960 | 0.9605 | +0.0004 | +10.4974 | -2.2146 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | g-vwap-btc-p0-v1 | 9 | -1.2322 | 44.4444 | 0.3655 | 2.1893 | -0.1477 | 0.5575 | -0.0037 | +10.4491 | -2.2630 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | g-squeeze-btc-p1-v1 | 14 | -1.3808 | 21.4286 | 0.4970 | 2.0509 | -0.0991 | 0.9609 | +0.0001 | +10.3009 | -2.4111 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | g-vwap-btc-p1-v1 | 14 | -1.4424 | 50.0000 | 0.4810 | 2.6612 | -0.1099 | 0.8003 | -0.0061 | +10.2392 | -2.4728 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | f3-rsi2-5m-v1 | 8 | -1.4944 | 37.5000 | 0.1673 | 2.2184 | -0.1834 | 0.4509 | +0.0001 | +10.1977 | -2.5144 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | g-squeeze-eth-p1-v1 | 11 | -1.5506 | 27.2727 | 0.3798 | 2.1065 | -0.1410 | 0.7300 | -0.0019 | +10.1785 | -2.5335 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | g-rsi2-sol-p1-v1 | 7 | -1.8461 | 28.5714 | 0.0825 | 1.9797 | -0.2598 | 0.3453 | +0.0003 | +9.8465 | -2.8655 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | g-rsi2-all-p1-v1 | 12 | -1.9594 | 50.0000 | 0.2093 | 2.2269 | -0.1633 | 0.5943 | +0.0003 | +9.7697 | -2.9423 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 46 | g-vwap-btc-p2-v1 | 8 | -2.0732 | 12.5000 | 0.1625 | 2.4024 | -0.2592 | 0.4473 | -0.0032 | +9.6560 | -3.0561 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | g-squeeze-btc-p0-v1 | 18 | -2.1444 | 16.6667 | 0.3878 | 2.2093 | -0.1195 | 1.2194 | +0.0009 | +9.5377 | -3.1743 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 48 | f5-squeeze1m-v1 | 11 | -2.1846 | 9.0909 | 0.0292 | 2.3893 | -0.1986 | 0.7295 | +0.0016 | +9.5445 | -3.1675 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 49 | g-squeeze-eth-p2-v1 | 9 | -2.3227 | 11.1111 | 0.0598 | 2.4051 | -0.2581 | 0.6001 | -0.0002 | +9.4064 | -3.3056 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 50 | g-vwap-all-p1-v1 | 23 | -2.5372 | 34.7826 | 0.5707 | 5.3758 | -0.1103 | 1.2576 | +0.0016 | +9.1919 | -3.5201 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 51 | g-vwap-sol-p2-v1 | 16 | -2.5634 | 31.2500 | 0.4219 | 4.6910 | -0.1602 | 0.8066 | +0.0022 | +9.1658 | -3.5462 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 52 | f1-vwap5m-v1 | 20 | -2.6665 | 40.0000 | 0.4418 | 5.0345 | -0.1381 | 1.1100 | +0.0006 | +9.0156 | -3.6965 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 53 | g-vwap-sol-p0-v1 | 15 | -2.9076 | 33.3333 | 0.3243 | 5.0145 | -0.1938 | 0.7377 | +0.0026 | +8.8216 | -3.8904 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 54 | g-squeeze-eth-p0-v1 | 17 | -3.1729 | 23.5294 | 0.2410 | 3.3755 | -0.1866 | 1.1229 | -0.0012 | +8.5562 | -4.1558 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 55 | g-vwap-sol-p1-v1 | 17 | -3.3817 | 35.2941 | 0.2392 | 4.0909 | -0.1973 | 0.9091 | +0.0015 | +8.3113 | -4.4007 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |

## Slow / long-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | l1-supertrend1h-v1 [cluster:TREND] | 1 | +0.3643 | 100.0000 | inf | 1.1588 | 0.3643 | 0.0214 | +0.0031 | +12.0934 | -0.6186 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-supertrend-sol-p0-v1 [cluster:TREND] | 1 | +0.3643 | 100.0000 | inf | 1.1588 | 0.3643 | 0.0214 | +0.0031 | +12.0934 | -0.6186 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | n1-tsmom-mh1h-v1 [cluster:TREND] | 1 | +0.3606 | 100.0000 | inf | 0.8811 | 0.3606 | 0.0163 | +0.0022 | +11.7259 | -0.6223 | 434 | — | 2 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | g-supertrend-sol-p1-v1 [cluster:TREND] | 0 | +0.0025 | — | — | 0.1655 | — | 0.0052 | -0.0001 | +11.7242 | -0.9879 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | s1-donchian40-ablation-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | s2-bb40-ema200-ablation-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | s4-ewmac-riskcap-noadd-ablation-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | r1-trend-rsi-pullback-market-lane-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | l2-macd4h-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | l3-funding1h-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | l4-weekly1d-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-supertrend-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-supertrend-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-supertrend-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-supertrend-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-supertrend-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-supertrend-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-macd-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-macd-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-macd-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-macd-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-macd-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-macd-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-macd-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | g-macd-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-macd-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-funding-btc-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-funding-btc-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-funding-btc-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-funding-eth-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-funding-eth-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-funding-eth-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-funding-sol-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | g-funding-sol-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-funding-sol-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | g-weekly-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 37 | g-weekly-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-weekly-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | g-weekly-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | g-weekly-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | g-weekly-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | g-weekly-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | g-weekly-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | g-weekly-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7292 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | n3-negfund-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.3654 | -0.9829 | 434 | — | 2 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 46 | n5-weekend-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.3654 | -0.9829 | 434 | — | 2 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | n6-ethbtc-z1h-v1 [UNHEDGED_ETH_DIRECTIONAL] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.3654 | -0.9829 | 434 | — | 2 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 48 | n7-xsmom72h-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.3654 | -0.9829 | 434 | — | 2 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | g-supertrend-btc-p2-v1 [cluster:TREND] | 0 | -0.0833 | — | — | 0.1425 | — | 0.0068 | -0.0006 | +11.6361 | -1.0759 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 50 | n2-shockrev1h-v1 [cluster:SHOCKREV] | 1 | -0.4808 | 0.0000 | 0.0000 | 0.4916 | -0.4808 | 0.0132 | -0.0003 | +10.8846 | -1.4636 | 434 | — | 2 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |

## Spot buy-and-hold controls (16.24 virtual USDC, 1x long, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-hold-usol-v1 (RETIRED_DATA_QUALITY) | 1 | -0.0166 | 0.0000 | 0.0000 | 3.9287 | -0.0166 | 0.0226 | +0.0000 | +11.3526 | -1.0853 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 2 | sp-hold-hype-v1 | 0 | -0.9276 | — | — | 19.4142 | — | 0.0110 | +0.0000 | +5.6605 | -6.7773 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 3 | sp-hold-ubtc-v1 | 0 | -1.8496 | — | — | 16.5977 | — | 0.0113 | +0.0000 | -0.0138 | -12.4516 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 4 | sp-hold-ueth-v1 | 0 | -1.8624 | — | — | 18.4092 | — | 0.0114 | +0.0000 | -0.0928 | -12.5306 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |

## Spot fast / 5m and 15m (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-donchian5m-ueth-v1 [cluster:TREND] | 5 | +0.3116 | 60.0000 | 2.1904 | 1.7456 | 0.0623 | 0.1127 | +0.0000 | +13.3736 | +0.9358 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-ema15m-ueth-v1 [cluster:TREND] | 0 | +0.0567 | — | — | 1.5047 | — | 0.0113 | +0.0000 | +11.7143 | -0.7236 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-ema15m-hype-v1 [cluster:TREND] | 1 | +0.0551 | 0.0000 | 0.0000 | 4.3306 | -0.3205 | 0.0329 | +0.0000 | +11.7045 | -0.7333 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-donchian5m-ubtc-v1 [cluster:TREND] | 3 | +0.0034 | 33.3333 | 1.0310 | 1.8437 | 0.0011 | 0.0670 | +0.0000 | +11.4760 | -0.9618 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | sp-ema15m-ubtc-v1 [cluster:TREND] | 0 | +0.0010 | — | — | 1.2926 | — | 0.0110 | +0.0000 | +11.3745 | -1.0633 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | sp-ema15m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.4550 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | sp-donchian5m-hype-v1 [cluster:TREND] | 4 | -0.0366 | 25.0000 | 0.9190 | 3.8732 | -0.0092 | 0.0883 | +0.0000 | +11.2295 | -1.2083 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | sp-donchian5m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 1 | -0.1128 | 0.0000 | 0.0000 | 1.0376 | -0.1128 | 0.0226 | +0.0000 | +10.7603 | -1.6775 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | sp4-utc21-ubtc-v1 [NON_V1_RESEARCH, cluster:BTC_FRI21] | 1 | -0.3304 | 0.0000 | 0.0000 | 2.1185 | -0.3304 | 0.0225 | +0.0000 | +9.3307 | -3.0175 | 434 | — | 2 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |

## Spot slow / 1h (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-rsi1h-ubtc-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.4550 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-rsi1h-ueth-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.4550 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-rsi1h-usol-v1 (RETIRED_DATA_QUALITY) | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.4550 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-rsi1h-hype-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.4550 | -0.9829 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | sp4-shockrev1h-ubtc-v1 [NON_V1_RESEARCH, cluster:SHOCKREV] | 1 | -0.3852 | 0.0000 | 0.0000 | 2.4557 | -0.3852 | 0.0224 | +0.0000 | +8.9932 | -3.3550 | 434 | — | 2 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |

## Early read (not evidence)

Fast and spot_fast books with at least 10 closed trades, ranked by closed-trade count then net MTM after paid fees/funding (open exit cost not deducted). This is an operational early look so small-capital books can be watched before the 30-trade / DSR / fresh-OOS bar. It is **not** significance, **not** a PASS, and **does not** change the promotion bar. Nothing in this section is a CANDIDATE.

| Rank | Book | Lane | Closed | Net MTM USDC | Win % | Fees | Funding | Gate |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | g-vwap-all-p1-v1 | fast | 23 | -2.5372 | 34.7826 | 1.2576 | +0.0016 | NOT_SIGNIFICANT |
| 2 | f1-vwap5m-v1 | fast | 20 | -2.6665 | 40.0000 | 1.1100 | +0.0006 | NOT_SIGNIFICANT |
| 3 | g-squeeze-sol-p0-v1 | fast | 18 | -0.1323 | 27.7778 | 1.1978 | -0.0017 | NOT_SIGNIFICANT |
| 4 | g-squeeze-btc-p0-v1 | fast | 18 | -2.1444 | 16.6667 | 1.2194 | +0.0009 | NOT_SIGNIFICANT |
| 5 | g-squeeze-btc-p2-v1 | fast | 17 | -0.9329 | 29.4118 | 1.1540 | -0.0054 | NOT_SIGNIFICANT |
| 6 | g-squeeze-eth-p0-v1 | fast | 17 | -3.1729 | 23.5294 | 1.1229 | -0.0012 | NOT_SIGNIFICANT |
| 7 | g-vwap-sol-p1-v1 | fast | 17 | -3.3817 | 35.2941 | 0.9091 | +0.0015 | NOT_SIGNIFICANT |
| 8 | g-vwap-sol-p2-v1 | fast | 16 | -2.5634 | 31.2500 | 0.8066 | +0.0022 | NOT_SIGNIFICANT |
| 9 | g-vwap-eth-p1-v1 | fast | 15 | +0.1220 | 53.3333 | 0.7538 | +0.0072 | NOT_SIGNIFICANT |
| 10 | g-vwap-sol-p0-v1 | fast | 15 | -2.9076 | 33.3333 | 0.7377 | +0.0026 | NOT_SIGNIFICANT |
| 11 | g-squeeze-sol-p2-v1 | fast | 14 | -1.1853 | 28.5714 | 0.9605 | +0.0004 | NOT_SIGNIFICANT |
| 12 | g-squeeze-btc-p1-v1 | fast | 14 | -1.3808 | 21.4286 | 0.9609 | +0.0001 | NOT_SIGNIFICANT |
| 13 | g-vwap-btc-p1-v1 | fast | 14 | -1.4424 | 50.0000 | 0.8003 | -0.0061 | NOT_SIGNIFICANT |
| 14 | g-squeeze-sol-p1-v1 | fast | 12 | -1.1833 | 16.6667 | 0.7991 | -0.0009 | NOT_SIGNIFICANT |
| 15 | g-rsi2-all-p1-v1 | fast | 12 | -1.9594 | 50.0000 | 0.5943 | +0.0003 | NOT_SIGNIFICANT |
| 16 | g-vwap-eth-p0-v1 | fast | 11 | +1.5286 | 63.6364 | 0.6101 | +0.0067 | NOT_SIGNIFICANT |
| 17 | g-vwap-eth-p2-v1 | fast | 11 | +0.7218 | 54.5455 | 0.5134 | +0.0012 | NOT_SIGNIFICANT |
| 18 | g-squeeze-eth-p1-v1 | fast | 11 | -1.5506 | 27.2727 | 0.7300 | -0.0019 | NOT_SIGNIFICANT |
| 19 | f5-squeeze1m-v1 | fast | 11 | -2.1846 | 9.0909 | 0.7295 | +0.0016 | NOT_SIGNIFICANT |

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
