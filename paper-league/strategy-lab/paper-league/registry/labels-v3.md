# Append-only registry note: labels-v3

Recorded UTC: 2026-11-12T06:42:12.028Z. Decided by Skippy (desk coordinator) on 12 Nov 2026 after the n1/n7 ablation (`/workspace/trading-desk/research/ablation/2026-11-12-trend-n1-n7/README.md`). Frozen rules are not altered mid-run: no rule file is edited and no registered sha256 changes. Sizing, signals, data rules, book status and the engine are unchanged. These books are NOT retired, halted or disabled; they keep running in the paper league. labels-v1 and labels-v2 are unchanged.

1. ABLATION_FAIL_2026-11-12: n1-tsmom-mh1h-v1, n7-xsmom72h-v1. Historical stepwise ablation research/ablation/2026-11-12-trend-n1-n7 (HL 1h, 197 tradable days): no edge after HL costs. n1 full book net PF 0.76 IS / 0.71 OOS (gross 1.03/1.00); n7 1.12 / 0.50 (gross OOS 0.67). Research tag only.
   Rule files and sha256 unchanged (as registered in extension-v4.json):
   - `n1-tsmom-mh1h-v1`: `5d121c7829f05cd80ea05af36eb527a9c6f375c55e15561d52ce5de0f88d5ea5`
   - `n7-xsmom72h-v1`: `5a5d8eccc96b4847af0b16b11bc35307363e90ba7d79b3c56c5ca2be32446b84`
2. The n7 24h-lookback leave-one-out result (OOS PF 1.59) is discovery-only, seen after the holdout was used. No rule change; it is UNTRADEABLE until a new frozen rule set under a new id passes a forward test.
3. DSR multiplicity: desk total 550 known trials (500 + 50 fresh research trials from that ablation). No league book is added or removed.
