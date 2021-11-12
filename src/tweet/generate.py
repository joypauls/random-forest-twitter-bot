"""
Functions to generate the actual "text" of the tweets
"""
import numpy as np
# from typing import List


class Regular():
    BASE_TOKENS = ["🌳", "🌲", "🍄"]
    # proportion out of 100
    BASE_WEIGHTS = np.array([50, 45, 5])
    SPECIAL_TOKENS = ["🐿️", "🐦", "🐇", "🦋", "🦔", "🦊", "🐝", "🐻"]
    # proportion out of 100
    SPECIAL_WEIGHTS = [30, 30, 10, 10, 10, 5, 4, 1]
    # probability of any token being special
    SPECIAL_PROBABILITY = 0.03
    def __init__(self):
        # normalize as probabilities
        self.BASE_WEIGHTS = self.BASE_WEIGHTS / np.sum(self.BASE_WEIGHTS)
        self.SPECIAL_WEIGHTS = self.SPECIAL_WEIGHTS / np.sum(self.SPECIAL_WEIGHTS)


# class Tropical():
#     BASE_TOKENS = ["🌳", "🌲", "🍄"]
#     # proportion out of 100
#     BASE_WEIGHTS = np.array([50, 45, 5])
#     SPECIAL_TOKENS = ["🐿️", "🐦", "🐇", "🦋", "🦔", "🦊", "🐝", "🐻"]
#     # proportion out of 100
#     SPECIAL_WEIGHTS = [30, 30, 10, 10, 10, 5, 4, 1]
#     # probability of any token being special
#     SPECIAL_PROBABILITY = 0.03
#     def __init__(self):
#         # normalize as probabilities
#         self.BASE_WEIGHTS = self.BASE_WEIGHTS / np.sum(self.BASE_WEIGHTS)
#         self.SPECIAL_WEIGHTS = self.SPECIAL_WEIGHTS / np.sum(self.SPECIAL_WEIGHTS)


# TODO: implement ponds and water animals, different night/day
# WATER_TOKEN = "💧"
# WATER_SPECIAL_TOKENS = ["🐸", "🦢", "🦆"]
# NIGHT_SPECIAL_TOKENS = ["🦉", "🦝", "🦇"]


def _sample_tokens(k, tokens, weights) -> np.array:
    return np.random.choice(tokens, k, p=weights)


def generate_forest(m: int = 7, n: int = 12) -> str:
    forest = Regular()
    # fill background
    base_tokens = _sample_tokens(m * n, forest.BASE_TOKENS, forest.BASE_WEIGHTS)
    # pass through and replace
    for i in range(0, base_tokens.size):
        p = np.random.uniform(0, 1, 1)
        if (p <= forest.SPECIAL_PROBABILITY):
            base_tokens[i] = _sample_tokens(1, forest.SPECIAL_TOKENS, forest.SPECIAL_WEIGHTS)[0]
    # text formatting
    lines = ["".join(base_tokens[(i * n):((i + 1) * n)]) for i in range(0, m)]
    forest = "\n".join(lines)
    return forest
