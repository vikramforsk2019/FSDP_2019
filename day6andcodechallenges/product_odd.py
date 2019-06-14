#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:28:30 2019

@author: vikram
"""


"""
This Python function accepts a list of numbers and computes the product of all the odd numbers:

def productOfOdds(list):
    result = 1
    for i in list:
        if i % 2 == 1:
            result *= i
    return result
    
Rewrite the Python code using map, filter, and reduce:

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))

    
"""
from functools import reduce
my_list=[1,2,3,4,5,6,7]
my_filter_list =filter ( lambda x:x%2==1, my_list)
result=reduce(lambda x,y:x*y,my_filter_list)
print(result)

