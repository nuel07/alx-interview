#!/usr/bin/python3
''' calculate minimum number of operations on a file '''


def minOperations(n: int) -> int:
    ''' returns minimum number of operations
    Args:
        n(int): number of H characters
    Return: int
    '''
    num_ops = 0
    ops = 2 ## copy All and Paste
    while n > 1:
        while n % ops == 0:
            num_ops += ops
            n /= ops
        ops += 1
    return num_ops
