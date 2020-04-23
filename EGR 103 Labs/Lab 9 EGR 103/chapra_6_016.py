#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[chapra_06_016.py]
[Kush Gulati]
[4/14/2020]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [kg227]
"""


import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt 
 
def fun(h):
    return -8+ (25*np.arccos((5-h)/5) - (5-h)*np.sqrt(10*h-h**2))*5

h  = np.linspace(0.2,0.8, 1000)
V= fun(h)

fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.plot(h,V, 'k-')
ax.set(ylabel = 'Volume of Liquid $V$', xlabel = 'Depth of Liquid $h$', title = "Volume vs. Depth of Liquid in Cylinder")
fig.tight_layout()
fig.savefig('chapra_6_016_plot.png')

r1 = opt.brentq(lambda xi: fun(xi), 0.5, 0.6)
print("H when V=8,L=5,r=5: " + str(r1))
