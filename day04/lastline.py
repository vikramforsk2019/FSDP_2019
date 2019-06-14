#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:02:28 2019

@author: vikram
"""
list=[]
input_str=input('enter a file name>')
print(input_str)
with open(input_str, mode='rt') as file :
   for line in file:
       list.append(line)
print(list[-1])