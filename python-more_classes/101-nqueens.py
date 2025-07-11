#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    # Check if another queen is in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(row, board, n):
    if row == n:
        # Print the board in the required format
        solution = [[i, board[i]] for i in range(n)]
        print(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(row + 1, board, n)


def main():
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

    board = [0] * n
    solve_nqueens(0, board, n)


if __name__ == "__main__":
    main()
