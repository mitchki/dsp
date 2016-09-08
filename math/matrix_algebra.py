# Matrix Algebra

import numpy as np
A = np.array([[1,2,3],[2,7,4]])
print A

B = np.array([[1,-1],[0,1]])
print  B

C = np.array([[5,-1],[9,1],[6,0]])
print C

D = np.array([[3,-2,-1],[1,2,3]])
print D

u = np.array([6,2,-3,5])
print u

v = np.array([3,5,-1,4])
print v

w = np.array([[1],[8],[0],[5]])
print w

# 1. Matrix Dimensions

# 1.1
np.shape(A)
#(2, 3)

# 1.2
np.shape(B)
#(2, 2)

# 1.3
np.shape(C)
#(3, 2)

# 1.4
np.shape(D)
#(2, 3)

# 1.5
np.shape(u)
#(4,)

# 1.6
np.shape(w)
#(4,1)

# 2. Vector Operations

# 2.1
u + v
# array([ 9,  7, -4,  9])

# 2.2
u - v
#array([ 3, -3, -2,  1])


# 2.3
6 * u
# array([ 36,  12, -18,  30])

# 2.4
np.dot(u,v)
# 51

# 2.5
np.linalg.norm(u)
# 8.6023252670426267


# 3. Matrix Operations

# 3.1
A + C
# not defined

# 3.2
A - C.T
#array([[-4, -7, -3],
#       [ 3,  6,  4]])


# 3.3
C.T + 3*D
#array([[14,  3,  3],
#       [ 2,  7,  9]])


# 3.4
np.dot(B,A)
#array([[-1, -5, -1],
#       [ 2,  7,  4]])


# 3.5
np.dot(B,A.T)
# not defined


# Optional
# 3.6
np.dot(B,C)
# not defined

# 3.7
np.dot(C,B)
#array([[ 5, -6],
#       [ 9, -8],
#       [ 6, -6]])

# 3.8
np.dot(np.dot(B,B),np.dot(B,B))
#array([[  1, -12],
#       [  0,   1]])

# 3.9
np.dot(A,A.T)
#array([[14, 28],
#       [28, 69]])

# 3.10
np.dot(D.T,D)
#array([[10, -4,  0],
#       [-4,  8,  8],
#       [ 0,  8, 10]])


