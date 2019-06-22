#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:56:08 2019

@author: vikram
"""

"""
Code Challenge
  Name: 
    Exploratory Data Analysis - Titanic Analysis
  Filename: 
    titanic.py
  Dataset:
    training_titanic.csv
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people in the given training set survived the disaster ?
      How many people in the given training set died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
"""
import numpy as np
import pandas as pd
#Read csv file
df = pd.read_csv("training_titanic.csv")

# Not a good technique to print the Data Frame
print (df)
df.info() 
df.head()
df.columns      # list(df.columns) df.columns.tolist()
df.values
df.describe()
df.max() 
df.min()


list1=df['Survived'].value_counts()
print("Survied people:",list1[1])
print("Died people:",list1[0])
# all value replace by nan
df = df.fillna(np.NaN)
df["bool_sex"] = df["Sex"].map(lambda x: 0 if x == 'male' else 1 )
list2=df["bool_sex"].value_counts()
print(list2[0],list2[1])




male_survived = df["Survived"][(df['Sex']=='male')].value_counts(normalize=True)
print("male survived/male unsurvived%:",male_survived[0]*100)

female_survived = df["Survived"][(df['Survived']==1) & (df['Sex']=='female')].value_counts()
df['voice mail plan'][(df['voice mail plan']=='yes') & (df['international plan']=='yes')].value_counts()

print('number female who survived:',female_survived)

#df['Age'] = df['Age'].replace(0, np.NaN)
df=df.dropna(subset=['Age'])


df["age_group"] = df["Age"].map(lambda x: 1 if x <18 else 0 )

child_survived = df["Survived"][(df['Survived']==1) & (df['age_group']==1)].value_counts()

old_survived = df["Survived"][(df['Survived']==1) & (df['age_group']==0)].value_counts()

