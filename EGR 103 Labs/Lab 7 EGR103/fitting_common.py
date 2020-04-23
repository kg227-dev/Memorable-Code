#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 20:43:32 2020

@author: kushgulati
"""


import numpy as np
import matplotlib.pyplot as plt


def get_beam_data():
    # Load data from Cantilever.dat
    beam_data = np.loadtxt("Cantilever.dat")
    # Copy data from each column into new variables
    mass = beam_data[:, 0].copy()
    disp = beam_data[:, 1].copy()
    # Convert mass to force
    force = mass * 9.81
    # Convert disp to meters
    disp = (disp * 2.54) / 100

    fmodel = np.linspace(np.min(force), np.max(force), 100)

    # Return values
    return force, disp, fmodel


def calc_stats(y, yhat, to_print=1):
    # Calculate statistics
    st = np.sum((y - np.mean(y)) ** 2)
    sr = np.sum((y - yhat) ** 2)
    r2 = (st - sr) / st
    if to_print:
        print("st: {:.3e}\nsr: {:.3e}\nr2: {:.3e}".format(st, sr, r2))
    return st, sr, r2


def make_plot(x, y, yhat, xmodel, ymodel, fig_num=1):
    fig, ax = plt.subplots(num=fig_num, clear=True)
    ax.plot(x, y, "ko", label="Data")
    ax.plot(x, yhat, "ks", label="Estimates", mfc="none")
    ax.plot(xmodel, ymodel, "k-", label="Model")
    ax.grid(True)
    ax.legend(loc="best")
    fig.tight_layout()
    return fig, ax