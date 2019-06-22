#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:36:04 2019

@author: vikram
"""

"""
Code Challenge 

import Automobile.csv file.

Using MatPlotLib create a PIE Chart of top 10 car makers according to the number 
of their cars and explode the largest car maker


"""
import matplotlib.pyplot as plt
import pandas as pd
#Read csv file
df = pd.read_csv("Automobile.csv")
df.info()
new_df=df['make'].value_counts()
list2=new_df[0:10].tolist()
list3=new_df.index[0:10].tolist()
#df.loc[1:10,['make']]

explode = (0.5, 0, 0, 0, 0, 0, 0, 0, 0,0)
#plt.style.use('fivethirtyeight')

plt.pie(list2,labels=list3,explode=explode,wedgeprops={'edgecolor':'black'},autopct='%.0f%%')
plt.show()












