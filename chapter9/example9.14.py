#!/usr/bin/python
## example9_14
from householder import *
from eigenvals3 import *
from inversePower3 import *
import numpy as np

N = 3   # Number of eigenvalues requested
a = np.array([[ 11.0, 2.0,  3.0,  1.0,  4.0],  \
        [  2.0, 9.0,  3.0,  5.0,  2.0],  \
        [  3.0, 3.0, 15.0,  4.0,  3.0],  \
        [  1.0, 5.0,  4.0, 12.0,  4.0],  \
        [  4.0, 2.0,  3.0,  4.0, 17.0]])

xx = np.zeros((len(a),N))
d,c = householder(a)
p = computeP(a)
lambdas = eigenvals3(d,c,N)
for i in range(N):
    s = lambdas[i]*1.0000001
    lam,x = inversePower3(d,c,s) # Compute eigenvector [x]
    xx[:,i] = x                  # Place [x] in array [xx]

xx = np.dot(p,xx)
print("Eigenvalues:\n",lambdas)
print("\nEigenvectors:\n",xx)
input("Press return to exit")

