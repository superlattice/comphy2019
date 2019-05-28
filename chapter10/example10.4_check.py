#!/usr/bin/python
## example10_4_check
import numpy as np
from newtonRaphson2 import *
def F(x):
    return np.array([2.0*(x[0] - 5.0) + x[2]*x[1],  \
            2.0*(x[1] - 8.0) + x[2]*x[0],  \
            x[0]*x[1] - 5.0])

xStart = np.array([1.0, 5.0, 1.0])
print("x = ", newtonRaphson2(F,xStart))
input("Press return to exit")
