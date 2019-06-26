#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 10:55:00 2019

@author: vikram
"""


"""
Code Challenge
  Name: 
    Baltimore City Analysis
  Filename: 
    baltimore.py
  Problem Statement:
    Read the Baltimore_City_Employee_Salaries_FY2014.csv file 
    and perform the following task :

    0. remove the dollar signs in the AnnualSalary field and assign it as a float
    0. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
       Sort the data and display to show who get the highest salary
       

    0. Try to group on JobTitle only and sort the data and display
    0. How many employess are there for each JobRoles and Graph it
    0. Graph and show which Job Title spends the most
    0. List All the Agency ID and Agency Name 
    0. Find all the missing Gross data in the dataset 
    
  Hint:

import pandas as pd
import requests
import StringIO as StringIO
import numpy as np
        
url = "https://data.baltimorecity.gov/api/views/2j28-xzd7/rows.csv?accessType=DOWNLOAD"
r = requests.get(url)
data = StringIO.StringIO(r.content)

dataframe = pd.read_csv(data,header=0)

dataframe['AnnualSalary'] = dataframe['AnnualSalary'].str.lstrip('$')
dataframe['AnnualSalary'] = dataframe['AnnualSalary'].astype(float)

# group the data
grouped = dataframe.groupby(['JobTitle'])['AnnualSalary']
aggregated = grouped.agg([np.sum, np.mean, np.std, np.size, np.min, np.max])

# sort the data
pd.set_option('display.max_rows', 10000000)
output = aggregated.sort(['amax'],ascending=0)
output.head(15)


aggregated = grouped.agg([np.sum])
output = aggregated.sort(['sum'],ascending=0)
output = output.head(15)
output.rename(columns={'sum': 'Salary'}, inplace=True)

import json
config = json.loads(open('usagov_bitly_data.json').read())
config['a']


from matplotlib.ticker import FormatStrFormatter

myplot = output.plot(kind='bar',title='Baltimore Total Annual Salary by Job Title - 2014')
myplot.set_ylabel('$')
myplot.yaxis.set_major_formatter(FormatStrFormatter('%d'))



"""

import pandas as pd
#Read csv file
df = pd.read_csv("Baltimore_City_Employee_Salaries_FY2014.csv")

grouped = df.groupby(['JobTitle','AnnualSalary'])
grouped.count()
grouped.groups
grouped.groups.keys()

 
# 0. remove the dollar signs in the AnnualSalary field and assign it as a float
df['AnnualSalary']=df['AnnualSalary'].str.replace('$','')
df['AnnualSalary'] = df['AnnualSalary'].astype(float)


#Calculate mean,max value for each numeric column per each group
 
#Sort the data and display to show who get the highest salary
grouped.mean()

df.groupby('JobTitle')[['AnnualSalary']].min()
df.groupby('JobTitle')[['AnnualSalary']].max()
df.groupby('JobTitle')[['AnnualSalary']].mean()
df.groupby('JobTitle')[['AnnualSalary']].sum()
df.groupby('JobTitle')[['AnnualSalary']].sort_values(by='AnnualSalary')
df.info()

"""
       import numpy as np
       
       result = df.groupby("JobTitle")["AnnualSalary"].mean().sort_values()
       print(result[-1])
OR

       result = pd.pivot_table(df, values="AnnualSalary", index="JobTitle", aggfunc=np.mean)
       result2 = pd.pivot_table(df, values="AnnualSalary", index="JobTitle", aggfunc=np.sum)
     
       res = result.sort_values("AnnualSalary")
       print('highest salary::',res['AnnualSalary'].index[-1],res['AnnualSalary'][-1])
"""


#   0. Try to group on JobTitle only and sort the data and display
grouped = df.groupby('JobTitle', sort = True).groups




grouped = df.groupby(df['AnnualSalary'], sort = True).groups.values()






"""
  0. List All the Agency ID and Agency Name 
  
"""
grouped = df.groupby(['AgencyID','Agency'])
print(grouped.head(1))

grouped.groups.keys()

#  0. Find all the missing Gross data in the dataset 
fd=df[df['GrossPay'].isnull()]


# 0. How many employess are there for each JobRoles and Graph it

df_rank=df.groupby('JobTitle')[['JobTitle']]
list2=df_rank.count()
import matplotlib.pyplot as plt
plt.bar(list2.index[:10],list2["JobTitle"][:10])
plt.xticks(rotation=90)


#  0. Graph and show which Job Title spends the most

list8=df.groupby('JobTitle')[['GrossPay']].sum()

import matplotlib.pyplot as plt
plt.bar(list8.index[:10],list8["GrossPay"][:10])
plt.xticks(rotation=90)












