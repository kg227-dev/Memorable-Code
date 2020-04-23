"""
[chapra_02_22.py]
[Kush Gulati]
[4/10/2020]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [kg227]
"""

import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure(num=1, clear= True)
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2, projection = '3d')

fig.set_size_inches(6, 8, forward=True) 

t =np.arange(0,6 *np.pi, np.pi/64)


x = t* np.cos(6*t)
y = t* np.sin(6*t)

ax1.plot(x,y,'r-')
ax1.grid(True)
ax1.set(xlabel = 'x', ylabel = 'y')
ax1.axis('equal')

ax2.plot(x, y, t, 'c-')
ax2.set_xticks([-20,0,20])
ax2.set_yticks([-20,0,20])
ax2.set_zticks([0,10,20])
ax2.set_zlim(0,20)
ax2.set(xlabel = 'x', ylabel = 'y', zlabel = 'z')

fig.tight_layout()
fig.savefig('chapra_02_22_plot.png')

