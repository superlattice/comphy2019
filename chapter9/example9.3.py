#!/usr/bin/python
## example9_3
import numpy
from jacobi import *
import math
from sortJacobi import *
from stdForm import *
A = np.array([[ 1/3, -1/3,  0.0], \
        [-1/3,  4/3, -1.0],\
        [ 0.0, -1.0,  2.0]])
B = np.array([[1.0, 0.0, 0.0],\
        [0.0, 1.0, 0.0],\
        [0.0, 0.0, 2.0]])

H,T = stdForm(A,B) # Transform into std. form
lam,Z = jacobi(H) # Z = eigenvecs. of H
X = np.dot(T,Z) # Eigenvecs. of original problem
sortJacobi(lam,X) # Arrange in ascending order of eigenvecs.
for i in range(3): # Normalize eigenvecs.
    X[:,i] = X[:,i]/math.sqrt(np.dot(X[:,i],X[:,i]))

print("Eigenvalues:\n",lam)
print("Eigenvectors:\n",X)
input ("Press return to exit")


