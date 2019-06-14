#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:31:12 2019

@author: vikram
"""

#item_name = { 'BANANA FRIES':12, 'POTATO CHIPS':30, 'CANDY':11,'CANDY':21 }
"""
 BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    """
my_dict = {}
while True:
    user_input = input("Enter values >")
    
    #append this entry to other data structure
    value=user_input.split(" ")
    print(value)
    if user_input:
            if ' '.join(value[:-1]) not in my_dict:
             my_dict[' '.join(value[:-1])]=value[-1]
            else:
             my_dict[' '.join(value[:-1])]=int(my_dict[' '.join(value[:-1])])+int(value[-1])
    if not user_input:
        break
