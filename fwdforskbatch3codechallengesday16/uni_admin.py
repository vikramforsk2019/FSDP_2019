#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 17:13:03 2019

@author: vikram
"""

"""

Code Challenges:
    Name:
        University Admission Prediction Tool
    File Name:
        uni_admin.py
    Dataset:
        University_data.csv
    Problem Statement:
         Perform Linear regression to predict the chance of admission based on all the features given.
         Based on the above trained results, what will be your estimated chance of admission.

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
# Importing the dataset
dataset = pd.read_csv('University_data.csv')
#temp = dataset.values

#dataset= dataset.get_dummies(dataset)
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

#Check if any NaN values in dataset
dataset.isnull().any(axis=0)


#check data types for each column
print (dataset.dtypes)


# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])


from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()

# Avoiding the Dummy Variable Trap
# dropping first column
features = features[:, 1:]


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)
print(regressor.intercept_)  
print (regressor.coef_)


Pred = regressor.predict(features_test)

import pandas as pd

print (pd.DataFrame(Pred, labels_test))



df = pd.DataFrame({'Actual': labels_test, 'Predicted': Pred})  
print (df) 





df1 = df.head(5)

df1.plot(kind='bar',figsize=(5,5))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
#plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

