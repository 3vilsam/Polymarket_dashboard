# PAPER league — 100 virtual USDC perp books + 16.24 virtual USDC spot books

Updated 2026-11-16T07:52:03+08:00 MYT | tick 729 | 125 books (107 perp @100 USDC, 18 spot @16.24 USDC; incl. 9 v4 research-sweep books registered 12 Nov 2026) | public reads only

Spot research books use 5m/15m/1h timeframes. Do not compare raw Net MTM USDC across the 100-USDC and 16.24-USDC tables. An 'Early read (not evidence)' table lists fast books with >=10 closed trades; it is not the promotion bar. Ranks use net MTM (open exit cost not deducted). Gate comparisons use same-start indicative exit equity: perp books deduct taker+2bp; spot books deduct official tier-0 spot taker 0.070%+2bp. Official promotion controls remain the BTC-perp hold and random-entry books.

## Controls / luck benchmarks (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | c1-random15m-v1 | 8 | +0.8979 | 37.5000 | 1.3031 | 1.8864 | 0.0582 | 0.3274 | -0.0008 | +12.6415 | +0.0000 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); CONTROL |
| 2 | b0-btc-1x-hold-control-v1 | 0 | -11.7498 | — | — | 16.9854 | — | 0.0450 | -0.0871 | +0.0000 | -12.6415 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); CONTROL; NONTRADABLE risk-exempt |

