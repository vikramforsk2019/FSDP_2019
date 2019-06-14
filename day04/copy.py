#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:01:07 2019

@author: vikram
"""


with open('words.txt', mode='rt') as file :
 with open('new.txt',mode='wt') as w_file:
   for line in file:
      w_file.write(line)
      