#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 21:04:54 2019

@author: vikram
"""
def multiply(input_str):
    sum1=1
    for i in input_str:
     sum1*=int(i)
    return sum1 
def add(input_str):
    sum1=0
    for i in input_str:
     sum1+=int(i)
    return sum1
def max_num(input_str):
    max_num=0
    for i in input_str:
        if(int(i)>max_num):
            max_num=int(i)
    return max_num
def min_num(input_str):
    mix_num=int(input_str[0])
    for i in input_str:
        if(int(i)<mix_num):
            mix_num=int(i)
    return mix_num
def sorting(input_num):
                          pass
                          """
                          for i in range(0,len(input_num)):
                         for j in range(0,len(input_num)):
                         if(input_num[i]<input_num[j]):
                            input_num=input_num[i]
                         return input_num
                         """ 
def duplicate(input_num):
    new_list=[]
    for i in input_num:
        if(i not in new_list ):
            new_list.append(i)
    return new_list
input_num=input("enter numbers>").split()
print(add(input_num))
print(multiply(input_num))
print(max_num(input_num))
print(min_num(input_num))
print(sorting(input_num))
print(duplicate(input_num))
