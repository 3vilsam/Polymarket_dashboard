#!/usr/bin/env python3
"""One-shot append-only SPOT extension. Never rewrites a legacy file or running state."""
from pathlib import Path
import json
import league as L
import strategies_v3 as S
ROOT=L.ROOT
if (ROOT/'registry/spot-extension-v3.json').exists(): raise SystemExit('Refusing frozen spot extension overwrite')
created=L.utc(L.sc.now_ms())
files=['league_v3.py','strategies_v3.py','evaluation_v3.py','register_v3.py']
implementation={p:L.sha(ROOT/p) for p in files}
common='''## Frozen common rules for this prospective SPOT extension
- PAPER only, public Hyperliquid mainnet /info reads only, no wallet/private endpoint/key/order/signing/testnet/exchange writes. Desk-defined spot experiments at the owner's 11 Nov 2026 request, not independently supplied or proven bot strategies. No optimized parameter choice or return claim. All variants and losses retained.
- Each spot book starts with 16.24 virtual USDC independently at its first live v3 tick (the owner's stated live cash, not the 100 USDC perp-book capital). Long-only, 1x, no leverage, no shorting, no liquidation. Sizing is all-in free cash rounded down to the base token szDecimals, never rounded up to the $10 minimum. One position per book. Mandatory protective stop on research books = max(0.5%, 2*arithmetic ATR14/close); abstain from entry if stop >4.5%. Buy-and-hold controls have no stop and no daily-halt flatten.
- Universe: live USDC spot pairs UBTC/USDC (@142), UETH/USDC (@151), USOL/USDC (@156), HYPE/USDC (@107), verified from public spotMeta / spotMetaAndAssetCtxs / allMids / l2Book on 11 Nov 2026. Price source for all four is the spot pair itself, not a perp-mid proxy. A missing mid, identity change, or failed 1m continuity fails the tick closed.
- Official tier-0 spot fees from https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees retrieved 11 Nov 2026: taker 0.070%, maker 0.040%. Every fill charges taker 0.070%. Maker 0.040% is documented and NEVER used without a resting-limit/queue model; there are no maker spot books. Slippage is the more adverse of a 2bp mid floor and an L2 walk of the intended notional; if visible depth is insufficient the 2bp floor is used and labelled. Stop/halt exits use 5bp adverse. No funding is charged or credited on spot. Minimum notional $10.
- Signals use fully closed UTC bars only. 250-bar seed on 15m/1h/4h; 1m cache retains 512 closed bars. EMA/EWM adjust=False. Missing data refuses the tick. No historical bar-open signal/time fills. 15m/1h/4h entries within 90 seconds of bar close; missed entries are logged, never entered retrospectively.
- No leverage and no funding reserve. Daily MYT -2% halt still latches on research books (not hold controls) and flattens at the next actually observed quote. Halt stays across midnight until owner reset. Virtual gap loss can exceed a tight cash buffer; this is still not liquidation.
- Mandatory virtual stops for research books: replay every missed closed 1m candle before decisions. Touch=trigger+5bp adverse; gap through trigger=bar open+5bp. Entry-minute touch conservatively stopped and flagged ambiguous. These explicit candle-reconstructed STOP assumptions are the only retrospective fills, NOT real exchange protection. >5000-minute retention or any missing replay minute blocks all new entries without advancing the cursor.
- Frozen v1 and v2 registrations, implementation files and running 100 perp-book capital/history stay byte-identical and are never reset. This append-only spot extension has a separate manifest pinned in state; changes require new ids and a new prospective registration.
- Evaluation: same promotion bar as the perp league. >=30 closed trades, positive costed return, beats BOTH the BTC-perp hold and random-entry controls after costs, DSR>0.95, not halted, then a following non-overlapping fresh-MYT-day/flat-book OOS >=7 days OR >=30 new trades for spot_fast books. First OOS endpoint is fixed PASS/FAIL. CANDIDATE_REVIEW_ONLY only. No automatic promotion, message, permission or trade. Known DSR trials = 309 prior + every league book including these 16 = 425 at 116 books. Do not hide failed variants. Spot hold controls are measurement controls, not promotion benchmarks and not live-trading permission.
- Original five, the 95 v2 books, league.py, strategies.py, league_v2.py, strategies_v2.py, evaluation_v2.py and register_v2.py remain frozen. This engine adds public endpoint spotMetaAndAssetCtxs to the allowlist. Collector estimated-weight cap 1000 vs official shared-IP 1200/min.
'''
manifest=dict(version=3,mode='PAPER_ONLY',registered_utc=created,
 original_manifest_sha256=L.sha(ROOT/'registry/manifest.json'),
 extension_v2_sha256=L.sha(ROOT/'registry/extension-v2.json'),
 implementation_sha256=implementation,
 prior_backtest_trials=309,prior_league_books=100,spot_books=16,
 total_league_books=116,total_known_trials=425,
 fee_source=S.FEE_SOURCE,fee_source_retrieved_myt=S.FEE_SOURCE_RETRIEVED_MYT,
 spot_taker=S.SPOT_TAKER,spot_maker_documented=S.SPOT_MAKER,
 starting_equity=S.STARTING_EQUITY,strategies=[])
for spec in S.entries():
    id=spec['id']; path=ROOT/'registry'/f'{id}.md'
    body=f'# {id}\n\nRegistered UTC: {created}\n\n## Frozen specification\n\n```json\n{json.dumps(spec,indent=2,sort_keys=True)}\n```\n\n{S.DESCRIPTIONS[spec["kind"]]}\n\nPrice source: {spec["price_source"]} ({spec["spot_pair"]}, API coin {spec["api_coin"]}). Not a perp-mid proxy.\n\n{common}\n## Spot extension implementation SHA256\n'+''.join(f'- `{n}`: `{d}`\n' for n,d in implementation.items())
    with path.open('x') as f: f.write(body)
    digest=L.sha(path)
    with (path.with_suffix('.sha256')).open('x') as f: f.write(f'{digest}  {path.name}\n')
    manifest['strategies'].append(dict(spec,sha256=digest))
with (ROOT/'registry/spot-extension-v3.json').open('x') as f: json.dump(manifest,f,indent=2)
with (ROOT/'registry/spot-extension-v3.sha256').open('x') as f: f.write(L.sha(ROOT/'registry/spot-extension-v3.json')+'  spot-extension-v3.json\n')
L.atomic(ROOT/'spot-extension-registration-receipt.json',manifest)
print(f'Registered {len(manifest["strategies"])} additional PAPER spot books, total 116; known trials 425; original and v2 manifests unchanged')
