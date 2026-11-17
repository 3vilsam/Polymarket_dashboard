# PAPER league — 100 virtual USDC perp books + 16.24 virtual USDC spot books

Updated 2026-11-17T16:00:09+08:00 MYT | tick 1003 | 125 books (107 perp @100 USDC, 18 spot @16.24 USDC; incl. 9 v4 research-sweep books registered 12 Nov 2026) | public reads only

Spot research books use 5m/15m/1h timeframes. Do not compare raw Net MTM USDC across the 100-USDC and 16.24-USDC tables. An 'Early read (not evidence)' table lists fast books with >=10 closed trades; it is not the promotion bar. Ranks use net MTM (open exit cost not deducted). Gate comparisons use same-start indicative exit equity: perp books deduct taker+2bp; spot books deduct official tier-0 spot taker 0.070%+2bp. Official promotion controls remain the BTC-perp hold and random-entry books.

## Controls / luck benchmarks (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | c1-random15m-v1 | 14 | +0.5234 | 42.8571 | 1.2924 | 2.0147 | 0.0394 | 0.5577 | -0.0008 | +12.9962 | +0.0000 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); CONTROL |
| 2 | b0-btc-1x-hold-control-v1 | 0 | -12.4790 | — | — | 16.9854 | — | 0.0450 | -0.1108 | +0.0000 | -12.9962 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); CONTROL; NONTRADABLE risk-exempt |

