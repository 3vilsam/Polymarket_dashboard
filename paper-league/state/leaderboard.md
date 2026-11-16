# PAPER league — 100 virtual USDC perp books + 16.24 virtual USDC spot books

Updated 2026-11-16T17:18:04+08:00 MYT | tick 836 | 125 books (107 perp @100 USDC, 18 spot @16.24 USDC; incl. 9 v4 research-sweep books registered 12 Nov 2026) | public reads only

Spot research books use 5m/15m/1h timeframes. Do not compare raw Net MTM USDC across the 100-USDC and 16.24-USDC tables. An 'Early read (not evidence)' table lists fast books with >=10 closed trades; it is not the promotion bar. Ranks use net MTM (open exit cost not deducted). Gate comparisons use same-start indicative exit equity: perp books deduct taker+2bp; spot books deduct official tier-0 spot taker 0.070%+2bp. Official promotion controls remain the BTC-perp hold and random-entry books.

## Controls / luck benchmarks (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | c1-random15m-v1 | 11 | +0.4569 | 45.4545 | 1.4803 | 2.0147 | 0.0697 | 0.4422 | -0.0004 | +13.5441 | +0.0000 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); CONTROL |
| 2 | b0-btc-1x-hold-control-v1 | 0 | -13.0934 | — | — | 16.9854 | — | 0.0450 | -0.0915 | +0.0000 | -13.5441 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); CONTROL; NONTRADABLE risk-exempt |

