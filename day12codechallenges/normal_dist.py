#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 17:36:47 2019

@author: vikram
"""


"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""
import numpy as np
incomes = np.random.normal(150.0, 20.0, 1000)
print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))
print("Standard Deviation is: ", np.std(incomes))
print("Varience:",(np.std(incomes))**2)
#print (incomes)

import matplotlib.pyplot as plt
plt.hist(incomes, 100)
plt.show()
 
plt.boxplot(incomes)