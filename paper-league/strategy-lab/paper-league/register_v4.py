#!/usr/bin/env python3
"""One-shot append-only v4 research-sweep registration (9 books). Never rewrites a legacy file or running state."""
import json
import league as L
import strategies_v3 as S3
import strategies_v4 as S4
ROOT = L.ROOT
if (ROOT/'registry/extension-v4.json').exists(): raise SystemExit('Refusing frozen v4 extension overwrite')
created = L.utc(L.sc.now_ms())
files = ['league_v4.py', 'strategies_v4.py', 'register_v4.py']
implementation = {p: L.sha(ROOT/p) for p in files}
common = '''## Frozen common rules for the v4 research-sweep extension (registered before its first live tick)
- PAPER only, public Hyperliquid mainnet /info reads only through the unchanged v3 collector (no new request type). No wallet, key, private endpoint, order, signing, testnet or exchange write. Requested by the owner on 12 Nov 2026 ("go online research find more different strategy and run test"). Families are motivated by the cited public sources; parameters are the sources' headline settings or round numbers fixed here, never tuned on league results. No return claim. All variants and losses retained.
- Perp books (n1-n7): 100 virtual USDC each, BTC/ETH/SOL only, frozen risk-limits v1 sizing via the existing league.open_paper: 0.5% cost-inclusive risk per trade (including 24h funding reserve), <=3x notional, one position per book (cluster max 1, inside the 2-position desk cap), mandatory protective stop 0.5%-4.5% else abstain, sticky -2% MYT daily halt, observed-mid entry +2bp adverse, Hyperliquid perp taker fee from the existing config on every fill, hourly settled funding charged/credited, stops replayed on every closed 1m candle (touch = trigger+5bp, gap = bar open+5bp), time exits at first observed quote after the hold cap +2bp.
- Spot books (sp4-*): 16.24 virtual USDC each, UBTC/USDC (@142) spot pair only, long-only 1x all-in cash, official tier-0 spot taker 0.070% every fill (maker never assumed), max(2bp, L2 walk) slippage, 5bp on stops, $10 minimum notional, no funding, same stop replay and -2% sticky halt as the v3 spot books.
- Signals use fully closed 1h UTC bars only; entries only within 90 seconds of the bar close; missed entries are logged, never back-filled. Missing, stale or misaligned data fails the whole tick closed (no partial state).
- Frozen v1/v2/v3 registrations, implementation files and the 116 running books stay byte-identical and execute their own code first each tick; v4 books are evaluated with the same evaluation_v3 code.
- Evaluation: same bar as the league. >=30 closed trades, positive costed return, beats BOTH the BTC-perp hold and random-entry controls after costs, DSR probability >0.95, not halted, then a following non-overlapping fresh-MYT-day/flat-book OOS >=7 days (or >=30 new trades for fast/spot_fast lanes). First OOS endpoint is fixed PASS/FAIL. CANDIDATE_REVIEW_ONLY only: no automatic promotion, message, permission or trade. Known DSR trials = 425 prior + these 9 = 434 at 125 books. Low-frequency books (weekend, xs-momentum, negative-funding, shock-reversal) may never reach 30 trades in a short window; they stay NOT_SIGNIFICANT, which is not a pass.
'''
manifest = dict(version=4, mode='PAPER_ONLY', registered_utc=created,
    original_manifest_sha256=L.sha(ROOT/'registry/manifest.json'),
    extension_v2_sha256=L.sha(ROOT/'registry/extension-v2.json'),
    spot_extension_v3_sha256=L.sha(ROOT/'registry/spot-extension-v3.json'),
    implementation_sha256=implementation, prior_known_trials=425, prior_league_books=116, v4_books=9,
    total_league_books=125, total_known_trials=434, research_memo='/workspace/trading-desk/research/strategy-sweep-2026-11-12.md',
    strategies=[])
for spec in S4.entries():
    id = spec['id']; path = ROOT/'registry'/f'{id}.md'
    body = (f'# {id}\n\nRegistered UTC: {created}\n\n## Frozen specification\n\n```json\n{json.dumps(spec, indent=2, sort_keys=True)}\n```\n\n'
            f'{S4.DESCRIPTIONS[spec["kind"]]}\n\nSources: '+', '.join(spec['sources'])+f'\n\n{common}\n## v4 implementation SHA256\n'
            +''.join(f'- `{n}`: `{d}`\n' for n, d in implementation.items()))
    with path.open('x') as f: f.write(body)
    digest = L.sha(path)
    with path.with_suffix('.sha256').open('x') as f: f.write(f'{digest}  {path.name}\n')
    manifest['strategies'].append(dict(spec, sha256=digest))
with (ROOT/'registry/extension-v4.json').open('x') as f: json.dump(manifest, f, indent=2)
with (ROOT/'registry/extension-v4.sha256').open('x') as f: f.write(L.sha(ROOT/'registry/extension-v4.json')+'  extension-v4.json\n')
L.atomic(ROOT/'v4-registration-receipt.json', manifest)
print(f'Registered {len(manifest["strategies"])} v4 PAPER books, total 125; known trials 434; prior manifests unchanged')
