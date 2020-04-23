# -*- coding: utf-8 -*-
"""
Python version of Chapra Example 14.2
From: Applied Numerical Methods with MATLAB
      for Engineers and Scientists, 4th ed
      Steven C. Chapra
      McGraw-Hill 2018
@author: DukeEgr93
v. 1.0, 10/20/2018
"""

import numpy as np
import matplotlib.pyplot as plt

n = 1000
t = 4
m = 68.1
g = 9.81
cd = 0.25
cdmin = cd - 0.025
cdmax = cd + 0.025
# Note - can put low and high in np.random.uniform!
cdrand = np.random.uniform(cdmin, cdmax, size=(n, 1))
meancd = np.mean(cdrand)
stdcd = np.std(cdrand, ddof=1) # to divide by N-1 vs N
Deltacd = (np.max(cdrand) - np.min(cdrand)) / meancd / 2 * 100
print('{:.4f} {:.4f} {:.4f}'. format(meancd, stdcd, Deltacd))

plt.figure(1)
plt.clf()

plt.subplot(2, 1, 1)
plt.hist(cdrand)
plt.title('(a) Distribution of drag')
plt.xlabel('cd (kg/m)')

vrand = np.sqrt(g * m / cdrand) * np.tanh(np.sqrt(g * cdrand / m) * t)
meanv = np.mean(vrand)
Deltav = (np.max(vrand) - np.min(vrand)) / meanv / 2 * 100
print('{:.4f} {:.4f}'. format(meanv, Deltav))

plt.subplot(2, 1, 2)
plt.hist(vrand)
plt.title('(b) Distribution of velocity')
plt.xlabel('v (m/s)')

plt.tight_layout() # Corrects subplot label overlap