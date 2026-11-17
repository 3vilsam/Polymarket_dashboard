# PAPER league — 100 virtual USDC perp books + 16.24 virtual USDC spot books

Updated 2026-11-17T11:39:03+08:00 MYT | tick 953 | 125 books (107 perp @100 USDC, 18 spot @16.24 USDC; incl. 9 v4 research-sweep books registered 12 Nov 2026) | public reads only

Spot research books use 5m/15m/1h timeframes. Do not compare raw Net MTM USDC across the 100-USDC and 16.24-USDC tables. An 'Early read (not evidence)' table lists fast books with >=10 closed trades; it is not the promotion bar. Ranks use net MTM (open exit cost not deducted). Gate comparisons use same-start indicative exit equity: perp books deduct taker+2bp; spot books deduct official tier-0 spot taker 0.070%+2bp. Official promotion controls remain the BTC-perp hold and random-entry books.

## Controls / luck benchmarks (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | c1-random15m-v1 | 13 | +0.7637 | 46.1538 | 1.4567 | 2.0147 | 0.0587 | 0.4999 | -0.0004 | +12.8316 | +0.0000 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); CONTROL |
| 2 | b0-btc-1x-hold-control-v1 | 0 | -12.0463 | — | — | 16.9854 | — | 0.0450 | -0.1086 | +0.0000 | -12.8316 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); CONTROL; NONTRADABLE risk-exempt |

