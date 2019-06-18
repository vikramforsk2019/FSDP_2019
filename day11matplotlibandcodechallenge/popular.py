#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:20:56 2019
@author: vikram
"""

"""
Code Challenge ( Bar Plot )
  Name: 
    Most Popular Programming Language out of 28 Languages
  Filename: 
    popular.py
  Problem Statement:
    Read the bardata.csv file
    It has a the survey of 87,570 people at the StackOverFlow Annual Developer Day
    The data has two parts
      1) ID of the Responser
      2) Semicolon seperated data of the languages known by them
    
    We need to now read the csv file using the csv reader and create a dictionary 
    This dictionary should store the Language as the key and value as the number 
    of times the responder has voted for it.
    
    Now display the data in the form of Horizontal Bar Chart to show the popularity of the 
    top 10 languages and the votes from the developer 

  Hint:
      Use the concept of DictReader from csv 
      Also use the concept of Counter class from collections 
      and update it for each row of data
      
      with open ('data.csv') as csv_reader :
          csv_reader = csv.DictReader()
          
          language_counter = Counter()
          
          for row in csv_reader:
              language_counter.update(row['LanguageWorkedWith'].split(';'))
      
      # You could have used the zip function here 
      print(language_counter.most_common(10))
      languages=[]
      popularity=[]
      for item i language_counter.most_common(10):
          languages.append(item[0])
          popularity.append(item[1])
                 
"""
from matplotlib import pyplot as plt
languages=[]
popularity=[]
data_list={}
import csv
with open ('bardata.csv') as csv_reader :
    csv_reader2 = csv.DictReader(csv_reader)
    for row in csv_reader2:
        #print(row)
        language=row['LanguagesWorkedWith'].split(';')
        for i in language:
            if i in data_list:
                data_list[i] += 1
            else:
                data_list[i] = 1
             
newlist=sorted(data_list.items(), key = lambda k:k[1])

for i,j in newlist[-10:]:
     languages.append(i)
     popularity.append(j)
plt.xlabel("language")
plt.ylabel("Popularity")
plt.title("Rank of language")
plt.barh(languages,popularity,label='Language',color='green',)
plt.legend()
plt.show()
    





 
















