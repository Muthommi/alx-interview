#!/usr/bin/python3


def is_prime(n):
    """
    Returns: List indicating if the numbers 0-n are prime.
    """
    if n < 2:
        return [False] * (n + 1)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


def isWinner(x, nums):
    """
    Determines who wins the prime game.
    :parameter x: number of rounds.
    :parameter nums: array of integers representing n each round.
    :return: None or name of player who wins.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    prime_flags = is_prime(max_n)

    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if prime_flags[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
