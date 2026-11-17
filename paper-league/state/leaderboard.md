# PAPER league — 100 virtual USDC perp books + 16.24 virtual USDC spot books

Updated 2026-11-17T21:45:08+08:00 MYT | tick 1069 | 125 books (107 perp @100 USDC, 18 spot @16.24 USDC; incl. 9 v4 research-sweep books registered 12 Nov 2026) | public reads only

Spot research books use 5m/15m/1h timeframes. Do not compare raw Net MTM USDC across the 100-USDC and 16.24-USDC tables. An 'Early read (not evidence)' table lists fast books with >=10 closed trades; it is not the promotion bar. Ranks use net MTM (open exit cost not deducted). Gate comparisons use same-start indicative exit equity: perp books deduct taker+2bp; spot books deduct official tier-0 spot taker 0.070%+2bp. Official promotion controls remain the BTC-perp hold and random-entry books.

## Controls / luck benchmarks (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | c1-random15m-v1 | 17 | -0.1317 | 41.1765 | 0.9291 | 2.4293 | -0.0112 | 0.6721 | -0.0013 | +12.0095 | +0.0000 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); CONTROL |
| 2 | b0-btc-1x-hold-control-v1 | 0 | -12.1471 | — | — | 16.9854 | — | 0.0450 | -0.1160 | +0.0000 | -12.0095 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); CONTROL; NONTRADABLE risk-exempt |

