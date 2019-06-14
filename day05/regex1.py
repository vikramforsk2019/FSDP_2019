#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:42:22 2019

@author: vikram
"""
import re
input_num=input('enter a  float number>').split(",")
for li in input_num:
 if re.findall(r'^[+-]?\d*\.\d*',li):
     print('True')
 else:
     print('False')
 
