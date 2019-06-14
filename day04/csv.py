#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 07:08:18 2019

@author: vikram
"""
my_dict={}
import csv
with open("passwd") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=":")
    print(csv_reader)
    for row in csv_reader:
     a=row[0]
     b=row[2]
     if a not in my_dict:
        if a[0]!='_':
           my_dict[a]=b  
#print(my_dict)

for key, value in my_dict.items() :
  #print ( key, value )
  with open('data.csv', mode='a') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=' ')
        print(key,value)
        employee_writer.writerow([key,value])
   