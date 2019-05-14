#!/usr/bin/python
## example2_7
import numpy as np
from LUdecomp import *

a = np.array([[ 3.0, -1.0,  4.0], \
        [-2.0,  0.0,  5.0], \
        [ 7.0,  2.0, -2.0]])

b = np.array([[ 6.0,  3.0,  7.0], \
        [-4.0,  2.0, -5.0]])

a = LUdecomp(a) # Decompose [a]
det = np.prod(np.diagonal(a))
print("\nDeterminant =",det)

for i in range(len(b)): # Back-substitute one
    x = LUsolve(a,b[i]) # constant vector at a time
    print("x",i+1,"=",x)

input("\nPress return to exit")
