#!/usr/bin/python3
""" My Module for pascal's triangle
"""


def pascal_triangle(n):
    """ Prints a list of lists of a pascal triangle

    Args:
        n (int): how many rows to make

    Returns:
        The Pascal Triangle as a list of lists
    """
    pascal = []
    prev_row = [1]
    row = 0
    if n <= 0:
        return []
    pascal.append(prev_row)
    if n == 1:
        return pascal
    while row < n - 1:
        current_row = []
        current_row.append(prev_row[0])
        i = 0
        while i < row:
            current_row.append(prev_row[i] + prev_row[i + 1])
            i += 1
        current_row.append(prev_row[len(prev_row) - 1])
        pascal.append(current_row)
        prev_row = current_row
        row += 1
    return pascal
