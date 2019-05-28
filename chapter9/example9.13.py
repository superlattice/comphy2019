#!/usr/bin/python
## example9_13

import numpy as np
from lamRange import *
from inversePower3 import *

N = 10
n = 100
d = np.ones(n)*2.0
c = np.ones(n-1)*(-1.0)
r = lamRange(d,c,N)
s = (r[N-1] + r[N])/2.0
lam,x = inversePower3(d,c,s)  # Inverse power method

print("Eigenvalue No.",N," =",lam)
input("\nPress return to exit")

