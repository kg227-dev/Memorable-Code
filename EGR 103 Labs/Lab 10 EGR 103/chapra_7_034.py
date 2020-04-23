#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[chapra_7_034.py]
[Kush Gulati]
[4/17/2020]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [kg227]
"""

import numpy as np
import scipy.optimize as opt

def fun(s):
    return -1* ((15*s*(1-s)) / ((1-s)*(4*s**2 - 3*s +4 )))

out1 = opt.fminbound(fun,.5,3, full_output = True)
print(out1)

out2 = opt.fmin(fun,2)
print(out2)