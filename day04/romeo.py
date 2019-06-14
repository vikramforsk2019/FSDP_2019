#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:35:01 2019

@author: vikram
"""
list=[]
my_dict={}
with open('romeo.txt', mode='rt') as file :
   for line in file:
    value=line.split(" ")
    #print(value)
    for values in value: 
        if values not in my_dict:
           my_dict[values]=1
        else:
           my_dict[values]+=1
print(my_dict)