## Fast / short-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | g-vwap-eth-p2-v1 | 15 | +2.6965 | 66.6667 | 2.1020 | 2.6304 | 0.1798 | 0.7671 | +0.0025 | +14.4680 | +1.8265 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-vwap-eth-p0-v1 | 16 | +2.5710 | 68.7500 | 2.2366 | 2.2871 | 0.1569 | 0.9183 | +0.0077 | +14.3047 | +1.6632 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | g-vwap-eth-p1-v1 | 22 | +1.4877 | 63.6364 | 1.3822 | 3.4650 | 0.0676 | 1.1691 | +0.0080 | +13.2592 | +0.6177 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | g-ema-sol-p1-v1 [cluster:TREND] | 3 | +1.3512 | 66.6667 | 3.8273 | 0.9790 | 0.4504 | 0.1183 | +0.0018 | +13.1227 | +0.4812 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | g-ema-sol-p0-v1 [cluster:TREND] | 1 | +0.0313 | 0.0000 | 0.0000 | 0.8629 | -0.3276 | 0.0401 | -0.0004 | +11.7782 | -0.8632 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | g-asia-btc-p0-v1 | 1 | -0.0076 | 0.0000 | 0.0000 | 0.2813 | -0.0076 | 0.0668 | +0.0021 | +11.7639 | -0.8776 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | g-asia-btc-p1-v1 | 1 | -0.0076 | 0.0000 | 0.0000 | 0.2813 | -0.0076 | 0.0668 | +0.0021 | +11.7639 | -0.8776 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | g-asia-btc-p2-v1 | 1 | -0.0076 | 0.0000 | 0.0000 | 0.2813 | -0.0076 | 0.0668 | +0.0021 | +11.7639 | -0.8776 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | g-ema-btc-p2-v1 [cluster:TREND] | 3 | -0.0514 | 33.3333 | 0.8758 | 1.3431 | -0.0401 | 0.1567 | -0.0013 | +11.6837 | -0.9578 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | g-asia-eth-p0-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +11.6422 | -0.9993 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | g-asia-eth-p1-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +11.6422 | -0.9993 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-asia-eth-p2-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +11.6422 | -0.9993 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-ema-eth-p2-v1 [cluster:TREND] | 1 | -0.1503 | 0.0000 | 0.0000 | 0.9322 | -0.1503 | 0.0324 | -0.0000 | +11.6212 | -1.0203 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-ema-eth-p0-v1 [cluster:TREND] | 1 | -0.1704 | 0.0000 | 0.0000 | 0.9322 | -0.1704 | 0.0324 | -0.0003 | +11.6011 | -1.0404 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-rsi2-eth-p2-v1 | 2 | -0.2057 | 50.0000 | 0.5837 | 0.5261 | -0.1028 | 0.0688 | +0.0000 | +11.5658 | -1.0757 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-rsi2-btc-p2-v1 | 3 | -0.3078 | 66.6667 | 0.3702 | 1.0646 | -0.1026 | 0.1389 | +0.0007 | +11.4637 | -1.1778 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | f4-ema15m-v1 [cluster:TREND] | 1 | -0.3314 | 0.0000 | 0.0000 | 1.1290 | -0.4883 | 0.0599 | -0.0045 | +11.4032 | -1.2383 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-ema-btc-p0-v1 [cluster:TREND] | 1 | -0.3314 | 0.0000 | 0.0000 | 1.1290 | -0.4883 | 0.0599 | -0.0045 | +11.4032 | -1.2383 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-rsi2-btc-p1-v1 | 9 | -0.3424 | 66.6667 | 0.5331 | 0.8211 | -0.0380 | 0.5501 | +0.0000 | +11.4291 | -1.2124 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-squeeze-sol-p0-v1 | 22 | -0.3546 | 27.2727 | 0.9217 | 3.1837 | -0.0161 | 1.4653 | -0.0017 | +11.4169 | -1.2246 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-squeeze-sol-p2-v1 | 16 | -0.3784 | 37.5000 | 0.8791 | 2.5033 | -0.0237 | 1.0594 | +0.0004 | +11.3931 | -1.2484 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-rsi2-sol-p2-v1 | 4 | -0.3841 | 50.0000 | 0.4742 | 1.0809 | -0.0960 | 0.1989 | +0.0003 | +11.3874 | -1.2541 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | n4-utc21-btc-v1 [cluster:BTC_FRI21] | 2 | -0.4512 | 50.0000 | 0.0673 | 0.5879 | -0.2256 | 0.0408 | -0.0003 | +10.9566 | -1.3212 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-ema-sol-p2-v1 [cluster:TREND] | 2 | -0.4847 | 0.0000 | 0.0000 | 2.1116 | -0.4183 | 0.0784 | -0.0011 | +11.2627 | -1.3788 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | f2-asia15m-v1 | 2 | -0.4854 | 0.0000 | 0.0000 | 0.8244 | -0.2427 | 0.1140 | +0.0022 | +11.2861 | -1.3554 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-asia-all-p1-v1 | 2 | -0.4854 | 0.0000 | 0.0000 | 0.8244 | -0.2427 | 0.1140 | +0.0022 | +11.2861 | -1.3554 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-ema-eth-p1-v1 [cluster:TREND] | 4 | -0.4994 | 25.0000 | 0.5046 | 1.1450 | -0.1249 | 0.1642 | +0.0001 | +11.2720 | -1.3694 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-rsi2-eth-p0-v1 | 6 | -0.5659 | 33.3333 | 0.3736 | 1.4383 | -0.0943 | 0.2999 | +0.0001 | +11.2056 | -1.4359 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-rsi2-btc-p0-v1 | 7 | -0.7135 | 42.8571 | 0.3260 | 1.0859 | -0.1019 | 0.3992 | +0.0000 | +11.0580 | -1.5835 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-rsi2-eth-p1-v1 | 10 | -0.7659 | 50.0000 | 0.3897 | 1.0885 | -0.0766 | 0.5552 | +0.0000 | +11.0056 | -1.6359 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-asia-sol-p0-v1 | 2 | -0.8276 | 0.0000 | 0.0000 | 1.0277 | -0.4138 | 0.1038 | +0.0005 | +10.9439 | -1.6976 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-asia-sol-p1-v1 | 2 | -0.8276 | 0.0000 | 0.0000 | 1.0277 | -0.4138 | 0.1038 | +0.0005 | +10.9439 | -1.6976 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-asia-sol-p2-v1 | 2 | -0.8276 | 0.0000 | 0.0000 | 1.0277 | -0.4138 | 0.1038 | +0.0005 | +10.9439 | -1.6976 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | g-rsi2-sol-p0-v1 | 6 | -0.9101 | 33.3333 | 0.2610 | 1.6721 | -0.1517 | 0.2901 | +0.0003 | +10.8614 | -1.7801 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-vwap-btc-p1-v1 | 20 | -0.9200 | 55.0000 | 0.7366 | 3.0700 | -0.0460 | 1.1618 | -0.0043 | +10.8515 | -1.7900 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | g-ema-all-p1-v1 [cluster:TREND] | 5 | -1.1459 | 20.0000 | 0.3064 | 1.3432 | -0.2292 | 0.2352 | -0.0020 | +10.6256 | -2.0159 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 37 | g-squeeze-sol-p1-v1 | 15 | -1.1463 | 20.0000 | 0.6519 | 2.9026 | -0.0764 | 0.9984 | -0.0009 | +10.6252 | -2.0163 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-ema-btc-p1-v1 [cluster:TREND] | 3 | -1.1740 | 0.0000 | 0.0000 | 1.2480 | -0.3913 | 0.1407 | -0.0016 | +10.5975 | -2.0440 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | g-squeeze-btc-p2-v1 | 20 | -1.1942 | 30.0000 | 0.7481 | 2.3161 | -0.0597 | 1.3200 | -0.0063 | +10.5773 | -2.0642 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | f3-rsi2-5m-v1 | 11 | -1.3903 | 36.3636 | 0.2202 | 2.2184 | -0.1264 | 0.6083 | +0.0001 | +10.3812 | -2.2603 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | g-vwap-btc-p0-v1 | 15 | -1.5884 | 53.3333 | 0.4549 | 2.8246 | -0.1103 | 0.9398 | -0.0019 | +10.1377 | -2.5038 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | g-squeeze-btc-p1-v1 | 16 | -1.7082 | 18.7500 | 0.4451 | 2.1754 | -0.1068 | 1.0598 | +0.0001 | +10.0632 | -2.5782 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | g-squeeze-eth-p1-v1 | 12 | -1.7706 | 25.0000 | 0.3491 | 2.1065 | -0.1476 | 0.7960 | -0.0019 | +10.0009 | -2.6406 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | g-vwap-btc-p2-v1 | 12 | -2.0229 | 33.3333 | 0.3125 | 2.9146 | -0.1686 | 0.7083 | -0.0014 | +9.7486 | -2.8929 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | g-rsi2-sol-p1-v1 | 10 | -2.1310 | 20.0000 | 0.0713 | 2.2755 | -0.2131 | 0.4879 | +0.0003 | +9.6405 | -3.0010 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 46 | f1-vwap5m-v1 | 27 | -2.1819 | 48.1481 | 0.6172 | 5.6463 | -0.0832 | 1.5333 | +0.0024 | +9.5446 | -3.0969 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | f5-squeeze1m-v1 | 11 | -2.1846 | 9.0909 | 0.0292 | 2.3893 | -0.1986 | 0.7295 | +0.0016 | +9.5868 | -3.0546 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 48 | g-rsi2-all-p1-v1 | 15 | -2.2321 | 46.6667 | 0.2194 | 2.4464 | -0.1488 | 0.7776 | +0.0003 | +9.5394 | -3.1021 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | g-squeeze-eth-p2-v1 | 9 | -2.3227 | 11.1111 | 0.0598 | 2.4051 | -0.2581 | 0.6001 | -0.0002 | +9.4488 | -3.1927 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 50 | g-vwap-all-p1-v1 | 23 | -2.5372 | 34.7826 | 0.5707 | 5.3758 | -0.1103 | 1.2576 | +0.0016 | +9.2343 | -3.4072 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 51 | g-vwap-sol-p2-v1 | 17 | -2.5568 | 35.2941 | 0.4233 | 4.6910 | -0.1504 | 0.8694 | +0.0024 | +9.2147 | -3.4268 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 52 | g-squeeze-btc-p0-v1 | 22 | -2.6255 | 18.1818 | 0.3559 | 2.6435 | -0.1193 | 1.4478 | -0.0000 | +9.1460 | -3.4955 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 53 | g-vwap-sol-p0-v1 | 18 | -2.7337 | 38.8889 | 0.3881 | 5.2270 | -0.1498 | 0.9139 | +0.0030 | +9.0042 | -3.6373 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 54 | g-squeeze-eth-p0-v1 | 17 | -3.1729 | 23.5294 | 0.2410 | 3.3755 | -0.1866 | 1.1229 | -0.0012 | +8.5986 | -4.0429 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 55 | g-vwap-sol-p1-v1 | 23 | -3.4172 | 43.4783 | 0.3588 | 4.1948 | -0.1486 | 1.2088 | +0.0022 | +8.3543 | -4.2872 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |

## Slow / long-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | l1-supertrend1h-v1 [cluster:TREND] | 1 | +0.3643 | 100.0000 | inf | 1.1588 | 0.3643 | 0.0214 | +0.0031 | +12.1357 | -0.5057 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-supertrend-sol-p0-v1 [cluster:TREND] | 1 | +0.3643 | 100.0000 | inf | 1.1588 | 0.3643 | 0.0214 | +0.0031 | +12.1357 | -0.5057 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | n1-tsmom-mh1h-v1 [cluster:TREND] | 1 | +0.3606 | 100.0000 | inf | 0.8811 | 0.3606 | 0.0163 | +0.0022 | +11.7684 | -0.5094 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | g-supertrend-sol-p1-v1 [cluster:TREND] | 0 | +0.0745 | — | — | 0.3828 | — | 0.0052 | +0.0004 | +11.8384 | -0.8031 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | s1-donchian40-ablation-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | s2-bb40-ema200-ablation-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | s4-ewmac-riskcap-noadd-ablation-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | r1-trend-rsi-pullback-market-lane-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | l2-macd4h-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | l3-funding1h-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | l4-weekly1d-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-supertrend-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-supertrend-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-supertrend-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-supertrend-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-supertrend-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-supertrend-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-macd-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-macd-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-macd-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-macd-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-macd-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-macd-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-macd-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | g-macd-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-macd-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-funding-btc-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-funding-btc-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-funding-btc-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-funding-eth-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-funding-eth-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-funding-eth-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-funding-sol-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | g-funding-sol-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-funding-sol-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | g-weekly-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 37 | g-weekly-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-weekly-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | g-weekly-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | g-weekly-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | g-weekly-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | g-weekly-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | g-weekly-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | g-weekly-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.7715 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | n3-negfund-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.4078 | -0.8700 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 46 | n5-weekend-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.4078 | -0.8700 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | n6-ethbtc-z1h-v1 [UNHEDGED_ETH_DIRECTIONAL] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.4078 | -0.8700 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 48 | n7-xsmom72h-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.4078 | -0.8700 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | g-supertrend-btc-p2-v1 [cluster:TREND] | 0 | -0.0905 | — | — | 0.3447 | — | 0.0068 | -0.0018 | +11.6713 | -0.9702 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 50 | n2-shockrev1h-v1 [cluster:SHOCKREV] | 1 | -0.4808 | 0.0000 | 0.0000 | 0.4916 | -0.4808 | 0.0132 | -0.0003 | +10.9271 | -1.3508 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |

