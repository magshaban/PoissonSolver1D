# This code to evalute the Load matrix b or bi1. 
#The main file is PoissonSolver1D.py

import numpy as np
from inputFunctions import *

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
