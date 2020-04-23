#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[chapra_15_6.py]
[Kush Gulati]
[4/10/2020]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [kg227]
"""

import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm



data = np.loadtxt("chapra_p15_5.dat")

c = data[:,0].copy()
T = data[:,1].copy()
OC = data[:,2].copy()

OCm= np.reshape(OC, (7,3))
Cm = np.reshape(c, (7,3))
Tm = np.reshape(T, (7,3))

xmodel, ymodel = np.meshgrid(np.linspace(c.min(), c.max(),7), np.linspace(T.min(),T.max(),19))


def zfun(xe,ye,coefs):
    return coefs[0] + coefs[1] * xe + coefs[2] * ye**3 + coefs[3] * ye**2 + coefs[4]* ye

xv = np.reshape(c, (-1, 1))
yv = np.reshape(T, (-1, 1))
zv = np.reshape(OC, (-1, 1))
phi_mat = np.block([[xv**0, xv, yv**3, yv**2, yv]])
pvec = np.linalg.lstsq(phi_mat, zv, rcond=None)[0]
print("Coefficients:")
print("A:    {:0.4e}".format(float(pvec[0])))
print("B:    {:0.4e}".format(float(pvec[1])))
print("C:    {:0.4e}".format(float(pvec[2])))
print("D:    {:0.4e}".format(float(pvec[3])))
print("E:    {:0.4e}".format(float(pvec[4])))


zhatv = zfun(xv, yv, pvec) # for stats
zhatm = zfun(c, T, pvec) # for graphics
zmodelm = zfun(xmodel, ymodel, pvec)

zestimates = zfun(c,T, pvec)
zestimatesm = np.reshape(zestimates, (7,3))

resids = OCm - zestimatesm 


fig = plt.figure(num=1, clear= True)
fig.set_size_inches(6, 4, forward=True) 
ax = fig.add_subplot(1,1,1, projection = '3d')
ax.plot_surface(xmodel, ymodel, zmodelm, cmap = cm.viridis)
ax.set(ylabel = '$T$, $^\circ$C', xlabel = '$c$, g/L', zlabel = '$OC$, mg/L')
ax.view_init(elev=5, azim=45)
ax.set_xticks([0,10,20])
ax.set_yticks([0,5,10,15,20,25,30])
fig.tight_layout()
fig.savefig('chapra_15_7_plot.png')


fig2 = plt.figure(num=2, clear= True)
fig2.set_size_inches(6, 4, forward=True) 
ax2 = fig2.add_subplot(1,1,1, projection = '3d')
ax2.plot_surface(Cm,Tm,resids, cmap = cm.magma)
ax2.set(ylabel = '$T$, $^\circ$C', xlabel = '$c$, g/L', zlabel = 'Residual, mg/L')
ax2.set_xticks([0,10,20])
ax2.set_yticks([0,5,10,15,20,25,30])
fig2.tight_layout()
fig2.savefig('chapra_15_7_plot2.png')


estimate= zfun(15,12,pvec)
print("Estimate Value: {:0.4}".format(float(estimate)))
percent_error = (estimate-9.09)/9.09*100
print("Percent Error: {:0.3}%".format(float(percent_error)))

from lab7_common import calc_stats
calc_stats(zv,zhatv,1)