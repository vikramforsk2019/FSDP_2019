#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:13:27 2019

@author: vikram
"""
"""

{"a" : 2, "b" : 15, "c" : 13}
"""

def fix_teen(my_dict):
    
    sum1=0
    for age in my_dict.values():
        if int(age) in [13,14,17,18,19]:
            continue
        else:
            sum1+=int(age)
    return (sum1)

my_dict = {}
while True:
    user_input = input("Enter values >")
    
    #append this entry to other data structure
    value=user_input.split(" ")
    if user_input:
            if ' '.join(value[:-1]) not in my_dict:
             my_dict[' '.join(value[:-1])]=value[-1]
    if not user_input:
        break
result = fix_teen(my_dict)
print(result)

    
    