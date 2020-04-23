#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:45:28 2020

@author: kushgulati
"""

# %% Import modules
import numpy as np
from fitting_common import *
import scipy.optimize as opt

# %% Load and manipulate data
x = np.array([50,80,130,200,250,350,450,550,700])
y = np.array([99,177,202,248,229,219,173,142,72])
xmodel = np.linspace(np.min(x), np.max(x), 100)

# %% Perform calculations
def yfun(x, *coefs):
    return coefs[0] * x * np.exp((-x/coefs[1])+1) 


popt = opt.curve_fit(yfun, x, y, [10, 5])[0]
print(popt)





# %% Generate estimates and model
yhat = yfun(x, *popt)
ymodel = yfun(xmodel, *popt)

# %% Calculate statistics
calc_stats(y, yhat, 1)


# %% Generate plots
fig, ax = plt.subplots(num=1, clear=True)
ax.plot(x, y, "rD", label="Data")
ax.plot(xmodel, ymodel, "g-", label="Model")
ax.set(xlabel = "t", ylabel = "p(t)")
ax.grid(True)

fig.tight_layout()
fig.savefig("chapra_15_011_plot.png")
