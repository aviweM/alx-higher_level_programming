#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for u in range(len(matrix)):
        for k in range(len(matrix[u])):
            print("{:d}".format(matrix[u][k]), end="")
            if k != (len(matrix[u]) - 1):
                print(" ", end="")
        print("")
