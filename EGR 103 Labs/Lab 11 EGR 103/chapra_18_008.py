#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[chapra_18_008.py]
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

x = np.array([1.8,2,2.2,2.4,2.6])
J1 = np.array([0.5815, 0.5767, 0.556, 0.5202, 0.4708])
xmodel = np.linspace(x.min(),x.max(),100)

n = len(x)
poly_fun = np.polyval(np.polyfit(x,J1,n-1),xmodel)
cs_fun = CubicSpline(x,J1)




fig = plt.figure(num=1, clear = True)
ax = fig.add_subplot(1,1,1)
ax.plot(x,J1, 'mo', label = 'Data')
ax.plot(xmodel, poly_fun, 'r-', label = 'Polynomial')
ax.plot(xmodel, cs_fun(xmodel), 'b--', label = 'Cubic Spline')
ax.legend()
ax.grid(True)
fig.savefig('chapra_18_008_plot.png')

print(np.polyval(np.polyfit(x,J1,n-1),2.1))
print(cs_fun(2.1))