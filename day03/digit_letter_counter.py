#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:42:56 2019

@author: vikram
"""
count=0
user_input =input("Enter values >")
letter,digit=user_input.split(" ")
for i in  digit:
               if int(i) in [0,1,2,3,4,5,6,7,8,9]:
                   count+=1
print("letter ",len(letter))
print("digits ",count)                