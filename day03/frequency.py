#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 09:30:25 2019

@author: vikram
"""
my_dict={}
input_str=input('enter a string>')
print(input_str)
for item,value in enumerate(input_str):
    if value not in my_dict:
        my_dict[value]=1
    else:
        my_dict[value]+=1
print(my_dict)