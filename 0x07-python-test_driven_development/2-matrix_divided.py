#!/usr/bin/python3
def matrix_divided(matrix, div):
    """if not isinstance(matrix[0], list):"""
    if not all(type(num) in [int, float] for row in matrix for num in row):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        std = len(matrix[0])
        if std != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