## Fast / short-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | g-vwap-eth-p2-v1 | 21 | +3.0617 | 66.6667 | 2.0148 | 2.6304 | 0.1458 | 1.1470 | +0.0040 | +15.1296 | +2.2980 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-vwap-eth-p0-v1 | 26 | +2.1099 | 65.3846 | 1.5588 | 2.2871 | 0.0811 | 1.5226 | +0.0089 | +14.1777 | +1.3461 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | g-vwap-eth-p1-v1 | 30 | +1.4086 | 63.3333 | 1.2745 | 3.4650 | 0.0470 | 1.6734 | +0.0095 | +13.4765 | +0.6449 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |
| 4 | g-ema-sol-p1-v1 [cluster:TREND] | 6 | -0.1136 | 33.3333 | 0.9415 | 2.1965 | -0.0189 | 0.2263 | -0.0014 | +11.9543 | -0.8773 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | g-asia-eth-p0-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +11.9386 | -0.8930 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | g-asia-eth-p1-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +11.9386 | -0.8930 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | g-asia-eth-p2-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +11.9386 | -0.8930 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | g-rsi2-eth-p2-v1 | 2 | -0.2057 | 50.0000 | 0.5837 | 0.5261 | -0.1028 | 0.0688 | +0.0000 | +11.8622 | -0.9694 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | g-rsi2-btc-p1-v1 | 10 | -0.2717 | 70.0000 | 0.6295 | 0.8211 | -0.0272 | 0.6166 | +0.0000 | +11.7962 | -1.0354 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | g-rsi2-btc-p2-v1 | 4 | -0.2851 | 75.0000 | 0.4166 | 1.1377 | -0.0713 | 0.2053 | +0.0007 | +11.7827 | -1.0489 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | g-rsi2-sol-p2-v1 | 4 | -0.3841 | 50.0000 | 0.4742 | 1.0809 | -0.0960 | 0.1989 | +0.0003 | +11.6838 | -1.1478 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | n4-utc21-btc-v1 [cluster:BTC_FRI21] | 2 | -0.4512 | 50.0000 | 0.0673 | 0.5879 | -0.2256 | 0.0408 | -0.0003 | +11.2542 | -1.2150 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-rsi2-eth-p0-v1 | 6 | -0.5659 | 33.3333 | 0.3736 | 1.4383 | -0.0943 | 0.2999 | +0.0001 | +11.5020 | -1.3296 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-squeeze-sol-p2-v1 | 27 | -0.7142 | 37.0370 | 0.8708 | 3.0069 | -0.0265 | 1.7933 | -0.0017 | +11.3536 | -1.4780 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-asia-btc-p0-v1 | 3 | -0.7269 | 0.0000 | 0.0000 | 0.9987 | -0.2423 | 0.1615 | +0.0021 | +11.3409 | -1.4907 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-asia-btc-p2-v1 | 3 | -0.7269 | 0.0000 | 0.0000 | 0.9987 | -0.2423 | 0.1615 | +0.0021 | +11.3409 | -1.4907 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-rsi2-eth-p1-v1 | 10 | -0.7659 | 50.0000 | 0.3897 | 1.0885 | -0.0766 | 0.5552 | +0.0000 | +11.3020 | -1.5296 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-rsi2-btc-p0-v1 | 8 | -0.7660 | 37.5000 | 0.3106 | 1.0859 | -0.0958 | 0.4656 | +0.0000 | +11.3018 | -1.5298 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-squeeze-btc-p2-v1 | 30 | -0.8666 | 36.6667 | 0.8470 | 2.3161 | -0.0289 | 1.9788 | -0.0122 | +11.2013 | -1.6304 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |
| 20 | g-asia-btc-p1-v1 | 4 | -0.8847 | 0.0000 | 0.0000 | 1.1560 | -0.2212 | 0.2103 | +0.0021 | +11.1832 | -1.6484 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-rsi2-sol-p0-v1 | 6 | -0.9101 | 33.3333 | 0.2610 | 1.6721 | -0.1517 | 0.2901 | +0.0003 | +11.1578 | -1.6739 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-ema-eth-p2-v1 [cluster:TREND] | 4 | -0.9506 | 0.0000 | 0.0000 | 1.7076 | -0.2376 | 0.1360 | -0.0029 | +11.1173 | -1.7143 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-ema-sol-p0-v1 [cluster:TREND] | 3 | -1.0369 | 0.0000 | 0.0000 | 1.3824 | -0.3456 | 0.0866 | -0.0005 | +11.0310 | -1.8007 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-ema-sol-p2-v1 [cluster:TREND] | 3 | -1.1676 | 0.0000 | 0.0000 | 2.3393 | -0.3892 | 0.0948 | -0.0009 | +10.9003 | -1.9313 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | f2-asia15m-v1 | 4 | -1.1995 | 0.0000 | 0.0000 | 1.3988 | -0.2999 | 0.2081 | +0.0022 | +10.8684 | -1.9632 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-asia-sol-p0-v1 | 3 | -1.2183 | 0.0000 | 0.0000 | 1.4176 | -0.4061 | 0.1365 | +0.0005 | +10.8496 | -1.9820 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-asia-sol-p1-v1 | 3 | -1.2183 | 0.0000 | 0.0000 | 1.4176 | -0.4061 | 0.1365 | +0.0005 | +10.8496 | -1.9820 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-asia-sol-p2-v1 | 3 | -1.2183 | 0.0000 | 0.0000 | 1.4176 | -0.4061 | 0.1365 | +0.0005 | +10.8496 | -1.9820 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-vwap-btc-p1-v1 | 26 | -1.2542 | 53.8462 | 0.7179 | 3.0700 | -0.0482 | 1.5499 | -0.0059 | +10.8137 | -2.0179 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-ema-btc-p2-v1 [cluster:TREND] | 6 | -1.2967 | 16.6667 | 0.3952 | 2.1685 | -0.2161 | 0.2751 | +0.0009 | +10.7712 | -2.0604 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-squeeze-sol-p1-v1 | 20 | -1.3271 | 20.0000 | 0.6914 | 3.0102 | -0.0664 | 1.3302 | -0.0016 | +10.7408 | -2.0908 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-asia-all-p1-v1 | 5 | -1.3572 | 0.0000 | 0.0000 | 1.5563 | -0.2714 | 0.2569 | +0.0022 | +10.7106 | -2.1210 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-ema-btc-p0-v1 [cluster:TREND] | 4 | -1.3978 | 0.0000 | 0.0000 | 1.8317 | -0.3494 | 0.1812 | -0.0023 | +10.6701 | -2.1615 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | f3-rsi2-5m-v1 | 12 | -1.4423 | 33.3333 | 0.2140 | 2.2184 | -0.1202 | 0.6741 | +0.0001 | +10.6256 | -2.2061 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-vwap-btc-p0-v1 | 22 | -1.5126 | 50.0000 | 0.6283 | 2.8246 | -0.0688 | 1.3628 | -0.0037 | +10.5553 | -2.2763 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | g-squeeze-sol-p0-v1 | 31 | -1.5800 | 22.5806 | 0.7603 | 3.9460 | -0.0510 | 2.0644 | -0.0012 | +10.4878 | -2.3438 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |
| 37 | g-ema-eth-p0-v1 [cluster:TREND] | 4 | -1.6133 | 0.0000 | 0.0000 | 2.1753 | -0.4033 | 0.1569 | +0.0002 | +10.4546 | -2.3770 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | f4-ema15m-v1 [cluster:TREND] | 5 | -1.8806 | 0.0000 | 0.0000 | 2.3123 | -0.3761 | 0.2179 | -0.0028 | +10.1873 | -2.6443 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | g-vwap-sol-p0-v1 | 27 | -2.0445 | 40.7407 | 0.6097 | 5.2270 | -0.0757 | 1.3612 | +0.0012 | +10.0233 | -2.8083 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | g-rsi2-sol-p1-v1 | 11 | -2.1438 | 18.1818 | 0.0709 | 2.2755 | -0.1949 | 0.5410 | +0.0003 | +9.9241 | -2.9075 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | g-ema-btc-p1-v1 [cluster:TREND] | 6 | -2.1515 | 0.0000 | 0.0000 | 2.2777 | -0.3280 | 0.3020 | +0.0013 | +9.8796 | -2.9520 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | g-rsi2-all-p1-v1 | 17 | -2.1754 | 47.0588 | 0.2426 | 2.4464 | -0.1280 | 0.8960 | +0.0003 | +9.8925 | -2.9391 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | f5-squeeze1m-v1 | 11 | -2.1846 | 9.0909 | 0.0292 | 2.3893 | -0.1986 | 0.7295 | +0.0016 | +9.8832 | -2.9484 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 44 | g-squeeze-eth-p2-v1 | 9 | -2.3227 | 11.1111 | 0.0598 | 2.4051 | -0.2581 | 0.6001 | -0.0002 | +9.7451 | -3.0865 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 45 | g-squeeze-btc-p0-v1 | 31 | -2.3955 | 25.8065 | 0.5256 | 3.2137 | -0.0773 | 2.0321 | -0.0051 | +9.6723 | -3.1593 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |
| 46 | g-squeeze-btc-p1-v1 | 20 | -2.5358 | 15.0000 | 0.3508 | 2.9991 | -0.1268 | 1.3215 | +0.0001 | +9.5320 | -3.2996 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | g-vwap-all-p1-v1 | 23 | -2.5372 | 34.7826 | 0.5707 | 5.3758 | -0.1103 | 1.2576 | +0.0016 | +9.5306 | -3.3010 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 48 | g-vwap-btc-p2-v1 | 18 | -2.6154 | 38.8889 | 0.3980 | 2.9428 | -0.1453 | 1.0984 | -0.0046 | +9.4525 | -3.3791 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | g-ema-eth-p1-v1 [cluster:TREND] | 9 | -2.6642 | 11.1111 | 0.1603 | 3.2481 | -0.2960 | 0.3712 | -0.0015 | +9.4037 | -3.4279 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 50 | g-vwap-sol-p2-v1 | 22 | -2.8187 | 31.8182 | 0.4499 | 5.1710 | -0.1281 | 1.1435 | +0.0015 | +9.2492 | -3.5825 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 51 | g-ema-all-p1-v1 [cluster:TREND] | 10 | -2.8883 | 10.0000 | 0.1491 | 3.0082 | -0.2888 | 0.4567 | -0.0002 | +9.1796 | -3.6520 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 52 | g-squeeze-eth-p1-v1 | 18 | -2.9467 | 22.2222 | 0.3273 | 3.4777 | -0.1637 | 1.1883 | -0.0026 | +9.1211 | -3.7105 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 53 | f1-vwap5m-v1 | 41 | -3.0955 | 48.7805 | 0.6354 | 5.6463 | -0.0755 | 2.3442 | +0.0028 | +8.9724 | -3.8592 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |
| 54 | g-squeeze-eth-p0-v1 | 17 | -3.1729 | 23.5294 | 0.2410 | 3.3755 | -0.1866 | 1.1229 | -0.0012 | +8.8949 | -3.9367 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 55 | g-vwap-sol-p1-v1 | 30 | -4.1016 | 40.0000 | 0.3941 | 4.9059 | -0.1367 | 1.5717 | +0.0015 | +7.9662 | -4.8654 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |

## Slow / long-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | l1-supertrend1h-v1 [cluster:TREND] | 1 | +0.3643 | 100.0000 | inf | 1.1588 | 0.3643 | 0.0214 | +0.0031 | +12.4321 | -0.3995 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-supertrend-sol-p0-v1 [cluster:TREND] | 1 | +0.3643 | 100.0000 | inf | 1.1588 | 0.3643 | 0.0214 | +0.0031 | +12.4321 | -0.3995 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | n1-tsmom-mh1h-v1 [cluster:TREND] | 3 | +0.2497 | 66.6667 | 2.9673 | 1.1001 | 0.0832 | 0.0435 | +0.0025 | +11.9551 | -0.5141 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | s1-donchian40-ablation-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | s2-bb40-ema200-ablation-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | r1-trend-rsi-pullback-market-lane-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | l2-macd4h-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | l3-funding1h-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | l4-weekly1d-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | g-supertrend-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | g-supertrend-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-supertrend-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-supertrend-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-supertrend-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-macd-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-macd-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-macd-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-macd-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-macd-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-macd-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-macd-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-macd-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-macd-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-funding-btc-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | g-funding-btc-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-funding-btc-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-funding-eth-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-funding-eth-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-funding-eth-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-funding-sol-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-funding-sol-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-funding-sol-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-weekly-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | g-weekly-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-weekly-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | g-weekly-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 37 | g-weekly-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-weekly-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | g-weekly-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | g-weekly-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | g-weekly-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.0679 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | n3-negfund-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7054 | -0.7637 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | n5-weekend-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7054 | -0.7637 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | n6-ethbtc-z1h-v1 [UNHEDGED_ETH_DIRECTIONAL] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7054 | -0.7637 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | s4-ewmac-riskcap-noadd-ablation-v1 [cluster:TREND] | 0 | -0.0297 | — | — | 0.1264 | — | 0.0047 | +0.0003 | +12.0314 | -0.8002 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 46 | g-supertrend-btc-p2-v1 [cluster:TREND] | 0 | -0.1408 | — | — | 0.4317 | — | 0.0068 | -0.0054 | +11.9173 | -0.9143 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | n7-xsmom72h-v1 [cluster:TREND] | 0 | -0.1980 | — | — | 0.2499 | — | 0.0055 | -0.0008 | +11.4994 | -0.9698 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 48 | g-supertrend-sol-p1-v1 [cluster:TREND] | 1 | -0.2468 | 0.0000 | 0.0000 | 0.4058 | -0.2468 | 0.0103 | +0.0004 | +11.8210 | -1.0106 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | n2-shockrev1h-v1 [cluster:SHOCKREV] | 1 | -0.4808 | 0.0000 | 0.0000 | 0.4916 | -0.4808 | 0.0132 | -0.0003 | +11.2247 | -1.2445 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 50 | g-supertrend-btc-p1-v1 [cluster:TREND] | 1 | -0.4810 | 0.0000 | 0.0000 | 0.6346 | -0.4810 | 0.0245 | +0.0012 | +11.5869 | -1.2447 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |

