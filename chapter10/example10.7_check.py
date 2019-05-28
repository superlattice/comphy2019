#!/usr/bin/python
## example10_7_check
import numpy as np
import math
from newtonRaphson2 import *
def f(x):
    f = np.zeros(4)
    f[0] = 1.0 + x[3]*x[1]
    f[1] = 2.0/math.cos(x[2]) + x[3]*(x[0]        \
            + 2.0*x[1]*math.tan(x[2]))
    f[2] = 2.0*x[1]*math.tan(x[2])/math.cos(x[2]) \
            + x[3]*(x[1]/math.cos(x[2]))**2
    f[3] = (x[0] + x[1]*math.tan(x[2]))*x[1] - 8.0
    return f

xStart = np.array([3.0, 2.0, 0.0, 1.0])
print("x =",newtonRaphson2(f,xStart))
input("Press return to exit")
