#!/usr/bin/python
## example2_11
import numpy as np
from LUdecomp3 import *

d = np.ones((5))*2.0
c = np.ones((4))*(-1.0)
b = np.array([5.0, -5.0, 4.0, -5.0, 5.0])
e = c.copy()
c,d,e = LUdecomp3(c,d,e)
x = LUsolve3(c,d,e,b)
print("\nx =\n",x)
input("\nPress return to exit")
