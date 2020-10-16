"""
Functions to generate the actual "text" of the tweets
"""
import numpy as np

VOCAB = [
    "🌲",
    "🌳",
    "🍄"
]
VOCAB_WEIGHTS = [
    0.5,
    0.4,
    0.1
]

vocab_idx = np.arange(0, len(VOCAB), 1)


def sample_token() -> str:
    idx = np.random.choice(vocab_idx, p=VOCAB_WEIGHTS)
    return VOCAB[idx]


def generate_forest(m: int = 2, n: int = 6):
    tokens = [sample_token() for i in range(0, m * n)]
    lines = ["".join(tokens[(i * n):((i + 1) * n)]) for i in range(0, m)]
    forest = "\n".join(lines)
    return forest
