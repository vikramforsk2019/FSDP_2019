#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:40:11 2019

@author: vikram
"""

Code Challenge 01: (Prostate Dataset)
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat", delimiter =' ')

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?
    find mean:
         if <mean low:
            >mean high
            use classification model and predict

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

#imports the CSV dataset using pandas

dataset = pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat", delimiter =' ')  


features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, -1].values


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  


from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
lm = LinearRegression ()
lm_lasso = Lasso() 
lm_ridge =  Ridge() 



#Fit a model on the train data

lm.fit(features_train, labels_train)  
lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)

predict_test_lm =	lm.predict(features_test ) 
predict_test_lasso = lm_lasso.predict (features_test) 
predict_test_ridge = lm_ridge.predict (features_test)

df = pd.DataFrame({'Actual': labels_test, 'Predicted': predict_test_lm})  
print ( df )

from sklearn import metrics
print ("Simple Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lm),2) )

print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lasso),2))

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_ridge),2))




"""
(b) Can we predict whether lpsa is high or low, from other variables?
    find mean:
         if <mean low:
            >mean high
            use classification model and predict
"""

mean_value=np.mean(labels)
df = pd.DataFrame({"A": [10,20,30], "B": [20, 30, 10]})

def fx(x):
    if x<mean_value:
        return 'low'
    else:
        return 'high'
    
dataset['lpsa_new'] = dataset.lpsa.apply(fx)

labels=dataset.iloc[:,-1].values


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)  

#Training and making predictions
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  
















"""
print(np.std(labels))
print(np.mean(labels)) # lpsa column haveing scaling so mean not measure

You can see that the value of root mean squared error is 0.7349, 
which is less than 10% of the mean value of the percentages of all the students i.e. 51.48. 
This means that our algorithm did a decent job.
MSE ==sd(labels)
MSE <=10% mean(labels)

"""










