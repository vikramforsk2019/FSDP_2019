#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:09:05 2019

@author: vikram
"""

dataset: BreadBasket_DMS.csv# Importing the libraries
import pandas as pd
from apyori import apriori

# Data Preprocessing
dataset = pd.read_csv('BreadBasket_DMS.csv')




Q1. In this code challenge, you are given a dataset which has data and time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.

import pandas as pd
from apyori import apriori

# Data Preprocessing
dataset = pd.read_csv('BreadBasket_DMS.csv')



series=dataset['Item'].value_counts()
a=series.index[:].tolist()
b=series.values[:].tolist()


import matplotlib.pyplot as plt
         
plt.pie(b[:10],labels=a[:10], autopct='%.0f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
#same transcation id means buy together 
#2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
dataset = dataset[dataset["Item"] != "NONE"]
    
def cart(values):
   return list(set(values)) 
    
transactions = list(dataset.groupby('Transaction')['Item'].apply(cart))

rules = apriori(transactions, min_support = 0.0025, min_confidence = 0.2, min_lift = 2)

results = list(rules)


for item in results:
   pair = item[0] 
   items = [x for x in pair]
   print("Rule: " + items[0] + " -> " + items[1])

   #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")

    print("associated items: ",item[2][0][1])
    #or    
3. Out of given results sets, show only names of the associated item from given result row wise.

for item in results:
   pair2= item[2] 
   items = [x for x in pair2]
   print("associated items: ",items[0][1])

