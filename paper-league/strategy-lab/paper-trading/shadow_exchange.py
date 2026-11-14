"""L2 size cap used by league.open_paper before it reapplies the funding reserve.

Reconstructed. The frozen open_paper path still computes the 0.5% / 3x / $10 size and then
takes min(that size, this estimate). Returning the visible size does not raise the league's
own cap; a thin book can only make the size smaller.
"""


def size_order(cfg, book, coin, direction, stop, depth, ctx):
    levels = depth['asks'] if direction > 0 else depth['bids']
    visible = sum(float(sz) for _, sz in levels)
    return dict(size=max(0.0, visible), coin=coin)
