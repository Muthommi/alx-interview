#!/usr/bin/python3
"""
Module to solve change-making problem.
"""


def makeChange(coins, total):
    """
    Determines minimum number of coins needed for a given total.
    Returns: int: minimum number of coins needed to meet total.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total %= coin

    return count if total == 0 else -1
