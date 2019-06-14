#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:11:59 2019

@author: vikram
"""

"""

#  Print all the even numbers from 1 to 10 using while True loop
"""
first=1
last_num=input('enter the number>')
num=int(last_num)
while(True) :
  rem=first%2

  if ( rem==0 ) :
    print(first)
  first+=1    
  if (first>num) :
      break
    