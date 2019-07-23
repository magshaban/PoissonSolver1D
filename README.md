# PoissonSolver1D
 This a python solver for Poisson equation in 1D using FEM.<br />
The main file is <PoissonSolver1D.py><br />

 The Poisson eguation given as following: 

    -(a(x)u'(x))' = f(x) for all x belongs to I = (0,1)  
     a(x)u'(0) = k_0(u(0) - g_0)  
    -a(x)u'(1) = k_1(u(1) - g_1) 

 Which is Robin general boundry condition (BC).
 
## Notes:

 If k_i = 0, this implies Neumann BC (in the following example in the code we use k_1 = 0). <br />
 While if k_i tends to infinity, this implies Dirichlet BC. <br />
 (also in the same example, we take k_0 = 10^6 which gives u(0) = g_0).<br />
 
## a(x) and f(x):

    You can change the input functions a(x) and f(x) for a specific problem from the file <inputfuncs.py> 
## k and g:

The input parameters k_i and g_i for i = {0,1} can be changed from the main file <PoissonSolver1D.py>.

    kappa = [k_0, k_1]
    g = [g_0 g_1]
    
# Results:


In the domain [2,8] for 
       
    k_0 = 10^6, K_1 = 0 and g_0 = -1.  
    with a(x) = 0.1*(5 - 0.6*x)
    and f(x) = 0.03*(x-6)**4
we have the approximated solution U_h is: <br />

![result](/solution.png)
<br />

Where the linear shape functions is:<br />
![result1](/shapefun.png)
<br />
which gives the mass matrix: <br />
![result55](/massmat.png)
<br />

# Author:
 Maged Shaban <br />
 magshaban[at]gmail.com <br />
