"""Scale twins at 1,000 virtual USDT. Not a new strategy trial.

Twins live in league_state['scale_k1000'], not in books, so the frozen extend
checks and the DSR trial count (434) never see them. Existing book objects are
not rewritten here. Rules, stops, and risk fractions are the parent's. Bankroll
is the only difference. Retired and halted parents get no twin.

Public /info only. No wallet, key, order, or exchange write.
"""
import copy
import json
import time
from pathlib import Path

import league as L
import league_v2 as V
import league_v3 as V3
import league_v4 as V4
import league_v5 as V5
import league_v6 as V6
import league_v7 as V7
import strategies as S
import strategies_v3 as S3

BANK = 1000.0
SUFFIX = '-k1000'
NOTE = 'scale twins, not new strategy trials; bankroll is the only difference; trial count unchanged'


def is_active(book):
    return not book.get('retired') and not book.get('halted')


def rules_sha(parent, root):
    for key in ('spec', 'spot_spec', 'spec4', 'spot4_spec'):
        spec = parent.get(key)
        if spec and spec.get('sha256'):
            return spec['sha256']
    manifest = L.read_json(Path(root) / 'registry' / 'manifest.json')
    for strategy in manifest['strategies']:
        if strategy['id'] == parent['id']:
            return strategy['sha256']
    raise ValueError(f'no rules hash for {parent["id"]}')


def make_twin(parent, now, sha):
    book = L.sc.new_state(dict(L.CFG, starting_equity=BANK))
    spot = parent.get('market') == 'spot' or 'spot_spec' in parent or 'spot4_spec' in parent
    book.update(
        id=parent['id'] + SUFFIX, parent_id=parent['id'], owner=parent.get('owner'),
        kind=parent.get('kind'), lane=parent.get('lane'), market='spot' if spot else parent.get('market', 'perp'),
        events=[], peak=BANK, max_drawdown_pct=0., decisions={}, stopped_sides={},
        day_date=L.sc.myt_date(now), day_start_equity=BANK, starting_equity=BANK, cash=BANK,
        last_tick_myt=None, activation_ms=now, scale_cohort='k1000', rules_sha256=sha,
        bankroll=BANK, halted=False, halt_reason=None, leverage=1 if spot else parent.get('leverage'),
    )
    for key in ('spec', 'spot_spec', 'spec4', 'spot4_spec'):
        if key in parent:
            book[key] = copy.deepcopy(parent[key])
    L.event(book, 'registered', now, rules_sha256=sha, status='UNPROVEN_PAPER_ONLY',
            starting_equity=BANK, parent_id=parent['id'], scale_twin=True,
            bankroll_only_difference=True, trial_count_delta=0)
    return book


def symbols_of(book):
    if book.get('kind') == 'benchmark':
        return {'BTC'}
    for key in ('spot_spec', 'spot4_spec', 'spec', 'spec4'):
        if key in book:
            return set(book[key].get('coins') or [])
    return set(S.COINS)


# These runs committed no tick. One gap row records them; it is not a ledger entry.
LOST_TICK_RUNS = (
    43672089302, 43674376748, 43676274556, 43677031366, 43678153687,
    43681513829, 43681888108, 43682249187, 43684477611, 43685268287, 43685660547,
)


def _present(data, coins, spot):
    minutes = (data.get('spot_minutes') if spot else data.get('minutes')) or {}
    mids = data.get('mids') or {}
    return [c for c in coins if c in minutes and c in mids]


def _covered(data, start, end, coins, spot):
    key = 'spot_minutes' if spot else 'minutes'
    series = data.get(key) or {}
    for coin in coins:
        have = {row['t'] for row in series.get(coin, [])}
        for stamp in range(start, end, S.MINUTE):
            if stamp not in have:
                return False
    return True


