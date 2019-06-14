#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 14:06:56 2019

@author: vikram
"""
"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic2.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      You need to develop using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:if input_num:
    True
"""
list1=[]
input_num=input('enter the numbers>')
value=input_num.split(" ")
list1 = [n==n[::-1] for n in value]
print(list1)
print(any(list1))


"""
list (map(lambda x: True if x % 2 == 0 else False, range(1, 11)))
for i in value: 
  list.append((i[::-1]))
for i in list:
    print(i)
    if i in value:
        list2.append('True')
    else:
        list2.append('False')
print(any(list2))
print(any(value))  
"""