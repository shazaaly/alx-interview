#!/usr/bin/python3
"""module to draw pascal"""

def pascal_triangle(n):
    """Pascal Triangle building function"""
    if n <= 0:
        return []

    def helper(row, col):
        """recurs"""
        if col == 0 or col == row:
            return 1
        return helper(row - 1, col - 1) + helper(row - 1, col)

    triangle = []

    for i in range(n):
        curr_row = []
        for j in range(i + 1):
            curr_row.append(helper(i, j))
        triangle.append(curr_row)

    return triangle


