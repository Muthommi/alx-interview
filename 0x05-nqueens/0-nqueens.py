#!/usr/bin/python3
import sys


def print_solution(queens):
    """Function to print solution in required format."""
    print([[row, col] for row, col in enumerate(queens)])


def is_safe(queens, row, col):
    """Function to check if placing a queen is safe."""
    for r, c in enumerate(queens[:row]):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, row, queens):
    """Function to recursively solve the N-queens problem."""
    if row == n:
        print_solution(queens)
        return
    for col in range(n):
        if is_safe(queens, row, col):
            queens[row] = col
            solve_nqueens(n, row + 1, queens)
            queens[row] = -1


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

    queens = [-1] * n
    solve_nqueens(n, 0, queens)


if __name__ == "__main__":
    main()