## Spot buy-and-hold controls (16.24 virtual USDC, 1x long, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-hold-usol-v1 (RETIRED_DATA_QUALITY) | 1 | -0.0166 | 0.0000 | 0.0000 | 3.9287 | -0.0166 | 0.0226 | +0.0000 | +11.6923 | -0.8661 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 2 | sp-hold-hype-v1 | 0 | -0.4276 | — | — | 19.4142 | — | 0.0110 | +0.0000 | +9.0767 | -3.4818 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 3 | sp-hold-ueth-v1 | 0 | -1.7597 | — | — | 18.4092 | — | 0.0114 | +0.0000 | +0.8788 | -11.6796 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 4 | sp-hold-ubtc-v1 | 0 | -1.9070 | — | — | 16.5977 | — | 0.0113 | +0.0000 | -0.0273 | -12.5857 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |

## Spot fast / 5m and 15m (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-ema15m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7947 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-ema15m-hype-v1 [cluster:TREND] | 2 | -0.0934 | 50.0000 | 0.7086 | 4.3306 | -0.0467 | 0.0441 | +0.0000 | +11.2196 | -1.3388 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-donchian5m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 1 | -0.1128 | 0.0000 | 0.0000 | 1.0376 | -0.1128 | 0.0226 | +0.0000 | +11.1001 | -1.4584 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-donchian5m-ueth-v1 [cluster:TREND] | 9 | -0.1148 | 33.3333 | 0.8332 | 3.9796 | -0.0128 | 0.2038 | +0.0000 | +11.0879 | -1.4705 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 5 | sp-donchian5m-ubtc-v1 [cluster:TREND] | 5 | -0.2151 | 20.0000 | 0.3459 | 3.1640 | -0.0430 | 0.1106 | +0.0000 | +10.4704 | -2.0880 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | sp-ema15m-ubtc-v1 [cluster:TREND] | 2 | -0.2564 | 0.0000 | 0.0000 | 2.9158 | -0.1282 | 0.0436 | +0.0000 | +10.2160 | -2.3425 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | sp-ema15m-ueth-v1 [cluster:TREND] | 3 | -0.3207 | 0.0000 | 0.0000 | 3.5351 | -0.1069 | 0.0673 | +0.0000 | +9.8202 | -2.7382 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | sp4-utc21-ubtc-v1 [NON_V1_RESEARCH, cluster:BTC_FRI21] | 1 | -0.3304 | 0.0000 | 0.0000 | 2.1185 | -0.3304 | 0.0225 | +0.0000 | +9.6708 | -2.7984 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |
| 9 | sp-donchian5m-hype-v1 [cluster:TREND] | 7 | -0.4082 | 14.2857 | 0.5043 | 4.6199 | -0.0583 | 0.1535 | +0.0000 | +9.2810 | -3.2774 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |

