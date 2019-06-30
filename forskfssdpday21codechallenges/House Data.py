#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 11:54:16 2019

@author: vikram
"""
"""
Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score

"""

import pandas as pd  
import numpy as np  
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("kc_house_data.csv", delimiter =',')  

dataset=dataset.fillna(dataset.mean())

labels=dataset['price'].values

features=dataset.iloc[:,3:].values


sc = StandardScaler()
features = sc.fit_transform(features)

#backword Elimanation 
import statsmodels.api as sm

features_obj = sm.add_constant(features)
while (True):
    regressor_OLS = sm.OLS(endog = labels,exog =features_obj).fit()
    p_values = regressor_OLS.pvalues
    if p_values.max() > 0.05 :
        features_obj = np.delete(features_obj, p_values.argmax(),1)
    else:
        break
regressor_OLS.summary()


features_train, features_test, labels_train,labels_test	=	train_test_split(features_obj, labels, test_size=0.3, random_state=1)



 
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
lm = LinearRegression ()
lm_lasso = Lasso() 
lm_ridge =  Ridge() 
lm.fit(features_train, labels_train)
lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)



predict_test_lm =	lm.predict(features_test ) 
predict_test_lasso = lm_lasso.predict (features_test) 
predict_test_ridge = lm_ridge.predict (features_test)


from sklearn import metrics

print (np.round (metrics .mean_squared_error(labels_test, predict_test_lm),2) )


print (np.round (metrics .mean_squared_error(labels_test, predict_test_lasso),2))

print (np.round (metrics .mean_squared_error(labels_test, predict_test_ridge),2))










