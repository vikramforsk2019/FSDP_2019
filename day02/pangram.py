#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:22:01 2019

@author: vikram
"""

"""
Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
"""
input_str=input('enter a string sentence>')
match_list = []
alpha_str = 'qwertyuioplkjhgfdsazxcvbnm'
for i in alpha_str:
    if i in input_str:
        match_list.append(i) #create list with maching value
        print(match_list)
if(len(match_list)==26):
    print('Panagaram')
else:
    print('Not Pangaram')
         