#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 15:48:35 2019

@author: vikram
"""

"""
Q1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" respectively
    Display the Car Name with highest miles per gallon value
    Build the Decision Tree and Random Forest models and find out which of the two is more accurate in predicting the MPG value
    Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from both the models)

"""
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

dataset = pd.read_csv("Auto_mpg.csv",delim_whitespace=True,header=None,names=['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','car name'])  
dataset.info()

a=dataset['horsepower'].min()
dataset['horsepower']=dataset['horsepower'].replace('?',a).astype(np.float)

new_dataset = dataset.drop('mpg', axis=1)  
labels = dataset['mpg']  

features=new_dataset.iloc[:,:-1].values
 



from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)  



#using random forest
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test) 

from sklearn.tree import DecisionTreeRegressor  
classifier = DecisionTreeRegressor()  
classifier.fit(features_train, labels_train)


labels_pred = classifier.predict(features_test) 

x=np.array([6,215,100,2630,22.2,80,3]).reshape(1,-1)
labels_pred = classifier.predict(x)
print(labels_pred[0])

labels_pred = classifier.predict(features_test)

labels_pred = classifier.predict(features_test)
df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
df  



#usint Random forest method
from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=10, random_state=0)  
regressor.fit(features_train, labels_train)  
labels_pred = regressor.predict(features_test)  

x=np.array([6,215,100,2630,22.2,80,3]).reshape(1,-1)
labels_pred = regressor.predict(x)
print(labels_pred[0])


from sklearn import metrics

print('Mean Absolute Error:', metrics.mean_absolute_error(labels_test, labels_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(labels_test, labels_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(labels_test, labels_pred)))  







    Find out the MPG value of a 
    80's model car of origin 3,
    weighing 2630 kgs with 6 cylinders, 
    having acceleration around 22.2 m/s
    due to it's 100 horsepower engine giving 
    it a displacement of about 215. (Give the prediction from both the models)




