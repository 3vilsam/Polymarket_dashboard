# PAPER league — 100 virtual USDC perp books + 16.24 virtual USDC spot books

Updated 2026-11-18T18:53:05+08:00 MYT | tick 1311 | 125 books (107 perp @100 USDC, 18 spot @16.24 USDC; incl. 9 v4 research-sweep books registered 12 Nov 2026) | public reads only

Spot research books use 5m/15m/1h timeframes. Do not compare raw Net MTM USDC across the 100-USDC and 16.24-USDC tables. An 'Early read (not evidence)' table lists fast books with >=10 closed trades; it is not the promotion bar. Ranks use net MTM (open exit cost not deducted). Gate comparisons use same-start indicative exit equity: perp books deduct taker+2bp; spot books deduct official tier-0 spot taker 0.070%+2bp. Official promotion controls remain the BTC-perp hold and random-entry books.

## Controls / luck benchmarks (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | c1-random15m-v1 | 20 | +0.2859 | 45.0000 | 1.0906 | 2.8823 | 0.0143 | 0.7674 | -0.0020 | +13.3079 | +0.0000 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); CONTROL |
| 2 | b0-btc-1x-hold-control-v1 | 0 | -13.0006 | — | — | 16.9854 | — | 0.0450 | -0.1382 | +0.0000 | -13.3079 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); CONTROL; NONTRADABLE risk-exempt |

