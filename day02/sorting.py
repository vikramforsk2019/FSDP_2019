#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 08:05:11 2019

@author: vikram
"""

student_list = []

while True:
    user_input = input("Enter name, age and score: ")
    
    if not user_input:
        break
    
    name, age, marks = user_input.split(",")
    print(name)
    student_list.append( (name, int(age), int(marks) ) )
    #print(student_list)
student_list.sort()
print (student_list)