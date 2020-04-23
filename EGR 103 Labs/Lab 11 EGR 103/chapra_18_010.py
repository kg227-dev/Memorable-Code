#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[chapra_18_010.py]
[Kush Gulati]
[4/21/2020]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [kg227]
"""

import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import CubicSpline

x = np.array([0,2,4,7,10,12])
y = np.array([20,20,12,7,6,6])


cs_fun = CubicSpline(x,y)
cs_fun_clamped = CubicSpline(x,y, bc_type = 'clamped')


print(cs_fun(1.5))
print(cs_fun_clamped(1.5))

xmodel = np.linspace(x.min(), x.max(), 100)

fig = plt.figure(num=1, clear = True)
ax = fig.add_subplot(1,1,1)
ax.plot(x,y, 'mo', label = 'Data')
ax.plot(xmodel, cs_fun(xmodel), 'r-', label = 'Cubic Spline')
ax.plot(xmodel, cs_fun_clamped(xmodel), 'b:', label = 'Clamped')



ax.legend()
ax.grid(True)
fig.savefig('chapra_18_010_plot.png')