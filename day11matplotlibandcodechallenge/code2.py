#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:19:30 2019

@author: vikram
"""

"""
Code Challenge ( Line Plot )

We have to find sea level rise in past 100 years
Read the file sealevel.csv which has data for 135 years

It has two parts in the data, year and the sea level rise in inches

Read the csv file using the csv reader and create two list
    1) Which stores the years from 1880 to 2014
    2) Which stores the sealevel increase in inches
    
Now plot the data using Line Plot
The plot should have the valid title,labels, ticks ( x and y ), legend

Is the  sea level increasing almost every year.

"""


from matplotlib import pyplot as plt
year_list=[]
inch_list=[]
import csv
with open("sealevel.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip the first row
    next(csv_reader)
    for row in csv_reader:
        year_list.append(int(row[0]))
        inch_list.append(float(row[-1]))
plt.xlabel("Year")
plt.ylabel("sealevel in Inches")
plt.title("sealevel")
plt.plot(year_list,inch_list,label='Sealevel',color='red')
        
        
