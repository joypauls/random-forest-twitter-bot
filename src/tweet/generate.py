"""
Functions to generate the actual "text" of the tweets
"""
import numpy as np

TOKENS = [
    "🌲",
    "🌳",
    "🍄",
    "🐿️",
    "🐦",
    "🐇",
    "🐸",
    "🦔",
    "🦉",
    "🦝",
    "🦊"
]
TOKEN_WEIGHTS = [
    0.45,
    0.4,
    0.05,
    0.02,
    0.02,
    0.02,
    0.01,
    0.01,
    0.01,
    0.005,
    0.005
]


def sample_token() -> str:
    return np.random.choice(TOKENS, p=TOKEN_WEIGHTS)


def generate_forest(m: int = 6, n: int = 8):
    tokens = [sample_token() for i in range(0, m * n)]
    lines = ["".join(tokens[(i * n):((i + 1) * n)]) for i in range(0, m)]
    forest = "\n".join(lines)
    return forest
