"""
[chapra_03_09.py]
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


(B,H) = np.meshgrid(np.linspace(0.01,20,40), np.linspace(0.01,5,41))

U = np.sqrt(0.001)/0.02 * (B*H/(B+2*H))**(2/3)

plot = ax.plot_surface(B,H,U, cmap = cm.viridis)
ax.set(xlabel = 'Width $B$, m', ylabel = 'Depth $H$, m', zlabel = 'Velocity $U$, m/s', title = "Velocity Using Manning's Equation")
ax.set_xticks(np.arange(0,25,5))
ax.set_yticks(np.arange(0,6,1))
ax.set_zticks(np.arange(0,4,.5))
ax.view_init(elev=35, azim=-135)
fig.colorbar(plot)
fig.tight_layout()
fig.savefig('chapra_03_09_plot.png')