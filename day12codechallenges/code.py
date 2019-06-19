#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:48:08 2019

@author: vikram
"""


# Hands On 

# Find the mean, median, mode, and range for the following list of values:
# 13, 18, 13, 14, 13, 16, 14, 21, 13


#Answer : Mean = 15, Median = 14 , Mode = 13 , Range = 21 - 13 = 8

import numpy as np

                           #mean, sd, total
income = [13,18,13,14,16,21,13]

incomes = np.array( income ) 

print (type(incomes))
print (incomes.size)
print (incomes)
print (len(incomes))
print (incomes.ndim)
print (incomes.shape)
print (incomes.dtype)

print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))
print("Standard Deviation is: ", np.std(incomes))

from scipy import stats
print("Mode value is: ", stats.mode(incomes)[0])
 
print("Minimum value is: ", np.min(incomes))
print("Maximum value is: ", np.max(incomes))
