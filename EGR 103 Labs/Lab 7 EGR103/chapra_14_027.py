#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:45:44 2020

@author: kushgulati
"""

# %% Import modules
import numpy as np
from fitting_common import *

# %% Load and manipulate data
x = np.array([2,3,4,5,7,10])
y = np.array([5.2,7.8,10.7,13,19.3,27.5])
xmodel = np.linspace(np.min(x), np.max(x), 100)

# %% Perform calculations (polyfit)
n = 1
p = np.polyfit(x, y, n)
print("Polyfit coefs: ")
print(p)

# %% Perform calculations (linear reg gen)
def yfun(xe, coefs):
    return coefs[0] * xe**1 

# Reshape data for block matrices
xv = np.reshape(x, (-1, 1))
yv = np.reshape(y, (-1, 1))
phi_mat = np.block([[xv**1]])
pvec = np.linalg.lstsq(phi_mat, yv, rcond=None)[0]
print("Linear Reg coefs:")
print(pvec)

# %% Generate estimates and model (polyfit)
yhat = np.polyval(p, x)
ymodel = np.polyval(p, xmodel)
y_estimate = np.polyval(p, 3.0)
print(y_estimate)
# %% Generate estimates and model (linear reg gen)
yhat_gen = yfun(x, pvec)
ymodel_gen = yfun(xmodel, pvec)
ymodel_estimate = yfun(3,pvec)
print(ymodel_estimate)
# %% Generate plots
fig, ax = plt.subplots(num=1, clear=True)
ax.plot(x, y, "ko", label="Data")
ax.plot(xmodel, ymodel, "b-", label="Polyfit Model")
ax.plot(xmodel, ymodel_gen, "r--", label = "General LinReg")
ax.grid(True)
ax.set(xlabel = "Voltage (V)", ylabel= "Current (I)")
ax.legend(loc="best")
fig.tight_layout()
fig.savefig("chapra_14_027_plot.png")


