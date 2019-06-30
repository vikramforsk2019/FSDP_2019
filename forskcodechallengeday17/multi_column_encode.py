#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 08:52:58 2019

@author: vikram
"""

import pandas as pd
from sklearn import preprocessing 
df= pd.DataFrame({
    'fruit':  ['apple','orange','pear','orange'],
    'color':  ['red','orange','green','green'],
    'weight': [5,6,3,4]
})

dataset= pd.get_dummies(df)

#cat_df = df.select_dtypes(include=['object']).copy()

features = dataset.iloc[:, 2:-1].values
labels=dataset.iloc[:,0].values


#features=cat_df.apply(LabelEncoder().fit_transform)

#features[:, 0] = labelencoder.fit_transform(features[:, 0])


#from sklearn.preprocessing import OneHotEncoder

#onehotencoder = OneHotEncoder(categorical_features = [0])

#features = onehotencoder.fit_transform(features).toarray()

# Avoiding the Dummy Variable Trap
# dropping first column


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

#To see the value of the intercept and slop calculated by the linear regression algorithm for our dataset, execute the following code.
print(regressor.intercept_)  
print (regressor.coef_)


Pred = regressor.predict(features_test)

print (pd.DataFrame(Pred, labels_test))








