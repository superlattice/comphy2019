#!/usr/bin/python
## example5_4

def LUdecomp3(c,d,e):
  n = len(d)
  for k in range(1,n):
    lam = c[k-1]/d[k-1]
    d[k] = d[k] - lam*e[k-1]
    c[k-1] = lam
  return c,d,e
def LUsolve3(c,d,e,b):
  n = len(d)
  for k in range(1,n):
    b[k] = b[k] - c[k-1]*b[k-1]
  b[n-1] = b[n-1]/d[n-1]
  for k in range(n-2,-1,-1):
    b[k] = (b[k] - e[k]*b[k+1])/d[k]
  return b

def curvatures(xData,yData):
  n = len(xData) - 1
  c = np.zeros(n)
  d = np.ones(n+1)
  e = np.zeros(n)
  k = np.zeros(n+1)
  c[0:n-1] = xData[0:n-1] - xData[1:n]
  d[1:n] = 2.0*(xData[0:n-1] - xData[2:n+1])
  e[1:n] = xData[1:n] - xData[2:n+1]
  k[1:n] =6.0*(yData[0:n-1] - yData[1:n]) \
               /(xData[0:n-1] - xData[1:n]) \
               -6.0*(yData[1:n] - yData[2:n+1]) \
               /(xData[1:n] - xData[2:n+1])
  LUdecomp3(c,d,e)
  LUsolve3(c,d,e,k)
  return k

#from cubicSpline import curvatures
#from LUdecomp3 import *
import numpy as np
xData = np.array([1.5,1.9,2.1,2.4,2.6,3.1])
yData = np.array([1.0628,1.3961,1.5432,1.7349,1.8423, 2.0397])
print(curvatures(xData,yData))
input("Press return to exit")
