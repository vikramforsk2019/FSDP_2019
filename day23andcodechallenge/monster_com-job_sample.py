#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:39:26 2019

@author: vikram
"""

Q.3.
"""
Code Challenge - 
 This is a pre-crawled dataset, taken as subset of a bigger dataset 
 (more than 4.7 million job listings) that was created by extracting data 
 from Monster.com, a leading job board.
 
 
 
 Remove location from Organization column?
 Remove organization from Location column?
 
 In Location column, instead of city name, zip code is given, deal with it?
 
 Seperate the salary column on hourly and yearly basis and after modification
 salary should not be in range form , handle the ranges with their average
 
 Which organization has highest, lowest, and average salary?
 
 which Sector has how many jobs?
 Which organization has how many jobs
 Which Location has how many jobs?
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset (Bivariate Data Set with 3 Clusters)
dataset = pd.read_csv('monster_com-job_sample.csv')
dataset.info()



import re

dataset["organization"] = dataset["organization"].fillna("Missing")

def loc_org_swap(values):
    org, loc = values
    if re.match(r"[A-Za-z\s]+\,\s[A-Z]{2}\s?\d*",org):
        org, loc = loc, org
    if re.match("[\w\,\s-]{30,}",loc):
        loc = "Missing Location"
    return pd.Series([org, loc])

data=dataset[[
    
    "location",
    "organization"

]].dropna(axis=0, how='any')


data = pd.DataFrame()
data[["organization","location"]] = dataset[["organization","location"]].apply(loc_org_swap,axis=1)


   """  

data=dataset[[
    
    "location",
    "organization"

]].dropna(axis=0, how='any')


for org in data['organization']:
     result=re.findall(r'[a-zA-Z]+[\sa-zA-Z]*,\s[A-Z]{2}$|\w+, \w+ \d+',org)
     if result!=[]:
        print(result)
        data['value']=1
     else:
        print(result)
        data['value']=0
        
        
        
   
         idx = (data['organization'] == org)
         data.loc[idx,['location','organization']] = data.loc[idx,['location','organization']].values 
    
         #data['location'],data['organization']=data['location'],data['organization']
     #else:
       
     """
     
#3   salary
sal_list=[]
import re
for sal in dataset['salary']:
     result=re.findall(r'(/hour)$',str(sal))
     if result!=[]:
       salary=sal.replace('$ /hour','')
       a=salary.replace('-','')
       salary.split('-','')
       
     
for sal in dataset['salary']:
     result=re.findall(r'(/year)$',str(sal))
     if result!=[]:
      print(sal)     
     
     
     
     
     
     
import pandas as pd

d = {'L':  ['left', 'right', 'left', 'right', 'left', 'right'],
     'R': ['right', 'left', 'right', 'left', 'right', 'left'],
     'VALUE': [-1, 1, -1, 1, -1, 1]}
df = pd.DataFrame(d)

idx = (df['VALUE'] == 1)     
     
df.loc[idx,['L','R']] = df.loc[idx,['R','L']].values
     

