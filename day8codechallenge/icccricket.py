#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:56:55 2019

@author: vikram
"""


"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""
from bs4 import BeautifulSoup
import requests
url= "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(url).text
soup = BeautifulSoup(source,"lxml")

print (soup.prettify())
right_table=soup.find('table', class_='table')
print (right_table.prettify())
A=[]
B=[]
C=[]
D=[]
E=[]
#for making first heaader
states = right_table.find('tr')
s = states.find_all('th')
print(s[1].text)

for row in right_table.findAll('tr'):
      # first row has no TH, but other rows have one TH and 6 TD
    cells = row.findAll('td') 
    # first row has 7 TH 
    if len(cells) == 5:
        A.append(cells[0].text.strip()) #rank,it is not position
        #skip the sequence number column
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
      
from collections import OrderedDict

col_name = ["Rank","Team","Match","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))


# If you want to store the data in a csv file
import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("former2.csv")
