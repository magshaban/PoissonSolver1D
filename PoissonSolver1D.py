# This is a poisson equation solver in 1D using FEM.
# Poisson function given as following: 
#
# -(a(x)u'(x))' = f(x) for all x belongs to I = (0,1)
#  a(x)u'(0) = k_0(u(0) - g_0) 
# -a(x)u'(1) = k_1(u(1) - g_1) 
#
# Which is Robin general boundry condition (BC).
#
# Note that: if k_i = 0, this implies Neumann BC (in the following example in the code we use k_1 = 0). 
# While if k_i tends to infinity, this implies Dirichlet BC (also in the same example, we take k_0 = 10^6 which gives u(0) = g_0).
#
# You can change the input functions a(x) and f(x) for a specific problem from the file <inputfuncs.py> 
#
# Maged Shaban
# magshaban[at]gmail.com  

import numpy as np
import matplotlib.pyplot as plt

from stiffnessMatrix import *
from loadMatrix import *
from plotpf import *

x = np.arange(2,8.1,0.1) # the discretization vector 

#the input variables
kappa = np.array([10**6,0]) #[k_0,k_1]
g = np.array([-1,0])        #[g_0,g_1]

#Evaluate the A and b
M = StiffMat1D(x,kappa)
inverse_M = np.linalg.inv(M)
b = LoadVec1D(x,kappa,g)

U = inverse_M@b # The solution

print('x= \n',x)
print('\nLoad vector b = \n', b)
print('\nThe Mass Matrix M = \n',M)
print('\nThe solution u_h =  \n' ,U)

plotall(x,U,M)