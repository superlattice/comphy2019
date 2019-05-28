!/usr/bin/python
## example10_8
import numpy as np
from stdForm import *
from inversePower import *
from downhill import *
def F(x):
    global eVal
    lam = 1.0e6
    eVal_min = 0.4
    A = np.array([[4.0*(x[0]**4 + x[1]**4), 2.0*x[1]**4],  \
            [2.0*x[1]**4, 4.0*x[1]**4]])
    B = np.array([[4.0*(x[0]**2 + x[1]**2), -3.0*x[1]**2], \
            [-3*x[1]**2, 4.0*x[1]**2]])
    H,t = stdForm(A,B)
    eVal,eVec = inversePower(H,0.0)
    return x[0]**2 + x[1]**2 + lam*(max(0.0,eVal_min - eVal))**2

xStart = np.array([1.0, 1.0])
x = downhill(F,xStart,0.1)
print("x = ", x)
print("eigenvalue = ",eVal)
input ("Press return to exit")
