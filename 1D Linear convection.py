# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:01:40 2022

@author: HP
"""

#Step 1: Linear convection:

import numpy as np
import matplotlib.pyplot as plt


nx=41 #number of grid points
dx= 2/(nx-1) #distance between adjacent grid points
nt=25 #number of timesteps
dt=0.025
c=1 #speed of wave taken as 1

#Initial conditions:
u=np.ones(nx)
u[int(.5 / dx):int(1 / dx + 1)] = 2  #setting u = 2 between 0.5 and 1 as per our I.C.s

plt.plot(np.linspace(0, 2, nx), u) #plot of IC's
plt.ylabel("u")
plt.xlabel("grid points")
plt.title("Initial conditions- Nonlinear convection in 1D")
plt.show()

#applying FDM:
un=np.ones(nx) #temporary array for next time step

for n in range(nt):
    un=u.copy()
    for i in range(1,nx):
        u[i] = un[i] - c * dt / dx * (un[i] - un[i-1]) #applying FD formula

plt.plot(np.linspace(0, 2, nx),u)
plt.ylabel("u")
plt.xlabel("grid points")
plt.title("After time t - Linear convection in 1D")
plt.show()         