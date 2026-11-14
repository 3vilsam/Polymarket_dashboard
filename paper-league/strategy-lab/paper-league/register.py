#!/usr/bin/env python3
"""One-shot registration, refuses overwrite and refuses registration after any tick."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, importlib.metadata, sys
ROOT=Path(__file__).resolve().parent
if (ROOT/'league_state.json').exists() or (ROOT/'registry/manifest.json').exists():
    sys.exit('Refusing overwrite: registrations are immutable; changed rules need new ids/league.')
created=datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00','Z')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
files=['league.py','strategies.py','../paper-trading/simcore.py','../paper-trading/shadow_exchange.py',
       '../paper-trading/sentinel.py','../../risk-limits.md']
implementation={name:sha(ROOT/name) for name in files}
common='''## Frozen shared execution and evaluation rules
- Mode: forward research PAPER ONLY on public Hyperliquid mainnet data. No keys, accounts, signing, order/testnet/exchange writes, auto-promotion or real capital. Previous failures remain failures. This is not a Risk PASS.
- Independent 100 virtual USDC book (USDT treated 1:1); BTC, ETH, SOL perpetuals, deterministic conflict priority BTC then ETH then SOL. One position per coin and **one major-cluster position total**, applying the stricter risk-limits.md despite max-positions ceiling of 2. No cross-book netting or sharing equity. All candidates share the engine and execution assumptions.
- Indicators use fully closed UTC candles only, immutable initial collected seed then append only: 710 four-hour bars; 250 daily bars. EMA adjust=False. Missing warmup or candles is an error. Historical seed data is NOT counted as forward performance. The initial closed signal is evaluated but expires if not within its entry window.
- Signal on completed 4h/day bar; fill at first live observed tick after boundary within 120 seconds, **not at a fictitious historical next open**. Signals outside the entry window are logged and cannot create hindsight entries. Missed closed-bar signal exits execute at next actual observation and record delay. This timing differs from the historical backtests.
- Public endpoints: api.hyperliquid.xyz/info types allMids, metaAndAssetCtxs, candleSnapshot, fundingHistory, l2Book only. Poll 60 seconds; shared cache. Full successful-read request/response evidence saved compressed with hashes. Mids are observation-time proxies, not guaranteed executable prices. L2 walked for new research entries when available; fallback mid +2bp adverse if depth absent. Taker only: 0.045% every entry/exit; maker 0.015% recorded but no maker fills claimed. Signal/time exits mid +2bp adverse; stop/halt/risk-budget exits +5bp adverse. No queue/partial-fill/liquidation modelling.
- Risk per trade <=0.5% of equity including entry+exit fees, 5bp stop slippage, plus 24 hours funding reserve at max(current adverse hourly rate, 0.00125%/h). Size rounded DOWN to szDecimals. Risk never rounded up to satisfy $10 minimum; reject notional <$10. Max open risk 2%; notional/equity <=3x and 20% margin headroom. Expected stop loss is a sizing estimate, not a guarantee against gaps or future funding.
- A fixed mandatory virtual stop is set with every research entry. Candidate stop distance must be 0.5% through 4.5%. After each minute/current tick, close if accrued costs plus estimated remaining stop loss exceed min(initial risk budget, 0.5% current equity). Costs can still exceed budget on a jump. No additions inside an episode.
- Daily MYT equity rollover; -2% day-start-equity breach flattens at observed price +5bp adverse and sets a sticky no-new-risk halt. Midnight does NOT clear the halt; owner reset is required. Mandatory stops remain in force during any pause.
- Hourly FUNDING: actual settled fundingHistory prints, one per UTC hour while position held at the hour boundary. Long pays positive; short receives. Cash= -direction * units * actual rate * settlement-minute OPEN PRICE PROXY (historical oracle is not supplied by fundingHistory). Dollar payments are simulated estimates, NOT observed exact exchange cash flows. All missed hours are replayed, without a 3-hour accrual cap. A missing/duplicate print blocks the tick, never zero-filled. Funding at hour boundary is applied before intraminute stop resolution; exact subminute ordering is unknown.
- DOWNTIME: persist last processed closed 1m candle. On restart replay every missed closed minute chronologically. Stop touch fills at stop trigger +5bp adverse; if opening price gapped through the stop, fill at that opening price +5bp. Log original bar time, observation/replay time, gap flag, trigger and resolution. Entry partial-minute stop touch is conservatively counted and flagged ambiguous because pre/post-entry price sequence is unknown. Never invent ticks or say the order was on the exchange. If any replay minute is missing (including >5000-minute retention outage), block progress and new entries with UNRESOLVED_REPLAY_GAP; no optimistic skip/fill.
- Crash safety: one engine lock, one supervisor lock; atomic fsync state contains ALL books and their complete events. Ledgers/leaderboard are rebuildable exports of that state, not a second source of truth. No partial tick is committed when validation fails. Restart resumes book, positions, signal cursors and funding markers, never resets capital. Rule and implementation hashes checked each tick; changing any frozen implementation or manifest stops the league.
- Metrics: completed episode count, net-of-fees/funding win %, PF and net expectancy in USDC/trade. Net MTM PnL includes open unrealized PnL, paid fees/funding but not hypothetical future exit fee. MaxDD is % of 1m-close/live-mid equity peaks, not true tick-level MaxDD. Missing statistics are unavailable, not zero. Under 30 completed trades: NOT SIGNIFICANT. Even >=30 is no PASS; desk requires >=100, independent forensic/risk review and owner-approved exact ticket for any future real trade. No annualized profit promise. First checkpoint 15 Nov 2026 is operational only, not a performance deadline. Preserve every candidate and loss; no retuning winner on the same forward window. Prior search multiplicity is at least 309 trials and is not reset by this league.
- NONTRADABLE CONTROL EXCEPTION: only the BTC benchmark ignores stop/risk sizing/halt to provide a true buy-and-hold comparator; this is never permission for a research strategy or real trade to bypass risk.
'''
entries=[
('s1-donchian40-ablation-v1','donchian','Crypto Ablation Lab (historical idea provenance)', '''## S1 Donchian frozen candidate
- Source: ../backtests/2026-11-09_hl-3strat/README.md and backtest.py, selected N=40 final-step rule. Prior verdict NO EDGE; forward observation is NOT evidence of recovery.
- 4h: long when close > prior 40 highs; short when close < prior 40 lows, current bar excluded. Exit long when close < prior 20 lows; exit short when close > prior 20 highs; opposite valid entry also exits.
- EMA200 trend: long only close > EMA200; short only close < EMA200.
- ATR14 = arithmetic rolling mean of true range. ATR% = ATR14/close. Rank = fraction of previous 499 ATR% values strictly below the current value, in trailing 500-bar window. Entry only rank <0.8 (same source code convention).
- Last 24 observed hourly funding prints before bar boundary: no long if mean >0.000025 per hour; no short if mean <0. All 24 prints required. Stop 3% from actual fill. No fixed profit target or time cap. This retains original signal/filter parameters but uses the shared stricter $100 desk sizing, live-observed fill window and hourly funding/replay, not original $10k sleeves/1% risk.
'''),
('s2-bb40-ema200-ablation-v1','bb','Crypto Ablation Lab (historical idea provenance)', '''## S2 Bollinger + EMA200 frozen candidate
- Source: ../backtests/2026-11-09_hl-3strat/{README.md,backtest.py} step 2 (+stop3 +trend), NOT the final +vol/+fund variant. This specific EMA-only ablation is explicitly chosen as the named BB+EMA200 candidate, not a claim that the rejected final strategy passed.
- 4h: SMA40, sample SD40 (ddof=1); z=(close-SMA)/SD. Long z<-2 AND close>EMA200; short z>2 AND close<EMA200. No entry when SD=0.
- Exit long close>=SMA40, exit short close<=SMA40; opposite valid entry also exits. Fixed stop 3% from fill. No vol/funding entry filter, no TP/time cap. Actual hourly funding is always charged. Shared risk sizing and observable fills replace original notional sizing.
'''),
('s4-ewmac-riskcap-noadd-ablation-v1','ewmac','Crypto Ablation Lab (historical idea provenance; desk risk overlay)', '''## S4 EWMAC daily risk-capped no-add variant
- Source: ../backtests/2026-11-09_hl-3strat/carver_ewmac_daily/{README.md,carver.py}, decision trial 308. Original venue Binance; this is an explicitly NEW Hyperliquid forward variant, not an exact venue/position-sizing replication. Prior trial remains NO EDGE.
- Daily UTC closed close. EMA speeds 8/32,16/64,32/128; EWMA price-change SD span25 adjust=False unbiased std, raw=(EMAfast-EMAslow)/SD. Multiply scalars 5.3,3.75,2.65 respectively, cap each at +/-20 and equal-weight average. Forecast zero if volatility undefined/zero; at least128 daily bars. Initial seed250 observed HL bars retained and appended.
- annualized volatility = EWMA daily pct-change std span25 *sqrt365. Scale=0.20/annualizedVol. Target signed units = equity*scale*forecast/10/signalClose. Buffer = 0.10*equity*scale/signalClose. If current signed units are inside target +/-buffer, do nothing; otherwise target nearer buffer edge. Do not open when buffer-edge target is opposite forecast.
- On entry cap this target to common risk/notional limits. **No additions within a live episode** (different from original full rebalance); same-side target reductions allowed only for delta notional >=$10 and rounded down. Mandatory fixed 4.5% stop. Stop stays unchanged on reductions. Sign flip/zero exits. A stop locks out that coin/direction until combined forecast sign changes or reaches zero. Hourly funding + cost budget enforcement apply.
'''),
('r1-trend-rsi-pullback-market-lane-v1','rsi','Market Analyst lane (desk-defined; NOT independently submitted/endorsed)', '''## R1 simple trend/RSI pullback candidate
- Provenance: the owner's request for parallel strategy study and the delegated simple 4h trend/RSI candidate. No existing Market Analyst note supplied complete rules. These are explicitly desk-defined experimental rules, NOT a bot's proven strategy or a reuse of the failed 15m RSI<30 rule. Attribution is a lane assignment, not an invented bot submission.
- Long only, 4h. Require close>EMA200 AND EMA20>EMA200. RSI14 uses gain/loss EWMA alpha=1/14, adjust=False, first difference seed, at least200 bars; zero-loss RSI100, all-flat RSI50.
- Entry when previous RSI<40 AND current RSI>=40 while trend holds. Stop distance=2*arithmetic ATR14 / signal close as fraction, applied from actual fill; abstain if outside0.5%-4.5%. ATR includes current completed bar only.
- Exit when RSI>=60 OR close<EMA200; market exit after48h observed time regardless of next4h signal (minute replay/first observable mid). No fixed price TP, no short, no additions. Common costs, funding and risk apply.
'''),
('b0-btc-1x-hold-control-v1','benchmark','Desk measurement control (not a bot strategy)', '''## B0 nontradable 1x BTC buy-and-hold control
- Synthetic Hyperliquid BTC PERP long at the first successful live tick. Initial fill = observed BTC mid*(1+0.0002); units=100/[fill*(1+0.00045)]. Entry fee charged; initial notional equals post-fee equity at fill (1x). Fractional units allowed in this index/control only.
- Hold fixed units forever until a separately agreed evaluation end; no exit, stop, rebalance or daily halt. Initial1x leverage drifts thereafter. All actual hourly funding rates charged using shared settlement-minute price proxy. Equity MTM at live BTC mid. No closed trades yet means no win rate/PF/expectancy.
- **This control is deliberately NOT risk-compliant and is NEVER an executable strategy, proposal, copy-trade model or authorization to bypass risk.** It is a costed long-perp exposure comparator, not spot BTC and not a claim to replicate funding-free spot buy-and-hold.
''')]
manifest=dict(version=1,mode='PAPER_ONLY',registered_utc=created,implementation_sha256=implementation,
              dependencies={n:importlib.metadata.version(n) for n in ('numpy','pandas')},strategies=[])
for id,kind,owner,specific in entries:
    path=ROOT/'registry'/f'{id}.md'
    body=f'# {id}\n\nRegistered UTC: {created}\n\nIdea owner/provenance: {owner}\n\n{specific}\n{common}\n## Frozen implementation SHA-256\n\n'+''.join(f'- `{n}`: `{h}`\n' for n,h in implementation.items())
    with path.open('x') as f:f.write(body)
    digest=sha(path)
    (ROOT/'registry'/f'{id}.sha256').write_text(f'{digest}  {id}.md\n')
    manifest['strategies'].append(dict(id=id,kind=kind,owner=owner,sha256=digest))
with (ROOT/'registry/manifest.json').open('x') as f:json.dump(manifest,f,indent=2)
(ROOT/'registry/manifest.sha256').write_text(sha(ROOT/'registry/manifest.json')+'  manifest.json\n')
print(json.dumps(manifest,indent=2))
