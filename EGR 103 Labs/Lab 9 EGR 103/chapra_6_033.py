#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[chapra_06_033.py]
[Kush Gulati]
[4/14/2020]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [kg227]
"""
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt 

def fun(t):
	return -15+ 77* np.exp(-1.5*t) + 20 * np.exp(-.08*t)

r1 = opt.brentq(fun, 0,40)
print(r1)