## Spot slow / 1h (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-rsi1h-ubtc-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7947 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-rsi1h-ueth-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7947 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-rsi1h-usol-v1 (RETIRED_DATA_QUALITY) | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7947 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-rsi1h-hype-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7947 | -0.7637 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | sp4-shockrev1h-ubtc-v1 [NON_V1_RESEARCH, cluster:SHOCKREV] | 1 | -0.3852 | 0.0000 | 0.0000 | 2.4557 | -0.3852 | 0.0224 | +0.0000 | +9.3333 | -3.1359 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |

## Early read (not evidence)

Fast and spot_fast books with at least 10 closed trades, ranked by closed-trade count then net MTM after paid fees/funding (open exit cost not deducted). This is an operational early look so small-capital books can be watched before the 30-trade / DSR / fresh-OOS bar. It is **not** significance, **not** a PASS, and **does not** change the promotion bar. Nothing in this section is a CANDIDATE.

| Rank | Book | Lane | Closed | Net MTM USDC | Win % | Fees | Funding | Gate |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | f1-vwap5m-v1 | fast | 41 | -3.0955 | 48.7805 | 2.3442 | +0.0028 | UNPROVEN |
| 2 | g-squeeze-sol-p0-v1 | fast | 31 | -1.5800 | 22.5806 | 2.0644 | -0.0012 | UNPROVEN |
| 3 | g-squeeze-btc-p0-v1 | fast | 31 | -2.3955 | 25.8065 | 2.0321 | -0.0051 | UNPROVEN |
| 4 | g-vwap-eth-p1-v1 | fast | 30 | +1.4086 | 63.3333 | 1.6734 | +0.0095 | UNPROVEN |
| 5 | g-squeeze-btc-p2-v1 | fast | 30 | -0.8666 | 36.6667 | 1.9788 | -0.0122 | UNPROVEN |
| 6 | g-vwap-sol-p1-v1 | fast | 30 | -4.1016 | 40.0000 | 1.5717 | +0.0015 | UNPROVEN |
| 7 | g-squeeze-sol-p2-v1 | fast | 27 | -0.7142 | 37.0370 | 1.7933 | -0.0017 | NOT_SIGNIFICANT |
| 8 | g-vwap-sol-p0-v1 | fast | 27 | -2.0445 | 40.7407 | 1.3612 | +0.0012 | NOT_SIGNIFICANT |
| 9 | g-vwap-eth-p0-v1 | fast | 26 | +2.1099 | 65.3846 | 1.5226 | +0.0089 | NOT_SIGNIFICANT |
| 10 | g-vwap-btc-p1-v1 | fast | 26 | -1.2542 | 53.8462 | 1.5499 | -0.0059 | NOT_SIGNIFICANT |
| 11 | g-vwap-all-p1-v1 | fast | 23 | -2.5372 | 34.7826 | 1.2576 | +0.0016 | NOT_SIGNIFICANT |
| 12 | g-vwap-btc-p0-v1 | fast | 22 | -1.5126 | 50.0000 | 1.3628 | -0.0037 | NOT_SIGNIFICANT |
| 13 | g-vwap-sol-p2-v1 | fast | 22 | -2.8187 | 31.8182 | 1.1435 | +0.0015 | NOT_SIGNIFICANT |
| 14 | g-vwap-eth-p2-v1 | fast | 21 | +3.0617 | 66.6667 | 1.1470 | +0.0040 | NOT_SIGNIFICANT |
| 15 | g-squeeze-sol-p1-v1 | fast | 20 | -1.3271 | 20.0000 | 1.3302 | -0.0016 | NOT_SIGNIFICANT |
| 16 | g-squeeze-btc-p1-v1 | fast | 20 | -2.5358 | 15.0000 | 1.3215 | +0.0001 | NOT_SIGNIFICANT |
| 17 | g-vwap-btc-p2-v1 | fast | 18 | -2.6154 | 38.8889 | 1.0984 | -0.0046 | NOT_SIGNIFICANT |
| 18 | g-squeeze-eth-p1-v1 | fast | 18 | -2.9467 | 22.2222 | 1.1883 | -0.0026 | NOT_SIGNIFICANT |
| 19 | g-rsi2-all-p1-v1 | fast | 17 | -2.1754 | 47.0588 | 0.8960 | +0.0003 | NOT_SIGNIFICANT |
| 20 | g-squeeze-eth-p0-v1 | fast | 17 | -3.1729 | 23.5294 | 1.1229 | -0.0012 | NOT_SIGNIFICANT |
| 21 | f3-rsi2-5m-v1 | fast | 12 | -1.4423 | 33.3333 | 0.6741 | +0.0001 | NOT_SIGNIFICANT |
| 22 | g-rsi2-sol-p1-v1 | fast | 11 | -2.1438 | 18.1818 | 0.5410 | +0.0003 | NOT_SIGNIFICANT |
| 23 | f5-squeeze1m-v1 | fast | 11 | -2.1846 | 9.0909 | 0.7295 | +0.0016 | NOT_SIGNIFICANT |
| 24 | g-rsi2-btc-p1-v1 | fast | 10 | -0.2717 | 70.0000 | 0.6166 | +0.0000 | NOT_SIGNIFICANT |
| 25 | g-rsi2-eth-p1-v1 | fast | 10 | -0.7659 | 50.0000 | 0.5552 | +0.0000 | NOT_SIGNIFICANT |
| 26 | g-ema-all-p1-v1 [cluster:TREND] | fast | 10 | -2.8883 | 10.0000 | 0.4567 | -0.0002 | NOT_SIGNIFICANT |

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
