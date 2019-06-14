#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:37:50 2019

@author: vikram
"""

"""

  Problem Statement:
    Convert to uppercase character
    Convert to lower character 
    Convert to CamelCase or TitleCase.
  Hint: 
    Try to find some function in the str class and see its help on how to use it.
    Using dir and help functions
  Input:
    Take the name as input from the keyboard. ( SyLvEsTeR )
"""
#import str
#dir(str)
help(str.upper)
x=input('enter a string')
print(x.upper())
print(x.lower())
print(x.title())