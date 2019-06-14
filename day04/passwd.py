#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:10:28 2019

@author: vikram
"""
my_dict={}
with open('passwd', mode='rt') as file :
   for line in file:
    value=line.split(":") 
    a=value[0]
    b=value[2]
    
    if a not in my_dict:
        if a[0]!='_':
           my_dict[a]=b
print(my_dict)
for key, value in my_dict.items() :
  print ( key, value )
       
        