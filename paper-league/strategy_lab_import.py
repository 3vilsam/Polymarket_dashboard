"""Put the reconstructed paper-trading package on sys.path for local tests."""
import sys
from pathlib import Path


def add_parent():
    root = Path(__file__).resolve().parent
    for path in (
        root / 'strategy-lab' / 'paper-trading',
        root / 'strategy-lab' / 'paper-league',
        root,
    ):
        text = str(path)
        if text not in sys.path:
            sys.path.insert(0, text)
