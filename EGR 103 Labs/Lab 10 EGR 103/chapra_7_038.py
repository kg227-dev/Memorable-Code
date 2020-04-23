#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[chapra_7_038.py]
[Kush Gulati]
[4/17/2020]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [kg227]
"""


import numpy as np
import scipy.optimize as opt

A=55
def perimeter(w,d):
    theta = np.arctan2(d**2,w*d - A)
    return w - 2*d/np.tan(theta) + 2*d/np.sin(theta)

out = opt.fmin(lambda vec: perimeter(vec[0],vec[1]), [10,5])
print(out)
 
w,d = out

theta = np.arctan2(d**2, w*d - A)

print(np.degrees(theta))
    