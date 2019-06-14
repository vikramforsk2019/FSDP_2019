#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:36:50 2019

@author: vikram
"""

"""
 Make a function days_in_month to return the number of days in a specific month of a year
"""
import leap_year
def days_in_month(month):
    list1=['january','march','may','july','august','octomber','december']
    list2=['april','june','september','november']
    list3=['february']
    if (month in list1):
       return '31'
    elif (month in list2):
       return '30'
    elif(month in list3):
       print(leap_year.find_year(2000))
       if(leap_year.find_year(2000)=='True'):
           return '28'
       else:
           return '29'
    else:
         return 'invalid month'
month_name=input('enter a month>')
day=days_in_month(month_name)
print(day)