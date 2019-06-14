#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 08:14:24 2019

@author: vikram
"""

"""
 Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
     Input:
    Welcome to Pink City Jaipur
  Output:
    Welcome*to*Pink*City*Jaipur
"""
input_str=input('enter a format>')
output_str=input_str.replace(' ','*')
print(output_str)