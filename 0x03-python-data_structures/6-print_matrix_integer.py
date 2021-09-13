#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print()
    i = 0
    j = 0
    while (i < len(matrix)):
        for j in range(len(matrix[i])):
            k = len(matrix[i])
            p = matrix[i][j]
            print("{:d}".format(p), end=" " if j != (k - 1) else "\n")
            j += 1
        i += 1
