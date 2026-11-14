"""Stop-touch primitive used by league.resolve_stop.

Reconstructed. Original sentinel.py was not in the league export. A long is adverse at or
below its stop; a short is adverse at or above its stop. The fill is the worse of the stop
and the reference price (gap open), then stop-slippage bps against the position.
"""


def hit_adverse(position, price):
    stop = position.get('stop')
    if stop is None or price is None:
        return False
    if position['dir'] > 0:
        return price <= stop
    return price >= stop


def stop_fill(position, cfg, reference):
    slip = float(cfg.get('stop_slippage_bps', 5.0)) / 1e4
    px = reference if hit_adverse(position, reference) else position['stop']
    return px * (1 - position['dir'] * slip)
