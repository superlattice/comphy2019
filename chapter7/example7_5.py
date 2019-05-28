#!/usr/bin/python
## example7_5
import numpy as np
from run_kut4 import *
from printSoln import *
from math import exp

def F(x,y):
    F = np.zeros(1)
    F[0] = 3.0*y[0] - 4.0*exp(-x)
    return F

x = 0.0 # Start of integration
xStop = 10.0 # End of integration
y = np.array([1.0]) # Initial values of {y}
h = 0.1 # Step size
freq = 20 # Printout frequency

X,Y = integrate(F,x,y,xStop,h)
printSoln(X,Y,freq)
input("\nPress return to exit")
