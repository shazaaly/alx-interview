#!/usr/bin/python3
"""module to draw pascal"""

def pascal_triangle(n):
    '''Creates a list of lists of
    the Pascal's triangle.
    '''
    if n <= 0 or type(n) is not int:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == i or j == 0:
                row.append(1)
            if i > j and j > 0:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle
