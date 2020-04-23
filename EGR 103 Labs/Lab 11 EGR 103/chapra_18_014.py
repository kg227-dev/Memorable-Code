#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[chapra_18_014.py]
[Kush Gulati]
[4/21/2020]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [kg227]
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from scipy.interpolate import interp2d

x = np.linspace(-2,0,9)
y = np.linspace(0,3,9)

xm, ym = np.meshgrid(x,y)

def fun(x,y):
    return 2+x-y+2*(x**2)+2*x*y+y**2

Tm = fun(xm,ym)

Tinterp = interp2d(x,y,Tm, kind = 'linear')
Tinterp_spline = interp2d(x,y,Tm, kind = 'cubic')

print(fun(-1.63,1.627))
print(Tinterp(-1.63,1.627))
print(Tinterp_spline(-1.63,1.627))

zmodelf = Tinterp(x,y)
zmodelm = zmodelf.reshape(9, 9)


fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_wireframe(xm, ym, zmodelm)
ax.set(xlabel="x", ylabel="y", zlabel="Temperature (T)")
ax.scatter(xm, ym, Tm, color='b', linewidth=12)

ax.scatter(-1.63, 1.627, Tinterp(-1.63,1.627), color='g', linewidth=12)