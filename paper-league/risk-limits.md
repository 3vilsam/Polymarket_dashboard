# risk-limits v1 (stand-in)

The frozen manifest hashes `risk-limits.md` at this path (`sha256 bc8c5b8637374ff5b54fb45d6bb732ce88a726c35866b6c1d2aa7bfa64ce18f0`). That file was not in the league export, and the engine only hashes it; it does not parse it. These are the v1 numbers the 12–13 Nov risk reviews applied to the same books. They are not a new rule set.

- 0.5% of equity per trade, including entry and exit costs
- 2% open risk per book
- 3x notional cap
- mandatory stop, 0.5% to 4.5%, else no entry
- sticky −2% MYT daily halt until an owner reset
- −10% drawdown is a review flag, not an automatic flatten
- no exchange orders, no API keys, paper books only

Drop the original file in place of this one. When its SHA-256 matches the manifest, the scheduler stops substituting the pinned digest.
