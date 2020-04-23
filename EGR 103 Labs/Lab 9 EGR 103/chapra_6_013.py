#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[chapra_6_013.py]
[Kush Gulati]
[4/14/2020]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [kg227]
"""

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt 

def fun(T):
    return -1.1 + 0.99403+ 1.671*(10**-4)*T + 9.7215*(10**-8)*(T**2)-9.5838*(10**-11)*(T**3)+ 1.9520*(10**-14)*(T**4)

t = np.linspace(0,1200,100)
cp = fun(t)

fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)

ax.plot(t,cp, 'k-')
ax.set(ylabel = 'Zero-Pressure Specific Heat of dry air $c_p$ (kJ/(kg K))', xlabel = 'Temperature (K)', title = "$c_p$ vs Temperature")
ax.grid(True)
fig.tight_layout()
fig.savefig('chapra_6_013_plot.png')


r1 = opt.brentq(lambda xi: fun(xi), 400, 800)
print("Temperature at 1.1: " + str(r1) + " K")