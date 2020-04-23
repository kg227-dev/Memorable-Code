#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[chapra_06_017.py]
[Kush Gulati]
[4/14/2020]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [kg227]
"""

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt 

def fun(TA):
    return -15+ TA/10 * np.cosh(500/TA) + 8 - TA/10

TA_root = opt.fsolve(fun, 1000)
print(TA_root)

def plot(x):
    return TA_root/10* np.cosh(10*x/TA_root) + 8 - TA_root/10

x = np.linspace(-50,100,1000)
y = plot(x)
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.plot(x,y, 'k-')
ax.set(ylabel = 'Height of Cable, $y$', xlabel = 'Distance, $x$', title = "Height of Caternary Cable vs. Distance")
fig.tight_layout()
fig.savefig('chapra_6_017_plot.png')