#!/usr/bin/env python3
"""One-shot append-only retirement note for the USOL/USDC spot books. Original book rules stay byte-identical."""
import json
import league as L
ROOT = L.ROOT
if (ROOT/'registry/retirement-usol-v1.json').exists(): raise SystemExit('Refusing retirement overwrite')
created = L.utc(L.sc.now_ms())
books = ['sp-hold-usol-v1', 'sp-ema15m-usol-v1', 'sp-rsi1h-usol-v1', 'sp-donchian5m-usol-v1']
spot = L.read_json(ROOT/'registry/spot-extension-v3.json'); by_id = {s['id']: s['sha256'] for s in spot['strategies']}
impl = {p: L.sha(ROOT/p) for p in ['league_v6.py', 'register_retirement_usol_v1.py']}
reason = ('USOL/USDC spot pair too thin: Hyperliquid omits 1m candles for no-trade minutes, so the frozen 512-bar continuity '
          'check fails for hours at a time, and real fills on a pair this thin would also be poor.')
note = f'''# Append-only note: USOL/USDC spot books RETIRED_DATA_QUALITY

Recorded UTC: {created}. Decided by Skippy (desk coordinator) on 12 Nov 2026. Data-quality retirement, not a risk-limit change.

Books: {', '.join(books)}. Their original frozen rule files and sha256 are unchanged:
''' + ''.join(f'- `{b}`: `{by_id[b]}`\n' for b in books) + f'''
Reason: {reason}

Effect (from the first engine tick after this note; not retroactive):
1. Status RETIRED_DATA_QUALITY. The books stop ticking: no new signals, entries, exits or stop checks.
2. All history (events, ledgers, closed trades, evaluation) is preserved, and the books stay in the league state and in the DSR trial count (125 books, 434 known trials).
3. Any open virtual position is closed once at the last valid observed USOL/USDC mid from the last successful engine tick (minus 2bp, plus the 0.070% spot taker fee), reason `retired_data_quality_close_at_last_valid_mark`. If that mark is older than 5 minutes or the book was skipped by data-isolation v1, the position is marked UNRESOLVED instead; no price is invented.
4. USOL is removed from the engine and warm-up data checks. SOL perp books (BTC/ETH/SOL perps) are unaffected.
5. Reinstating USOL needs a new, separately registered decision with new book ids.
'''
path = ROOT/'registry/retirement-usol-v1.md'
with path.open('x') as f: f.write(note)
digest = L.sha(path)
with path.with_suffix('.sha256').open('x') as f: f.write(f'{digest}  {path.name}\n')
m = dict(status='RETIRED_DATA_QUALITY', mode='PAPER_ONLY', recorded_utc=created, symbols=['USOL'], books={b: by_id[b] for b in books},
         reason=reason, note_sha256=digest, data_isolation_v1_sha256=L.sha(ROOT/'registry/data-isolation-v1.json'),
         implementation_sha256=impl, total_league_books=125, total_known_trials=434, history_preserved=True)
with (ROOT/'registry/retirement-usol-v1.json').open('x') as f: json.dump(m, f, indent=2)
with (ROOT/'registry/retirement-usol-v1.json.sha256').open('x') as f: f.write(L.sha(ROOT/'registry/retirement-usol-v1.json')+'  retirement-usol-v1.json\n')
print('Registered retirement-usol-v1', digest)
