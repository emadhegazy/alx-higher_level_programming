#!/usr/bin/python3
"""
The module for pascal_triangle method.
"""


def pascal_triangle(n):
    """
    to return a list of lists of integers
        Args:
            n (int): number of lists and digits
        Return: list of lists
    """
    rows = [[1 for j in range(i + 1)] for i in range(n)]
    for n in range(n):
        for i in range(n - 1):
            rows[n][i + 1] = sum(rows[n - 1][i:i + 2])
    return rows
