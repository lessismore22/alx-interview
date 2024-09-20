#!/usr/bin/python3

""" Contains makeCange function"""


def makeCange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    #sort the coins in descending order
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= (temp * coin)
        if total != 0:
            return -1
    return change
