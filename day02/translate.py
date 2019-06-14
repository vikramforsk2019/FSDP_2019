#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 07:52:48 2019

@author: vikram
"""

def translate_fun(input_str):
    for i in input_str:
        if(i==' '):
            print(' ',end="")
        elif(i not in ['a','e','i','o','u']):
         print(i+'o'+i,end="")
       
        else:
            print(i,end="")
input_str=input("enter numbers>")
translate_fun(input_str)