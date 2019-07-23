#This file contains the input functions.
#The conductivity is a(x) and the source function is f(x).
#The main file is PoissonSolver1D.py


# this is the conductivity function.
def conductivity(a):
    return 0.1*(5 - 0.6*a)


# this is the source matrix f(x)
def SourceFunc(v):
    return 0.03*(v-6)**4
    