## Spot buy-and-hold controls (16.24 virtual USDC, 1x long, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-hold-usol-v1 (RETIRED_DATA_QUALITY) | 1 | -0.0166 | 0.0000 | 0.0000 | 3.9287 | -0.0166 | 0.0226 | +0.0000 | +11.3950 | -0.9724 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 2 | sp-hold-hype-v1 | 0 | -0.8193 | — | — | 19.4142 | — | 0.0110 | +0.0000 | +6.3695 | -5.9979 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 3 | sp-hold-ueth-v1 | 0 | -1.7534 | — | — | 18.4092 | — | 0.0114 | +0.0000 | +0.6204 | -11.7470 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 4 | sp-hold-ubtc-v1 | 0 | -1.8562 | — | — | 16.5977 | — | 0.0113 | +0.0000 | -0.0120 | -12.3793 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |

## Spot fast / 5m and 15m (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-ema15m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.4974 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-ema15m-ueth-v1 [cluster:TREND] | 1 | -0.0859 | 0.0000 | 0.0000 | 2.5887 | -0.0859 | 0.0225 | +0.0000 | +10.9683 | -1.3991 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-ema15m-hype-v1 [cluster:TREND] | 2 | -0.0934 | 50.0000 | 0.7086 | 4.3306 | -0.0467 | 0.0441 | +0.0000 | +10.9223 | -1.4451 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-donchian5m-ubtc-v1 [cluster:TREND] | 4 | -0.1048 | 25.0000 | 0.5204 | 2.4980 | -0.0262 | 0.0890 | +0.0000 | +10.8518 | -1.5156 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | sp-donchian5m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 1 | -0.1128 | 0.0000 | 0.0000 | 1.0376 | -0.1128 | 0.0226 | +0.0000 | +10.8028 | -1.5646 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | sp-donchian5m-ueth-v1 [cluster:TREND] | 9 | -0.1148 | 33.3333 | 0.8332 | 3.9796 | -0.0128 | 0.2038 | +0.0000 | +10.7906 | -1.5768 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 7 | sp-ema15m-ubtc-v1 [cluster:TREND] | 1 | -0.1569 | 0.0000 | 0.0000 | 2.6790 | -0.1964 | 0.0327 | +0.0000 | +10.4443 | -1.9231 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | sp-donchian5m-hype-v1 [cluster:TREND] | 6 | -0.2665 | 16.6667 | 0.6092 | 3.8732 | -0.0444 | 0.1320 | +0.0000 | +9.8565 | -2.5109 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | sp4-utc21-ubtc-v1 [NON_V1_RESEARCH, cluster:BTC_FRI21] | 1 | -0.3304 | 0.0000 | 0.0000 | 2.1185 | -0.3304 | 0.0225 | +0.0000 | +9.3732 | -2.9046 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |

