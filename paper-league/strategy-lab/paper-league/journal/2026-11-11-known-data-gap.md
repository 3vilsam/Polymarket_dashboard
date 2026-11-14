# Known data gap — 11 Nov 2026 (Asia/Kuala_Lumpur)

This is a known paper-league data gap. Stops during the gap are unverified. Fills were not backfilled.

## Window

- Last successful tick: **58** at **2026-11-11T17:19:23+08:00 Asia/Kuala_Lumpur**
- State cursor `next_minute`: **2026-11-11T17:19:00+08:00 Asia/Kuala_Lumpur**
- After tick 58 the engine fail-closed repeatedly (USOL 1m warmup/continuity, minute-boundary, 60s collection). Last start before the box pause: 18:25:09, fail-closed at **18:26:07 Asia/Kuala_Lumpur** (minute boundary).
- Box pause: about **18:26 to 21:09 Asia/Kuala_Lumpur**.
- After resume the supervisor started the engine at 21:09:05; it fail-closed at **21:10:12 Asia/Kuala_Lumpur** with `ValueError('snapshot collection exceeded 60s; no stale fills')`. A later retry at 21:15:12 fail-closed the same way at **21:16:35 Asia/Kuala_Lumpur**. No tick was committed after 58. No fills were written for the gap.

## Open paper positions at tick 58 (not fills)

Stops on these books cannot be verified for the gap. No gap fills were invented.

- `b0-btc-1x-hold-control-v1` — BTC long hold, no stop
- `g-vwap-btc-p1-v1` — BTC long, stop 73330.7407155
- `g-vwap-all-p1-v1` — BTC long, stop 73330.7407155
- `sp-hold-ubtc-v1`, `sp-hold-ueth-v1`, `sp-hold-usol-v1`, `sp-hold-hype-v1` — 1x spot holds, no stop

## Restart method

Public candle cache was pre-warmed outside the 60-second snapshot window (`warm_cache.py`). The 60s / no-stale-fills rule was not loosened. Frozen v1/v2/v3 implementation files were not modified. Machine record: `data-gaps.jsonl`.

## Resume (do not treat as closing the unverified-stop window)

- First tick after the gap: **59** at **2026-11-11T21:19:32+08:00 Asia/Kuala_Lumpur**. Collection 16.39s (60s rule held). Supervisor PID 305107, engine PID 305128 (`python3 -u league_v3.py`).
- Next tick confirmed: **60** at **2026-11-11T21:20:46+08:00 Asia/Kuala_Lumpur**.
- No fills were backfilled into the gap minutes. On tick 59 the engine flattened `g-vwap-btc-p1-v1` and `g-vwap-all-p1-v1` at the first actually observed mid as `observed_time_exit` (designed unseen-time-exit behaviour, not a historical stop fill). The four spot holds and the BTC perp hold stayed open. Stops during 17:19:23–21:19:32 Asia/Kuala_Lumpur remain unverified.
