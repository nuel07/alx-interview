#!/usr/bin/python3
""" Rotate a 2D matrix 90 degrees clockwise """

def rotate_2d_matrix(matrix):
    """ rotates given nxn 2D matrix,
    rotates the matrix in place """
    mtrx_cp = matrix.copy()
    for p in range(len(matrix)):
        colmn = [row[p] for row in mtrx_cp]
        matrix[p] = colmn[::-1]
