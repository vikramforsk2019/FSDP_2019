#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 21:58:11 2019

@author: vikram
"""
final_list2=[]
final_list=[]
str1=""
import re
while True:
        input_num=input('enter the emails>')
        if input_num:
            final_list.append(input_num)
        if not input_num:
                        break
for li in final_list:
    result=re.findall(r'\w+[_-]?\w*\@\w+\.\w{2,4}',li)
    a=str1.join(result)
    final_list2.append(a)
print(sorted(final_list2))