## Fast / short-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | g-vwap-eth-p2-v1 | 26 | +1.7189 | 57.6923 | 1.3608 | 2.6304 | 0.0661 | 1.4816 | +0.0033 | +13.8875 | +1.8780 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-vwap-eth-p0-v1 | 31 | +1.5069 | 61.2903 | 1.3053 | 2.2871 | 0.0486 | 1.8602 | +0.0084 | +13.6756 | +1.6660 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |
| 3 | g-ema-sol-p1-v1 [cluster:TREND] | 6 | -0.1136 | 33.3333 | 0.9415 | 2.1965 | -0.0189 | 0.2263 | -0.0014 | +12.0551 | +0.0456 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | g-asia-eth-p0-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +12.0394 | +0.0298 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | g-asia-eth-p1-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +12.0394 | +0.0298 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | g-asia-eth-p2-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +12.0394 | +0.0298 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | g-rsi2-btc-p1-v1 | 11 | -0.2832 | 63.6364 | 0.6198 | 0.8211 | -0.0257 | 0.6829 | +0.0000 | +11.8855 | -0.1240 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | g-rsi2-btc-p2-v1 | 4 | -0.2851 | 75.0000 | 0.4166 | 1.1377 | -0.0713 | 0.2053 | +0.0007 | +11.8835 | -0.1260 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | n4-utc21-btc-v1 [cluster:BTC_FRI21] | 2 | -0.4512 | 50.0000 | 0.0673 | 0.5879 | -0.2256 | 0.0408 | -0.0003 | +11.3554 | -0.2921 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | g-vwap-eth-p1-v1 | 34 | -0.5160 | 55.8824 | 0.9269 | 3.5470 | -0.0152 | 1.9368 | +0.0088 | +11.6526 | -0.3569 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |
| 11 | g-rsi2-eth-p2-v1 | 3 | -0.6817 | 33.3333 | 0.2973 | 1.0005 | -0.2272 | 0.1356 | +0.0000 | +11.4870 | -0.5226 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-asia-btc-p0-v1 | 3 | -0.7269 | 0.0000 | 0.0000 | 0.9987 | -0.2423 | 0.1615 | +0.0021 | +11.4417 | -0.5678 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-asia-btc-p2-v1 | 3 | -0.7269 | 0.0000 | 0.0000 | 0.9987 | -0.2423 | 0.1615 | +0.0021 | +11.4417 | -0.5678 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-rsi2-btc-p0-v1 | 8 | -0.7660 | 37.5000 | 0.3106 | 1.0859 | -0.0958 | 0.4656 | +0.0000 | +11.4026 | -0.6069 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-asia-btc-p1-v1 | 4 | -0.8847 | 0.0000 | 0.0000 | 1.1560 | -0.2212 | 0.2103 | +0.0021 | +11.2840 | -0.7256 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-rsi2-sol-p2-v1 | 6 | -0.9213 | 33.3333 | 0.2732 | 1.6143 | -0.1535 | 0.3308 | +0.0003 | +11.2474 | -0.7622 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-ema-eth-p2-v1 [cluster:TREND] | 4 | -0.9506 | 0.0000 | 0.0000 | 1.7076 | -0.2376 | 0.1360 | -0.0029 | +11.2181 | -0.7914 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-rsi2-eth-p0-v1 | 7 | -1.0397 | 28.5714 | 0.2450 | 1.8044 | -0.1485 | 0.3664 | +0.0001 | +11.1289 | -0.8806 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-ema-sol-p2-v1 [cluster:TREND] | 3 | -1.1676 | 0.0000 | 0.0000 | 2.3393 | -0.3892 | 0.0948 | -0.0009 | +11.0011 | -1.0085 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-squeeze-btc-p2-v1 | 32 | -1.2148 | 34.3750 | 0.7979 | 2.3161 | -0.0380 | 2.1114 | -0.0126 | +10.9539 | -1.0556 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |
| 21 | g-asia-sol-p1-v1 | 3 | -1.2183 | 0.0000 | 0.0000 | 1.4176 | -0.4061 | 0.1365 | +0.0005 | +10.9504 | -1.0591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-asia-sol-p2-v1 | 3 | -1.2183 | 0.0000 | 0.0000 | 1.4176 | -0.4061 | 0.1365 | +0.0005 | +10.9504 | -1.0591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-rsi2-eth-p1-v1 | 11 | -1.2395 | 45.4545 | 0.2829 | 1.3470 | -0.1127 | 0.6217 | +0.0000 | +10.9291 | -1.0804 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-asia-all-p1-v1 | 5 | -1.3572 | 0.0000 | 0.0000 | 1.5563 | -0.2714 | 0.2569 | +0.0022 | +10.8114 | -1.1981 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | f2-asia15m-v1 | 5 | -1.3799 | 0.0000 | 0.0000 | 1.5789 | -0.2760 | 0.2454 | +0.0022 | +10.7887 | -1.2208 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-asia-sol-p0-v1 | 4 | -1.3987 | 0.0000 | 0.0000 | 1.5977 | -0.3497 | 0.1738 | +0.0005 | +10.7699 | -1.2396 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-rsi2-sol-p0-v1 | 8 | -1.4787 | 25.0000 | 0.1825 | 2.0957 | -0.1800 | 0.4474 | +0.0003 | +10.6513 | -1.3582 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-ema-eth-p0-v1 [cluster:TREND] | 4 | -1.6133 | 0.0000 | 0.0000 | 2.1753 | -0.4033 | 0.1569 | +0.0002 | +10.5554 | -1.4541 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-ema-btc-p2-v1 [cluster:TREND] | 8 | -1.6837 | 12.5000 | 0.3245 | 2.7630 | -0.2205 | 0.4087 | +0.0024 | +10.4469 | -1.5626 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-ema-sol-p0-v1 [cluster:TREND] | 5 | -1.6848 | 0.0000 | 0.0000 | 2.0281 | -0.3370 | 0.1724 | -0.0009 | +10.4839 | -1.5257 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-vwap-btc-p1-v1 | 28 | -1.7727 | 50.0000 | 0.6429 | 3.0700 | -0.0633 | 1.6816 | -0.0065 | +10.3959 | -1.6136 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-vwap-sol-p0-v1 | 30 | -1.7764 | 43.3333 | 0.6886 | 5.2270 | -0.0592 | 1.5547 | +0.0029 | +10.3923 | -1.6173 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |
| 33 | g-squeeze-sol-p2-v1 | 31 | -1.9970 | 32.2581 | 0.7069 | 3.4264 | -0.0644 | 2.0561 | -0.0023 | +10.1716 | -1.8379 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |
| 34 | g-ema-btc-p0-v1 [cluster:TREND] | 6 | -2.1574 | 0.0000 | 0.0000 | 2.7275 | -0.3495 | 0.3149 | -0.0016 | +9.9732 | -2.0363 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | f5-squeeze1m-v1 | 11 | -2.1846 | 9.0909 | 0.0292 | 2.3893 | -0.1986 | 0.7295 | +0.0016 | +9.9840 | -2.0255 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 36 | g-squeeze-eth-p2-v1 | 9 | -2.3227 | 11.1111 | 0.0598 | 2.4051 | -0.2581 | 0.6001 | -0.0002 | +9.8459 | -2.1636 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 37 | g-vwap-btc-p0-v1 | 25 | -2.3349 | 48.0000 | 0.5334 | 3.1526 | -0.0934 | 1.5592 | -0.0049 | +9.8338 | -2.1758 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-ema-btc-p1-v1 [cluster:TREND] | 8 | -2.3676 | 0.0000 | 0.0000 | 2.3941 | -0.2959 | 0.3846 | +0.0035 | +9.8011 | -2.2084 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | f3-rsi2-5m-v1 | 14 | -2.4158 | 28.5714 | 0.1417 | 2.9980 | -0.1698 | 0.8321 | +0.0001 | +9.7142 | -2.2953 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | g-vwap-all-p1-v1 | 23 | -2.5372 | 34.7826 | 0.5707 | 5.3758 | -0.1103 | 1.2576 | +0.0016 | +9.6314 | -2.3781 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 41 | g-ema-eth-p1-v1 [cluster:TREND] | 9 | -2.5717 | 11.1111 | 0.1603 | 3.3256 | -0.2960 | 0.3883 | -0.0014 | +9.5722 | -2.4373 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | f4-ema15m-v1 [cluster:TREND] | 7 | -2.6362 | 0.0000 | 0.0000 | 3.2041 | -0.3680 | 0.3511 | -0.0021 | +9.4945 | -2.5151 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | g-rsi2-sol-p1-v1 | 15 | -2.6776 | 20.0000 | 0.1362 | 2.7524 | -0.1640 | 0.8197 | +0.0003 | +9.4514 | -2.5581 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | g-squeeze-sol-p1-v1 | 25 | -2.7621 | 16.0000 | 0.5185 | 4.3724 | -0.1105 | 1.6568 | -0.0016 | +9.4065 | -2.6030 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | g-vwap-sol-p2-v1 | 24 | -2.7853 | 33.3333 | 0.5013 | 5.1710 | -0.1161 | 1.2737 | +0.0035 | +9.3833 | -2.6262 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 46 | g-squeeze-eth-p1-v1 | 20 | -2.8842 | 25.0000 | 0.3731 | 3.4777 | -0.1442 | 1.3184 | -0.0027 | +9.2845 | -2.7250 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | g-squeeze-sol-p0-v1 | 36 | -3.0048 | 19.4444 | 0.6252 | 5.2885 | -0.0835 | 2.3901 | -0.0008 | +9.1639 | -2.8457 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN; HALTED |
| 48 | g-squeeze-btc-p1-v1 | 23 | -3.0138 | 13.0435 | 0.3126 | 3.4748 | -0.1310 | 1.5169 | -0.0007 | +9.1548 | -2.8547 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | g-ema-all-p1-v1 [cluster:TREND] | 11 | -3.0203 | 9.0909 | 0.1399 | 3.3094 | -0.2829 | 0.5302 | +0.0022 | +9.1238 | -2.8858 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 50 | g-vwap-btc-p2-v1 | 21 | -3.1480 | 38.0952 | 0.3583 | 3.7288 | -0.1499 | 1.2932 | -0.0045 | +9.0207 | -2.9888 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 51 | g-squeeze-eth-p0-v1 | 17 | -3.1729 | 23.5294 | 0.2410 | 3.3755 | -0.1866 | 1.1229 | -0.0012 | +8.9957 | -3.0138 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 52 | g-rsi2-all-p1-v1 | 23 | -3.1880 | 39.1304 | 0.2367 | 3.2632 | -0.1291 | 1.3043 | +0.0003 | +8.9410 | -3.0685 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 53 | f1-vwap5m-v1 | 48 | -3.3259 | 50.0000 | 0.6532 | 5.6463 | -0.0693 | 2.7901 | +0.0014 | +8.8427 | -3.1668 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |
| 54 | g-squeeze-btc-p0-v1 | 38 | -3.4488 | 21.0526 | 0.4349 | 3.4488 | -0.0908 | 2.4857 | -0.0052 | +8.7198 | -3.2897 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |
| 55 | g-vwap-sol-p1-v1 | 36 | -4.5456 | 41.6667 | 0.4415 | 4.9706 | -0.1263 | 1.9304 | +0.0032 | +7.6231 | -4.3865 | 434 | — | 5 | not flagged | UNPROVEN; UNPROVEN |

