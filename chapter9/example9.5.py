#!/usr/bin/python
## example9_5
import numpy as np
from inversePower import *

s = 5.0
a = np.array([[ 11.0, 2.0,  3.0,  1.0,  4.0],\
        [  2.0, 9.0,  3.0,  5.0,  2.0],\
        [  3.0, 3.0, 15.0,  4.0,  3.0],  \
        [  1.0, 5.0,  4.0, 12.0,  4.0],  \
        [  4.0, 2.0,  3.0,  4.0, 17.0]])

lam,x = inversePower(a,s)
print("Eigenvalue =",lam)
print("\nEigenvector:\n",x)
input("\nPrint press return to exit")

