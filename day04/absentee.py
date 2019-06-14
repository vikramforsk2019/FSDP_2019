#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:07:23 2019

@author: vikram
"""
"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""
file=open('absentee.txt',mode='wt') 
for i in range(25):
        user_input=input('enter the student name>')
        if not user_input:
            break
        file.write(user_input)
        file.write("\n")
       
with open('absentee.txt', mode='rt') as file :
 print(file.readlines())      