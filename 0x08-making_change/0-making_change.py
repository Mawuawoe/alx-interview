#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0
    if isinstance(coins, list) and isinstance(total, int):
        coins.sort(reverse=True)
        count = 0
        for coin in coins:
            if coin <= total:
                count += total // coin
                total = total % coin
        if total == 0:
            return count
        else:
            return -1
