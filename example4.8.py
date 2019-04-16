#!/usr/bin/python
## example4_8
def f(x): return x**4 - 6.4*x**3 + 6.45*x**2 + 20.538*x - 31.752
def df(x): return 4.0*x**3 - 19.2*x**2 + 12.9*x + 20.538
def newtonRaphson(x,tol=1.0e-9):
    for i in range(30):
        dx = -f(x)/df(x)
        x = x + dx
        if abs(dx) < tol: return x,i
    print ('Too many iterations\n')
root,numIter = newtonRaphson(2.0)
print ('Root =',root)
print ('Number of iterations =',numIter)
input("Press return to exit")
