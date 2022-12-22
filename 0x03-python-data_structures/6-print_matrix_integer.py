#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for matrix_row in matrix:
        print(" ".join("{:d}".format(elm) for elm in matrix_row))
