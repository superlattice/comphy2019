#!/usr/bin/python
## example 3_6
import numpy as np
from rational import *
from neville import *
import matplotlib.pyplot as plt

xData = np.array([0.1,0.2,0.5,0.6,0.8,1.2,1.5])
yData = np.array([-1.5342,-1.0811,-0.4445,-0.3085, \
        -0.0868,0.2281,0.3824])

x = np.arange(0.1,1.55,0.05)
n = len(x)
y = np.zeros((n,2))
for i in range(n):
    y[i,0] = rational(xData,yData,x[i])
    y[i,1] = neville(xData,yData,x[i])

plt.plot(xData,yData,’o’,x,y[:,0],’-’,x,y[:,1],’--’)
plt.xlabel(’x’)
plt.legend((’Data’,’Rational’,’Neville’),loc = 0)
plt.show()
input("\nPress return to exit")
