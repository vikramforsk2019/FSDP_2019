#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 14:29:40 2019

@author: vikram
"""

input_num= input('enter the numbers>').split()
print(input_num)
user_list = []
for i in input_num:
    user_list.append(int(i))
print(sorted(input_num))
user_list.sort()
#print(user_list[1:-1])
final_list=user_list[1:-1]
# Calculating average
average = sum( final_list ) / len( final_list )

print ("Average is :", int( average ))