## Fast / short-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | g-vwap-eth-p0-v1 | 41 | +0.5277 | 58.5366 | 1.0789 | 3.2597 | 0.0129 | 2.4857 | +0.0095 | +13.5497 | +0.2418 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |
| 2 | g-vwap-eth-p2-v1 | 31 | +0.3983 | 51.6129 | 1.0639 | 3.7789 | 0.0128 | 1.7771 | +0.0035 | +13.4203 | +0.1124 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |
| 3 | n4-utc21-btc-v1 [cluster:BTC_FRI21] | 3 | -0.1276 | 66.6667 | 0.7362 | 0.5879 | -0.0425 | 0.0628 | -0.0009 | +12.5359 | -0.4135 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | g-asia-eth-p0-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +12.8928 | -0.4152 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | g-asia-eth-p2-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +12.8928 | -0.4152 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | g-asia-eth-p1-v1 | 2 | -0.2303 | 0.0000 | 0.0000 | 0.4686 | -0.1151 | 0.1135 | +0.0009 | +12.7918 | -0.5161 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | g-ema-sol-p2-v1 [cluster:TREND] | 4 | -0.2791 | 25.0000 | 0.7610 | 2.3393 | -0.0698 | 0.1294 | +0.0003 | +12.7429 | -0.5650 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | g-rsi2-btc-p2-v1 | 4 | -0.2851 | 75.0000 | 0.4166 | 1.1377 | -0.0713 | 0.2053 | +0.0007 | +12.7369 | -0.5710 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | g-rsi2-btc-p1-v1 | 13 | -0.2855 | 61.5385 | 0.6394 | 0.8211 | -0.0220 | 0.8167 | +0.0000 | +12.7365 | -0.5714 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | g-rsi2-eth-p2-v1 | 3 | -0.6817 | 33.3333 | 0.2973 | 1.0005 | -0.2272 | 0.1356 | +0.0000 | +12.3404 | -0.9675 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | g-asia-btc-p0-v1 | 3 | -0.7269 | 0.0000 | 0.0000 | 0.9987 | -0.2423 | 0.1615 | +0.0021 | +12.2951 | -1.0128 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-asia-btc-p2-v1 | 3 | -0.7269 | 0.0000 | 0.0000 | 0.9987 | -0.2423 | 0.1615 | +0.0021 | +12.2951 | -1.0128 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-vwap-eth-p1-v1 | 41 | -0.7852 | 56.0976 | 0.9076 | 4.1658 | -0.0192 | 2.3541 | +0.0093 | +12.2369 | -1.0710 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |
| 14 | g-rsi2-btc-p0-v1 | 9 | -0.8025 | 33.3333 | 0.3008 | 1.0859 | -0.0892 | 0.5319 | +0.0000 | +12.2196 | -1.0884 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-ema-sol-p1-v1 [cluster:TREND] | 8 | -0.8149 | 25.0000 | 0.6918 | 2.8832 | -0.1019 | 0.2922 | -0.0030 | +12.2072 | -1.1007 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-asia-btc-p1-v1 | 4 | -0.8847 | 0.0000 | 0.0000 | 1.1560 | -0.2212 | 0.2103 | +0.0021 | +12.1374 | -1.1705 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-rsi2-eth-p0-v1 | 7 | -1.0397 | 28.5714 | 0.2450 | 1.8044 | -0.1485 | 0.3664 | +0.0001 | +11.9823 | -1.3256 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-asia-sol-p1-v1 | 3 | -1.2183 | 0.0000 | 0.0000 | 1.4176 | -0.4061 | 0.1365 | +0.0005 | +11.8038 | -1.5041 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-asia-sol-p2-v1 | 3 | -1.2183 | 0.0000 | 0.0000 | 1.4176 | -0.4061 | 0.1365 | +0.0005 | +11.8038 | -1.5041 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-rsi2-eth-p1-v1 | 12 | -1.3475 | 41.6667 | 0.2663 | 1.4822 | -0.1123 | 0.6879 | +0.0000 | +11.6746 | -1.6333 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | f2-asia15m-v1 | 5 | -1.3799 | 0.0000 | 0.0000 | 1.5789 | -0.2760 | 0.2454 | +0.0022 | +11.6421 | -1.6658 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-asia-sol-p0-v1 | 4 | -1.3987 | 0.0000 | 0.0000 | 1.5977 | -0.3497 | 0.1738 | +0.0005 | +11.6233 | -1.6846 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-rsi2-sol-p2-v1 | 8 | -1.4286 | 25.0000 | 0.1951 | 2.2105 | -0.1786 | 0.4624 | +0.0003 | +11.5934 | -1.7145 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-asia-all-p1-v1 | 6 | -1.4571 | 0.0000 | 0.0000 | 1.7439 | -0.2429 | 0.3029 | +0.0028 | +11.5649 | -1.7430 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | g-rsi2-sol-p0-v1 | 14 | -1.6039 | 35.7143 | 0.2977 | 2.5933 | -0.1146 | 0.7938 | +0.0011 | +11.4181 | -1.8898 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-ema-eth-p0-v1 [cluster:TREND] | 5 | -1.6877 | 0.0000 | 0.0000 | 2.2756 | -0.3375 | 0.1964 | -0.0025 | +11.3343 | -1.9736 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-ema-eth-p2-v1 [cluster:TREND] | 6 | -1.9084 | 0.0000 | 0.0000 | 2.4687 | -0.3181 | 0.2210 | -0.0022 | +11.1137 | -2.1942 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-ema-sol-p0-v1 [cluster:TREND] | 6 | -1.9279 | 0.0000 | 0.0000 | 2.2885 | -0.3213 | 0.1934 | -0.0022 | +11.0942 | -2.2138 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | f5-squeeze1m-v1 | 11 | -2.1846 | 9.0909 | 0.0292 | 2.3893 | -0.1986 | 0.7295 | +0.0016 | +10.8374 | -2.4705 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 30 | g-squeeze-eth-p2-v1 | 9 | -2.3227 | 11.1111 | 0.0598 | 2.4051 | -0.2581 | 0.6001 | -0.0002 | +10.6993 | -2.6086 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 31 | g-squeeze-sol-p2-v1 | 32 | -2.4629 | 31.2500 | 0.6616 | 3.8854 | -0.0770 | 2.1217 | -0.0023 | +10.5592 | -2.7487 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN; HALTED |
| 32 | g-vwap-all-p1-v1 | 23 | -2.5372 | 34.7826 | 0.5707 | 5.3758 | -0.1103 | 1.2576 | +0.0016 | +10.4848 | -2.8231 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 33 | f3-rsi2-5m-v1 | 21 | -2.5745 | 33.3333 | 0.2251 | 3.4896 | -0.1226 | 1.2403 | +0.0009 | +10.4475 | -2.8604 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | g-rsi2-sol-p1-v1 | 21 | -2.6771 | 23.8095 | 0.2197 | 3.0884 | -0.1275 | 1.1643 | +0.0002 | +10.3449 | -2.9630 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-vwap-sol-p2-v1 | 31 | -2.8046 | 38.7097 | 0.5828 | 5.1710 | -0.0905 | 1.6295 | +0.0022 | +10.2174 | -3.0905 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |
| 36 | g-squeeze-sol-p1-v1 | 31 | -2.9004 | 16.1290 | 0.5707 | 5.4943 | -0.0936 | 2.0433 | -0.0039 | +10.1217 | -3.1862 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |
| 37 | g-ema-btc-p1-v1 [cluster:TREND] | 10 | -2.9624 | 0.0000 | 0.0000 | 3.2189 | -0.3127 | 0.4985 | +0.0054 | +10.0166 | -3.2913 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-squeeze-sol-p0-v1 | 36 | -3.0048 | 19.4444 | 0.6252 | 5.2885 | -0.0835 | 2.3901 | -0.0008 | +10.0173 | -3.2907 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN; HALTED |
| 39 | g-ema-eth-p1-v1 [cluster:TREND] | 10 | -3.1387 | 10.0000 | 0.1395 | 3.7198 | -0.3139 | 0.4052 | -0.0016 | +9.8834 | -3.4246 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | g-squeeze-eth-p0-v1 | 17 | -3.1729 | 23.5294 | 0.2410 | 3.3755 | -0.1866 | 1.1229 | -0.0012 | +9.8491 | -3.4588 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 41 | g-ema-btc-p0-v1 [cluster:TREND] | 9 | -3.1997 | 0.0000 | 0.0000 | 3.6256 | -0.3555 | 0.4263 | +0.0016 | +9.8224 | -3.4855 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | g-rsi2-all-p1-v1 | 31 | -3.3426 | 35.4839 | 0.2774 | 3.5985 | -0.1078 | 1.7757 | +0.0002 | +9.6795 | -3.6284 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |
| 43 | g-ema-btc-p2-v1 [cluster:TREND] | 13 | -3.3617 | 7.6923 | 0.2013 | 4.2153 | -0.2586 | 0.6244 | +0.0039 | +9.6603 | -3.6476 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | g-vwap-sol-p0-v1 | 37 | -3.4096 | 40.5405 | 0.5530 | 5.7773 | -0.0922 | 1.9463 | +0.0023 | +9.6125 | -3.6954 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |
| 45 | g-vwap-btc-p1-v1 | 37 | -3.4116 | 48.6486 | 0.5155 | 4.1403 | -0.0922 | 2.2433 | -0.0065 | +9.6104 | -3.6975 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |
| 46 | g-squeeze-btc-p2-v1 | 44 | -3.5484 | 25.0000 | 0.5748 | 3.7203 | -0.0806 | 2.8942 | -0.0098 | +9.4737 | -3.8343 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN; HALTED |
| 47 | g-vwap-btc-p0-v1 | 31 | -3.6596 | 45.1613 | 0.4381 | 4.1589 | -0.1181 | 1.9250 | -0.0038 | +9.3624 | -3.9455 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |
| 48 | f4-ema15m-v1 [cluster:TREND] | 10 | -3.6730 | 0.0000 | 0.0000 | 4.0969 | -0.3673 | 0.4619 | +0.0011 | +9.3490 | -3.9589 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | f1-vwap5m-v1 | 50 | -4.2557 | 48.0000 | 0.5954 | 6.1582 | -0.0851 | 2.8789 | +0.0014 | +8.7663 | -4.5416 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN; HALTED |
| 50 | g-vwap-btc-p2-v1 | 30 | -4.4037 | 40.0000 | 0.3418 | 4.7251 | -0.1468 | 1.8314 | -0.0040 | +8.6183 | -4.6896 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |
| 51 | g-ema-all-p1-v1 [cluster:TREND] | 15 | -4.7976 | 6.6667 | 0.0954 | 4.9151 | -0.3198 | 0.6709 | +0.0038 | +8.2245 | -5.0834 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 52 | g-squeeze-eth-p1-v1 | 31 | -4.8749 | 19.3548 | 0.2681 | 4.8749 | -0.1573 | 2.0276 | -0.0012 | +8.1472 | -5.1607 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |
| 53 | g-squeeze-btc-p1-v1 | 33 | -5.4306 | 9.0909 | 0.2015 | 5.9012 | -0.1646 | 2.1565 | +0.0002 | +7.5915 | -5.7164 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN; HALTED |
| 54 | g-vwap-sol-p1-v1 | 43 | -5.5967 | 44.1860 | 0.4111 | 6.3581 | -0.1302 | 2.3235 | +0.0011 | +7.4253 | -5.8826 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |
| 55 | g-squeeze-btc-p0-v1 | 58 | -5.9349 | 20.6897 | 0.3663 | 5.9349 | -0.1023 | 3.7617 | -0.0035 | +7.0871 | -6.2208 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN; HALTED |

