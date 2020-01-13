#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix=[]
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")
    elif type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(0, len(matrix)):
        if type(matrix[i]) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        inner=[]
        for j in range(0, len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            elif len(matrix[0]) != len(matrix[i]):
                raise TypeError("Each row of the matrix must have the same size")
            else:
                inner.append(round((matrix[i][j] / div), 2))
        new_matrix.append(inner)
    return(new_matrix)