## Fast / short-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | g-vwap-eth-p2-v1 | 23 | +2.9761 | 65.2174 | 1.8485 | 2.6304 | 0.1294 | 1.2853 | +0.0043 | +15.4767 | +2.4805 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-vwap-eth-p0-v1 | 29 | +2.4855 | 65.5172 | 1.6281 | 2.2871 | 0.0857 | 1.7281 | +0.0092 | +14.9860 | +1.9898 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | g-vwap-eth-p1-v1 | 31 | +0.9244 | 61.2903 | 1.1646 | 3.4650 | 0.0298 | 1.7414 | +0.0095 | +13.4250 | +0.4288 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |
| 4 | g-ema-sol-p1-v1 [cluster:TREND] | 6 | -0.1136 | 33.3333 | 0.9415 | 2.1965 | -0.0189 | 0.2263 | -0.0014 | +12.3870 | -0.6092 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | g-asia-eth-p0-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +12.3713 | -0.6250 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | g-asia-eth-p1-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +12.3713 | -0.6250 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | g-asia-eth-p2-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +12.3713 | -0.6250 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | g-rsi2-btc-p2-v1 | 4 | -0.2851 | 75.0000 | 0.4166 | 1.1377 | -0.0713 | 0.2053 | +0.0007 | +12.2154 | -0.7808 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | g-rsi2-btc-p1-v1 | 10 | -0.3196 | 70.0000 | 0.6295 | 0.8211 | -0.0272 | 0.6498 | +0.0000 | +12.1330 | -0.8632 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | g-rsi2-sol-p2-v1 | 5 | -0.4475 | 40.0000 | 0.4363 | 1.2414 | -0.0895 | 0.2643 | +0.0003 | +12.0531 | -0.9432 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | n4-utc21-btc-v1 [cluster:BTC_FRI21] | 2 | -0.4512 | 50.0000 | 0.0673 | 0.5879 | -0.2256 | 0.0408 | -0.0003 | +11.6887 | -0.9469 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-rsi2-eth-p2-v1 | 3 | -0.6817 | 33.3333 | 0.2973 | 1.0005 | -0.2272 | 0.1356 | +0.0000 | +11.8189 | -1.1773 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-asia-btc-p0-v1 | 3 | -0.7269 | 0.0000 | 0.0000 | 0.9987 | -0.2423 | 0.1615 | +0.0021 | +11.7736 | -1.2226 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-asia-btc-p2-v1 | 3 | -0.7269 | 0.0000 | 0.0000 | 0.9987 | -0.2423 | 0.1615 | +0.0021 | +11.7736 | -1.2226 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-rsi2-btc-p0-v1 | 8 | -0.7660 | 37.5000 | 0.3106 | 1.0859 | -0.0958 | 0.4656 | +0.0000 | +11.7345 | -1.2617 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-squeeze-btc-p2-v1 | 30 | -0.8666 | 36.6667 | 0.8470 | 2.3161 | -0.0289 | 1.9788 | -0.0122 | +11.6339 | -1.3623 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |
| 17 | g-asia-btc-p1-v1 | 4 | -0.8847 | 0.0000 | 0.0000 | 1.1560 | -0.2212 | 0.2103 | +0.0021 | +11.6159 | -1.3803 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-ema-eth-p2-v1 [cluster:TREND] | 4 | -0.9506 | 0.0000 | 0.0000 | 1.7076 | -0.2376 | 0.1360 | -0.0029 | +11.5500 | -1.4462 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-rsi2-sol-p0-v1 | 7 | -0.9709 | 28.5714 | 0.2487 | 1.6878 | -0.1387 | 0.3548 | +0.0003 | +11.5296 | -1.4666 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-ema-sol-p0-v1 [cluster:TREND] | 3 | -1.0369 | 0.0000 | 0.0000 | 1.3824 | -0.3456 | 0.0866 | -0.0005 | +11.4636 | -1.5326 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-rsi2-eth-p0-v1 | 7 | -1.0397 | 28.5714 | 0.2450 | 1.8044 | -0.1485 | 0.3664 | +0.0001 | +11.4608 | -1.5354 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-ema-sol-p2-v1 [cluster:TREND] | 3 | -1.1676 | 0.0000 | 0.0000 | 2.3393 | -0.3892 | 0.0948 | -0.0009 | +11.3330 | -1.6633 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-asia-sol-p1-v1 | 3 | -1.2183 | 0.0000 | 0.0000 | 1.4176 | -0.4061 | 0.1365 | +0.0005 | +11.2823 | -1.7139 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-asia-sol-p2-v1 | 3 | -1.2183 | 0.0000 | 0.0000 | 1.4176 | -0.4061 | 0.1365 | +0.0005 | +11.2823 | -1.7139 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | g-rsi2-eth-p1-v1 | 11 | -1.2395 | 45.4545 | 0.2829 | 1.3470 | -0.1127 | 0.6217 | +0.0000 | +11.2610 | -1.7352 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-asia-all-p1-v1 | 5 | -1.3572 | 0.0000 | 0.0000 | 1.5563 | -0.2714 | 0.2569 | +0.0022 | +11.1433 | -1.8529 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | f2-asia15m-v1 | 5 | -1.3799 | 0.0000 | 0.0000 | 1.5789 | -0.2760 | 0.2454 | +0.0022 | +11.1206 | -1.8756 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-asia-sol-p0-v1 | 4 | -1.3987 | 0.0000 | 0.0000 | 1.5977 | -0.3497 | 0.1738 | +0.0005 | +11.1018 | -1.8944 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-squeeze-sol-p2-v1 | 29 | -1.4455 | 34.4828 | 0.7692 | 3.0069 | -0.0498 | 1.9254 | -0.0017 | +11.0551 | -1.9411 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-vwap-sol-p0-v1 | 28 | -1.5445 | 42.8571 | 0.7051 | 5.2270 | -0.0552 | 1.4271 | +0.0020 | +10.9561 | -2.0401 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-ema-btc-p2-v1 [cluster:TREND] | 7 | -1.6109 | 14.2857 | 0.3508 | 2.4799 | -0.2240 | 0.3538 | +0.0002 | +10.8485 | -2.1478 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-ema-eth-p0-v1 [cluster:TREND] | 4 | -1.6133 | 0.0000 | 0.0000 | 2.1753 | -0.4033 | 0.1569 | +0.0002 | +10.8873 | -2.1089 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-vwap-btc-p1-v1 | 27 | -1.7224 | 51.8519 | 0.6495 | 3.0700 | -0.0638 | 1.6156 | -0.0059 | +10.7782 | -2.2181 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | g-ema-btc-p0-v1 [cluster:TREND] | 5 | -1.7903 | 0.0000 | 0.0000 | 2.2224 | -0.3494 | 0.2599 | -0.0030 | +10.6690 | -2.3272 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | f3-rsi2-5m-v1 | 13 | -1.9126 | 30.7692 | 0.1703 | 2.4979 | -0.1471 | 0.7401 | +0.0001 | +10.5880 | -2.4083 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | g-rsi2-sol-p1-v1 | 13 | -1.9375 | 23.0769 | 0.1668 | 2.2755 | -0.1490 | 0.6722 | +0.0003 | +10.5630 | -2.4332 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 37 | g-vwap-btc-p0-v1 | 23 | -1.9796 | 47.8261 | 0.5636 | 2.8246 | -0.0861 | 1.4284 | -0.0037 | +10.5209 | -2.4753 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-squeeze-sol-p1-v1 | 22 | -2.0551 | 18.1818 | 0.5913 | 3.6771 | -0.0934 | 1.4617 | -0.0016 | +10.4454 | -2.5508 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | g-ema-btc-p1-v1 [cluster:TREND] | 7 | -2.1843 | 0.0000 | 0.0000 | 2.2777 | -0.3059 | 0.3560 | +0.0014 | +10.2750 | -2.7212 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | f5-squeeze1m-v1 | 11 | -2.1846 | 9.0909 | 0.0292 | 2.3893 | -0.1986 | 0.7295 | +0.0016 | +10.3159 | -2.6803 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 41 | f4-ema15m-v1 [cluster:TREND] | 6 | -2.2690 | 0.0000 | 0.0000 | 2.6991 | -0.3710 | 0.2961 | -0.0035 | +10.1903 | -2.8059 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | g-squeeze-sol-p0-v1 | 33 | -2.3081 | 21.2121 | 0.6847 | 4.6082 | -0.0699 | 2.1959 | -0.0012 | +10.1925 | -2.8038 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |
| 43 | g-squeeze-eth-p2-v1 | 9 | -2.3227 | 11.1111 | 0.0598 | 2.4051 | -0.2581 | 0.6001 | -0.0002 | +10.1778 | -2.8184 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 44 | g-vwap-sol-p2-v1 | 23 | -2.3236 | 34.7826 | 0.5465 | 5.1710 | -0.1010 | 1.2087 | +0.0023 | +10.1769 | -2.8193 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | g-squeeze-btc-p0-v1 | 31 | -2.3933 | 25.8065 | 0.5256 | 3.2137 | -0.0773 | 2.0647 | -0.0051 | +10.0601 | -2.9361 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |
| 46 | g-rsi2-all-p1-v1 | 20 | -2.4834 | 45.0000 | 0.2743 | 2.4861 | -0.1218 | 1.1245 | +0.0003 | +9.9704 | -3.0258 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | g-squeeze-btc-p1-v1 | 20 | -2.5336 | 15.0000 | 0.3508 | 3.0510 | -0.1268 | 1.3541 | +0.0001 | +9.9198 | -3.0764 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 48 | g-vwap-all-p1-v1 | 23 | -2.5372 | 34.7826 | 0.5707 | 5.3758 | -0.1103 | 1.2576 | +0.0016 | +9.9633 | -3.0329 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 49 | g-ema-eth-p1-v1 [cluster:TREND] | 9 | -2.6642 | 11.1111 | 0.1603 | 3.2481 | -0.2960 | 0.3712 | -0.0015 | +9.8364 | -3.1598 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 50 | f1-vwap5m-v1 | 44 | -2.7387 | 50.0000 | 0.6838 | 5.6463 | -0.0622 | 2.5393 | +0.0031 | +9.7618 | -3.2344 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |
| 51 | g-ema-all-p1-v1 [cluster:TREND] | 10 | -2.9309 | 10.0000 | 0.1491 | 3.0508 | -0.2888 | 0.4849 | -0.0001 | +9.5288 | -3.4674 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 52 | g-squeeze-eth-p1-v1 | 18 | -2.9467 | 22.2222 | 0.3273 | 3.4777 | -0.1637 | 1.1883 | -0.0026 | +9.5538 | -3.4424 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 53 | g-squeeze-eth-p0-v1 | 17 | -3.1729 | 23.5294 | 0.2410 | 3.3755 | -0.1866 | 1.1229 | -0.0012 | +9.3276 | -3.6686 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 54 | g-vwap-btc-p2-v1 | 20 | -3.1768 | 35.0000 | 0.3524 | 3.5023 | -0.1588 | 1.2283 | -0.0039 | +9.3237 | -3.6725 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 55 | g-vwap-sol-p1-v1 | 33 | -3.9823 | 42.4242 | 0.4487 | 4.9706 | -0.1207 | 1.7499 | +0.0024 | +8.5182 | -4.4780 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |

