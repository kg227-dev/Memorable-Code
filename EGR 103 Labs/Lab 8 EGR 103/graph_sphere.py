#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[graph_sphere.py]
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


fig = plt.figure(num=1, clear=True)
fig.set_size_inches(6, 6, forward=True) 
ax = fig.add_subplot(1, 1, 1, projection='3d')

(theta, phi) = np.meshgrid(np.linspace(0,2*np.pi, 40), np.linspace(0,2*np.pi,20))

x = np.sin(phi)*np.cos(theta)
y = np.sin(phi)* np.sin(theta)
z = np.cos(phi)

ax.plot_wireframe(x,y,z, color = 'm')
ax.set_xticks([-1,0,1])
ax.set_yticks([-1,0,1])
ax.set_zticks([-1,0,1])

ax.set(xlabel = 'x', ylabel = 'y', zlabel = 'z')
fig.tight_layout()

fig.savefig('sphere_plot.png')

