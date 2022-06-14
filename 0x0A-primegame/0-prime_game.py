#!/usr/bin/python3
"""Determine the winner of the prime games"""


def isPrime(n: int) -> bool:
    """determine if a number is prime"""
    if n <= 1:
        return False
    for num in range(2, n):
        if num % 2 == 0:
            return False
    return True


def isWinner(x: int, nums: list) -> str:
    """return winner of the prime games"""
    M_wins = 0
    B_wins = 0

    for turn in range(x):
        for n in range(len(nums)):
            if isPrime(nums[n]):
                temp = nums[n]
                nums.pop(n)
                for i in nums:
                    if i % temp == 0:
                        nums.remove(i)
                if turn % 2 == 0:
                    M_wins += 1
                else:
                    B_wins += 1
                break
            if n + 1 == len(nums) and M_wins == 0 and B_wins == 0:
                return None
    if M_wins == B_wins:
        return None
    if M_wins > B_wins:
        return "Maria"
    return "Ben"
