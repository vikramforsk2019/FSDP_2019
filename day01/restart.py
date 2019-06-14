#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:02:56 2019

@author: vikram

"""
"""
 Problem Statement:
    In a hardcoded string RESTART, replace all the R with $ except the first occurrence and print it.
"""

input_str=input('enter string>')
avoid_first_char=input_str[ 1: ]
print(input_str[0]+avoid_first_char.replace('R','$'))