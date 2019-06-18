#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 08:24:53 2019

@author: vikram
"""

"""
Code Challenge ( Pie Chart )

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area

Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 

Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""
from matplotlib import pyplot as plt
from selenium import webdriver

wiki = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"


#driver = webdriver.Chrome("C:/Users/rohit/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Firefox(executable_path="/home/vikram/anaconda3/geckodriver")

driver.get(wiki)    # Opening the submission url



right_table=driver.find_element_by_class_name('wikitable')


#Generate lists
state_name=[]
shared=[]
newlist=[]
my_dict={}
for row in right_table.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    if len(cells) == 7:
        state=cells[1].text.strip()#cells[0] remove bcoz it is se no. it take automaticly
        share=cells[4].text.strip()
        my_dict[share]=state
 
newlist =list( my_dict.items())
for i,j in newlist[0:6]:
     shared.append(i) 
     state_name.append(j)
     
explode = (0.4,0,0,0,0,0)      
plt.pie(shared,labels=state_name,wedgeprops={'edgecolor':'black'},autopct='%1.1f%%',explode=explode)
plt.show()




