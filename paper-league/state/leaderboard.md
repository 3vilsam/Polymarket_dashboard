# PAPER league — 100 virtual USDC perp books + 16.24 virtual USDC spot books

Updated 2026-11-18T05:42:04+08:00 MYT | tick 1160 | 125 books (107 perp @100 USDC, 18 spot @16.24 USDC; incl. 9 v4 research-sweep books registered 12 Nov 2026) | public reads only

Spot research books use 5m/15m/1h timeframes. Do not compare raw Net MTM USDC across the 100-USDC and 16.24-USDC tables. An 'Early read (not evidence)' table lists fast books with >=10 closed trades; it is not the promotion bar. Ranks use net MTM (open exit cost not deducted). Gate comparisons use same-start indicative exit equity: perp books deduct taker+2bp; spot books deduct official tier-0 spot taker 0.070%+2bp. Official promotion controls remain the BTC-perp hold and random-entry books.

## Controls / luck benchmarks (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | c1-random15m-v1 | 18 | -0.2511 | 38.8889 | 0.7872 | 2.8823 | -0.0373 | 0.7098 | -0.0031 | +12.6763 | +0.0000 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); CONTROL |
| 2 | b0-btc-1x-hold-control-v1 | 0 | -12.9336 | — | — | 16.9854 | — | 0.0450 | -0.1240 | +0.0000 | -12.6763 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); CONTROL; NONTRADABLE risk-exempt |

