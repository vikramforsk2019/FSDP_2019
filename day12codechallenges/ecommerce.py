#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:32:11 2019

@author: vikram
"""

"""
Code Challenge
  Name: 
    E-commerce Data Exploration
  Filename: 
    ecommerce.py
  Problem Statement:
      To create an array of random e-commerce data of total amount spent per transaction. 
      Segment this incomes data into 50 buckets (number of bars) and plot it as a histogram.
      Find the mean and median of this data using NumPy package.
      Add outliers 
          
  Hint:
      Execute the code snippet below.
      import numpy as np
      import matplotlib.pyplot as plt
      incomes = np.random.normal(100.0, 20.0, 10000)
      print (incomes)
 
    outlier is an observation that lies an abnormal distance from other values 
    
"""
import numpy as np
incomes = np.random.normal(100.0, 20.0, 10000)
print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))
print("Standard Deviation is: ", np.std(incomes))
print("varience:",(np.std(incomes))**2)

import matplotlib.pyplot as plt
plt.hist(incomes, 50)
plt.show()
 
plt.boxplot(incomes)




#how to replace outliers data by nan or inf and replace by one
list_out_data=[]
import numpy as np
incomes = np.random.normal(100.0, 20.0, 10000)
mean=np.mean(incomes)
median=np.median(incomes)
sd=np.std(incomes)
for data in incomes:
 if data>(mean+3*sd) or data<(mean-3*sd):
    list_out_data.append(np.nan)
 else:else:
     list_out_data.append(data)
print(list_out_data)
missing_bool = np.isnan(list_out_data) | np.isinf(list_out_data)
print (missing_bool)
incomes[missing_bool] = -1  

     list_out_data.append(data)
print(list_out_data)
missing_bool = np.isnan(list_out_data) | np.isinf(list_out_data)
print (missing_bool)
incomes[missing_bool] = -1  


#how to show's outliers data by standard devation
import numpy as np
incomes = np.random.normal(100.0, 20.0, 10000)
mean=np.mean(incomes)
median=np.median(incomes)
sd=np.std(incomes)
for data in incomes:
 if data>(mean+3*sd) or data<(mean-3*sd):
    outliers_incomes = np.append(outliers_incomes,[data])
print("outliers e commerece data::",outliers_incomes)

#outliers data histogram
import matplotlib.pyplot as plt
plt.hist(outliers_incomes, 10)
plt.show(outliers_incomes)





