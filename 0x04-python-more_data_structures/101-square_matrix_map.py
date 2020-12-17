#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(square, matrix))


def square(num=[]):
    return list(map(lambda x: (x * x), num))