## Fast / short-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | g-vwap-eth-p2-v1 | 28 | +0.7379 | 53.5714 | 1.1284 | 2.9724 | 0.0264 | 1.5782 | +0.0033 | +13.6930 | +1.0167 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | g-vwap-eth-p0-v1 | 34 | +0.2225 | 55.8824 | 1.0635 | 3.2597 | 0.0113 | 2.0534 | +0.0078 | +13.1375 | +0.4612 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |
| 3 | g-asia-eth-p0-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +12.8257 | +0.1495 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | g-asia-eth-p1-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +12.8257 | +0.1495 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | g-asia-eth-p2-v1 | 1 | -0.1293 | 0.0000 | 0.0000 | 0.4686 | -0.1293 | 0.0670 | +0.0002 | +12.8257 | +0.1495 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | g-rsi2-btc-p1-v1 | 11 | -0.2832 | 63.6364 | 0.6198 | 0.8211 | -0.0257 | 0.6829 | +0.0000 | +12.6719 | -0.0044 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | g-rsi2-btc-p2-v1 | 4 | -0.2851 | 75.0000 | 0.4166 | 1.1377 | -0.0713 | 0.2053 | +0.0007 | +12.6699 | -0.0064 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | n4-utc21-btc-v1 [cluster:BTC_FRI21] | 2 | -0.3025 | 50.0000 | 0.0673 | 0.5879 | -0.2256 | 0.0517 | -0.0003 | +12.2779 | -0.0396 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | g-vwap-eth-p1-v1 | 37 | -0.3216 | 56.7568 | 0.9787 | 3.6506 | -0.0043 | 2.1298 | +0.0095 | +12.5936 | -0.0826 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |
| 10 | g-ema-sol-p1-v1 [cluster:TREND] | 7 | -0.3331 | 28.5714 | 0.8459 | 2.4663 | -0.0476 | 0.2498 | -0.0030 | +12.6219 | -0.0543 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | g-rsi2-eth-p2-v1 | 3 | -0.6817 | 33.3333 | 0.2973 | 1.0005 | -0.2272 | 0.1356 | +0.0000 | +12.2734 | -0.4029 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-asia-btc-p0-v1 | 3 | -0.7269 | 0.0000 | 0.0000 | 0.9987 | -0.2423 | 0.1615 | +0.0021 | +12.2281 | -0.4482 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-asia-btc-p2-v1 | 3 | -0.7269 | 0.0000 | 0.0000 | 0.9987 | -0.2423 | 0.1615 | +0.0021 | +12.2281 | -0.4482 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-rsi2-btc-p0-v1 | 8 | -0.7660 | 37.5000 | 0.3106 | 1.0859 | -0.0958 | 0.4656 | +0.0000 | +12.1890 | -0.4873 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-asia-btc-p1-v1 | 4 | -0.8847 | 0.0000 | 0.0000 | 1.1560 | -0.2212 | 0.2103 | +0.0021 | +12.0704 | -0.6059 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-rsi2-sol-p2-v1 | 6 | -0.9213 | 33.3333 | 0.2732 | 1.6143 | -0.1535 | 0.3308 | +0.0003 | +12.0338 | -0.6425 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-ema-sol-p2-v1 [cluster:TREND] | 3 | -0.9492 | 0.0000 | 0.0000 | 2.3393 | -0.3892 | 0.1119 | -0.0009 | +11.9810 | -0.6953 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-rsi2-eth-p0-v1 | 7 | -1.0397 | 28.5714 | 0.2450 | 1.8044 | -0.1485 | 0.3664 | +0.0001 | +11.9153 | -0.7609 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-ema-eth-p2-v1 [cluster:TREND] | 4 | -1.0927 | 0.0000 | 0.0000 | 1.7076 | -0.2376 | 0.1548 | -0.0029 | +11.8353 | -0.8410 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-asia-sol-p1-v1 | 3 | -1.2183 | 0.0000 | 0.0000 | 1.4176 | -0.4061 | 0.1365 | +0.0005 | +11.7368 | -0.9395 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-asia-sol-p2-v1 | 3 | -1.2183 | 0.0000 | 0.0000 | 1.4176 | -0.4061 | 0.1365 | +0.0005 | +11.7368 | -0.9395 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-rsi2-eth-p1-v1 | 11 | -1.2395 | 45.4545 | 0.2829 | 1.3470 | -0.1127 | 0.6217 | +0.0000 | +11.7155 | -0.9608 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-asia-all-p1-v1 | 5 | -1.3572 | 0.0000 | 0.0000 | 1.5563 | -0.2714 | 0.2569 | +0.0022 | +11.5978 | -1.0785 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-rsi2-sol-p0-v1 | 9 | -1.3611 | 33.3333 | 0.2273 | 2.1275 | -0.1512 | 0.4742 | +0.0003 | +11.5939 | -1.0824 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | g-ema-eth-p0-v1 [cluster:TREND] | 4 | -1.3734 | 0.0000 | 0.0000 | 2.2583 | -0.4033 | 0.1767 | +0.0002 | +11.5529 | -1.1233 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | f2-asia15m-v1 | 5 | -1.3799 | 0.0000 | 0.0000 | 1.5789 | -0.2760 | 0.2454 | +0.0022 | +11.5751 | -1.1012 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-asia-sol-p0-v1 | 4 | -1.3987 | 0.0000 | 0.0000 | 1.5977 | -0.3497 | 0.1738 | +0.0005 | +11.5563 | -1.1200 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-ema-sol-p0-v1 [cluster:TREND] | 6 | -1.9279 | 0.0000 | 0.0000 | 2.2885 | -0.3213 | 0.1934 | -0.0022 | +11.0272 | -1.6491 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | f5-squeeze1m-v1 | 11 | -2.1846 | 9.0909 | 0.0292 | 2.3893 | -0.1986 | 0.7295 | +0.0016 | +10.7704 | -1.9059 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 30 | f3-rsi2-5m-v1 | 15 | -2.2982 | 33.3333 | 0.1702 | 3.0298 | -0.1532 | 0.8589 | +0.0001 | +10.6569 | -2.0194 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-squeeze-eth-p2-v1 | 9 | -2.3227 | 11.1111 | 0.0598 | 2.4051 | -0.2581 | 0.6001 | -0.0002 | +10.6323 | -2.0440 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 32 | g-vwap-sol-p2-v1 | 28 | -2.3438 | 39.2857 | 0.6150 | 5.1710 | -0.0833 | 1.4812 | +0.0034 | +10.5763 | -2.0999 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-squeeze-btc-p2-v1 | 36 | -2.4087 | 30.5556 | 0.6657 | 2.5827 | -0.0669 | 2.3745 | -0.0116 | +10.5464 | -2.1299 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |
| 34 | g-ema-btc-p2-v1 [cluster:TREND] | 9 | -2.4258 | 11.1111 | 0.2747 | 3.4072 | -0.2486 | 0.4503 | +0.0028 | +10.5067 | -2.1696 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-squeeze-sol-p2-v1 | 32 | -2.4629 | 31.2500 | 0.6616 | 3.8854 | -0.0770 | 2.1217 | -0.0023 | +10.4922 | -2.1841 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN; HALTED |
| 36 | g-vwap-all-p1-v1 | 23 | -2.5372 | 34.7826 | 0.5707 | 5.3758 | -0.1103 | 1.2576 | +0.0016 | +10.4178 | -2.2585 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 37 | g-rsi2-sol-p1-v1 | 16 | -2.5571 | 18.7500 | 0.1317 | 2.7524 | -0.1598 | 0.8472 | +0.0003 | +10.3979 | -2.2784 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-vwap-btc-p1-v1 | 31 | -2.6460 | 48.3871 | 0.5585 | 3.6289 | -0.0840 | 1.8869 | -0.0065 | +10.2622 | -2.4141 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |
| 39 | g-ema-btc-p0-v1 [cluster:TREND] | 7 | -2.7161 | 0.0000 | 0.0000 | 3.2776 | -0.3669 | 0.3584 | -0.0005 | +10.2139 | -2.4624 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | g-ema-btc-p1-v1 [cluster:TREND] | 9 | -2.8692 | 0.0000 | 0.0000 | 2.8905 | -0.2958 | 0.4441 | +0.0061 | +10.0503 | -2.6260 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | g-squeeze-sol-p0-v1 | 36 | -3.0048 | 19.4444 | 0.6252 | 5.2885 | -0.0835 | 2.3901 | -0.0008 | +9.9502 | -2.7260 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN; HALTED |
| 42 | g-rsi2-all-p1-v1 | 24 | -3.0675 | 37.5000 | 0.2309 | 3.2632 | -0.1278 | 1.3318 | +0.0003 | +9.8875 | -2.7888 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | g-vwap-btc-p0-v1 | 28 | -3.1243 | 46.4286 | 0.4740 | 3.6264 | -0.1116 | 1.7315 | -0.0056 | +9.8308 | -2.8455 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | g-ema-eth-p1-v1 [cluster:TREND] | 10 | -3.1387 | 10.0000 | 0.1395 | 3.7198 | -0.3139 | 0.4052 | -0.0016 | +9.8163 | -2.8599 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | g-squeeze-eth-p0-v1 | 17 | -3.1729 | 23.5294 | 0.2410 | 3.3755 | -0.1866 | 1.1229 | -0.0012 | +9.7821 | -2.8942 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 46 | g-vwap-sol-p0-v1 | 33 | -3.1760 | 39.3939 | 0.5529 | 5.2771 | -0.0962 | 1.6983 | +0.0029 | +9.7790 | -2.8973 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |
| 47 | f4-ema15m-v1 [cluster:TREND] | 8 | -3.1948 | 0.0000 | 0.0000 | 3.7543 | -0.3809 | 0.3945 | -0.0010 | +9.7351 | -2.9412 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 48 | g-squeeze-sol-p1-v1 | 28 | -3.6917 | 14.2857 | 0.4462 | 5.2865 | -0.1318 | 1.8495 | -0.0019 | +9.2634 | -3.4129 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | g-vwap-btc-p2-v1 | 25 | -3.7795 | 40.0000 | 0.3588 | 4.3502 | -0.1495 | 1.5423 | -0.0058 | +9.1291 | -3.5472 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 50 | g-squeeze-eth-p1-v1 | 25 | -4.0557 | 20.0000 | 0.2974 | 4.0557 | -0.1622 | 1.6423 | -0.0020 | +8.8993 | -3.7770 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 51 | g-ema-all-p1-v1 [cluster:TREND] | 13 | -4.0838 | 7.6923 | 0.1154 | 4.2022 | -0.2984 | 0.6062 | +0.0045 | +8.8361 | -3.8402 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 52 | f1-vwap5m-v1 | 50 | -4.2557 | 48.0000 | 0.5954 | 6.1582 | -0.0851 | 2.8789 | +0.0014 | +8.6993 | -3.9769 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN; HALTED |
| 53 | g-squeeze-btc-p0-v1 | 45 | -4.3680 | 22.2222 | 0.4147 | 4.5563 | -0.0971 | 2.9358 | -0.0061 | +8.5871 | -4.0892 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |
| 54 | g-squeeze-btc-p1-v1 | 29 | -4.8337 | 10.3448 | 0.2209 | 5.2860 | -0.1667 | 1.9028 | -0.0006 | +8.1214 | -4.5549 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 55 | g-vwap-sol-p1-v1 | 39 | -5.4489 | 41.0256 | 0.3982 | 5.7875 | -0.1397 | 2.0741 | +0.0022 | +7.5061 | -5.1702 | 434 | — | 6 | not flagged | UNPROVEN; UNPROVEN |

