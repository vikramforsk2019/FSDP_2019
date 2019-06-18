#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:04:21 2019

@author: vikram
"""
"""
Code Challenge ( Bar Plot )
  Name: 
    Zoo Visualisation
  Filename: 
    zoo_visual.py
  Problem Statement:
    Read the zoo.csv file
    Print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    Show the total number of water needs by individual animal using a Bar Chart
  Hint:
      Use the concept of Dictionary
import csv
zoo_data = {}
with open('zoo.csv','rt') as ani:
    reader = csv.reader(ani,delimiter = ',')
    next(reader)
    for i in reader:
        if i[0] in zoo_data:
            zoo_data[i[0]] += int(i[2])
        else:
            zoo_data[i[0]] = int(i[2])

objects = tuple(map(lambda x: x ,zoo_data.keys()))
performance = list(map(lambda x: x ,zoo_data.values()))

"""
from matplotlib import pyplot as plt
import csv
zoo_data = {}
with open('zoo.csv','rt') as ani:
    reader = csv.reader(ani,delimiter = ',')
    next(reader)
    for i in reader:
        if i[0] in zoo_data:
            zoo_data[i[0]] += int(i[2])
        else:
            zoo_data[i[0]] = int(i[2])

objects = tuple(map(lambda x: x ,zoo_data.keys()))
performance = list(map(lambda x: x ,zoo_data.values()))
plt.xlabel("animals")
plt.ylabel("water")
plt.title("Zoo data")
plt.bar(objects,performance,label='Zoo Visualisation',color='green')
plt.legend()
plt.show()
      