#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for i in matrix:
        result.append([x ** 2 for x in i])
    return result
