# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:31:36 2022

@author: HP
"""

#Step 2: nonlinear convection

import numpy as np
import matplotlib.pyplot as plt

nx = 41
dx = 2 / (nx - 1)
nt = 20    
dt = .025

u=np.ones(nx)
u[int(.5 / dx) : int(1 / dx + 1)] = 2 #as per ICs

un=np.ones(nx)

for n in range(nt):
    un=u.copy()
    for i in range(1,nx):
        u[i] = un[i] - u[i] * dt / dx * (un[i] - un[i-1])
        
plt.plot(np.linspace(0, 2, nx),u)
plt.ylabel("u")
plt.xlabel("grid points")
plt.title("After time t - Nonlinear convection in 1D")
plt.show()         