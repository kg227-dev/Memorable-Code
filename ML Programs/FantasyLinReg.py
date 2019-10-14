#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 01:11:26 2019

@author: kushgulati
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
#matplotlib inline

dataset = pd.read_csv('train75.csv')
print(dataset.shape)
print(dataset.describe())



