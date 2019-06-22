#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 08:47:04 2019

@author: vikram
"""

"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
    
To perfrom analysis on the Telecom industry churn dataset -
1. Predict the count of Churned customer availing both voice mail plan and international plan schema
2. Total charges for international calls made by churned and non-churned customer and visualize it
3. Predict the state having highest night call minutes for churned customer
4. Visualize -
    a. the most popular call type among churned user
    b. the minimum charges among all call type among churned user
5. Which category of customer having maximum account lenght?
   Predict and print it
6. Predict a relation between the customer and customer care service that 
whether churned customer have shown their concern to inform the customer care 
service about their problem or not
7. In which area code the international plan is most availed?
"""


import pandas as pd
#Read csv file
df = pd.read_csv("Telecom_churn.csv")

# Not a good technique to print the Data Frame
print (df)
df.head(5)
df.info()

df['voice mail plan'].value_counts()
voice_inter_plan=df['churn'][(df['voice mail plan']=='yes') & (df['international plan']=='yes')].value_counts()

print('total voice and inter mail plan in churned::',voice_inter_plan[1])

#total_charge_intl_churn=df['total intl charge'][df['churn']]
#print("total_charge_intl_churn::",total_charge_intl_churn.sum())  #483 rows
#print( df['total intl charge'].sum())

df_sub1 = df[df['churn'] == False ][['total intl charge','churn']]
df_sub2 = df[df['churn'] == True ][['total intl charge','churn']]
print('total intl charge for churned:',df_sub1['total intl charge'].sum())
print('total intl charge not churned:',df_sub2['total intl charge'].sum())



df_sub1 = df[df['churn'] == True ][['total night calls','churn']]
max_value=df_sub1['total night calls'].max()

df_sub5=df['state'] [(df['total night calls']==max_value) & \
                    (df['churn'] == True) & \
                    (df['state'] )]

print('state code::',df_sub5)

##call type popular 4.1

df2 = df[df['churn'] == True ][['total day calls','total night calls','total eve calls','total intl calls','churn']]


list_sum=[df2['total day calls'].sum(),df2['total eve calls'].sum(),df2['total night calls'].sum(),
                                                             df2['total intl calls'].sum()]

new_pd= pd.DataFrame(list_sum,index=['day calls','eve calls','night calls','intl calls'],columns=['max sum']) 

print(new_pd.index.values)
print(new_pd.max())
new_pd[new_pd["max sum"]==new_pd["max sum"].max()].index



#minimum charge of all calling 4.2
df3= df[df['churn'] == True ][['total day charge','total night charge','total eve charge','total intl charge','churn']]


list_min=[df3['total day charge'].min(),df3['total eve charge'].min(),df3['total night charge'].min(),
                                                             df3['total intl charge'].min()]

new_pd2= pd.DataFrame(list_min,index=['day charge','eve charge','night charge','intl charge'],columns=['min charge']) 

print(new_pd2.min())


## 5

acc_length=df['account length'][df['churn']==True]
print('max acc length:',acc_length.max())

##     7
new_area=df['area code'][df['international plan'] =='yes' ].value_counts()
print('international plan is most availed in this area code:',new_area.max())

##  6
df.info()
cus_care=df['customer service calls'][df['churn']==True].value_counts()

