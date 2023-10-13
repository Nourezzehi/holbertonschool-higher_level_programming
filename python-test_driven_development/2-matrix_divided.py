#!/usr/bin/python3
def matrix_divided(matrix, div):
    """devide every matrix item"""

    new_matrix = [[]]
    for row in matrix:
        for item in row:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers / floats")
    for i in range(len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError(
                "Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")
    new_matrix = [round(i / div, 2) for row in matrix for i in row]
    return new_matrix
