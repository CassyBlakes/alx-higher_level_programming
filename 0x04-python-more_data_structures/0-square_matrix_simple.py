#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        return[[elm**2 for elm in row] for row in matrix]