## Slow / long-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | s4-ewmac-riskcap-noadd-ablation-v1 [cluster:TREND] | 0 | +0.0831 | — | — | 0.2851 | — | 0.0047 | +0.0038 | +13.0984 | -0.2095 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | s1-donchian40-ablation-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | s2-bb40-ema200-ablation-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | r1-trend-rsi-pullback-market-lane-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | l2-macd4h-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | l3-funding1h-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | l4-weekly1d-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | g-supertrend-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | g-supertrend-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | g-supertrend-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | g-supertrend-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-supertrend-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-macd-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-macd-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-macd-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-macd-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-macd-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-macd-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-macd-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-macd-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-macd-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-funding-btc-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-funding-btc-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-funding-btc-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | g-funding-eth-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-funding-eth-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-funding-eth-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-funding-sol-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-funding-sol-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-funding-sol-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-weekly-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-weekly-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-weekly-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | g-weekly-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-weekly-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | g-weekly-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 37 | g-weekly-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-weekly-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | g-weekly-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.0221 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | n3-negfund-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.6636 | -0.2859 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | n5-weekend-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.6636 | -0.2859 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | n6-ethbtc-z1h-v1 [UNHEDGED_ETH_DIRECTIONAL] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.6636 | -0.2859 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | l1-supertrend1h-v1 [cluster:TREND] | 2 | -0.1293 | 50.0000 | 0.7380 | 1.4419 | -0.0647 | 0.0424 | +0.0026 | +12.8927 | -0.4152 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | g-supertrend-sol-p0-v1 [cluster:TREND] | 2 | -0.1293 | 50.0000 | 0.7380 | 1.4419 | -0.0647 | 0.0424 | +0.0026 | +12.8927 | -0.4152 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | n1-tsmom-mh1h-v1 [cluster:TREND] | 4 | -0.1532 | 50.0000 | 1.0656 | 1.2996 | 0.0058 | 0.0697 | +0.0036 | +12.4961 | -0.4533 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 46 | n2-shockrev1h-v1 [cluster:SHOCKREV] | 1 | -0.4808 | 0.0000 | 0.0000 | 0.4916 | -0.4808 | 0.0132 | -0.0003 | +12.1828 | -0.7666 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | n7-xsmom72h-v1 [cluster:TREND] | 1 | -0.4967 | 0.0000 | 0.0000 | 0.5555 | -0.4967 | 0.0112 | -0.0021 | +12.1669 | -0.7826 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 48 | g-supertrend-btc-p2-v1 [cluster:TREND] | 1 | -0.4976 | 0.0000 | 0.0000 | 0.5272 | -0.4976 | 0.0134 | -0.0071 | +12.5245 | -0.7835 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | g-supertrend-sol-p1-v1 [cluster:TREND] | 2 | -0.5277 | 0.0000 | 0.0000 | 0.8297 | -0.2639 | 0.0265 | +0.0014 | +12.4944 | -0.8136 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 50 | g-supertrend-btc-p1-v1 [cluster:TREND] | 2 | -0.9650 | 0.0000 | 0.0000 | 1.1179 | -0.4825 | 0.0484 | +0.0033 | +12.0570 | -1.2509 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |

