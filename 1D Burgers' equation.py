# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 12:04:10 2022

@author: HP
"""

#Step 4: Burgers' equation

import matplotlib.pyplot as plt
import numpy as np
import sympy

from sympy import init_printing
init_printing(use_latex=True)

#writing the intial condition using sympy:
x, nu, t =sympy.symbols('x nu t')
phi=(sympy.exp(-(x-4*t)**2/(4*nu*(t+1)))+sympy.exp(-(x-4*t-2*sympy.pi)**2/(4*nu*(t+1))))

#evaluating partial derivative of phi:
phiprime=phi.diff(x)

#using lambdify:
    
from sympy.utilities.lambdify import lambdify

u = -2 * nu * (phiprime / phi) + 4
ufunc = lambdify((t, x, nu), u) #analytical function of u


#setting up the variables and intial conditions:
nx = 101
nt = 100
dx = 2 * np.pi / (nx - 1)
nu = .07
dt = dx * nu

x = np.linspace(0, 2 * np.pi, nx)
un = np.empty(nx)
t = 0

u = np.asarray([ufunc(t, x0, nu) for x0 in x])

plt.figure(figsize=(11, 7), dpi=100)
plt.plot(x, u, marker='o', lw=2)
plt.xlim([0, 2 * np.pi])
plt.ylim([0, 10])
plt.ylabel("u")
plt.xlabel("grid points")
plt.title("Initial condition plot: Burgers' equation in 1D")
plt.show()  

#applying FDM:
for n in range(nt):
    un = u.copy()
    for i in range(1, nx-1):
        u[i] = un[i] - un[i] * dt / dx *(un[i] - un[i-1]) + nu * dt / dx**2 *\
                (un[i+1] - 2 * un[i] + un[i-1])
    u[0] = un[0] - un[0] * dt / dx * (un[0] - un[-2]) + nu * dt / dx**2 *\
                (un[1] - 2 * un[0] + un[-2])
    u[-1] = u[0]

#calculating analytical value of u:        
u_analytical = np.asarray([ufunc(nt * dt, xi, nu) for xi in x]) 

plt.figure(figsize=(11, 7), dpi=100)
plt.plot(x,u, marker='o', lw=2, label='Computational')
plt.plot(x, u_analytical, label='Analytical')
plt.xlim([0, 2 * np.pi])
plt.ylim([0, 10])
plt.ylabel('u')
plt.xlabel('grid points')
plt.title("Comparison of velocity plot after time: Burgers' equation in 1D")
plt.legend()