## Slow / long-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | l1-supertrend1h-v1 [cluster:TREND] | 1 | +0.3643 | 100.0000 | inf | 1.1588 | 0.3643 | 0.0214 | +0.0031 | +12.8648 | -0.1314 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-supertrend-sol-p0-v1 [cluster:TREND] | 1 | +0.3643 | 100.0000 | inf | 1.1588 | 0.3643 | 0.0214 | +0.0031 | +12.8648 | -0.1314 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | n1-tsmom-mh1h-v1 [cluster:TREND] | 3 | +0.2497 | 66.6667 | 2.9673 | 1.1001 | 0.0832 | 0.0435 | +0.0025 | +12.3896 | -0.2460 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | s4-ewmac-riskcap-noadd-ablation-v1 [cluster:TREND] | 0 | +0.0214 | — | — | 0.1264 | — | 0.0047 | +0.0006 | +12.5152 | -0.4810 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | s1-donchian40-ablation-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | s2-bb40-ema200-ablation-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | r1-trend-rsi-pullback-market-lane-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | l2-macd4h-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | l3-funding1h-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | l4-weekly1d-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | g-supertrend-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-supertrend-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-supertrend-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-supertrend-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-supertrend-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-macd-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-macd-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-macd-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-macd-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-macd-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-macd-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-macd-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-macd-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-macd-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | g-funding-btc-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-funding-btc-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-funding-btc-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-funding-eth-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-funding-eth-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-funding-eth-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-funding-sol-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-funding-sol-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-funding-sol-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | g-weekly-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-weekly-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | g-weekly-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 37 | g-weekly-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-weekly-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | g-weekly-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | g-weekly-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | g-weekly-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | g-weekly-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5006 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | n3-negfund-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1399 | -0.4957 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | n5-weekend-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1399 | -0.4957 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | n6-ethbtc-z1h-v1 [UNHEDGED_ETH_DIRECTIONAL] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1399 | -0.4957 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 46 | g-supertrend-btc-p2-v1 [cluster:TREND] | 0 | -0.2143 | — | — | 0.4317 | — | 0.0068 | -0.0058 | +12.2765 | -0.7197 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | g-supertrend-sol-p1-v1 [cluster:TREND] | 1 | -0.2311 | 0.0000 | 0.0000 | 0.6032 | -0.2468 | 0.0185 | +0.0008 | +12.2576 | -0.7386 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 48 | n7-xsmom72h-v1 [cluster:TREND] | 0 | -0.2403 | — | — | 0.3248 | — | 0.0055 | -0.0012 | +11.8916 | -0.7440 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | n2-shockrev1h-v1 [cluster:SHOCKREV] | 1 | -0.4808 | 0.0000 | 0.0000 | 0.4916 | -0.4808 | 0.0132 | -0.0003 | +11.6592 | -0.9764 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 50 | g-supertrend-btc-p1-v1 [cluster:TREND] | 1 | -0.4810 | 0.0000 | 0.0000 | 0.6346 | -0.4810 | 0.0245 | +0.0012 | +12.0196 | -0.9766 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |

