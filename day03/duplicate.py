#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:24:43 2019

@author: vikram
"""
final_list=[]
list1= [12,24,35,24,88,120,155,88,120,155]
 
for i in list1:
    if i not in final_list:
        final_list.append(i)
print(final_list)        
    