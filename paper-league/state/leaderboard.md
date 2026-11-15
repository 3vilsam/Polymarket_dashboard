# PAPER league — 100 virtual USDC perp books + 16.24 virtual USDC spot books

Updated 2026-11-16T05:21:03+08:00 MYT | tick 700 | 125 books (107 perp @100 USDC, 18 spot @16.24 USDC; incl. 9 v4 research-sweep books registered 12 Nov 2026) | public reads only

Spot research books use 5m/15m/1h timeframes. Do not compare raw Net MTM USDC across the 100-USDC and 16.24-USDC tables. An 'Early read (not evidence)' table lists fast books with >=10 closed trades; it is not the promotion bar. Ranks use net MTM (open exit cost not deducted). Gate comparisons use same-start indicative exit equity: perp books deduct taker+2bp; spot books deduct official tier-0 spot taker 0.070%+2bp. Official promotion controls remain the BTC-perp hold and random-entry books.

## Controls / luck benchmarks (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | c1-random15m-v1 | 8 | +0.3042 | 37.5000 | 1.3031 | 1.8601 | 0.0582 | 0.3274 | -0.0003 | +12.4765 | +0.0000 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); CONTROL |
| 2 | b0-btc-1x-hold-control-v1 | 0 | -12.1782 | — | — | 16.9854 | — | 0.0450 | -0.0849 | +0.0000 | -12.4765 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); CONTROL; NONTRADABLE risk-exempt |