## Slow / long-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | l1-supertrend1h-v1 [cluster:TREND] | 1 | +0.3259 | 100.0000 | inf | 1.1588 | 0.3643 | 0.0320 | +0.0029 | +12.4792 | +0.4697 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-supertrend-sol-p0-v1 [cluster:TREND] | 1 | +0.3259 | 100.0000 | inf | 1.1588 | 0.3643 | 0.0320 | +0.0029 | +12.4792 | +0.4697 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | n1-tsmom-mh1h-v1 [cluster:TREND] | 3 | +0.2497 | 66.6667 | 2.9673 | 1.1001 | 0.0832 | 0.0435 | +0.0025 | +12.0563 | +0.4088 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | s1-donchian40-ablation-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | s2-bb40-ema200-ablation-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | r1-trend-rsi-pullback-market-lane-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | l2-macd4h-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | l3-funding1h-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | l4-weekly1d-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | g-supertrend-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | g-supertrend-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-supertrend-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-supertrend-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-supertrend-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-macd-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-macd-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-macd-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-macd-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-macd-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-macd-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-macd-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-macd-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-macd-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-funding-btc-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | g-funding-btc-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-funding-btc-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-funding-eth-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-funding-eth-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-funding-eth-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-funding-sol-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-funding-sol-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-funding-sol-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-weekly-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | g-weekly-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-weekly-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | g-weekly-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 37 | g-weekly-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-weekly-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | g-weekly-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | g-weekly-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | g-weekly-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.1687 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | n3-negfund-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.8066 | +0.1591 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | n5-weekend-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.8066 | +0.1591 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | n6-ethbtc-z1h-v1 [UNHEDGED_ETH_DIRECTIONAL] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.8066 | +0.1591 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | s4-ewmac-riskcap-noadd-ablation-v1 [cluster:TREND] | 0 | -0.0178 | — | — | 0.1711 | — | 0.0047 | +0.0012 | +12.1441 | +0.1346 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 46 | g-supertrend-sol-p1-v1 [cluster:TREND] | 1 | -0.1036 | 0.0000 | 0.0000 | 0.6049 | -0.2468 | 0.0185 | +0.0012 | +12.0531 | +0.0436 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | g-supertrend-btc-p2-v1 [cluster:TREND] | 0 | -0.1579 | — | — | 0.4317 | — | 0.0068 | -0.0067 | +12.0010 | -0.0085 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 48 | n7-xsmom72h-v1 [cluster:TREND] | 0 | -0.3270 | — | — | 0.4770 | — | 0.0055 | -0.0015 | +11.4716 | -0.1759 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | n2-shockrev1h-v1 [cluster:SHOCKREV] | 1 | -0.4808 | 0.0000 | 0.0000 | 0.4916 | -0.4808 | 0.0132 | -0.0003 | +11.3259 | -0.3216 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 50 | g-supertrend-btc-p1-v1 [cluster:TREND] | 1 | -0.4810 | 0.0000 | 0.0000 | 0.6346 | -0.4810 | 0.0245 | +0.0012 | +11.6877 | -0.3218 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |

