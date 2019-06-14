#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:07:36 2019

@author: vikram
"""

"""
Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
"""
"""
list=[]
while True :
  num=input('enter a number>')
  list.append(num)
  print(list)
  num2=num [ ::-1 ] 
  print(num2)
  if num2 in list:
     print('True')
  else:
      print('False')
  if not num:
     break
"""
count=0
input_num= input('enter a number>').split()  #create input number list
print(input_num)
for i in range(len(input_num)) :
  reverse_num=input_num[i][ ::-1 ]  #take reverse each element one by one
  count+=1
  if(reverse_num in input_num) :
      print('True')
      break
      
if(count>len(input_num)):
 print(len(input_num))
 print("False")     
      
  
    
 