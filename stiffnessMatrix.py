

import numpy as np
from inputFunctions import *

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