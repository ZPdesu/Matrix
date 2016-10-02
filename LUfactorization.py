# coding=utf-8
from numpy import *


def create_matrix():
    """

    :return: Generate the default matrix A
    """
    A = mat([[1, 2, -3, 4], [4, 8, 12, -8], [2, 3, 2, 1], [-3, -1, 1, -4]], float)
    return A


def factorization(a):
    """

    :param a: Input matrix
    :return: Decomposed matrices L, U, P
    """
    m, n = shape(a)  # Calculate the number of rows and columns of a matrix
    if m != n:
        print "\nThe matrix is not square"
    elif linalg.matrix_rank(a) != n:
        print "\nThis is not a nonsingular matrix"
    else:
        L = eye(n, dtype=float)     # Initialize matrix L, U, P
        U = zeros((n, n), float)
        P = zeros((n, n), float)
        b = arange(1, n + 1, dtype=float)       # b is used to record the order of exchange
        c = c_[a, b]
        for i in range(0, n - 1):       # Partial Pivoting
            temp = i
            for j in range(i + 1, n):       # Select and exchange the row that corresponds to  the max absolute value
                if abs(c[j, i]) > abs(c[temp, i]):
                    temp = j
            temp_row = c[temp].copy()
            c[temp] = c[i]
            c[i] = temp_row
            for j in range(i + 1, n):       # Eliminate the following lines
                if abs(c[j, i]) > 0:
                    temp_ratio = c[j, i] / c[i, i]
                    c[j, i: n] = c[j, i: n] - temp_ratio * c[i, i:n]
                    c[j, i] = temp_ratio
        for i in range(1, n):       # Calculate L
            for j in range(0, i):
                L[i, j] = c[i, j]
        for i in range(0, n):       # Calculate U and P
            for j in range(i, n):
                U[i, j] = c[i, j]
            P[i, int(c[i, n]) - 1] = 1
        print "When A =", '\n', a
        print "Matrix L = ", '\n', L
        print "Matrix U = ", '\n', U
        print "Matrix P = ", '\n', P
        return L, U, P


def main():     # Test run
    A = create_matrix()
    factorization(A)


if '__main__' == __name__:
    main()
