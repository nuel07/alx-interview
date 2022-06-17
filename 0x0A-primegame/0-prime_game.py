#!/usr/bin/python3
""" Determine winner of the Prime Games """


def isprime(n: int) -> bool:
    """ n(int): number to check if it is prime"""
    for i in range(2, (n+1)//2):
        if n % i == 0:
            return False
    return True


def delete_numbers(n: int, nums: list):    
    """ delete numbers - assign zero """
    for i in range(len(nums)):
        if nums[i] % n == 0:
            nums[i] = 0


def isWinner(x: int, nums: list) -> str:
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    and if the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """
    nums.sort()
    winner = False
    M_wins = 0
    B_wins = 0
    
    for game in range(x):    
        nums2 = list(range(1, nums[game] + 1))
        turn = 0
        while True:
            """
            # uncomment to monitor turns
            if turn % 2 != 0:
                print("Ben turn ")
            else:
                print("Maria turn ")

            """
            change = False
            
            for i, n in enumerate(nums2):
                if n > 1 and isprime(n):
                    delete_numbers(n, nums2)
                    change = True
                    turn += 1
                    break
            if change is False:
                break
        if turn % 2 != 0:
            M_wins += 1
        else:
            B_wins += 1
            
    if M_wins == B_wins:
        return None
    if M_wins > B_wins:
        return "Maria"
    return "Ben"
