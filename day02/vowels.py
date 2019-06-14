#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:43:24 2019

@author: vikram
"""




final_list=[]
state_name= input('enter a state name>').split()  #create input number list
vowels=tuple('aeiouAEIOU')

for state in state_name: 
    temp_list=[]
    for char in state:
      if char not in vowels:
          temp_list.append(char)
    final_list.append("".join(temp_list))

print(final_list)