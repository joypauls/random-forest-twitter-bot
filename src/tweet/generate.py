"""
Functions to generate the actual "text" of the tweets
"""
import numpy as np
# from typing import List

BASE_TOKENS = ["🌳", "🌲", "🍄"]
# proportion out of 100
BASE_WEIGHTS = [50, 45, 5]
# normalized as probabilities
BASE_WEIGHTS = np.array(BASE_WEIGHTS) / np.sum(BASE_WEIGHTS)

SPECIAL_TOKENS = ["🐿️", "🐦", "🐇", "🦋", "🦔", "🦊", "🐝", "🐻"]
# proportion out of 100
SPECIAL_WEIGHTS = [30, 30, 10, 10, 10, 5, 4, 1]
# normalized as probabilities
SPECIAL_WEIGHTS = np.array(SPECIAL_WEIGHTS) / np.sum(SPECIAL_WEIGHTS)

# probability of any token being special
SPECIAL_PROBABILITY = 0.03


# TODO: implement ponds and water animals, different night/day
# WATER_TOKEN = "💧"
# WATER_SPECIAL_TOKENS = ["🐸", "🦢", "🦆"]
# NIGHT_SPECIAL_TOKENS = ["🦉", "🦝", "🦇"]


def sample_tokens(k, tokens, weights) -> np.array:
    return np.random.choice(tokens, k, p=weights)


def generate_forest(m: int = 7, n: int = 12):
    # fill background
    base_tokens = sample_tokens(m * n, BASE_TOKENS, BASE_WEIGHTS)
    # pass through and replace
    for i in range(0, base_tokens.size):
        p = np.random.uniform(0, 1, 1)
        if (p <= SPECIAL_PROBABILITY):
            base_tokens[i] = sample_tokens(1, SPECIAL_TOKENS, SPECIAL_WEIGHTS)[0]
    # text formatting
    lines = ["".join(base_tokens[(i * n):((i + 1) * n)]) for i in range(0, m)]
    forest = "\n".join(lines)
    return forest
