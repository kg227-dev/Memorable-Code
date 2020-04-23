#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:29:29 2020

@author: kushgulati
"""

# %% Import modules
import numpy as np
from fitting_common import *

# %% Load and manipulate data
x = np.array([0.5,1,2,3,4,5,6,7,9])
y = np.array([6,4.4,3.2,2.7,2,1.9,1.7,1.4,1.1])
xmodel = np.linspace(np.min(x), np.max(x), 100)

# %% Perform calculations
def yfun(xe, coefs):
    return coefs[0] * np.exp(xe*-1.5) + coefs[1] * np.exp(xe*-0.3) + coefs[2] * np.exp(xe*-0.05)


# Reshape data for block matrices
xv = np.reshape(x, (-1, 1))
yv = np.reshape(y, (-1, 1))
phi_mat = np.block([[np.exp(-1.5*xv),np.exp(-0.3*xv),np.exp(-0.05*xv)]])
pvec = np.linalg.lstsq(phi_mat, yv, rcond=None)[0]
print(pvec)


# %% Generate estimates and model
yhat = yfun(x, pvec)
ymodel = yfun(xmodel, pvec)

# %% Calculate statistics
calc_stats(y, yhat, 1)