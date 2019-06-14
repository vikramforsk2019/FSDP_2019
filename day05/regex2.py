#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:23:24 2019

@author: vikram
"""
"""
list convert into a string

str1=""

final_list=[]
 a=str1.join(result)
 
 final_list.append(a)
 
 """
final_list=[]
str1=""
import re
input_num=input('enter a  emailid>').split(",")
for li in input_num:
  result=re.findall(r'\w+[_-]?\w*\@\w+\.\w{2,4}',li)
  a=str1.join(result)
  final_list.append(a)
  print(a)
print(sorted(final_list))



