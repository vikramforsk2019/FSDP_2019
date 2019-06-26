#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:56:57 2019

@author: vikram
"""
"""

Forsk Labs <forsklabs@gmail.com>
	
Attachments3:49 PM (7 minutes ago)
	
to bcc: me
Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 
Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ?

#sample code is also attached
"""


import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

#imports the CSV dataset using pandas

dataset = pd.read_csv('iq_size.csv')  

#explore the dataset
print (dataset.shape)
print (dataset.ndim)
print (dataset.head())
print (dataset.describe())

dataset.isnull().any(axis=0)
features = dataset.iloc[:, 1:].values  
labels = dataset.iloc[:, 0].values 


from sklearn.linear_model import LinearRegression  
regressor1 = LinearRegression()  


regressor1.fit(features, labels)  



print(regressor1.intercept_)  
print (regressor1.coef_)
x = np.array([90,70,150]).reshape(1,-1) #or (1,3)  according features data

print ('PIQ::',regressor1.predict(x))
Pred = regressor1.predict(features)






 

#To compare the actual output values for features_test with the predicted values, execute the following script 
df = pd.DataFrame({'Actual': labels, 'Predicted': Pred})  
print (df) 





df1 = df.head(5)

df1.plot(kind='bar',figsize=(5,5))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
#plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