def _open_benchmark(book, data, now):
    """Same 1x buy-and-hold as the frozen control, sized off this twin's 1,000 bankroll.

    league.start_benchmark hardcodes the original 100. That function is left unchanged.
    """
    if book.get('benchmark_started'):
        return
    px = data['mids']['BTC'] * (1 + .0002)
    qty = BANK / (px * (1 + L.CFG['taker_fee']))
    fee = qty * px * L.CFG['taker_fee']
    book['cash'] -= fee
    book['stats']['fees'] += fee
    book['positions']['BENCH'] = dict(
        id='BENCH', coin='BTC', dir=1, side='long', size=qty, entry_px=px, entry_ms=now,
        stop=None, fees=fee, realized_gross=0., funding=0., funding_hour=now // S.HOUR)
    book['benchmark_started'] = True
    L.event(book, 'entry', now, trade_id='BENCH', coin='BTC', price=px, size=qty, fee=fee,
            reason='NONTRADABLE_1x_BTC_perp_buy_hold_control_no_stop', risk_exception=True,
            bankroll=BANK, scale_twin=True)


def _call(books, runnable, ids, fn):
    """Run one frozen apply. A missing-coin KeyError restores those books and skips them."""
    snap = {i: copy.deepcopy(books[i]) for i in ids if i in books}
    try:
        fn()
    except KeyError as exc:
        coin = str(exc.args[0]) if exc.args else 'unknown'
        for i, book in snap.items():
            books[i] = book
            runnable.pop(i, None)
        return coin
    return None


def _apply(books, data, now, start, retired_symbols):
    end = now // S.MINUTE * S.MINUTE
    failed = set(data.get('failed') or {})
    runnable = {}
    skipped = []
    missing = []
    for bid, book in books.items():
        coins = symbols_of(book)
        spot = book.get('market') == 'spot'
        if coins & failed or not _covered(data, start, end, coins, spot):
            skipped.append(bid)
            missing.extend(sorted(coins & failed))
            continue
        runnable[bid] = book
    with V6.without(retired_symbols):
        spot_ok = _present(data, S3.SPOT_COINS, True)
        perp_ok = _present(data, S.COINS, False)
        available = set(spot_ok) | set(perp_ok)
        missing.extend(c for c in list(S3.SPOT_COINS) + list(S.COINS) if c not in available)
        for bid, book in list(runnable.items()):
            if symbols_of(book) - available:
                skipped.append(bid)
                del runnable[bid]
        with V5.universe(perp_ok, spot_ok):
            originals = [bid for bid, book in runnable.items()
                         if book.get('kind') != 'benchmark' and not any(k in book for k in ('spec', 'spot_spec', 'spec4', 'spot4_spec'))]
            if originals:
                coin = _call(books, runnable, originals, lambda: L.apply_tick(
                    {'books': {i: runnable[i] for i in originals if i in runnable}, 'next_minute': start, 'ticks': 0}, data, now))
                if coin: missing.append(coin)
            view = {'books': runnable}
            groups = (
                ('spec', lambda: V.apply_new(view, data, now, start)),
                ('spot_spec', lambda: V3.apply_spot(view, data, now, start)),
                ('spec4', lambda: V4.apply_perp4(view, data, now, start)),
                ('spot4_spec', lambda: V4.apply_spot4(view, data, now, start)),
            )
            for key, fn in groups:
                ids = [bid for bid, book in runnable.items() if key in book]
                if not ids:
                    continue
                coin = _call(books, runnable, ids, fn)
                if coin:
                    missing.append(coin)
            for bid, book in list(runnable.items()):
                if book.get('kind') != 'benchmark':
                    continue
                def bench(book=book):
                    _open_benchmark(book, data, now)
                    L.apply_tick({'books': {book['id']: book}, 'next_minute': start, 'ticks': 0}, data, now)
                coin = _call(books, runnable, [bid], bench)
                if coin:
                    missing.append(coin)
    for bid in skipped:
        if bid in books:
            books[bid]['twin_next_minute'] = books[bid].get('twin_next_minute', start)
    for bid in runnable:
        books[bid].pop('twin_next_minute', None)
    return skipped, sorted(set(missing))


def _export_one(root, book):
    directory = Path(root) / 'books' / book['id']
    directory.mkdir(parents=True, exist_ok=True)
    L.atomic(directory / 'state.json', book)
    text = ''.join(json.dumps(event, allow_nan=False) + '\n' for event in book['events'])
    path = directory / 'ledger.jsonl'
    tmp = path.with_suffix('.jsonl.tmp')
    tmp.write_text(text)
    tmp.replace(path)


def _fingerprint(books):
    return {bid: json.dumps(book, sort_keys=True, default=str) for bid, book in books.items()}


def _append_gap(root, rec):
    path = Path(root) / 'data-gaps.jsonl'
    marker = rec.get('event')
    if marker == 'ticks_lost_keyerror_ueth' and path.exists() and 'ticks_lost_keyerror_ueth' in path.read_text():
        return
    with path.open('a') as handle:
        handle.write(json.dumps(rec, allow_nan=False) + '\n')


def record_lost_ticks(root):
    """The 11 KeyError runs wrote no tick. Record them once."""
    _append_gap(root, dict(
        event='ticks_lost_keyerror_ueth',
        recorded_utc='2026-11-15T06:51:00Z',
        failed_runs=list(LOST_TICK_RUNS),
        ticks_lost=len(LOST_TICK_RUNS),
        coin='UETH',
        fills_backfilled=False,
        double_counted=False,
        trial_count_unchanged=True,
        note='Eleven chained runs raised KeyError UETH in the scale-twin spot apply and committed no tick. Those attempts are not ledger ticks and are not replayed.',
    ))


def run_twins(root, data):
    started = time.monotonic()
    root = Path(root)
    state = L.read_json(root / 'league_state.json')
    before = _fingerprint(state['books'])
    now = data['observed_ms']
    end = now // S.MINUTE * S.MINUTE
    cohort = state.get('scale_k1000')
    created = False
    if not cohort:
        twins = {}
        for parent in state['books'].values():
            if not is_active(parent):
                continue
            twins[parent['id'] + SUFFIX] = make_twin(parent, now, rules_sha(parent, root))
        cohort = dict(
            version=1, bankroll=BANK, trial_count_delta=0, note=NOTE, created_ms=now,
            created_utc=L.utc(now), next_minute=end, books=twins,
        )
        created = True
    retired = set(L.read_json(root / 'registry' / 'retirement-usol-v1.json').get('symbols') or [])
    start = end if created else cohort.get('next_minute', end)
    skipped, missing = _apply(cohort['books'], data, now, start, retired)
    if missing:
        _append_gap(root, dict(
            event='missing_coin', recorded_ms=now, recorded_utc=L.utc(now), recorded_myt=L.sc.myt(now),
            tick=state.get('ticks'), coins=missing, skipped_books=skipped, fills_backfilled=False,
            double_counted=False, candles_fabricated=False,
            note='A coin was missing from this snapshot. Twins that trade it were not updated. No fill was invented.',
        ))
    cohort['next_minute'] = end
    cohort['last_tick_ms'] = now
    after = _fingerprint(state['books'])
    if before != after:
        raise RuntimeError('scale twins mutated an existing book')
    state['scale_k1000'] = cohort
    record_lost_ticks(root)
    L.atomic(root / 'league_state.json', state)
    for book in cohort['books'].values():
        _export_one(root, book)
    summary = dict(
        bankroll=BANK, count=len(cohort['books']), created=created, skipped=len(skipped),
        trial_count_delta=0, note=NOTE, wall_seconds=round(time.monotonic() - started, 4),
        ids=sorted(cohort['books']),
    )
    path = root / 'last_tick.json'
    if path.exists():
        result = L.read_json(path)
        result['scale_k1000'] = {k: summary[k] for k in ('bankroll', 'count', 'created', 'skipped', 'trial_count_delta', 'note', 'wall_seconds')}
        result['trial_count'] = result.get('trial_count', 434)
        L.atomic(path, result)
    return summary


def tick(root=L.ROOT):
    saved = {}
    original = V5.PublicData.fetch

    def fetch(self, st, now):
        data = original(self, st, now)
        saved['data'] = data
        return data

    V5.PublicData.fetch = fetch
    try:
        result = V7.tick(root)
    finally:
        V5.PublicData.fetch = original
    if 'data' not in saved:
        raise RuntimeError('parent tick did not collect a snapshot')
    summary = run_twins(root, saved['data'])
    result = L.read_json(Path(root) / 'last_tick.json')
    result['scale_k1000_wall_seconds'] = summary['wall_seconds']
    print(json.dumps(dict(scale_k1000_count=summary['count'], scale_k1000_wall_seconds=summary['wall_seconds'],
                          trial_count=result.get('trial_count'), collection_seconds=(result.get('load') or {}).get('collection_seconds'))), flush=True)
    return result
