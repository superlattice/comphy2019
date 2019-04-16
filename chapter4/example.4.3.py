#!/usr/bin/python
## example4_3
import math
#from rootsearch import *
#from bisection import *
def f(x): return x - math.tan(x)
a,b,dx = (0.0, 20.0, 0.01)
print("The roots are:")
while True:
    x1,x2 = rootsearch(f,a,b,dx)
    if x1 != None:
        a = x2
        root = bisection(f,x1,x2,1)
        if root != None: print(root)
    else:
        print("\nDone")
        break
input("Press return to exit")

