# Append-only registry note: labels-v2

Recorded UTC: 2026-11-12T06:31:50.918Z. Decided by Skippy (desk coordinator) on 12 Nov 2026 after the VWAP-family ablation (`/workspace/trading-desk/research/ablation/2026-11-12-vwap/README.md`). Frozen rules are not altered mid-run: no rule file is edited and no registered sha256 changes. Sizing, signals, data rules, book status and the engine are unchanged. These books are NOT retired, halted or disabled; they keep running in the paper league. labels-v1 is unchanged.

1. ABLATION_FAIL_2026-11-12: f1-vwap5m-v1, g-vwap-all-p1-v1, g-vwap-btc-p1-v1. Historical stepwise ablation research/ablation/2026-11-12-vwap: no edge survives costs (full frozen book PF < 1 IS and OOS on HL 5m 15.4d and on Binance 5m SUBSTITUTE 101d). Research tag only.
   Rule files and sha256 unchanged:
   - `f1-vwap5m-v1`: `323d5941fd3373584b63b9601a481367b8a087e48de5390d8bd760269a56658c`
   - `g-vwap-all-p1-v1`: `71de8b37311de75f20e0c8b0424a4bd7d695ee2086f6324ff816c7c1a2bb0880`
   - `g-vwap-btc-p1-v1`: `41c829cf4307855fe33990fbd55230a648f0c9a93c87d4bd5d630fd0952140d8`
2. DSR multiplicity: desk total 500 known trials (registry 434 + 66 fresh research trials from that ablation). No league book is added or removed (125 books).
