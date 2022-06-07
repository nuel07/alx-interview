#!/usr/bin/python3
""" Module for determining island perimeter """


def island_perimeter(grid):
    """returns island perimeter"""
    width = len(grid)
    height = len(grid[0])
    perimeter = 0

    for r in range(width):
        for c in range(height):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2
    return perimeter
