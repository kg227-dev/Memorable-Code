#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[chapra_15_5.py]
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

fig = plt.figure(num=1, clear= True)
ax = fig.add_subplot(1,1,1, projection = '3d')
fig.set_size_inches(6, 4, forward=True) 

data = np.loadtxt("chapra_p15_5.dat")

c = data[:,0].copy()
T = data[:,1].copy()
OC = data[:,2].copy()

c = np.reshape(c, (7,3))
T = np.reshape(T, (7,3))
OC = np.reshape(OC, (7,3))


ax.plot_surface(c,T,OC, cmap = cm.Blues) 
ax.set(ylabel = '$T$, $^\circ$C', xlabel = '$c$, g/L', zlabel = '$OC$, mg/L')
ax.set_xticks([0,10,20])
ax.set_yticks([0,5,10,15,20,25,30])
ax.view_init(elev=21, azim=-7)
fig.tight_layout()
fig.savefig('chapra_15_5_plot.png')