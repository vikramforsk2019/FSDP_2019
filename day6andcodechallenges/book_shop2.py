#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 09:11:23 2019

@author: vikram
"""


"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop2.py
  Problem Statement:
    The same bookshop, but this time we work on a different list.
    
    The sublists of our lists look like this:
    [ordernumber, (article number, quantity, price per unit), 
    ... (article number, quantity, price per unit) ]
       
    [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
    
   Write a program which returns a list of list with 
    [order number, total amount of order].
    
   Write a Python program, You need to write a solution without using lambda,map,list comprehension first and then with lambda,map,reduce
      
  Hint: 
    use lambda, map and reduce concept to solve the problem  
    from functools import reduce
    
  Input:
      orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
                 [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
                 [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
                 [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] 
               ]
     
  Output:
       [[1, 678.33], [2, 494.46], [3, 364.8], [4, 492.57]]     

"""
list2=[]
sum1=0
orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
                 [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
                 [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
                 [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)]]
      
for i in orders:
    order=i[0]
    a=i[1:]
    for j in a:
        b=j[1]*j[2]
        sum1+=b 
    list2.append([order,sum1])
    sum1=0
    
   
   