#!/usr/bin/python3
"""Solves the N Queens problem"""
import sys


def is_safe(board, row, col, n):
    """Check if placing a queen at (row, col) is safe"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """Backtracking function to solve the problem"""
    def backtrack(row, board):
        if row == n:
            result = [[r, board[r]] for r in range(n)]
            solutions.append(result)
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1, board)
    solutions = []
    board = [-1] * n
    backtrack(0, board)
    return solutions


# ----- Main Execution -----
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for sol in solutions:
        print(sol)
