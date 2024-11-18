#!/usr/bin/python3
"""Module to a function that returns a list of integers."""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's traingle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
