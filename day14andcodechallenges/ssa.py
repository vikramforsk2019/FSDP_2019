#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 16:07:31 2019

@author: vikram
"""


"""
Code Challenge
  Name: 
    SSA Analysis
  Filename: 
    ssa.py
  Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made available 
    data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip from Resources)  
    
    Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that particular data
    Concatinate all the data to form single dataframe using pandas concat method
    Display the top 5 male and female baby names of 2010
    Calculate sum of the births column by sex as the total number of births 
    in that year (use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  
     
"""

import os
entries = os.listdir('/home/vikram/Desktop/FSDP2019/day14andcodechallenges/baby_names')
for file_name in entries:
    if file_name[-3:]=='txt' and file_name[3:7] in range(1880,2010):
        print(file_name[3:7])
        with open(file_name, "r") as file:
        file_contents = file.readlines()
        print(file_contents)
        
        
df3=df1[2010].tolist()
for row in df3[0:]:
    num=row.split(',')
    if num[1]=='M' :
        print(num[0])





#satrt here

import matplotlib.pyplot as plt
import pandas as pd
df1=pd.DataFrame()
df=pd.DataFrame()

for i in range(2000,2011):
    file_name = 'yob'+str(i)+'.txt'
    df=pd.DataFrame()
    with open(file_name) as data:
        file_contents = data.readlines()
        df[i]= file_contents
    df1=pd.concat([df1,df],axis=1)


new_data = df1[2010].str.split(",", n = 2, expand = True) 


#0-name,1-male,2-number


#top five baby names

name_list_Male=new_data[0][new_data[1]=='M'].tolist()
print('male baby name:',name_list_Male[0:6])

name_list_Female=new_data[0][new_data[1]=='F'].tolist()
print('female baby name:',name_list_Female[0:6])


print('male birth in 2010::',len(name_list_Male))
print('female birth in 2010::',len(name_list_Female))


explode = (0, 0)
#plt.style.use('fivethirtyeight')

plt.pie([len(name_list_Male),len(name_list_Female)],labels=['Male','Female'],explode=explode,wedgeprops={'edgecolor':'black'},autopct='%.0f%%')
plt.show()






























import pandas as pd

df = pd.DataFrame()
df1 = pd.DataFrame()
df = pd.concat([df,df1])


   