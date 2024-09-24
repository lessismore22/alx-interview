#!/usr/bin/python3

""" Contains makeCange function"""


def makeChange(coins, total):
    # If total is less than or equal to 0, no coins are needed
    if total <= 0:
        return 0

    # Initialize dp array where dp[i] represents the fewest
    # number of coins to make amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make total of 0

    # Loop over all amounts from 1 to total
    for i in range(1, total + 1):
        # Try every coin denomination
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means
    # we cannot make the total with the given coins
    return dp[total] if dp[total] != float('inf') else -1