## Spot buy-and-hold controls (16.24 virtual USDC, 1x long, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-hold-usol-v1 (RETIRED_DATA_QUALITY) | 1 | -0.0166 | 0.0000 | 0.0000 | 3.9287 | -0.0166 | 0.0226 | +0.0000 | +12.1263 | -0.5981 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 2 | sp-hold-hype-v1 | 0 | -0.5276 | — | — | 19.4142 | — | 0.0110 | +0.0000 | +8.8956 | -3.8288 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 3 | sp-hold-ueth-v1 | 0 | -1.7716 | — | — | 18.4092 | — | 0.0114 | +0.0000 | +1.2399 | -11.4845 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 4 | sp-hold-ubtc-v1 | 0 | -1.9783 | — | — | 16.5977 | — | 0.0113 | +0.0000 | -0.0318 | -12.7562 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |

## Spot fast / 5m and 15m (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-ema15m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.2287 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-ema15m-hype-v1 [cluster:TREND] | 2 | -0.0934 | 50.0000 | 0.7086 | 4.3306 | -0.0467 | 0.0441 | +0.0000 | +11.6537 | -1.0707 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-donchian5m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 1 | -0.1128 | 0.0000 | 0.0000 | 1.0376 | -0.1128 | 0.0226 | +0.0000 | +11.5341 | -1.1903 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-donchian5m-ueth-v1 [cluster:TREND] | 9 | -0.1148 | 33.3333 | 0.8332 | 3.9796 | -0.0128 | 0.2038 | +0.0000 | +11.5219 | -1.2025 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 5 | sp-donchian5m-ubtc-v1 [cluster:TREND] | 5 | -0.2151 | 20.0000 | 0.3459 | 3.1640 | -0.0430 | 0.1106 | +0.0000 | +10.9044 | -1.8200 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | sp-ema15m-ueth-v1 [cluster:TREND] | 3 | -0.3207 | 0.0000 | 0.0000 | 3.5351 | -0.1069 | 0.0673 | +0.0000 | +10.2542 | -2.4702 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | sp4-utc21-ubtc-v1 [NON_V1_RESEARCH, cluster:BTC_FRI21] | 1 | -0.3304 | 0.0000 | 0.0000 | 2.1185 | -0.3304 | 0.0225 | +0.0000 | +10.1053 | -2.5303 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |
| 8 | sp-ema15m-ubtc-v1 [cluster:TREND] | 3 | -0.3581 | 0.0000 | 0.0000 | 3.2986 | -0.1194 | 0.0654 | +0.0000 | +10.0238 | -2.7006 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | sp-donchian5m-hype-v1 [cluster:TREND] | 7 | -0.4082 | 14.2857 | 0.5043 | 4.6199 | -0.0583 | 0.1535 | +0.0000 | +9.7151 | -3.0093 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |

## Spot slow / 1h (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-rsi1h-ubtc-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.2287 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-rsi1h-ueth-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.2287 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-rsi1h-usol-v1 (RETIRED_DATA_QUALITY) | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.2287 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-rsi1h-hype-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.2287 | -0.4957 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | sp4-shockrev1h-ubtc-v1 [NON_V1_RESEARCH, cluster:SHOCKREV] | 1 | -0.3852 | 0.0000 | 0.0000 | 2.4557 | -0.3852 | 0.0224 | +0.0000 | +9.7678 | -2.8678 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |

## Early read (not evidence)

Fast and spot_fast books with at least 10 closed trades, ranked by closed-trade count then net MTM after paid fees/funding (open exit cost not deducted). This is an operational early look so small-capital books can be watched before the 30-trade / DSR / fresh-OOS bar. It is **not** significance, **not** a PASS, and **does not** change the promotion bar. Nothing in this section is a CANDIDATE.

| Rank | Book | Lane | Closed | Net MTM USDC | Win % | Fees | Funding | Gate |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | f1-vwap5m-v1 | fast | 44 | -2.7387 | 50.0000 | 2.5393 | +0.0031 | UNPROVEN |
| 2 | g-squeeze-sol-p0-v1 | fast | 33 | -2.3081 | 21.2121 | 2.1959 | -0.0012 | UNPROVEN |
| 3 | g-vwap-sol-p1-v1 | fast | 33 | -3.9823 | 42.4242 | 1.7499 | +0.0024 | UNPROVEN |
| 4 | g-vwap-eth-p1-v1 | fast | 31 | +0.9244 | 61.2903 | 1.7414 | +0.0095 | UNPROVEN |
| 5 | g-squeeze-btc-p0-v1 | fast | 31 | -2.3933 | 25.8065 | 2.0647 | -0.0051 | UNPROVEN |
| 6 | g-squeeze-btc-p2-v1 | fast | 30 | -0.8666 | 36.6667 | 1.9788 | -0.0122 | UNPROVEN |
| 7 | g-vwap-eth-p0-v1 | fast | 29 | +2.4855 | 65.5172 | 1.7281 | +0.0092 | NOT_SIGNIFICANT |
| 8 | g-squeeze-sol-p2-v1 | fast | 29 | -1.4455 | 34.4828 | 1.9254 | -0.0017 | NOT_SIGNIFICANT |
| 9 | g-vwap-sol-p0-v1 | fast | 28 | -1.5445 | 42.8571 | 1.4271 | +0.0020 | NOT_SIGNIFICANT |
| 10 | g-vwap-btc-p1-v1 | fast | 27 | -1.7224 | 51.8519 | 1.6156 | -0.0059 | NOT_SIGNIFICANT |
| 11 | g-vwap-eth-p2-v1 | fast | 23 | +2.9761 | 65.2174 | 1.2853 | +0.0043 | NOT_SIGNIFICANT |
| 12 | g-vwap-btc-p0-v1 | fast | 23 | -1.9796 | 47.8261 | 1.4284 | -0.0037 | NOT_SIGNIFICANT |
| 13 | g-vwap-sol-p2-v1 | fast | 23 | -2.3236 | 34.7826 | 1.2087 | +0.0023 | NOT_SIGNIFICANT |
| 14 | g-vwap-all-p1-v1 | fast | 23 | -2.5372 | 34.7826 | 1.2576 | +0.0016 | NOT_SIGNIFICANT |
| 15 | g-squeeze-sol-p1-v1 | fast | 22 | -2.0551 | 18.1818 | 1.4617 | -0.0016 | NOT_SIGNIFICANT |
| 16 | g-rsi2-all-p1-v1 | fast | 20 | -2.4834 | 45.0000 | 1.1245 | +0.0003 | NOT_SIGNIFICANT |
| 17 | g-squeeze-btc-p1-v1 | fast | 20 | -2.5336 | 15.0000 | 1.3541 | +0.0001 | NOT_SIGNIFICANT |
| 18 | g-vwap-btc-p2-v1 | fast | 20 | -3.1768 | 35.0000 | 1.2283 | -0.0039 | NOT_SIGNIFICANT |
| 19 | g-squeeze-eth-p1-v1 | fast | 18 | -2.9467 | 22.2222 | 1.1883 | -0.0026 | NOT_SIGNIFICANT |
| 20 | g-squeeze-eth-p0-v1 | fast | 17 | -3.1729 | 23.5294 | 1.1229 | -0.0012 | NOT_SIGNIFICANT |
| 21 | f3-rsi2-5m-v1 | fast | 13 | -1.9126 | 30.7692 | 0.7401 | +0.0001 | NOT_SIGNIFICANT |
| 22 | g-rsi2-sol-p1-v1 | fast | 13 | -1.9375 | 23.0769 | 0.6722 | +0.0003 | NOT_SIGNIFICANT |
| 23 | g-rsi2-eth-p1-v1 | fast | 11 | -1.2395 | 45.4545 | 0.6217 | +0.0000 | NOT_SIGNIFICANT |
| 24 | f5-squeeze1m-v1 | fast | 11 | -2.1846 | 9.0909 | 0.7295 | +0.0016 | NOT_SIGNIFICANT |
| 25 | g-rsi2-btc-p1-v1 | fast | 10 | -0.3196 | 70.0000 | 0.6498 | +0.0000 | NOT_SIGNIFICANT |
| 26 | g-ema-all-p1-v1 [cluster:TREND] | fast | 10 | -2.9309 | 10.0000 | 0.4849 | -0.0001 | NOT_SIGNIFICANT |

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