## Fast / short-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | g-vwap-eth-p2-v1 | 14 | +2.0725 | 64.2857 | 1.8470 | 2.6304 | 0.1480 | 0.6989 | +0.0025 | +14.2723 | +1.7958 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-vwap-eth-p0-v1 | 15 | +1.8881 | 66.6667 | 1.9300 | 2.2871 | 0.1259 | 0.8241 | +0.0077 | +14.0879 | +1.6113 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | g-ema-sol-p1-v1 [cluster:TREND] | 3 | +1.3512 | 66.6667 | 3.8273 | 0.9790 | 0.4504 | 0.1183 | +0.0018 | +13.5510 | +1.0744 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | g-vwap-eth-p1-v1 | 19 | +0.5857 | 57.8947 | 1.1630 | 3.4650 | 0.0334 | 1.0069 | +0.0080 | +12.7367 | +0.2602 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | g-squeeze-sol-p0-v1 | 20 | +0.2045 | 30.0000 | 1.0515 | 3.1837 | 0.0102 | 1.3318 | -0.0017 | +12.4043 | -0.0722 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | g-asia-btc-p0-v1 | 1 | -0.0076 | 0.0000 | 0.0000 | 0.2813 | -0.0076 | 0.0668 | +0.0021 | +12.1922 | -0.2843 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | g-asia-btc-p1-v1 | 1 | -0.0076 | 0.0000 | 0.0000 | 0.2813 | -0.0076 | 0.0668 | +0.0021 | +12.1922 | -0.2843 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | g-asia-btc-p2-v1 | 1 | -0.0076 | 0.0000 | 0.0000 | 0.2813 | -0.0076 | 0.0668 | +0.0021 | +12.1922 | -0.2843 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | g-asia-eth-p0-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +12.0705 | -0.4061 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | g-asia-eth-p1-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +12.0705 | -0.4061 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | g-asia-eth-p2-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +12.0705 | -0.4061 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-ema-eth-p2-v1 [cluster:TREND] | 1 | -0.1503 | 0.0000 | 0.0000 | 0.9322 | -0.1503 | 0.0324 | -0.0000 | +12.0495 | -0.4271 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-ema-eth-p0-v1 [cluster:TREND] | 1 | -0.1704 | 0.0000 | 0.0000 | 0.9322 | -0.1704 | 0.0324 | -0.0003 | +12.0294 | -0.4472 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-rsi2-eth-p2-v1 | 2 | -0.2057 | 50.0000 | 0.5837 | 0.5261 | -0.1028 | 0.0688 | +0.0000 | +11.9941 | -0.4824 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-rsi2-btc-p2-v1 | 3 | -0.3078 | 66.6667 | 0.3702 | 1.0646 | -0.1026 | 0.1389 | +0.0007 | +11.8920 | -0.5846 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-ema-btc-p2-v1 [cluster:TREND] | 3 | -0.3234 | 33.3333 | 0.8758 | 1.3431 | -0.0401 | 0.1567 | +0.0001 | +11.8401 | -0.6365 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-squeeze-sol-p2-v1 | 16 | -0.3784 | 37.5000 | 0.8791 | 2.5033 | -0.0237 | 1.0594 | +0.0004 | +11.8214 | -0.6552 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-rsi2-sol-p2-v1 | 4 | -0.3841 | 50.0000 | 0.4742 | 1.0809 | -0.0960 | 0.1989 | +0.0003 | +11.8157 | -0.6609 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-rsi2-btc-p1-v1 | 8 | -0.4128 | 62.5000 | 0.5027 | 0.8211 | -0.0456 | 0.5167 | +0.0000 | +11.7389 | -0.7376 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | f2-asia15m-v1 | 2 | -0.4854 | 0.0000 | 0.0000 | 0.8244 | -0.2427 | 0.1140 | +0.0022 | +11.7143 | -0.7622 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-asia-all-p1-v1 | 2 | -0.4854 | 0.0000 | 0.0000 | 0.8244 | -0.2427 | 0.1140 | +0.0022 | +11.7143 | -0.7622 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-ema-sol-p0-v1 [cluster:TREND] | 1 | -0.4919 | 0.0000 | 0.0000 | 0.8393 | -0.3276 | 0.0401 | +0.0000 | +11.6837 | -0.7929 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-ema-eth-p1-v1 [cluster:TREND] | 4 | -0.4994 | 25.0000 | 0.5046 | 1.1450 | -0.1249 | 0.1642 | +0.0001 | +11.7003 | -0.7762 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | n4-utc21-btc-v1 [cluster:BTC_FRI21] | 1 | -0.5689 | 0.0000 | 0.0000 | 0.5872 | -0.4838 | 0.0302 | +0.0000 | +11.2538 | -0.8608 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | f4-ema15m-v1 [cluster:TREND] | 1 | -0.6067 | 0.0000 | 0.0000 | 1.0496 | -0.4883 | 0.0599 | -0.0031 | +11.5564 | -0.9201 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-ema-btc-p0-v1 [cluster:TREND] | 1 | -0.6067 | 0.0000 | 0.0000 | 1.0496 | -0.4883 | 0.0599 | -0.0031 | +11.5564 | -0.9201 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-rsi2-eth-p0-v1 | 5 | -0.6115 | 40.0000 | 0.3746 | 1.3796 | -0.1127 | 0.2665 | +0.0001 | +11.5401 | -0.9365 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-rsi2-btc-p0-v1 | 7 | -0.7135 | 42.8571 | 0.3260 | 1.0859 | -0.1019 | 0.3992 | +0.0000 | +11.4863 | -0.9903 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-asia-sol-p0-v1 | 2 | -0.8276 | 0.0000 | 0.0000 | 1.0277 | -0.4138 | 0.1038 | +0.0005 | +11.3722 | -1.1044 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-asia-sol-p1-v1 | 2 | -0.8276 | 0.0000 | 0.0000 | 1.0277 | -0.4138 | 0.1038 | +0.0005 | +11.3722 | -1.1044 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-asia-sol-p2-v1 | 2 | -0.8276 | 0.0000 | 0.0000 | 1.0277 | -0.4138 | 0.1038 | +0.0005 | +11.3722 | -1.1044 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-squeeze-sol-p1-v1 | 14 | -0.8497 | 21.4286 | 0.7164 | 2.9026 | -0.0607 | 0.9318 | -0.0009 | +11.3500 | -1.1265 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-rsi2-eth-p1-v1 | 8 | -0.9218 | 50.0000 | 0.3542 | 1.0316 | -0.0863 | 0.4553 | +0.0000 | +11.2300 | -1.2466 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | g-squeeze-btc-p2-v1 | 19 | -0.9451 | 31.5789 | 0.7896 | 2.3161 | -0.0497 | 1.2538 | -0.0054 | +11.2546 | -1.2219 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-ema-sol-p2-v1 [cluster:TREND] | 2 | -0.9978 | 0.0000 | 0.0000 | 2.0886 | -0.4183 | 0.0784 | -0.0006 | +11.1782 | -1.2983 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | g-rsi2-sol-p0-v1 | 5 | -1.0064 | 20.0000 | 0.2210 | 1.6311 | -0.1919 | 0.2574 | +0.0003 | +11.1463 | -1.3302 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 37 | g-ema-all-p1-v1 [cluster:TREND] | 5 | -1.1459 | 20.0000 | 0.3064 | 1.3432 | -0.2292 | 0.2352 | -0.0020 | +11.0539 | -1.4226 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-ema-btc-p1-v1 [cluster:TREND] | 3 | -1.1740 | 0.0000 | 0.0000 | 1.2480 | -0.3913 | 0.1407 | -0.0016 | +11.0258 | -1.4508 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | g-vwap-btc-p1-v1 | 17 | -1.3426 | 52.9412 | 0.5791 | 3.0700 | -0.0849 | 0.9970 | -0.0043 | +10.8099 | -1.6666 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | f3-rsi2-5m-v1 | 10 | -1.4356 | 40.0000 | 0.2205 | 2.2184 | -0.1388 | 0.5752 | +0.0001 | +10.7164 | -1.7601 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | g-vwap-btc-p0-v1 | 13 | -1.6283 | 46.1538 | 0.4300 | 2.8246 | -0.1331 | 0.8095 | -0.0019 | +10.5242 | -1.9524 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | g-squeeze-btc-p1-v1 | 16 | -1.7082 | 18.7500 | 0.4451 | 2.1754 | -0.1068 | 1.0598 | +0.0001 | +10.4915 | -1.9850 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | g-squeeze-eth-p1-v1 | 12 | -1.7706 | 25.0000 | 0.3491 | 2.1065 | -0.1476 | 0.7960 | -0.0019 | +10.4292 | -2.0474 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | g-vwap-btc-p2-v1 | 10 | -2.1120 | 20.0000 | 0.2478 | 2.9146 | -0.2213 | 0.6104 | -0.0014 | +10.0405 | -2.4360 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | f5-squeeze1m-v1 | 11 | -2.1846 | 9.0909 | 0.0292 | 2.3893 | -0.1986 | 0.7295 | +0.0016 | +10.0151 | -2.4614 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 46 | g-rsi2-sol-p1-v1 | 9 | -2.2273 | 22.2222 | 0.0744 | 2.2295 | -0.2262 | 0.4553 | +0.0003 | +9.9254 | -2.5511 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | g-squeeze-eth-p2-v1 | 9 | -2.3227 | 11.1111 | 0.0598 | 2.4051 | -0.2581 | 0.6001 | -0.0002 | +9.8770 | -2.5995 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 48 | g-vwap-sol-p2-v1 | 16 | -2.3456 | 31.2500 | 0.4219 | 4.6910 | -0.1602 | 0.8380 | +0.0024 | +9.8090 | -2.6676 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | g-squeeze-btc-p0-v1 | 21 | -2.3808 | 19.0476 | 0.3786 | 2.3852 | -0.1134 | 1.3828 | +0.0009 | +9.8190 | -2.6576 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 50 | g-rsi2-all-p1-v1 | 13 | -2.3856 | 46.1538 | 0.1938 | 2.3902 | -0.1660 | 0.6792 | +0.0003 | +9.7668 | -2.7097 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 51 | g-vwap-sol-p0-v1 | 17 | -2.4855 | 35.2941 | 0.3867 | 5.2270 | -0.1590 | 0.8594 | +0.0030 | +9.6691 | -2.8075 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 52 | g-vwap-all-p1-v1 | 23 | -2.5372 | 34.7826 | 0.5707 | 5.3758 | -0.1103 | 1.2576 | +0.0016 | +9.6625 | -2.8140 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 53 | f1-vwap5m-v1 | 25 | -2.7442 | 44.0000 | 0.5155 | 5.6463 | -0.1138 | 1.4048 | +0.0024 | +9.4088 | -3.0678 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 54 | g-vwap-sol-p1-v1 | 20 | -2.9846 | 40.0000 | 0.3427 | 4.1948 | -0.1601 | 1.0583 | +0.0017 | +9.1700 | -3.3066 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 55 | g-squeeze-eth-p0-v1 | 17 | -3.1729 | 23.5294 | 0.2410 | 3.3755 | -0.1866 | 1.1229 | -0.0012 | +9.0268 | -3.4497 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |

## Slow / long-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | l1-supertrend1h-v1 [cluster:TREND] | 1 | +0.3643 | 100.0000 | inf | 1.1588 | 0.3643 | 0.0214 | +0.0031 | +12.5640 | +0.0875 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-supertrend-sol-p0-v1 [cluster:TREND] | 1 | +0.3643 | 100.0000 | inf | 1.1588 | 0.3643 | 0.0214 | +0.0031 | +12.5640 | +0.0875 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | n1-tsmom-mh1h-v1 [cluster:TREND] | 1 | +0.3606 | 100.0000 | inf | 0.8811 | 0.3606 | 0.0163 | +0.0022 | +12.1985 | +0.0838 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | s1-donchian40-ablation-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | s2-bb40-ema200-ablation-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | s4-ewmac-riskcap-noadd-ablation-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | r1-trend-rsi-pullback-market-lane-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | l2-macd4h-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | l3-funding1h-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | l4-weekly1d-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | g-supertrend-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-supertrend-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-supertrend-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-supertrend-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-supertrend-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-supertrend-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-macd-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-macd-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-macd-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-macd-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-macd-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-macd-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-macd-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-macd-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | g-macd-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-funding-btc-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-funding-btc-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-funding-btc-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-funding-eth-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-funding-eth-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-funding-eth-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-funding-sol-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-funding-sol-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | g-funding-sol-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-weekly-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | g-weekly-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 37 | g-weekly-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-weekly-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | g-weekly-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | g-weekly-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | g-weekly-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | g-weekly-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | g-weekly-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1998 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | n3-negfund-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.8379 | -0.2768 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | n5-weekend-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.8379 | -0.2768 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 46 | n6-ethbtc-z1h-v1 [UNHEDGED_ETH_DIRECTIONAL] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.8379 | -0.2768 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | n7-xsmom72h-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.8379 | -0.2768 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 48 | g-supertrend-sol-p1-v1 [cluster:TREND] | 0 | -0.0865 | — | — | 0.3828 | — | 0.0052 | +0.0005 | +12.1058 | -0.3707 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | g-supertrend-btc-p2-v1 [cluster:TREND] | 0 | -0.1632 | — | — | 0.3447 | — | 0.0068 | -0.0014 | +12.0268 | -0.4497 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 50 | n2-shockrev1h-v1 [cluster:SHOCKREV] | 1 | -0.4808 | 0.0000 | 0.0000 | 0.4916 | -0.4808 | 0.0132 | -0.0003 | +11.3571 | -0.7575 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |

## Spot buy-and-hold controls (16.24 virtual USDC, 1x long, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-hold-usol-v1 (RETIRED_DATA_QUALITY) | 1 | -0.0166 | 0.0000 | 0.0000 | 3.9287 | -0.0166 | 0.0226 | +0.0000 | +11.8246 | -0.3792 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 2 | sp-hold-hype-v1 | 0 | -0.9713 | — | — | 19.4142 | — | 0.0110 | +0.0000 | +5.8639 | -6.3399 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 3 | sp-hold-ueth-v1 | 0 | -1.8948 | — | — | 18.4092 | — | 0.0114 | +0.0000 | +0.1800 | -12.0238 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 4 | sp-hold-ubtc-v1 | 0 | -1.9268 | — | — | 16.5977 | — | 0.0113 | +0.0000 | -0.0168 | -12.2206 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |

## Spot fast / 5m and 15m (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-donchian5m-ubtc-v1 [cluster:TREND] | 3 | +0.0034 | 33.3333 | 1.0310 | 1.8437 | 0.0011 | 0.0670 | +0.0000 | +11.9481 | -0.2557 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-ema15m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.9270 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-donchian5m-ueth-v1 [cluster:TREND] | 8 | -0.0032 | 37.5000 | 0.9944 | 3.3153 | -0.0004 | 0.1812 | +0.0000 | +11.9071 | -0.2967 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-ema15m-ueth-v1 [cluster:TREND] | 1 | -0.0859 | 0.0000 | 0.0000 | 2.5887 | -0.0859 | 0.0225 | +0.0000 | +11.3979 | -0.8059 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | sp-ema15m-hype-v1 [cluster:TREND] | 2 | -0.0934 | 50.0000 | 0.7086 | 4.3306 | -0.0467 | 0.0441 | +0.0000 | +11.3520 | -0.8518 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | sp-donchian5m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 1 | -0.1128 | 0.0000 | 0.0000 | 1.0376 | -0.1128 | 0.0226 | +0.0000 | +11.2324 | -0.9714 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | sp-donchian5m-hype-v1 [cluster:TREND] | 5 | -0.1581 | 20.0000 | 0.7243 | 3.8732 | -0.0316 | 0.1100 | +0.0000 | +10.9534 | -1.2504 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | sp-ema15m-ubtc-v1 [cluster:TREND] | 1 | -0.2340 | 0.0000 | 0.0000 | 2.5504 | -0.1964 | 0.0327 | +0.0000 | +10.3999 | -1.8038 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | sp4-utc21-ubtc-v1 [NON_V1_RESEARCH, cluster:BTC_FRI21] | 1 | -0.3304 | 0.0000 | 0.0000 | 2.1185 | -0.3304 | 0.0225 | +0.0000 | +9.8033 | -2.3114 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |

## Spot slow / 1h (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-rsi1h-ubtc-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.9270 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-rsi1h-ueth-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.9270 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-rsi1h-usol-v1 (RETIRED_DATA_QUALITY) | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.9270 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-rsi1h-hype-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.9270 | -0.2768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | sp4-shockrev1h-ubtc-v1 [NON_V1_RESEARCH, cluster:SHOCKREV] | 1 | -0.3852 | 0.0000 | 0.0000 | 2.4557 | -0.3852 | 0.0224 | +0.0000 | +9.4658 | -2.6489 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |

## Early read (not evidence)

Fast and spot_fast books with at least 10 closed trades, ranked by closed-trade count then net MTM after paid fees/funding (open exit cost not deducted). This is an operational early look so small-capital books can be watched before the 30-trade / DSR / fresh-OOS bar. It is **not** significance, **not** a PASS, and **does not** change the promotion bar. Nothing in this section is a CANDIDATE.

| Rank | Book | Lane | Closed | Net MTM USDC | Win % | Fees | Funding | Gate |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | f1-vwap5m-v1 | fast | 25 | -2.7442 | 44.0000 | 1.4048 | +0.0024 | NOT_SIGNIFICANT |
| 2 | g-vwap-all-p1-v1 | fast | 23 | -2.5372 | 34.7826 | 1.2576 | +0.0016 | NOT_SIGNIFICANT |
| 3 | g-squeeze-btc-p0-v1 | fast | 21 | -2.3808 | 19.0476 | 1.3828 | +0.0009 | NOT_SIGNIFICANT |
| 4 | g-squeeze-sol-p0-v1 | fast | 20 | +0.2045 | 30.0000 | 1.3318 | -0.0017 | NOT_SIGNIFICANT |
| 5 | g-vwap-sol-p1-v1 | fast | 20 | -2.9846 | 40.0000 | 1.0583 | +0.0017 | NOT_SIGNIFICANT |
| 6 | g-vwap-eth-p1-v1 | fast | 19 | +0.5857 | 57.8947 | 1.0069 | +0.0080 | NOT_SIGNIFICANT |
| 7 | g-squeeze-btc-p2-v1 | fast | 19 | -0.9451 | 31.5789 | 1.2538 | -0.0054 | NOT_SIGNIFICANT |
| 8 | g-vwap-btc-p1-v1 | fast | 17 | -1.3426 | 52.9412 | 0.9970 | -0.0043 | NOT_SIGNIFICANT |
| 9 | g-vwap-sol-p0-v1 | fast | 17 | -2.4855 | 35.2941 | 0.8594 | +0.0030 | NOT_SIGNIFICANT |
| 10 | g-squeeze-eth-p0-v1 | fast | 17 | -3.1729 | 23.5294 | 1.1229 | -0.0012 | NOT_SIGNIFICANT |
| 11 | g-squeeze-sol-p2-v1 | fast | 16 | -0.3784 | 37.5000 | 1.0594 | +0.0004 | NOT_SIGNIFICANT |
| 12 | g-squeeze-btc-p1-v1 | fast | 16 | -1.7082 | 18.7500 | 1.0598 | +0.0001 | NOT_SIGNIFICANT |
| 13 | g-vwap-sol-p2-v1 | fast | 16 | -2.3456 | 31.2500 | 0.8380 | +0.0024 | NOT_SIGNIFICANT |
| 14 | g-vwap-eth-p0-v1 | fast | 15 | +1.8881 | 66.6667 | 0.8241 | +0.0077 | NOT_SIGNIFICANT |
| 15 | g-vwap-eth-p2-v1 | fast | 14 | +2.0725 | 64.2857 | 0.6989 | +0.0025 | NOT_SIGNIFICANT |
| 16 | g-squeeze-sol-p1-v1 | fast | 14 | -0.8497 | 21.4286 | 0.9318 | -0.0009 | NOT_SIGNIFICANT |
| 17 | g-vwap-btc-p0-v1 | fast | 13 | -1.6283 | 46.1538 | 0.8095 | -0.0019 | NOT_SIGNIFICANT |
| 18 | g-rsi2-all-p1-v1 | fast | 13 | -2.3856 | 46.1538 | 0.6792 | +0.0003 | NOT_SIGNIFICANT |
| 19 | g-squeeze-eth-p1-v1 | fast | 12 | -1.7706 | 25.0000 | 0.7960 | -0.0019 | NOT_SIGNIFICANT |
| 20 | f5-squeeze1m-v1 | fast | 11 | -2.1846 | 9.0909 | 0.7295 | +0.0016 | NOT_SIGNIFICANT |
| 21 | f3-rsi2-5m-v1 | fast | 10 | -1.4356 | 40.0000 | 0.5752 | +0.0001 | NOT_SIGNIFICANT |
| 22 | g-vwap-btc-p2-v1 | fast | 10 | -2.1120 | 20.0000 | 0.6104 | -0.0014 | NOT_SIGNIFICANT |

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
