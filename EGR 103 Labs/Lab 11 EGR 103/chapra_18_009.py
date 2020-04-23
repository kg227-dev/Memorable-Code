#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[chapra_18_009.py]
[Kush Gulati]
[4/21/2020]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [kg227]
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline

T = np.array([0,8,16,24,32,40])
o = np.array([14.621,11.843,9.870, 8.418, 7.305, 6.413])
Tmodel = np.linspace(T.min(), T.max(), 100)


n = len(T)
poly_fun = np.polyval(np.polyfit(T,o,n-1),Tmodel)
lin_fun = interp1d(T,o,kind='linear')
cs_fun = CubicSpline(T,o)


fig = plt.figure(num=1, clear = True)
ax = fig.add_subplot(1,1,1)
ax.plot(T,o, 'mo', label = 'Data')
ax.plot(Tmodel, lin_fun(Tmodel), 'r-', label = 'Linear')
ax.plot(Tmodel, poly_fun, 'g--', label = 'Polynomial')
ax.plot(Tmodel, cs_fun(Tmodel), 'b:', label = 'Cubic Spline')
ax.legend()
ax.grid(True)
fig.savefig('chapra_18_009_plot.png')

print(lin_fun(27))
print(np.polyval(np.polyfit(T,o,n-1),27))
print(cs_fun(27))