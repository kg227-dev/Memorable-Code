#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:26:59 2020

@author: kushgulati
"""


# %% Import modules
import numpy as np
from fitting_common import *
import scipy.optimize as opt

# %% Load and manipulate data
x = np.array([0.5,1,2,3,4])
y = np.array([10.4,5.8,3.3,2.4,2])
xmodel = np.linspace(np.min(x), np.max(x), 100)

# %% Perform calculations
def yfun(x, *coefs):
    return ((coefs[0] + np.sqrt(x))/(coefs[1]*np.sqrt(x)))**2


popt = opt.curve_fit(yfun, x, y, [2, 2])[0]
print(popt)





# %% Generate estimates and model
yhat = yfun(x, *popt)
ymodel = yfun(xmodel, *popt)

y_est = yfun(1.6,*popt)
print(y_est)
# %% Calculate statistics
calc_stats(y, yhat, 1)


# %% Generate plots
fig, ax = plt.subplots(num=1, clear=True)
ax.plot(x, y, "ms", label="Data")
ax.plot(xmodel, ymodel, "y-", label="Model")
ax.set(xlabel= "x", ylabel = "y")
ax.grid(True)

fig.tight_layout()
fig.savefig("chapra_15_022_plot.png")
