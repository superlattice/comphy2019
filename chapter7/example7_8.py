#!/usr/bin/python
## example7_8
import numpy as np
import math
from run_kut5 import *
from printSoln import *

def F(x,y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -9.80665 + 65.351e-3 * y[1]**2 * math.exp(-10.53e-5*y[0])
    return F

x = 0.0
xStop = 10.0
y = np.array([9000, 0.0])
h = 0.5
freq = 1
X,Y = integrate(F,x,y,xStop,h,1.0e-2)
printSoln(X,Y,freq)
input("\nPress return to exit")
