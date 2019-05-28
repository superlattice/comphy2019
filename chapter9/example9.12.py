#!/usr/bin/python
## example9_12
import numpy as np
from eigenvals3 import *

N=3
n = 100
d = np.ones(n)*2.0
c = np.ones(n-1)*(-1.0)
lambdas = eigenvals3(d,c,N)
print(lambdas)
input("\nPress return to exit")
