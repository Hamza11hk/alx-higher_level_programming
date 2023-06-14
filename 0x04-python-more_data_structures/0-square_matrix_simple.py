#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        w = []
        for r in matrix:
            w.append(list(map(lambda x: x**2, r)))
        return (w)
    return None
