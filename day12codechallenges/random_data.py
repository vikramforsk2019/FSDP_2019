#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:06:00 2019

@author: vikram
"""

"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class and also bincount
      
      
"""
from collections import Counter
import numpy as np 
x = np.random.randint(5,15,40) # try with float16,float32,float64
p=Counter(x)
num = np.bincount(x).argmax()
print(num)


from scipy import stats
print("Mode value is: ", stats.mode(x)[0])