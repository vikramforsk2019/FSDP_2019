#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:04:03 2019

@author: vikram
"""


"""
Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

 

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.

"""

import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Female_Stats.csv')
#temp = dataset.values
features = dataset.iloc[:, 1:].values
labels = dataset.iloc[:, 0].values


# add code to automate the p value removing
import statsmodels.api as sm
import numpy as np
import pandas as pd
features = sm.add_constant(features)



from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

regressor_OLS = sm.OLS(endog = labels_train, exog = features_train).fit()
regressor_OLS.summary()

Pred=regressor_OLS.predict(features_test)
print (pd.DataFrame(Pred, labels_test))



#for both
features_opt = features[:, [0,1,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
regressor_OLS.predict([1,81,1])
regressor_OLS.predict([1,85,1])
regressor_OLS.predict([1,88,1])

#for only mom ,dad-contants
features_opt = features[:, [0,1]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
regressor_OLS.predict([1,81])
regressor_OLS.predict([1,85])
regressor_OLS.predict([1,88])
#for only dad
features_opt = features[:, [0,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
regressor_OLS.predict([1,80])
regressor_OLS.predict([1,81])
regressor_OLS.predict([1,85])
























