#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:55:44 2020

@author: kushgulati
"""

# %% Import modules
import numpy as np
from fitting_common import *
import scipy.optimize as opt

# %% Load and manipulate data
x = np.array([50,60,70,80,90,100,110,120,130])+273.15
y = np.log(np.array([82,2300,18500,80500,230000,500000,960000,1500000,2400000]))
xmodel = np.linspace(320, 410, 100)

# %% Perform calculations
def yfun(x, *coefs):
    return coefs[0] - (coefs[1]/(x+coefs[2]))


popt = opt.curve_fit(yfun, x, y, [0,0,0])[0]
print(popt)





# %% Generate estimates and model
yhat = yfun(x, *popt)
ymodel = yfun(xmodel, *popt)

# %% Calculate statistics
st,sr,r2 = calc_stats(y, yhat, False)
print(st,sr,r2)
# %% Generate plots
fig, ax = plt.subplots(num=1, clear=True)
ax.plot(x, y, "ch", label="Data")
ax.plot(xmodel, ymodel, "k--", label="Model")
ax.set(xlabel = "Temperature (K)", ylabel = "Vapor Pressure (Pa)")
ax.grid(True)

fig.tight_layout()
fig.savefig("chapra_15_029_plot.png")