## Spot buy-and-hold controls (16.24 virtual USDC, 1x long, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-hold-usol-v1 (RETIRED_DATA_QUALITY) | 1 | -0.0166 | 0.0000 | 0.0000 | 3.9287 | -0.0166 | 0.0226 | +0.0000 | +11.7934 | +0.0567 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 2 | sp-hold-hype-v1 | 0 | -0.5250 | — | — | 19.4142 | — | 0.0110 | +0.0000 | +8.5782 | -3.1585 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 3 | sp-hold-ueth-v1 | 0 | -1.8442 | — | — | 18.4092 | — | 0.0114 | +0.0000 | +0.4599 | -11.2768 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 4 | sp-hold-ubtc-v1 | 0 | -1.9246 | — | — | 16.5977 | — | 0.0113 | +0.0000 | -0.0345 | -11.7712 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |

## Spot fast / 5m and 15m (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-ema15m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.8958 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-ema15m-hype-v1 [cluster:TREND] | 2 | -0.0934 | 50.0000 | 0.7086 | 4.3306 | -0.0467 | 0.0441 | +0.0000 | +11.3207 | -0.4159 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-donchian5m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 1 | -0.1128 | 0.0000 | 0.0000 | 1.0376 | -0.1128 | 0.0226 | +0.0000 | +11.2012 | -0.5355 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-donchian5m-ueth-v1 [cluster:TREND] | 9 | -0.1148 | 33.3333 | 0.8332 | 3.9796 | -0.0128 | 0.2038 | +0.0000 | +11.1890 | -0.5477 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 5 | sp-donchian5m-ubtc-v1 [cluster:TREND] | 5 | -0.2299 | 20.0000 | 0.3459 | 3.4939 | -0.0430 | 0.1215 | +0.0000 | +10.3936 | -1.3431 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | sp-ema15m-ueth-v1 [cluster:TREND] | 3 | -0.3207 | 0.0000 | 0.0000 | 3.5351 | -0.1069 | 0.0673 | +0.0000 | +9.9213 | -1.8154 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | sp4-utc21-ubtc-v1 [NON_V1_RESEARCH, cluster:BTC_FRI21] | 1 | -0.3304 | 0.0000 | 0.0000 | 2.1185 | -0.3304 | 0.0225 | +0.0000 | +9.7720 | -1.8755 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |
| 8 | sp-ema15m-ubtc-v1 [cluster:TREND] | 3 | -0.3730 | 0.0000 | 0.0000 | 3.6233 | -0.1194 | 0.0763 | +0.0000 | +9.5129 | -2.2238 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | sp-donchian5m-hype-v1 [cluster:TREND] | 7 | -0.4082 | 14.2857 | 0.5043 | 4.6199 | -0.0583 | 0.1535 | +0.0000 | +9.3821 | -2.3545 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |

