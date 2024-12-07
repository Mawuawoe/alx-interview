#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    if not coins or not all(isinstance(c, int) and c > 0 for c in coins):
        return -1

    # Sort coins in descending order
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if coin <= total:
            # Use as many coins as possible for this denomination
            count += total // coin
            total %= coin

    return count if total == 0 else -1