## Slow / long-term (100 virtual USDC perp books)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | n1-tsmom-mh1h-v1 [cluster:TREND] | 3 | +0.1519 | 66.6667 | 2.9673 | 1.1001 | 0.0832 | 0.0516 | +0.0035 | +12.7365 | +0.4189 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | s4-ewmac-riskcap-noadd-ablation-v1 [cluster:TREND] | 0 | +0.0751 | — | — | 0.1935 | — | 0.0047 | +0.0021 | +13.0235 | +0.3472 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | s1-donchian40-ablation-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | s2-bb40-ema200-ablation-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | r1-trend-rsi-pullback-market-lane-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | l2-macd4h-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 7 | l3-funding1h-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | l4-weekly1d-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 9 | g-supertrend-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 10 | g-supertrend-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 11 | g-supertrend-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 12 | g-supertrend-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 13 | g-supertrend-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 14 | g-macd-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 15 | g-macd-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 16 | g-macd-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 17 | g-macd-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 18 | g-macd-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 19 | g-macd-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 20 | g-macd-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 21 | g-macd-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 22 | g-macd-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 23 | g-funding-btc-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 24 | g-funding-btc-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 25 | g-funding-btc-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 26 | g-funding-eth-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 27 | g-funding-eth-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 28 | g-funding-eth-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 29 | g-funding-sol-p0-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 30 | g-funding-sol-p1-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 31 | g-funding-sol-p2-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 32 | g-weekly-btc-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 33 | g-weekly-btc-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 34 | g-weekly-btc-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 35 | g-weekly-eth-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 36 | g-weekly-eth-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 37 | g-weekly-eth-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 38 | g-weekly-sol-p0-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 39 | g-weekly-sol-p1-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 40 | g-weekly-sol-p2-v1 [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.9550 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 41 | n3-negfund-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5963 | +0.2788 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 42 | n5-weekend-btc-v1 [cluster:BTC_FRI21] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5963 | +0.2788 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 43 | n6-ethbtc-z1h-v1 [UNHEDGED_ETH_DIRECTIONAL] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.5963 | +0.2788 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 44 | l1-supertrend1h-v1 [cluster:TREND] | 2 | -0.1293 | 50.0000 | 0.7380 | 1.4419 | -0.0647 | 0.0424 | +0.0026 | +12.8257 | +0.1494 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 45 | g-supertrend-sol-p0-v1 [cluster:TREND] | 2 | -0.1293 | 50.0000 | 0.7380 | 1.4419 | -0.0647 | 0.0424 | +0.0026 | +12.8257 | +0.1494 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 46 | n7-xsmom72h-v1 [cluster:TREND] | 0 | -0.3458 | — | — | 0.4829 | — | 0.0055 | -0.0022 | +12.2423 | -0.0752 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 47 | n2-shockrev1h-v1 [cluster:SHOCKREV] | 1 | -0.4808 | 0.0000 | 0.0000 | 0.4916 | -0.4808 | 0.0132 | -0.0003 | +12.1155 | -0.2020 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 48 | g-supertrend-btc-p2-v1 [cluster:TREND] | 1 | -0.4976 | 0.0000 | 0.0000 | 0.5272 | -0.4976 | 0.0134 | -0.0071 | +12.4575 | -0.2188 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 49 | g-supertrend-sol-p1-v1 [cluster:TREND] | 2 | -0.5277 | 0.0000 | 0.0000 | 0.8297 | -0.2639 | 0.0265 | +0.0014 | +12.4273 | -0.2489 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 50 | g-supertrend-btc-p1-v1 [cluster:TREND] | 1 | -0.6241 | 0.0000 | 0.0000 | 0.8690 | -0.4810 | 0.0363 | +0.0027 | +12.3137 | -0.3625 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |

## Spot buy-and-hold controls (16.24 virtual USDC, 1x long, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-hold-usol-v1 (RETIRED_DATA_QUALITY) | 1 | -0.0166 | 0.0000 | 0.0000 | 3.9287 | -0.0166 | 0.0226 | +0.0000 | +12.5822 | +0.1764 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 2 | sp-hold-hype-v1 | 0 | -0.6490 | — | — | 19.4142 | — | 0.0110 | +0.0000 | +8.6043 | -3.8015 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 3 | sp-hold-ueth-v1 | 0 | -1.9517 | — | — | 18.4092 | — | 0.0114 | +0.0000 | +0.5877 | -11.8182 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |
| 4 | sp-hold-ubtc-v1 | 0 | -2.0520 | — | — | 16.5977 | — | 0.0113 | +0.0000 | -0.0293 | -12.4352 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); CONTROL; SPOT HOLD CONTROL (no stop/halt flatten) |

## Spot fast / 5m and 15m (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-ema15m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.6846 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-donchian5m-usol-v1 (RETIRED_DATA_QUALITY) [cluster:TREND] | 1 | -0.1128 | 0.0000 | 0.0000 | 1.0376 | -0.1128 | 0.0226 | +0.0000 | +11.9900 | -0.4159 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-donchian5m-ueth-v1 [cluster:TREND] | 9 | -0.1148 | 33.3333 | 0.8332 | 3.9796 | -0.0128 | 0.2038 | +0.0000 | +11.9778 | -0.4280 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 4 | sp-ema15m-hype-v1 [cluster:TREND] | 2 | -0.1923 | 50.0000 | 0.7086 | 4.3306 | -0.0467 | 0.0553 | +0.0000 | +11.4129 | -0.9929 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | sp-ema15m-ueth-v1 [cluster:TREND] | 3 | -0.2565 | 0.0000 | 0.0000 | 3.8075 | -0.1069 | 0.0784 | +0.0000 | +11.0170 | -1.3889 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 6 | sp4-utc21-ubtc-v1 [NON_V1_RESEARCH, cluster:BTC_FRI21] | 1 | -0.3304 | 0.0000 | 0.0000 | 2.1185 | -0.3304 | 0.0225 | +0.0000 | +10.5616 | -1.7559 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |
| 7 | sp-donchian5m-ubtc-v1 [cluster:TREND] | 6 | -0.3367 | 16.6667 | 0.2607 | 3.9591 | -0.0538 | 0.1432 | +0.0000 | +10.5259 | -1.8800 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 8 | sp-donchian5m-hype-v1 [cluster:TREND] | 7 | -0.4082 | 14.2857 | 0.5043 | 4.6199 | -0.0583 | 0.1535 | +0.0000 | +10.1710 | -2.2349 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT; HALTED |
| 9 | sp-ema15m-ubtc-v1 [cluster:TREND] | 4 | -0.4852 | 0.0000 | 0.0000 | 4.0650 | -0.1213 | 0.0872 | +0.0000 | +9.6968 | -2.7090 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |

