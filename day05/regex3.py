#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:08:58 2019

@author: vikram
"""

final_list=[]
import re
input_num=input('enter a  credit card number>').split(",")
for li in input_num:
  result=re.match(r'(^[456]\d{15})|(^[4-6]\d{3}-\d{4}(-\d{4}){2})',li)
  print(result)
  cong=result.replace("-"," ")
  print(cong)
  re.search('\d\1{3,}',cong)
  
 # final_list.append(result)

     