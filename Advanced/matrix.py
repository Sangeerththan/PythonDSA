import numpy as np
import random

from numpy.core.fromnumeric import transpose

# 1.Matrix Creation
dim = int(input("Enter Dimension of matrix :"))
matrix = np.random.randint(10, size=(dim, dim))

# 2.Matrix inversion
inverse = np.linalg.inv(matrix)
print ("Inverse matrix : %s" %inverse)

# 3.dot Product won't exactly yield I 
I = np.dot(matrix, inverse)
print(" Dot product of matrix and its inverse is I: %s" %np.dot(matrix, inverse))

# 4.Verification of the identity matrix
EPS = 1e-8
r = np.all(np.abs(I - np.eye(dim)) < EPS)
print(r)

# 5.Trace of matrix
print(" Trace of matrix : %s" %matrix.trace())

# Random matrices with fixed dimension
A = np.random.randint(10, size=(2, 3))
B = np.random.randint(10, size=(3, 2))

# 6.cross product 
print("cross product of %s and %s is %s" %(A, B, np.outer(A, B)))


# 7.transpose of matrix
print("Transpose of matris is %s" %np.transpose(matrix))

# 8.norm of matrix
print("Norm of matrix is : %s" %np.linalg.norm(matrix))

# 9. Range of matrix
print('Range of the matrix is : %s' %np.ptp(matrix))

# 9. Rank of matrix
print('Rank of the matrix is : %s' %np.linalg.matrix_rank(matrix))