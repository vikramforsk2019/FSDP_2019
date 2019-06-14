#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:26:23 2019

@author: vikram
"""

"""
Problem Statement:
    Find the factorial of a number. 
  Hint: 
    Factorial of 3 = 3 * 2 * 1= 6 
    Try to first find the function from math module using dir and help 
  Input:
    Take the number from the keyboard as input from the user
"""
import math 

dir( math )
help(math.factorial)
x=input("enter a number")
y=int(x)
print(math.factorial(y))