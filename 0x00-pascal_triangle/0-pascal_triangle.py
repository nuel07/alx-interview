#!/usr/bin/python3
'''
Pascal's Triangle
'''


def pascal_triangle(n):
    '''
    returns a list of lists of integers representing
    the Pascal’s triangle of n:
    otherwise, returns an empty list if n <= 0
    '''
    pascals_t = []
    if n <= 0:
        return pascals_t
    pascals_t = [[1]]
    for i in range(1, n):
        tmp = [1]
        for j in range(len(pascals_t[i - 1]) - 1):
            current = pascals_t[i - 1]
            tmp.append(pascals_t[i - 1][j] + pascals_t[i - 1][j + 1])
        tmp.append(1)
        pascals_t.append(tmp)
    return pascals_t
