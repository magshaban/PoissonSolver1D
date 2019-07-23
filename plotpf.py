# The main file is L2Projection1D.py

import matplotlib.pyplot as plt
from LinShapeFun1D import *


def plotall(x,U,M):
    
    # To plot the basis function.
    for i in range(len(x)):
        plt.plot(x,basisf(x,i))
        
    plt.xlabel('x')
    plt.ylabel('$\phi_i (x)$')
    plt.title('Linear shape functions in 1D')
    plt.grid()
    plt.show()

    fig, (ax1, ax2) = plt.subplots(1,2)
    fig.suptitle('The Mass Matrix')
    ax1.matshow(M)
    ax2.spy(M)
    plt.show()
       
    plt.plot(x,U,'b')
    plt.xlabel('x')
    plt.ylabel('$U_h$')
    plt.title('The solution of the poission equation in 1D $U_h$')
    plt.grid()
    plt.show()   
       