## Fast / short-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | g-vwap-eth-p2-v1 | 18 | +3.3661 | 72.2222 | 2.3756 | 2.6304 | 0.1870 | 0.9613 | +0.0032 | +16.4808 | +2.9367 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-vwap-eth-p0-v1 | 21 | +2.6324 | 66.6667 | 1.9432 | 2.2871 | 0.1254 | 1.2005 | +0.0095 | +15.7472 | +2.2030 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | g-vwap-eth-p1-v1 | 27 | +1.5457 | 62.9630 | 1.3330 | 3.4650 | 0.0572 | 1.4917 | +0.0085 | +14.6604 | +1.1163 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | g-ema-sol-p1-v1 [cluster:TREND] | 4 | +0.8562 | 50.0000 | 1.8800 | 1.2469 | 0.2141 | 0.1526 | +0.0012 | +13.9710 | +0.4268 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | g-squeeze-sol-p2-v1 | 21 | -0.1181 | 38.0952 | 0.9621 | 2.5033 | -0.0079 | 1.4279 | +0.0004 | +12.9485 | -0.5956 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | g-squeeze-sol-p0-v1 | 25 | -0.1279 | 28.0000 | 0.9509 | 3.1837 | -0.0104 | 1.7001 | -0.0008 | +12.9387 | -0.6055 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | g-asia-eth-p0-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +12.9855 | -0.5587 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | g-asia-eth-p1-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +12.9855 | -0.5587 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | g-asia-eth-p2-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +12.9855 | -0.5587 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | g-rsi2-eth-p2-v1 | 2 | -0.2057 | 50.0000 | 0.5837 | 0.5261 | -0.1028 | 0.0688 | +0.0000 | +12.9091 | -0.6351 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | g-rsi2-btc-p2-v1 | 4 | -0.2851 | 75.0000 | 0.4166 | 1.1377 | -0.0713 | 0.2053 | +0.0007 | +12.8296 | -0.7145 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-rsi2-btc-p1-v1 | 9 | -0.3424 | 66.6667 | 0.5331 | 0.8211 | -0.0380 | 0.5501 | +0.0000 | +12.7724 | -0.7718 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-rsi2-sol-p2-v1 | 4 | -0.3841 | 50.0000 | 0.4742 | 1.0809 | -0.0960 | 0.1989 | +0.0003 | +12.7307 | -0.8135 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | n4-utc21-btc-v1 [cluster:BTC_FRI21] | 2 | -0.4512 | 50.0000 | 0.0673 | 0.5879 | -0.2256 | 0.0408 | -0.0003 | +12.3054 | -0.8806 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-rsi2-eth-p0-v1 | 6 | -0.5659 | 33.3333 | 0.3736 | 1.4383 | -0.0943 | 0.2999 | +0.0001 | +12.5489 | -0.9953 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-ema-eth-p0-v1 [cluster:TREND] | 2 | -0.6556 | 0.0000 | 0.0000 | 1.2232 | -0.3278 | 0.0688 | -0.0003 | +12.4591 | -1.0850 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-ema-eth-p2-v1 [cluster:TREND] | 3 | -0.7253 | 0.0000 | 0.0000 | 1.4748 | -0.2418 | 0.1003 | +0.0009 | +12.3895 | -1.1546 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-asia-btc-p0-v1 | 3 | -0.7269 | 0.0000 | 0.0000 | 0.9987 | -0.2423 | 0.1615 | +0.0021 | +12.3878 | -1.1563 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-asia-btc-p1-v1 | 3 | -0.7269 | 0.0000 | 0.0000 | 0.9987 | -0.2423 | 0.1615 | +0.0021 | +12.3878 | -1.1563 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-asia-btc-p2-v1 | 3 | -0.7269 | 0.0000 | 0.0000 | 0.9987 | -0.2423 | 0.1615 | +0.0021 | +12.3878 | -1.1563 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-rsi2-eth-p1-v1 | 10 | -0.7659 | 50.0000 | 0.3897 | 1.0885 | -0.0766 | 0.5552 | +0.0000 | +12.3489 | -1.1953 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-rsi2-btc-p0-v1 | 8 | -0.7660 | 37.5000 | 0.3106 | 1.0859 | -0.0958 | 0.4656 | +0.0000 | +12.3487 | -1.1954 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-squeeze-sol-p1-v1 | 17 | -0.7939 | 23.5294 | 0.7893 | 2.9026 | -0.0467 | 1.1320 | -0.0009 | +12.3209 | -1.2232 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-ema-btc-p2-v1 [cluster:TREND] | 5 | -0.8243 | 20.0000 | 0.5068 | 1.7912 | -0.1649 | 0.2250 | -0.0008 | +12.2904 | -1.2537 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | g-rsi2-sol-p0-v1 | 6 | -0.9101 | 33.3333 | 0.2610 | 1.6721 | -0.1517 | 0.2901 | +0.0003 | +12.2046 | -1.3395 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | f4-ema15m-v1 [cluster:TREND] | 3 | -0.9263 | 0.0000 | 0.0000 | 1.4561 | -0.3088 | 0.1298 | -0.0040 | +12.1884 | -1.3557 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-ema-btc-p0-v1 [cluster:TREND] | 3 | -0.9263 | 0.0000 | 0.0000 | 1.4561 | -0.3088 | 0.1298 | -0.0040 | +12.1884 | -1.3557 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-ema-eth-p1-v1 [cluster:TREND] | 6 | -0.9671 | 16.6667 | 0.2809 | 1.9357 | -0.2171 | 0.2649 | -0.0003 | +12.1180 | -1.4261 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-ema-sol-p0-v1 [cluster:TREND] | 3 | -1.0369 | 0.0000 | 0.0000 | 1.3824 | -0.3456 | 0.0866 | -0.0005 | +12.0778 | -1.4663 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-squeeze-btc-p2-v1 | 23 | -1.1219 | 34.7826 | 0.7519 | 2.3161 | -0.0542 | 1.5487 | -0.0071 | +11.9452 | -1.5989 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-ema-sol-p2-v1 [cluster:TREND] | 3 | -1.1676 | 0.0000 | 0.0000 | 2.3393 | -0.3892 | 0.0948 | -0.0009 | +11.9472 | -1.5970 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-vwap-btc-p1-v1 | 23 | -1.1776 | 52.1739 | 0.7039 | 3.0700 | -0.0512 | 1.3567 | -0.0052 | +11.9372 | -1.6070 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | f2-asia15m-v1 | 4 | -1.1995 | 0.0000 | 0.0000 | 1.3988 | -0.2999 | 0.2081 | +0.0022 | +11.9153 | -1.6289 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | g-asia-all-p1-v1 | 4 | -1.1995 | 0.0000 | 0.0000 | 1.3988 | -0.2999 | 0.2081 | +0.0022 | +11.9153 | -1.6289 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-asia-sol-p0-v1 | 3 | -1.2183 | 0.0000 | 0.0000 | 1.4176 | -0.4061 | 0.1365 | +0.0005 | +11.8965 | -1.6477 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | g-asia-sol-p1-v1 | 3 | -1.2183 | 0.0000 | 0.0000 | 1.4176 | -0.4061 | 0.1365 | +0.0005 | +11.8965 | -1.6477 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 37 | g-asia-sol-p2-v1 | 3 | -1.2183 | 0.0000 | 0.0000 | 1.4176 | -0.4061 | 0.1365 | +0.0005 | +11.8965 | -1.6477 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-vwap-btc-p0-v1 | 19 | -1.4389 | 52.6316 | 0.5906 | 2.8246 | -0.0757 | 1.1655 | -0.0019 | +11.6759 | -1.8682 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | f3-rsi2-5m-v1 | 12 | -1.4423 | 33.3333 | 0.2140 | 2.2184 | -0.1202 | 0.6741 | +0.0001 | +11.6724 | -1.8717 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | g-ema-all-p1-v1 [cluster:TREND] | 7 | -1.6078 | 14.2857 | 0.2103 | 2.0616 | -0.2714 | 0.3491 | -0.0013 | +11.4752 | -2.0689 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | g-ema-btc-p1-v1 [cluster:TREND] | 5 | -1.6360 | 0.0000 | 0.0000 | 1.9902 | -0.3856 | 0.2545 | -0.0008 | +11.4470 | -2.0971 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | g-squeeze-btc-p1-v1 | 18 | -2.0833 | 16.6667 | 0.3968 | 2.5637 | -0.1157 | 1.1908 | +0.0001 | +11.0314 | -2.5127 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | g-rsi2-sol-p1-v1 | 10 | -2.1310 | 20.0000 | 0.0713 | 2.2755 | -0.2131 | 0.4879 | +0.0003 | +10.9838 | -2.5604 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | g-vwap-btc-p2-v1 | 15 | -2.1627 | 40.0000 | 0.3658 | 2.9197 | -0.1442 | 0.9016 | -0.0028 | +10.9520 | -2.5921 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | f5-squeeze1m-v1 | 11 | -2.1846 | 9.0909 | 0.0292 | 2.3893 | -0.1986 | 0.7295 | +0.0016 | +10.9301 | -2.6140 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 46 | g-rsi2-all-p1-v1 | 15 | -2.2321 | 46.6667 | 0.2194 | 2.4464 | -0.1488 | 0.7776 | +0.0003 | +10.8827 | -2.6614 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | g-squeeze-eth-p2-v1 | 9 | -2.3227 | 11.1111 | 0.0598 | 2.4051 | -0.2581 | 0.6001 | -0.0002 | +10.7920 | -2.7521 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 48 | g-squeeze-eth-p1-v1 | 14 | -2.4615 | 21.4286 | 0.2784 | 2.4803 | -0.1758 | 0.9275 | -0.0020 | +10.6532 | -2.8909 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | g-vwap-all-p1-v1 | 23 | -2.5372 | 34.7826 | 0.5707 | 5.3758 | -0.1103 | 1.2576 | +0.0016 | +10.5775 | -2.9666 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 50 | g-vwap-sol-p0-v1 | 22 | -2.6043 | 40.9091 | 0.5033 | 5.2270 | -0.1106 | 1.1250 | +0.0030 | +10.4784 | -3.0658 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 51 | g-vwap-sol-p2-v1 | 20 | -2.6164 | 35.0000 | 0.4683 | 5.1710 | -0.1308 | 1.0336 | +0.0028 | +10.4983 | -3.0458 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 52 | f1-vwap5m-v1 | 33 | -2.6766 | 48.4848 | 0.6208 | 5.6463 | -0.0811 | 1.8656 | +0.0045 | +10.4381 | -3.1060 | 434 | — | 4 | not flagged | UNPROVEN; UNPROVEN |
| 53 | g-squeeze-btc-p0-v1 | 25 | -3.1491 | 16.0000 | 0.3153 | 3.1491 | -0.1260 | 1.6425 | -0.0000 | +9.9656 | -3.5785 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 54 | g-squeeze-eth-p0-v1 | 17 | -3.1729 | 23.5294 | 0.2410 | 3.3755 | -0.1866 | 1.1229 | -0.0012 | +9.9418 | -3.6023 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 55 | g-vwap-sol-p1-v1 | 26 | -3.9348 | 42.3077 | 0.3913 | 4.9059 | -0.1464 | 1.3952 | +0.0017 | +9.1469 | -4.3972 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |

## Slow / long-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | l1-supertrend1h-v1 [cluster:TREND] | 1 | +0.3643 | 100.0000 | inf | 1.1588 | 0.3643 | 0.0214 | +0.0031 | +13.4790 | -0.0651 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-supertrend-sol-p0-v1 [cluster:TREND] | 1 | +0.3643 | 100.0000 | inf | 1.1588 | 0.3643 | 0.0214 | +0.0031 | +13.4790 | -0.0651 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | n1-tsmom-mh1h-v1 [cluster:TREND] | 1 | +0.3606 | 100.0000 | inf | 0.8811 | 0.3606 | 0.0163 | +0.0022 | +13.1172 | -0.0688 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | s1-donchian40-ablation-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | s2-bb40-ema200-ablation-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | s4-ewmac-riskcap-noadd-ablation-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | r1-trend-rsi-pullback-market-lane-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | l2-macd4h-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | l3-funding1h-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | l4-weekly1d-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | g-supertrend-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-supertrend-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-supertrend-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-supertrend-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-supertrend-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-supertrend-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-macd-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-macd-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-macd-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-macd-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-macd-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-macd-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-macd-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-macd-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | g-macd-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-funding-btc-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-funding-btc-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-funding-btc-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-funding-eth-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-funding-eth-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-funding-eth-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-funding-sol-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-funding-sol-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | g-funding-sol-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-weekly-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | g-weekly-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 37 | g-weekly-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-weekly-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | g-weekly-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | g-weekly-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | g-weekly-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | g-weekly-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | g-weekly-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +13.1148 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | n3-negfund-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.7566 | -0.4294 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | n5-weekend-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.7566 | -0.4294 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 46 | n6-ethbtc-z1h-v1 [UNHEDGED_ETH_DIRECTIONAL] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.7566 | -0.4294 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | n7-xsmom72h-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.7566 | -0.4294 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 48 | g-supertrend-sol-p1-v1 [cluster:TREND] | 1 | -0.2468 | 0.0000 | 0.0000 | 0.4058 | -0.2468 | 0.0103 | +0.0004 | +12.8679 | -0.6762 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | g-supertrend-btc-p2-v1 [cluster:TREND] | 0 | -0.3187 | — | — | 0.3714 | — | 0.0068 | -0.0025 | +12.7865 | -0.7577 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 50 | n2-shockrev1h-v1 [cluster:SHOCKREV] | 1 | -0.4808 | 0.0000 | 0.0000 | 0.4916 | -0.4808 | 0.0132 | -0.0003 | +12.2759 | -0.9101 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |

## Spot buy-and-hold controls (16.24 virtual USDC, 1x long, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-hold-usol-v1 (RETIRED_DATA_QUALITY) | 1 | -0.0166 | 0.0000 | 0.0000 | 3.9287 | -0.0166 | 0.0226 | +0.0000 | +12.7424 | -0.5318 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 2 | sp-hold-hype-v1 | 0 | -1.1843 | — | — | 19.4142 | — | 0.0110 | +0.0000 | +5.4716 | -7.8026 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 3 | sp-hold-ueth-v1 | 0 | -2.0496 | — | — | 18.4092 | — | 0.0114 | +0.0000 | +0.1453 | -13.1290 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 4 | sp-hold-ubtc-v1 | 0 | -2.0819 | — | — | 16.5977 | — | 0.0113 | +0.0000 | -0.0532 | -13.3274 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |

## Spot fast / 5m and 15m (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-ema15m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.8448 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-ema15m-hype-v1 [cluster:TREND] | 2 | -0.0934 | 50.0000 | 0.7086 | 4.3306 | -0.0467 | 0.0441 | +0.0000 | +12.2698 | -1.0044 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-donchian5m-ubtc-v1 [cluster:TREND] | 4 | -0.1048 | 25.0000 | 0.5204 | 2.4980 | -0.0262 | 0.0890 | +0.0000 | +12.1992 | -1.0750 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-donchian5m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 1 | -0.1128 | 0.0000 | 0.0000 | 1.0376 | -0.1128 | 0.0226 | +0.0000 | +12.1502 | -1.1240 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | sp-donchian5m-ueth-v1 [cluster:TREND] | 9 | -0.1148 | 33.3333 | 0.8332 | 3.9796 | -0.0128 | 0.2038 | +0.0000 | +12.1380 | -1.1362 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 6 | sp-ema15m-ueth-v1 [cluster:TREND] | 2 | -0.1371 | 0.0000 | 0.0000 | 2.8634 | -0.0686 | 0.0450 | +0.0000 | +12.0005 | -1.2737 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | sp-ema15m-ubtc-v1 [cluster:TREND] | 2 | -0.2564 | 0.0000 | 0.0000 | 2.9158 | -0.1282 | 0.0436 | +0.0000 | +11.2661 | -2.0081 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | sp-donchian5m-hype-v1 [cluster:TREND] | 6 | -0.2665 | 16.6667 | 0.6092 | 3.8732 | -0.0444 | 0.1320 | +0.0000 | +11.2039 | -2.0703 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | sp4-utc21-ubtc-v1 [NON_V1_RESEARCH, cluster:BTC_FRI21] | 1 | -0.3304 | 0.0000 | 0.0000 | 2.1185 | -0.3304 | 0.0225 | +0.0000 | +10.7220 | -2.4640 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |

## Spot slow / 1h (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-rsi1h-ubtc-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.8448 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-rsi1h-ueth-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.8448 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-rsi1h-usol-v1 (RETIRED_DATA_QUALITY) | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.8448 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-rsi1h-hype-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.8448 | -0.4294 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | sp4-shockrev1h-ubtc-v1 [NON_V1_RESEARCH, cluster:SHOCKREV] | 1 | -0.3852 | 0.0000 | 0.0000 | 2.4557 | -0.3852 | 0.0224 | +0.0000 | +10.3845 | -2.8015 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |

## Early read (not evidence)

Fast and spot_fast books with at least 10 closed trades, ranked by closed-trade count then net MTM after paid fees/funding (open exit cost not deducted). This is an operational early look so small-capital books can be watched before the 30-trade / DSR / fresh-OOS bar. It is **not** significance, **not** a PASS, and **does not** change the promotion bar. Nothing in this section is a CANDIDATE.

| Rank | Book | Lane | Closed | Net MTM USDC | Win % | Fees | Funding | Gate |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | f1-vwap5m-v1 | fast | 33 | -2.6766 | 48.4848 | 1.8656 | +0.0045 | UNPROVEN |
| 2 | g-vwap-eth-p1-v1 | fast | 27 | +1.5457 | 62.9630 | 1.4917 | +0.0085 | NOT_SIGNIFICANT |
| 3 | g-vwap-sol-p1-v1 | fast | 26 | -3.9348 | 42.3077 | 1.3952 | +0.0017 | NOT_SIGNIFICANT |
| 4 | g-squeeze-sol-p0-v1 | fast | 25 | -0.1279 | 28.0000 | 1.7001 | -0.0008 | NOT_SIGNIFICANT |
| 5 | g-squeeze-btc-p0-v1 | fast | 25 | -3.1491 | 16.0000 | 1.6425 | -0.0000 | NOT_SIGNIFICANT |
| 6 | g-squeeze-btc-p2-v1 | fast | 23 | -1.1219 | 34.7826 | 1.5487 | -0.0071 | NOT_SIGNIFICANT |
| 7 | g-vwap-btc-p1-v1 | fast | 23 | -1.1776 | 52.1739 | 1.3567 | -0.0052 | NOT_SIGNIFICANT |
| 8 | g-vwap-all-p1-v1 | fast | 23 | -2.5372 | 34.7826 | 1.2576 | +0.0016 | NOT_SIGNIFICANT |
| 9 | g-vwap-sol-p0-v1 | fast | 22 | -2.6043 | 40.9091 | 1.1250 | +0.0030 | NOT_SIGNIFICANT |
| 10 | g-vwap-eth-p0-v1 | fast | 21 | +2.6324 | 66.6667 | 1.2005 | +0.0095 | NOT_SIGNIFICANT |
| 11 | g-squeeze-sol-p2-v1 | fast | 21 | -0.1181 | 38.0952 | 1.4279 | +0.0004 | NOT_SIGNIFICANT |
| 12 | g-vwap-sol-p2-v1 | fast | 20 | -2.6164 | 35.0000 | 1.0336 | +0.0028 | NOT_SIGNIFICANT |
| 13 | g-vwap-btc-p0-v1 | fast | 19 | -1.4389 | 52.6316 | 1.1655 | -0.0019 | NOT_SIGNIFICANT |
| 14 | g-vwap-eth-p2-v1 | fast | 18 | +3.3661 | 72.2222 | 0.9613 | +0.0032 | NOT_SIGNIFICANT |
| 15 | g-squeeze-btc-p1-v1 | fast | 18 | -2.0833 | 16.6667 | 1.1908 | +0.0001 | NOT_SIGNIFICANT |
| 16 | g-squeeze-sol-p1-v1 | fast | 17 | -0.7939 | 23.5294 | 1.1320 | -0.0009 | NOT_SIGNIFICANT |
| 17 | g-squeeze-eth-p0-v1 | fast | 17 | -3.1729 | 23.5294 | 1.1229 | -0.0012 | NOT_SIGNIFICANT |
| 18 | g-vwap-btc-p2-v1 | fast | 15 | -2.1627 | 40.0000 | 0.9016 | -0.0028 | NOT_SIGNIFICANT |
| 19 | g-rsi2-all-p1-v1 | fast | 15 | -2.2321 | 46.6667 | 0.7776 | +0.0003 | NOT_SIGNIFICANT |
| 20 | g-squeeze-eth-p1-v1 | fast | 14 | -2.4615 | 21.4286 | 0.9275 | -0.0020 | NOT_SIGNIFICANT |
| 21 | f3-rsi2-5m-v1 | fast | 12 | -1.4423 | 33.3333 | 0.6741 | +0.0001 | NOT_SIGNIFICANT |
| 22 | f5-squeeze1m-v1 | fast | 11 | -2.1846 | 9.0909 | 0.7295 | +0.0016 | NOT_SIGNIFICANT |
| 23 | g-rsi2-eth-p1-v1 | fast | 10 | -0.7659 | 50.0000 | 0.5552 | +0.0000 | NOT_SIGNIFICANT |
| 24 | g-rsi2-sol-p1-v1 | fast | 10 | -2.1310 | 20.0000 | 0.4879 | +0.0003 | NOT_SIGNIFICANT |

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
