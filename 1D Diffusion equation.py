# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:42:43 2022

@author: HP
"""

#Step 3: 1D Diffusion equation:

import numpy as np
import matplotlib.pyplot as plt

nx=41
dx=2/(nx-1)
nt=20
nu=0.3 #viscosity
sigma =0.2 #parameter
dt=sigma*dx**2/nu

#initial conditions:
u=np.ones(nx)
u[int(.5 / dx):int(1 / dx + 1)] = 2

un=np.ones(nx)

for n in range(nt): 
    un = u.copy() 
    for i in range(1, nx - 1):
        u[i] = un[i] + nu * dt / dx**2 * (un[i+1] - 2 * un[i] + un[i-1])
        
plt.plot(np.linspace(0,2,nx),u)
plt.ylabel("u")
plt.xlabel("grid points")
plt.title("plot of velocity after timestep- Diffusion equation in 1D")
plt.show()  