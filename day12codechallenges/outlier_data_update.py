#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:51:09 2019

@author: vikram
"""

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
 else:
     list_out_data.append(data)
print(list_out_data)
missing_bool = np.isnan(list_out_data) | np.isinf(list_out_data)
print (missing_bool)
incomes[missing_bool] = -1  
