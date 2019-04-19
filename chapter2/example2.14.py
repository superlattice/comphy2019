#!/usr/bin/python
## example2_14
import numpy as np
from LUdecomp3 import *
n=6
d = np.ones((n))*2.0
e = np.ones((n-1))*(-1.0) c = e.copy()
d[n-1] = 5.0
aInv = np.identity(n) c,d,e = LUdecomp3(c,d,e) 
for i in range(n):
    aInv[:,i] = LUsolve3(c,d,e,aInv[:,i])
print("\nThe inverse matrix is:\n",aInv)
input("\nPress return to exit")