## Spot slow / 1h (16.24 virtual USDC, long-only, no leverage)

| Rank | Book | Closed | Net MTM USDC | Win % | PF | MaxDD % | Expectancy | Fees | Funding | vs BTC pp | vs random pp | DSR trials | DSR probability | Full days | Fresh OOS | Gate |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | sp-rsi1h-ubtc-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.6846 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 2 | sp-rsi1h-ueth-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.6846 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 3 | sp-rsi1h-usol-v1 (RETIRED_DATA_QUALITY) | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.6846 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 4 | sp-rsi1h-hype-v1 | 0 | +0.0000 | — | — | 0.0000 | — | 0.0000 | +0.0000 | +12.6846 | +0.2788 | 434 | — | 6 | not flagged | NOT SIGNIFICANT (<30); NOT_SIGNIFICANT |
| 5 | sp4-shockrev1h-ubtc-v1 [NON_V1_RESEARCH, cluster:SHOCKREV] | 1 | -0.3852 | 0.0000 | 0.0000 | 2.4557 | -0.3852 | 0.0224 | +0.0000 | +10.2241 | -2.0934 | 434 | — | 5 | not flagged | NOT SIGNIFICANT (<30); INELIGIBLE_NON_V1_RESEARCH; HALTED |

## Early read (not evidence)

Fast and spot_fast books with at least 10 closed trades, ranked by closed-trade count then net MTM after paid fees/funding (open exit cost not deducted). This is an operational early look so small-capital books can be watched before the 30-trade / DSR / fresh-OOS bar. It is **not** significance, **not** a PASS, and **does not** change the promotion bar. Nothing in this section is a CANDIDATE.

