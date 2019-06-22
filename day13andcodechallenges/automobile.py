#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 22:36:08 2019

@author: vikram
"""


"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""
import numpy as np
import pandas as pd
#Read csv file
df = pd.read_csv("Automobile.csv")

df.info() 
df.head()

a = df['price'].mean()

    
# Filling the mean salaries for the different categories of discipline
df['price']=df['price'].fillna(a)
price_array=np.array(df['price'].tolist())

print('minimun price',df['price'].min())
print('maximum  price',df['price'].max())
print('average price',df['price'].mean())
print('standard deviation',df['price'].std())