## Spot slow / 1h (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-rsi1h-ubtc-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.8958 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-rsi1h-ueth-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.8958 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-rsi1h-usol-v1 (RETIRED_DATA_QUALITY) | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.8958 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-rsi1h-hype-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +11.8958 | +0.1591 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | sp4-shockrev1h-ubtc-v1 [NON_V1_RESEARCH, cluster:SHOCKREV] | 1 | -0.3852 | 0.0000 | 0.0000 | 2.4557 | -0.3852 | 0.0224 | +0.0000 | +9.4345 | -2.2130 | 434 | — | 4 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |

## Early read (not evidence)

Fast and spot_fast books with at least 10 closed trades, ranked by closed-trade count then net MTM after paid fees/funding (open exit cost not deducted). This is an operational early look so small-capital books can be watched before the 30-trade / DSR / fresh-OOS bar. It is **not** significance, **not** a PASS, and **does not** change the promotion bar. Nothing in this section is a CANDIDATE.

| Rank | Book | Lane | Closed | Net MTM USDC | Win % | Fees | Funding | Gate |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | f1-vwap5m-v1 | fast | 48 | -3.3259 | 50.0000 | 2.7901 | +0.0014 | UNPROVEN |
| 2 | g-squeeze-btc-p0-v1 | fast | 38 | -3.4488 | 21.0526 | 2.4857 | -0.0052 | UNPROVEN |
| 3 | g-squeeze-sol-p0-v1 | fast | 36 | -3.0048 | 19.4444 | 2.3901 | -0.0008 | UNPROVEN |
| 4 | g-vwap-sol-p1-v1 | fast | 36 | -4.5456 | 41.6667 | 1.9304 | +0.0032 | UNPROVEN |
| 5 | g-vwap-eth-p1-v1 | fast | 34 | -0.5160 | 55.8824 | 1.9368 | +0.0088 | UNPROVEN |
| 6 | g-squeeze-btc-p2-v1 | fast | 32 | -1.2148 | 34.3750 | 2.1114 | -0.0126 | UNPROVEN |
| 7 | g-vwap-eth-p0-v1 | fast | 31 | +1.5069 | 61.2903 | 1.8602 | +0.0084 | UNPROVEN |
| 8 | g-squeeze-sol-p2-v1 | fast | 31 | -1.9970 | 32.2581 | 2.0561 | -0.0023 | UNPROVEN |
| 9 | g-vwap-sol-p0-v1 | fast | 30 | -1.7764 | 43.3333 | 1.5547 | +0.0029 | UNPROVEN |
| 10 | g-vwap-btc-p1-v1 | fast | 28 | -1.7727 | 50.0000 | 1.6816 | -0.0065 | NOT_SIGNIFICANT |
| 11 | g-vwap-eth-p2-v1 | fast | 26 | +1.7189 | 57.6923 | 1.4816 | +0.0033 | NOT_SIGNIFICANT |
| 12 | g-vwap-btc-p0-v1 | fast | 25 | -2.3349 | 48.0000 | 1.5592 | -0.0049 | NOT_SIGNIFICANT |
| 13 | g-squeeze-sol-p1-v1 | fast | 25 | -2.7621 | 16.0000 | 1.6568 | -0.0016 | NOT_SIGNIFICANT |
| 14 | g-vwap-sol-p2-v1 | fast | 24 | -2.7853 | 33.3333 | 1.2737 | +0.0035 | NOT_SIGNIFICANT |
| 15 | g-vwap-all-p1-v1 | fast | 23 | -2.5372 | 34.7826 | 1.2576 | +0.0016 | NOT_SIGNIFICANT |
| 16 | g-squeeze-btc-p1-v1 | fast | 23 | -3.0138 | 13.0435 | 1.5169 | -0.0007 | NOT_SIGNIFICANT |
| 17 | g-rsi2-all-p1-v1 | fast | 23 | -3.1880 | 39.1304 | 1.3043 | +0.0003 | NOT_SIGNIFICANT |
| 18 | g-vwap-btc-p2-v1 | fast | 21 | -3.1480 | 38.0952 | 1.2932 | -0.0045 | NOT_SIGNIFICANT |
| 19 | g-squeeze-eth-p1-v1 | fast | 20 | -2.8842 | 25.0000 | 1.3184 | -0.0027 | NOT_SIGNIFICANT |
| 20 | g-squeeze-eth-p0-v1 | fast | 17 | -3.1729 | 23.5294 | 1.1229 | -0.0012 | NOT_SIGNIFICANT |
| 21 | g-rsi2-sol-p1-v1 | fast | 15 | -2.6776 | 20.0000 | 0.8197 | +0.0003 | NOT_SIGNIFICANT |
| 22 | f3-rsi2-5m-v1 | fast | 14 | -2.4158 | 28.5714 | 0.8321 | +0.0001 | NOT_SIGNIFICANT |
| 23 | g-rsi2-btc-p1-v1 | fast | 11 | -0.2832 | 63.6364 | 0.6829 | +0.0000 | NOT_SIGNIFICANT |
| 24 | g-rsi2-eth-p1-v1 | fast | 11 | -1.2395 | 45.4545 | 0.6217 | +0.0000 | NOT_SIGNIFICANT |
| 25 | f5-squeeze1m-v1 | fast | 11 | -2.1846 | 9.0909 | 0.7295 | +0.0016 | NOT_SIGNIFICANT |
| 26 | g-ema-all-p1-v1 [cluster:TREND] | fast | 11 | -3.0203 | 9.0909 | 0.5302 | +0.0022 | NOT_SIGNIFICANT |

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
