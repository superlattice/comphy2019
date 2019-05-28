## example7_9
import numpy as np
import matplotlib.pyplot as plt
from run_kut5 import *
from printSoln import *

def F(x,y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -4.75*y[0] - 10.0*y[1]
    return F

x = 0.0
xStop = 10.0
y = np.array([-9.0, 0.0])
h = 0.1
freq = 4
X,Y = integrate(F,x,y,xStop,h)
printSoln(X,Y,freq)
plt.plot(X,Y[:,0],'-o',X,Y[:,1],'-^')
plt.xlabel('x')
plt.legend(('y','dy/dx'),loc=0)
plt.grid(True)
plt.show()
input("\nPress return to exit")
