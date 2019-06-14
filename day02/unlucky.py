#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:03:28 2019

@author: vikram
"""
count=0
i=0
input_num= input('enter the numbers>').split()
print(input_num)
while i<len(input_num):
 b=int(input_num[i-1])
 a=int(input_num[i])
 if a==13: 
     i+=2
 elif(b==13):
      i-=1
 else:
     i+=1
     count+=a
 
    
print(count)