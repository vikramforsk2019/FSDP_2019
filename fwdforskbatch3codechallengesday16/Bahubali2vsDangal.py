#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:36:33 2019

@author: vikram
"""

"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""


import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

#imports the CSV dataset using pandas

dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')  

#explore the dataset
print (dataset.shape)
print (dataset.ndim)
print (dataset.head())
print (dataset.describe())

dataset.isnull().any(axis=0)
features = dataset.iloc[:, :-2].values  
labels_b = dataset.iloc[:, 1].values 
labels_d= dataset.iloc[:, -1].values 
lab=dataset.iloc[:,1:].values

from sklearn.linear_model import LinearRegression  
regressor1 = LinearRegression()  
regressor2 = LinearRegression() 
regressor3 = LinearRegression() 

regressor1.fit(features, labels_b)  #for bahubali

regressor2.fit(features, labels_d)  #for dangal

regressor3.fit(features, lab)  #for both

print(regressor1.intercept_)  
print (regressor1.coef_)

print(regressor2.intercept_)  
print (regressor2.coef_)

print(regressor3.intercept_)  
print (regressor3.coef_)
x = np.array(10).reshape(-1,1)

print ('collection for bahubali2::',regressor1.predict(x))

print ('collection for dangal::',regressor2.predict(x))

print ('collectionfor both::',regressor3.predict(x))






import matplotlib.pyplot as plt

# Visualising the  results
plt.scatter(features, labels_b, color = 'red')
plt.plot(features, regressor1.predict(features), color = 'blue')
plt.title('Study Hours and Exam Score')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score: Marks')
plt.show()






from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels_d, test_size=0.2, random_state=0)  

#train the algo
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train) 


"""
This means that for every one unit of change in hours studied, the change in the score is about 9.91%. 
"""

#making predictions
#To make pre-dictions on the test data, execute the following script:

labels_pred = regressor.predict(features_test) 

#To compare the actual output values for features_test with the predicted values, execute the following script 
df = pd.DataFrame({'Actual': labels_test, 'Predicted': labels_pred})  
print (df) 





df1 = df.head(5)

df1.plot(kind='bar',figsize=(5,5))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
#plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()








