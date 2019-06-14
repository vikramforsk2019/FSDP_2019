#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 22:15:21 2019

@author: vikram
"""
import re
with open('simpsons_phone_book.txt',mode='rt') as file:
    for line in file:
        if line[0]=='J':
         if re.findall(r'(Neu)',line):
          print(line)
    