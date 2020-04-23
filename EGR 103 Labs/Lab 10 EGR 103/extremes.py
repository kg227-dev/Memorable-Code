
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[extremes.py]
[Kush Gulati]
[4/17/2020]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [kg227]
"""
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

def fun1(x,y):
	return 2*(y**2)-2.5*x*y-1.75*y+1.5*(x**2)

def fun2(x,y):
	return (4*x+2*y+x**2-2*(x**4)+3*x*y-3*(y**2))*-1

def fun3(x,y):
	return -8*x+x**2+14*y+4*(y**2)-2*x*y

min_loc1 = opt.fmin(lambda vec: fun1(vec[0], vec[1]), [0, 0])
print(min_loc1)

max_loc2 = opt.fmin(lambda vec: fun2(vec[0], vec[1]), [0, 0])
print(max_loc2)

min_loc3 = opt.fmin(lambda vec: fun3(vec[0], vec[1]), [0, 0])
print(min_loc3)

