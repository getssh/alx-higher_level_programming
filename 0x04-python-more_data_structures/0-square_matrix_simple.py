#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq = []
    for row in range(len(matrix)):
        col = []
        for j in range(len(matrix[row])):
            col.append(matrix[row][j] * matrix[row][j])
        sq.append(col)
    return sq
