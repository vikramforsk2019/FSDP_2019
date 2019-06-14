#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:02:34 2019

@author: vikram
"""

tuple2=('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
print(tuple2)
input_day= input('enter days name>').split()
for day in tuple2:
    if(day not in input_day ):
        input_day.append(day)
tuple1=tuple(input_day)   
print(tuple1)
#print(final_tuple)
   