## Spot buy-and-hold controls (16.24 virtual USDC, 1x long, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-hold-usol-v1 (RETIRED_DATA_QUALITY) | 1 | -0.0166 | 0.0000 | 0.0000 | 3.9287 | -0.0166 | 0.0226 | +0.0000 | +12.6494 | -0.3883 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 2 | sp-hold-hype-v1 | 0 | -0.6767 | — | — | 19.4142 | — | 0.0110 | +0.0000 | +8.5010 | -4.5367 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 3 | sp-hold-ueth-v1 | 0 | -2.0007 | — | — | 18.4092 | — | 0.0114 | +0.0000 | +0.3536 | -12.6841 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 4 | sp-hold-ubtc-v1 | 0 | -2.0604 | — | — | 16.5977 | — | 0.0113 | +0.0000 | -0.0135 | -13.0512 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |

## Spot fast / 5m and 15m (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-ema15m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.7518 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-donchian5m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 1 | -0.1128 | 0.0000 | 0.0000 | 1.0376 | -0.1128 | 0.0226 | +0.0000 | +12.0572 | -0.9805 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-donchian5m-ueth-v1 [cluster:TREND] | 9 | -0.1148 | 33.3333 | 0.8332 | 3.9796 | -0.0128 | 0.2038 | +0.0000 | +12.0450 | -0.9927 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 4 | sp-ema15m-ueth-v1 [cluster:TREND] | 4 | -0.3235 | 0.0000 | 0.0000 | 3.8075 | -0.0809 | 0.0895 | +0.0000 | +10.7599 | -2.2778 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | sp4-utc21-ubtc-v1 [NON_V1_RESEARCH, cluster:BTC_FRI21] | 1 | -0.3304 | 0.0000 | 0.0000 | 2.1185 | -0.3304 | 0.0225 | +0.0000 | +10.6289 | -2.3205 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |
| 6 | sp-donchian5m-hype-v1 [cluster:TREND] | 7 | -0.4082 | 14.2857 | 0.5043 | 4.6199 | -0.0583 | 0.1535 | +0.0000 | +10.2382 | -2.7995 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 7 | sp-ema15m-hype-v1 [cluster:TREND] | 4 | -0.4430 | 25.0000 | 0.3389 | 4.9665 | -0.1107 | 0.0884 | +0.0000 | +10.0241 | -3.0136 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 8 | sp-donchian5m-ubtc-v1 [cluster:TREND] | 9 | -0.4608 | 22.2222 | 0.2663 | 4.6487 | -0.0512 | 0.1974 | +0.0000 | +9.9147 | -3.1230 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | sp-ema15m-ubtc-v1 [cluster:TREND] | 4 | -0.4852 | 0.0000 | 0.0000 | 4.0650 | -0.1213 | 0.0872 | +0.0000 | +9.7641 | -3.2737 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |

## Spot slow / 1h (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-rsi1h-ubtc-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.7518 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-rsi1h-ueth-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.7518 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-rsi1h-usol-v1 (RETIRED_DATA_QUALITY) | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.7518 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-rsi1h-hype-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.7518 | -0.2859 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | sp4-shockrev1h-ubtc-v1 [NON_V1_RESEARCH, cluster:SHOCKREV] | 1 | -0.3852 | 0.0000 | 0.0000 | 2.4557 | -0.3852 | 0.0224 | +0.0000 | +10.2914 | -2.6580 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |

## Early read (not evidence)

Fast and spot_fast books with at least 10 closed trades, ranked by closed-trade count then net MTM after paid fees/funding (open exit cost not deducted). This is an operational early look so small-capital books can be watched before the 30-trade / DSR / fresh-OOS bar. It is **not** significance, **not** a PASS, and **does not** change the promotion bar. Nothing in this section is a CANDIDATE.

| Rank | Book | Lane | Closed | Net MTM USDC | Win % | Fees | Funding | Gate |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | g-squeeze-btc-p0-v1 | fast | 58 | -5.9349 | 20.6897 | 3.7617 | -0.0035 | UNPROVEN |
| 2 | f1-vwap5m-v1 | fast | 50 | -4.2557 | 48.0000 | 2.8789 | +0.0014 | UNPROVEN |
| 3 | g-squeeze-btc-p2-v1 | fast | 44 | -3.5484 | 25.0000 | 2.8942 | -0.0098 | UNPROVEN |
| 4 | g-vwap-sol-p1-v1 | fast | 43 | -5.5967 | 44.1860 | 2.3235 | +0.0011 | UNPROVEN |
| 5 | g-vwap-eth-p0-v1 | fast | 41 | +0.5277 | 58.5366 | 2.4857 | +0.0095 | UNPROVEN |
| 6 | g-vwap-eth-p1-v1 | fast | 41 | -0.7852 | 56.0976 | 2.3541 | +0.0093 | UNPROVEN |
| 7 | g-vwap-sol-p0-v1 | fast | 37 | -3.4096 | 40.5405 | 1.9463 | +0.0023 | UNPROVEN |
| 8 | g-vwap-btc-p1-v1 | fast | 37 | -3.4116 | 48.6486 | 2.2433 | -0.0065 | UNPROVEN |
| 9 | g-squeeze-sol-p0-v1 | fast | 36 | -3.0048 | 19.4444 | 2.3901 | -0.0008 | UNPROVEN |
| 10 | g-squeeze-btc-p1-v1 | fast | 33 | -5.4306 | 9.0909 | 2.1565 | +0.0002 | UNPROVEN |
| 11 | g-squeeze-sol-p2-v1 | fast | 32 | -2.4629 | 31.2500 | 2.1217 | -0.0023 | UNPROVEN |
| 12 | g-vwap-eth-p2-v1 | fast | 31 | +0.3983 | 51.6129 | 1.7771 | +0.0035 | UNPROVEN |
| 13 | g-vwap-sol-p2-v1 | fast | 31 | -2.8046 | 38.7097 | 1.6295 | +0.0022 | UNPROVEN |
| 14 | g-squeeze-sol-p1-v1 | fast | 31 | -2.9004 | 16.1290 | 2.0433 | -0.0039 | UNPROVEN |
| 15 | g-rsi2-all-p1-v1 | fast | 31 | -3.3426 | 35.4839 | 1.7757 | +0.0002 | UNPROVEN |
| 16 | g-vwap-btc-p0-v1 | fast | 31 | -3.6596 | 45.1613 | 1.9250 | -0.0038 | UNPROVEN |
| 17 | g-squeeze-eth-p1-v1 | fast | 31 | -4.8749 | 19.3548 | 2.0276 | -0.0012 | UNPROVEN |
| 18 | g-vwap-btc-p2-v1 | fast | 30 | -4.4037 | 40.0000 | 1.8314 | -0.0040 | UNPROVEN |
| 19 | g-vwap-all-p1-v1 | fast | 23 | -2.5372 | 34.7826 | 1.2576 | +0.0016 | NOT_SIGNIFICANT |
| 20 | f3-rsi2-5m-v1 | fast | 21 | -2.5745 | 33.3333 | 1.2403 | +0.0009 | NOT_SIGNIFICANT |
| 21 | g-rsi2-sol-p1-v1 | fast | 21 | -2.6771 | 23.8095 | 1.1643 | +0.0002 | NOT_SIGNIFICANT |
| 22 | g-squeeze-eth-p0-v1 | fast | 17 | -3.1729 | 23.5294 | 1.1229 | -0.0012 | NOT_SIGNIFICANT |
| 23 | g-ema-all-p1-v1 [cluster:TREND] | fast | 15 | -4.7976 | 6.6667 | 0.6709 | +0.0038 | NOT_SIGNIFICANT |
| 24 | g-rsi2-sol-p0-v1 | fast | 14 | -1.6039 | 35.7143 | 0.7938 | +0.0011 | NOT_SIGNIFICANT |
| 25 | g-rsi2-btc-p1-v1 | fast | 13 | -0.2855 | 61.5385 | 0.8167 | +0.0000 | NOT_SIGNIFICANT |
| 26 | g-ema-btc-p2-v1 [cluster:TREND] | fast | 13 | -3.3617 | 7.6923 | 0.6244 | +0.0039 | NOT_SIGNIFICANT |
| 27 | g-rsi2-eth-p1-v1 | fast | 12 | -1.3475 | 41.6667 | 0.6879 | +0.0000 | NOT_SIGNIFICANT |
| 28 | f5-squeeze1m-v1 | fast | 11 | -2.1846 | 9.0909 | 0.7295 | +0.0016 | NOT_SIGNIFICANT |
| 29 | g-ema-btc-p1-v1 [cluster:TREND] | fast | 10 | -2.9624 | 0.0000 | 0.4985 | +0.0054 | NOT_SIGNIFICANT |
| 30 | g-ema-eth-p1-v1 [cluster:TREND] | fast | 10 | -3.1387 | 10.0000 | 0.4052 | -0.0016 | NOT_SIGNIFICANT |
| 31 | f4-ema15m-v1 [cluster:TREND] | fast | 10 | -3.6730 | 0.0000 | 0.4619 | +0.0011 | NOT_SIGNIFICANT |

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
