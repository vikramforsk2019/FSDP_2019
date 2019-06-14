#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:44:04 2019

@author: vikram
"""

"""
Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      *
"""
column=1
x=int(input('enter the columns>'))
for i in range(1,2*x,1) :
   for j in range(1,column,1) :
      print('*',end=" ")
   if(i<x) :
    column+=1
   else:
       column-=1
   print('\n')
          
   
   """"
   def pypart(n): 
    myList = [] 
    for i in range(1,n+1): 
      if i<n:
         myList.append("*"*i) 
        #print(myList)
         print("\n".join(myList)) 
      else :
       for i in range(n+1,1,-1):    
           myList.append("*"*i) 
        #print(myList)
           print("\n".join(myList))
# Driver Code 
n = 5
pypart(n) 
"""