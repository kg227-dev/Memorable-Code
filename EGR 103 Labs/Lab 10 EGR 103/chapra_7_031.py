#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[chapra_7_031.py]
[Kush Gulati]
[4/17/2020]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [kg227]
"""

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

os = 10
kd = 0.1
ka = 0.6
ks = 0.05
Lo = 70
Sb = 1

def fun(t):
    return os - ((kd*Lo)/(kd+ks-ka)) * (np.exp(-1*ka*t)-np.exp(-1*(kd+ks)*t)) - (Sb/ka) * (1-np.exp(-1*ka*t))

t = np.linspace(0,20,1000)

o = fun(t)
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)
ax.plot(t,o, 'k-')
ax.grid(True)
ax.set(ylabel = 'Dissolved Oxygen Concentration $o$ (mg/L)', xlabel = 'Time (days)', title = 'Dissolved Oxygen Concentration in a River Over Time')
fig.tight_layout()
fig.savefig('chapra_7_031_plot.png')

out1 = opt.fminbound(fun,2.5,7.5, full_output = True)
print(out1)

out2 = opt.fmin(fun,5)
print(out2)