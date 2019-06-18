#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:45:08 2019

@author: vikram
"""

"""
Code Challenge ( Scatter Plot )

Suppose the result was announced for a class. 
In this class both guys and girls appeared in the exam. 
The goal is to find out who performed better and how to get rid of shortcomings.
We are going to make a scatter plot for that.
Boys are in green while girls in red. 

girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

Are their any outliers

Hint: 
    Use the Scatter method to scatter the data on the plot

"""

from matplotlib import pyplot as plt
girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.xlabel("grades_range")
plt.ylabel("Marks_grades")
plt.title("Exam Result")
plt.scatter(grades_range,girls_grades,color='green',label='girls_grades')
plt.scatter(grades_range,boys_grades,color='red',label='boys_grades')
plt.legend()
plt.show()
