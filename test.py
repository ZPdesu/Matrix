# coding=utf-8
from numpy import *
import LUfactorization as lu


a = 'yes'
while a == 'yes':
    A = input("Enter your input matrix A like \nmatrix([[1, 2, -3, 4], "
              "[4, 8, 12, -8], [2, 3, 2, 1], [-3, -1, 1, -4]]) \n")
    L, U, P = lu.factorization(A)
    print "Matrix L = ", '\n', L
    print "Matrix U = ", '\n', U
    print "Matrix P = ", '\n', P

    a = raw_input("if continue, input yes \n")