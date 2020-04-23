#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[chapra_7_036.py]
[Kush Gulati]
[4/17/2020]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [kg227]
"""


import numpy as np
import scipy.optimize as opt

def fun(x):
    return -1* ((0.3)/np.sqrt(1+x**2) - np.sqrt(1+x**2)*(1 - (0.3)/(1+ x**2)) + x)

out1 = opt.fminbound(fun,0,4, full_output = True)
print(out1)

out2 = opt.fmin(fun,2)
print(out2)