#!/usr/bin/python
## example3_12
import numpy as np
from polyFit import *
xData = np.array([-0.04,0.93,1.95,2.90,3.83,5.0,      \
        5.98,7.05,8.21,9.08,10.09])
yData = np.array([-8.66,-6.44,-4.36,-3.27,-0.88,0.87, \
        3.31,4.63,6.19,7.4,8.85])
while True:
    try:
        m = eval(input("\nDegree of polynomial ==> "))
        coeff = polyFit(xData,yData,m)
        print("Coefficients are:\n",coeff)
        print("Std. deviation =",stdDev(coeff,xData,yData))
    except SyntaxError: break

input("Finished. Press return to exit")
