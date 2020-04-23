#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 20:48:57 2020

@author: kushgulati
"""

# %% Import modules
import numpy as np
from fitting_common import *


# %% Load and manipulate data
x = np.array([0,2,4,6,9,11,12,15,17,19])
y = np.array([5,6,7,6,9,8,8,10,12,12])
xmodel = np.linspace(np.min(x), np.max(x), 100)
xmodel2 = np.linspace(np.min(y), np.max(y),100)

# %% Perform calculations
n = 1
p = np.polyfit(x, y, n)
p2 = np.polyfit(y,x,n)
print(p)
print(p2)







# %% Generate estimates and model
yhat = np.polyval(p, x)
yhat2 = np.polyval(p2,y)
ymodel = np.polyval(p, xmodel)
ymodel2 = np.polyval(p2, xmodel2)

# %% Calculate statistics
calc_stats(y, yhat, 1)

st,sr,r2 = calc_stats(x,yhat2,False)
print(st,sr,r2)

# %% Generate plots
fig, ax = plt.subplots(2)
ax[0].plot(x, y, "ko", label="Data")
ax[0].plot(x, yhat, "ks", label="Estimates", mfc="none")
ax[0].plot(xmodel, ymodel, "k-", label="Model")
ax[0].set(xlabel = "x", ylabel = "y")
ax[0].grid(True)
ax[0].legend(loc="best")
ax[1].plot(y, x, "ko", label="Data")
ax[1].plot(y, yhat2, "ks", label="Estimates", mfc="none")
ax[1].plot(xmodel2, ymodel2, "k-", label="Model")
ax[1].set(xlabel = "y", ylabel = "x")
ax[1].grid(True)
ax[1].legend(loc="best")
fig.tight_layout()

fig.savefig("chapra_14_005_plot.png")