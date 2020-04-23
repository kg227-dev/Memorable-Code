#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[chapra_06_014.py]
[Kush Gulati]
[4/14/2020]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [kg227]
"""

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt 

def fun(x):
    return -0.05+ (x/(1-x)) * np.sqrt((2*3)/(2+x))

x  = np.linspace(0,0.05, 1000)
K = fun(x)

fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.plot(x,K, 'k-')
ax.set(ylabel = 'Equilibrium Constant $K$', xlabel = 'Mole fraction $x$ of $H_2O$', title = "Reaction Equilibrium Constant vs Mole Fraction of $H_2O$")
fig.tight_layout()
fig.savefig('chapra_6_014_plot.png')

r1 = opt.brentq(lambda xi: fun(xi), 0.01, 0.04)
print("X when K=0.05: " + str(r1))

