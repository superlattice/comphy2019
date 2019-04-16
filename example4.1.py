#!/usr/bin/python
## example4_1
#from rootsearch import *
def f(x): return x**3 - 10.0*x**2 + 5.0
x1 = 0.0; x2 = 1.0
for i in range(4):
    dx = (x2 - x1)/10.0
    x1,x2 = rootsearch(f,x1,x2,dx)
x = (x1 + x2)/2.0
print('x =', '{:6.4f}'.format(x))
input("Press return to exit")
