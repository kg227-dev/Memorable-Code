import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1, projection='3d')

x = np.array([[1, 3], [2, 4]])
y = np.array([[5, 6], [7, 8]])
z = np.array([[9, 12], [10, 11]])

ax.plot_surface(x, y, z)
ax.set(xlabel='x', ylabel='y', zlabel='z')

fig.tight_layout()
fig.savefig('PatchExOrig_py.png')