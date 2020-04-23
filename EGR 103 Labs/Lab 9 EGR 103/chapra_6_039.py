#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[chapra_06_039.py]
[Kush Gulati]
[4/14/2020]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [kg227]
"""
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt 

g = 9.81
h = 24
L = 65
d = 100
Leed = 30
Levd = 8
E_d = 0.005
K = 0.5
mu_density = 1.2 * 10**(-6)

def calc_re(V):
	return (1/mu_density)*V*(d/1000)

def calc_G(V):
	f = opt.fsolve(lambda f: (1/np.sqrt(f))+2*np.log10(((1/3.7)*E_d)+(2.51/(calc_re(V)*np.sqrt(f)))),0.05)
	return f 

def fun(v):
	return calc_G(v)*(((L+h)/(d/1000)) + Leed + Levd) * ((v**2)/2) + K*((v**2)/2) - g*h + ((v**2)/2)

v = opt.fsolve(lambda v: fun(v),1)
A_val = np.pi *(50/1000)**2
Q = v*A_val	

print(Q)

