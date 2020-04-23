#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[chapra_7_016.py]
[Kush Gulati]
[4/17/2020]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [kg227]
"""

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

q=75
rw = 0.006
k=0.17
h=12
Tair = 293
def fun(ri):
	return Tair + ((q/(2*np.pi))*((1/k)*np.log((rw+ri)/rw)+((1/h)*(1/(rw+ri)))))

ri = np.linspace(0.001,0.012,1000)

T = fun(ri)

fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.plot(ri,T, 'k-')
ax.grid(True)
ax.set(ylabel = 'Temperature $T$ (in K)', xlabel = 'Thickness of Insulation $r_i$ (in m)', title = 'Wire Steady-state Temperature vs. Thickness of Insulation')
fig.tight_layout()
fig.savefig('chapra_7_016_plot.png')

out1 = opt.fminbound(fun,0.006,0.012, full_output = True)
print(out1)

out2 = opt.fmin(fun,0.008)
print(out2)