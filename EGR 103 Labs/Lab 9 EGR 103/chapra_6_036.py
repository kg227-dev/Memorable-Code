#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[chapra_06_036.py]
[Kush Gulati]
[4/14/2020]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [kg227]
"""
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt 
k = 1.4
c = np.sqrt(k*287*277.15)
v = 625
M = v/c


def fun(B):
	first = (2*(M**2*(np.sin(B)**2)-1))
	second = (np.tan(B) * M**2*(k+np.cos(2*B)+2))
	return (first/second) - np.tan(4*np.pi/180)

B = np.linspace(2*np.pi/180,88*np.pi/180,100)

f = fun(B)

fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.plot(B,f, 'k-')
ax.set(ylabel = r'$f(\beta_u)$', xlabel = r'$\beta_u$', title = r"$f(\beta_u)$ vs. $\beta_u$")
fig.tight_layout()
fig.savefig('chapra_6_036_plot.png')

beta = opt.brentq(fun, .4, .8)
print(beta)

pressure = 110*((2*k/(k+1)) * (M*np.sin(beta))**2 - ((k-1)/(k+1)))
print(pressure)
