#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:18:22 2019

@author: vikram
"""

"""
# Make a function to find whether a year is a leap year or no, return True or False
"""
def find_year(year_check):
 if(year_check%4==0 and year_check%100!=0) :
   return 'True'
 elif( year_check%400==0 ) :
   return 'True'
 else:
     return 'False'
year_check=int(input('enter a year>'))
year_type=find_year(year_check)
print(year_type)