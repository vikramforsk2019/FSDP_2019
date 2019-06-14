#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 07:10:18 2019

@author: vikram
"""

"""
 Problem Statement:
    Take first and last name in single command from the user and print  
    them in reverse order with a space between them, 
    find the index using find/index function and then print using slicing concept of the index
"""

input_str=input('input fist and last name>')
reverse_str=input_str [::-1]
print(reverse_str) 
print("index of s:",input_str.index('s'))
newstr = "    "+input_str+"    "


print("right slicing:",newstr.rstrip())

print("left slicing:",newstr.lstrip())