#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 01:15:07 2020

@author: kushgulati
"""

# %% Import modules
import numpy as np
from fitting_common import *

# %% Load and manipulate data
x = np.array([-40,0,40,80,120,160])+273.15
x = x*1000/28
y = 10* np.array([6900,8100,9350,10500,11700,12800])
xmodel = np.linspace(np.min(x), np.max(x), 100)

# %% Perform calculations
def yfun(xe, coefs):
    return coefs[0] * xe**1 


# Reshape data for block matrices
xv = np.reshape(x, (-1, 1))
yv = np.reshape(y, (-1, 1))
phi_mat = np.block([[xv**1]])
pvec = np.linalg.lstsq(phi_mat, yv, rcond=None)[0]
print(pvec)

# %% Generate estimates and model
yhat = yfun(x, pvec)
ymodel = yfun(xmodel, pvec)

# %% Calculate statistics
calc_stats(y, yhat, 1)