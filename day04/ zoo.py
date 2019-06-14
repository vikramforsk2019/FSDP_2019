#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:04:51 2019

@author: vikram
"""

"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""
import csv
def function_read(input_file):
 with open(input_file) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print ( row )
input_file=input('enter the csv file name>')    
function_read(input_file)