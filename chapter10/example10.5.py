#!/usr/bin/python
## example10_5
from powell import *
from numpy import array
from math import sqrt
from gaussElimin import *
def F(x):
    global v, weight
    lam = 100.0
    c = 2.0*sqrt(2.0)
    A = array([[c*x[1] + x[2], -x[2],  x[2]],           \
            [-x[2],          x[2], -x[2]],              \
            [ x[2],         -x[2],  c*x[0] + x[2]]])/c
    b = array([0.0, -1.0, 0.0])
    v = gaussElimin(A,b)
    weight = x[0] + x[1] + sqrt(2.0)*x[2]
    penalty = max(0.0,abs(v[1]) - 1.0)**2   \
            + max(0.0,-x[0])**2             \
            + max(0.0,-x[1])**2             \
            + max(0.0,-x[2])**2
    return weight + penalty*lam

xStart = array([1.0, 1.0, 1.0])
x,numIter = powell(F,xStart)
print("x = ",x)
print("v = ",v)
print("Relative weight F = ",weight)
print("Number of cycles = ",numIter)
input("Press return to exit")