| Rank | Book | Lane | Closed | Net MTM USDC | Win % | Fees | Funding | Gate |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | f1-vwap5m-v1 | fast | 50 | -4.2557 | 48.0000 | 2.8789 | +0.0014 | UNPROVEN |
| 2 | g-squeeze-btc-p0-v1 | fast | 45 | -4.3680 | 22.2222 | 2.9358 | -0.0061 | UNPROVEN |
| 3 | g-vwap-sol-p1-v1 | fast | 39 | -5.4489 | 41.0256 | 2.0741 | +0.0022 | UNPROVEN |
| 4 | g-vwap-eth-p1-v1 | fast | 37 | -0.3216 | 56.7568 | 2.1298 | +0.0095 | UNPROVEN |
| 5 | g-squeeze-btc-p2-v1 | fast | 36 | -2.4087 | 30.5556 | 2.3745 | -0.0116 | UNPROVEN |
| 6 | g-squeeze-sol-p0-v1 | fast | 36 | -3.0048 | 19.4444 | 2.3901 | -0.0008 | UNPROVEN |
| 7 | g-vwap-eth-p0-v1 | fast | 34 | +0.2225 | 55.8824 | 2.0534 | +0.0078 | UNPROVEN |
| 8 | g-vwap-sol-p0-v1 | fast | 33 | -3.1760 | 39.3939 | 1.6983 | +0.0029 | UNPROVEN |
| 9 | g-squeeze-sol-p2-v1 | fast | 32 | -2.4629 | 31.2500 | 2.1217 | -0.0023 | UNPROVEN |
| 10 | g-vwap-btc-p1-v1 | fast | 31 | -2.6460 | 48.3871 | 1.8869 | -0.0065 | UNPROVEN |
| 11 | g-squeeze-btc-p1-v1 | fast | 29 | -4.8337 | 10.3448 | 1.9028 | -0.0006 | NOT_SIGNIFICANT |
| 12 | g-vwap-eth-p2-v1 | fast | 28 | +0.7379 | 53.5714 | 1.5782 | +0.0033 | NOT_SIGNIFICANT |
| 13 | g-vwap-sol-p2-v1 | fast | 28 | -2.3438 | 39.2857 | 1.4812 | +0.0034 | NOT_SIGNIFICANT |
| 14 | g-vwap-btc-p0-v1 | fast | 28 | -3.1243 | 46.4286 | 1.7315 | -0.0056 | NOT_SIGNIFICANT |
| 15 | g-squeeze-sol-p1-v1 | fast | 28 | -3.6917 | 14.2857 | 1.8495 | -0.0019 | NOT_SIGNIFICANT |
| 16 | g-vwap-btc-p2-v1 | fast | 25 | -3.7795 | 40.0000 | 1.5423 | -0.0058 | NOT_SIGNIFICANT |
| 17 | g-squeeze-eth-p1-v1 | fast | 25 | -4.0557 | 20.0000 | 1.6423 | -0.0020 | NOT_SIGNIFICANT |
| 18 | g-rsi2-all-p1-v1 | fast | 24 | -3.0675 | 37.5000 | 1.3318 | +0.0003 | NOT_SIGNIFICANT |
| 19 | g-vwap-all-p1-v1 | fast | 23 | -2.5372 | 34.7826 | 1.2576 | +0.0016 | NOT_SIGNIFICANT |
| 20 | g-squeeze-eth-p0-v1 | fast | 17 | -3.1729 | 23.5294 | 1.1229 | -0.0012 | NOT_SIGNIFICANT |
| 21 | g-rsi2-sol-p1-v1 | fast | 16 | -2.5571 | 18.7500 | 0.8472 | +0.0003 | NOT_SIGNIFICANT |
| 22 | f3-rsi2-5m-v1 | fast | 15 | -2.2982 | 33.3333 | 0.8589 | +0.0001 | NOT_SIGNIFICANT |
| 23 | g-ema-all-p1-v1 [cluster:TREND] | fast | 13 | -4.0838 | 7.6923 | 0.6062 | +0.0045 | NOT_SIGNIFICANT |
| 24 | g-rsi2-btc-p1-v1 | fast | 11 | -0.2832 | 63.6364 | 0.6829 | +0.0000 | NOT_SIGNIFICANT |
| 25 | g-rsi2-eth-p1-v1 | fast | 11 | -1.2395 | 45.4545 | 0.6217 | +0.0000 | NOT_SIGNIFICANT |
| 26 | f5-squeeze1m-v1 | fast | 11 | -2.1846 | 9.0909 | 0.7295 | +0.0016 | NOT_SIGNIFICANT |
| 27 | g-ema-eth-p1-v1 [cluster:TREND] | fast | 10 | -3.1387 | 10.0000 | 0.4052 | -0.0016 | NOT_SIGNIFICANT |

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
