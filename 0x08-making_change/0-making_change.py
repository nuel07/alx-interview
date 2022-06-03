#!/usr/bin/python3
""" making change module"""


def makeChange(coins: list, total: int) -> int:
    """return fewest number of coins to meet total"""

    if total <= 0:
        return 0
    num_coins = 0
    wallet = sorted(coins, reverse=True)
    current_amount = total

    for coin in wallet:
        while(current_amount >= coin):
            change = current_amount // coin
            num_coins += change
            current_amount = current_amount % coin
    if current_amount == 0:
        return num_coins
    return -1
