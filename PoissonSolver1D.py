# This is a poisson equation solver in 1D using FEM.

import numpy as np
import matplotlib.pyplot as plt


x = np.arange(2,8.1,0.1)
kappa = np.array([10**6,0])
g = np.array([-1,0])

def conductivity(a):
    return 0.1*(5 - 0.6*a)

def StiffMat1D(x,kappa):
    
    n = len(x) - 1 # number of intervials
    A = np.zeros((n+1,n+1))
    
    for i in range(n):
        h = x[i+1] - x[i]
        xmid = (x[i+1] + x[i])/2 # Iinterval mid point
        amid = conductivity(xmid)
        A[i,i] += amid/h
        A[i+1,i] -= amid/h
        A[i,i+1] -= amid/h
        A[i+1,i+1] += amid/h
    
    A[0,0] += kappa[0]
    A[n,n] += kappa[1]     
    
    return A

print(StiffMat1D(x,kappa))    
plt.spy(StiffMat1D(x,kappa));
plt.show()

def SourceFunc(v):
    return 0.03*(v-6)**4
    
    
def LoadVec1D(x,kappa,g):
    n = len(x) - 1
    b = np.zeros((n+1,1))
    
    for i in range(n):
        h = x[i+1] - x[i]
        b[i] += SourceFunc(x[i])*h/2 
        b[i+1] += SourceFunc(x[i+1])*h/2 
     
    b[0] += kappa[0]*g[0]
    b[n] += kappa[1]*g[1]   
    
    return b

M = StiffMat1D(x,kappa)
inverse_M = np.linalg.inv(M)
b = LoadVec1D(x,kappa,g)

U = inverse_M@b

plt.plot(x,U)