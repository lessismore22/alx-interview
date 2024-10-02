#!/usr/bin/python3
""" 0. Prime Game """


def is_winner(x, nums):
    if x <= 0 or not nums:
        return None

    # Step 1: Precompute the prime numbers up to the maximum value in nums
    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    # Step 2: Precompute the number of prime moves possible for each n
    prime_moves = [0] * (max_num + 1)

    for i in range(1, max_num + 1):
        prime_moves[i] = prime_moves[i - 1] + (1 if primes[i] else 0)

    # Step 3: Simulate the game for each round in nums
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count of prime moves determines the winner: Maria goes first
        if prime_moves[n] % 2 == 0:
            ben_wins += 1  # Even number of moves means Ben wins
        else:
            maria_wins += 1  # Odd number of moves means Maria wins

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
