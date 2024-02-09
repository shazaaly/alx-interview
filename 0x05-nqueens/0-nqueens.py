#!/usr/bin/python3
"""
Solution to the nqueens problem
"""

import sys

import sys

def is_safe(board, row, col, N):
    """_summary_

    Args:
        board (_type_): _description_
        row (_type_): _description_
        col (_type_): _description_
        N (_type_): _description_

    Returns:
        _type_: _description_
    """
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(N):
    """_summary_

    Args:
        N (_type_): _description_

    Returns:
        _type_: _description_
    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0] * N for _ in range(N)]
    solutions = []

    def backtrack(row):
        if row == N:
            solutions.append([row[:] for row in board])
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0
    
    backtrack(0)
    return solutions

def print_solutions(solutions):
    """_summary_

    Args:
        solutions (_type_): _description_
    """
    for sol in solutions:
        print(sol)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)
