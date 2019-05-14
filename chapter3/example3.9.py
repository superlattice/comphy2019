#!/usr/bin/python
## example3_9

import numpy as np
from cubicSpline import *
xData = np.array([1,2,3,4,5],float)
yData = np.array([0,1,0,1,0],float)
k = curvatures(xData,yData)

while True:
    try: x = eval(input("\nx ==> "))
    except SyntaxError: break
    print("y =",evalSpline(xData,yData,k,x))
input("Done. Press return to exit")