## Spot slow / 1h (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-rsi1h-ubtc-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.4974 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-rsi1h-ueth-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.4974 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-rsi1h-usol-v1 (RETIRED_DATA_QUALITY) | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.4974 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-rsi1h-hype-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.4974 | -0.8700 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | sp4-shockrev1h-ubtc-v1 [NON_V1_RESEARCH, cluster:SHOCKREV] | 1 | -0.3852 | 0.0000 | 0.0000 | 2.4557 | -0.3852 | 0.0224 | +0.0000 | +9.0357 | -3.2421 | 434 | — | 3 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |

## Early read (not evidence)

Fast and spot_fast books with at least 10 closed trades, ranked by closed-trade count then net MTM after paid fees/funding (open exit cost not deducted). This is an operational early look so small-capital books can be watched before the 30-trade / DSR / fresh-OOS bar. It is **not** significance, **not** a PASS, and **does not** change the promotion bar. Nothing in this section is a CANDIDATE.

| Rank | Book | Lane | Closed | Net MTM USDC | Win % | Fees | Funding | Gate |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | f1-vwap5m-v1 | fast | 27 | -2.1819 | 48.1481 | 1.5333 | +0.0024 | NOT_SIGNIFICANT |
| 2 | g-vwap-all-p1-v1 | fast | 23 | -2.5372 | 34.7826 | 1.2576 | +0.0016 | NOT_SIGNIFICANT |
| 3 | g-vwap-sol-p1-v1 | fast | 23 | -3.4172 | 43.4783 | 1.2088 | +0.0022 | NOT_SIGNIFICANT |
| 4 | g-vwap-eth-p1-v1 | fast | 22 | +1.4877 | 63.6364 | 1.1691 | +0.0080 | NOT_SIGNIFICANT |
| 5 | g-squeeze-sol-p0-v1 | fast | 22 | -0.3546 | 27.2727 | 1.4653 | -0.0017 | NOT_SIGNIFICANT |
| 6 | g-squeeze-btc-p0-v1 | fast | 22 | -2.6255 | 18.1818 | 1.4478 | -0.0000 | NOT_SIGNIFICANT |
| 7 | g-vwap-btc-p1-v1 | fast | 20 | -0.9200 | 55.0000 | 1.1618 | -0.0043 | NOT_SIGNIFICANT |
| 8 | g-squeeze-btc-p2-v1 | fast | 20 | -1.1942 | 30.0000 | 1.3200 | -0.0063 | NOT_SIGNIFICANT |
| 9 | g-vwap-sol-p0-v1 | fast | 18 | -2.7337 | 38.8889 | 0.9139 | +0.0030 | NOT_SIGNIFICANT |
| 10 | g-vwap-sol-p2-v1 | fast | 17 | -2.5568 | 35.2941 | 0.8694 | +0.0024 | NOT_SIGNIFICANT |
| 11 | g-squeeze-eth-p0-v1 | fast | 17 | -3.1729 | 23.5294 | 1.1229 | -0.0012 | NOT_SIGNIFICANT |
| 12 | g-vwap-eth-p0-v1 | fast | 16 | +2.5710 | 68.7500 | 0.9183 | +0.0077 | NOT_SIGNIFICANT |
| 13 | g-squeeze-sol-p2-v1 | fast | 16 | -0.3784 | 37.5000 | 1.0594 | +0.0004 | NOT_SIGNIFICANT |
| 14 | g-squeeze-btc-p1-v1 | fast | 16 | -1.7082 | 18.7500 | 1.0598 | +0.0001 | NOT_SIGNIFICANT |
| 15 | g-vwap-eth-p2-v1 | fast | 15 | +2.6965 | 66.6667 | 0.7671 | +0.0025 | NOT_SIGNIFICANT |
| 16 | g-squeeze-sol-p1-v1 | fast | 15 | -1.1463 | 20.0000 | 0.9984 | -0.0009 | NOT_SIGNIFICANT |
| 17 | g-vwap-btc-p0-v1 | fast | 15 | -1.5884 | 53.3333 | 0.9398 | -0.0019 | NOT_SIGNIFICANT |
| 18 | g-rsi2-all-p1-v1 | fast | 15 | -2.2321 | 46.6667 | 0.7776 | +0.0003 | NOT_SIGNIFICANT |
| 19 | g-squeeze-eth-p1-v1 | fast | 12 | -1.7706 | 25.0000 | 0.7960 | -0.0019 | NOT_SIGNIFICANT |
| 20 | g-vwap-btc-p2-v1 | fast | 12 | -2.0229 | 33.3333 | 0.7083 | -0.0014 | NOT_SIGNIFICANT |
| 21 | f3-rsi2-5m-v1 | fast | 11 | -1.3903 | 36.3636 | 0.6083 | +0.0001 | NOT_SIGNIFICANT |
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
