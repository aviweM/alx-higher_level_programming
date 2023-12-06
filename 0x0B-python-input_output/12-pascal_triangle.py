#!/usr/bin/python3
"""
Module 14-pascal_triangle
Contains function that returns int lists of pascal triangle of any given size
"""


def pascal_triangle(n):
    """
    Return:
        empty list [] if n <= 0
        if n is 7, we should expect:
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(n-1):
        triangle.append([c+d for c, d
                         in zip([0] + triangle[-1], triangle[-1] + [0])])
    return triangle
