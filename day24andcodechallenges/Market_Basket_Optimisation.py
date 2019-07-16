#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 12:51:13 2019

@author: vikram
"""

Code Challenge:
Datset: Market_Basket_Optimization.csv
Q2. In today's demo sesssion, we did not handle the null values before fitting the data to model, 
remove the null values from each row and perform the associations once again.
Also draw the bar chart of top 10 edibles.

# Apriori

# Importing the libraries
import numpy as np
import pandas as pd
from apyori import apriori

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)


"""

transactions = []

for i in range(0, 7501):
    #transactions.append(str(dataset.iloc[i,:].values)) #need to check this one
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])
for item in transactions:
       print(item[0][:])

"""


""""
for i in range(0, 7501):
    #transactions.append(str(dataset.iloc[i,:].values)) #need to check this one
    for j in range(0,20):
      if str(dataset.values[i,j])!='nan' :
        transactions.append([str(dataset.values[i,j])])
        
"""
transactions = dataset.apply(lambda x: x.dropna().tolist(), axis=1).tolist()
        
# Training Apriori on the dataset

rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

# Visualising the results
results = list(rules)




for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

  






