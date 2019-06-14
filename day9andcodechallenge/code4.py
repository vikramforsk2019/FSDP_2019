#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 18:15:43 2019

@author: vikram
"""
"""
Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi
"""

import sqlite3
from pandas import DataFrame


# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'teamranklist.db' )


# creating cursor
c = conn.cursor()

c.execute("DROP Table team_rank")
# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE team_rank(
          Rank INTEGER,
          Team  TEXT(255),
          Match TEXT,
          Points TEXT,
          Rating TEXT
          )""")

from bs4 import BeautifulSoup
import requests
url= "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(url).text
soup = BeautifulSoup(source,"lxml")

right_table=soup.find('table', class_='table')

for row in right_table.findAll('tr'):
      # first row has no TH, but other rows have one TH and 6 TD
    cells = row.findAll('td') 
    # first row has 7 TH 
    if len(cells) == 5:
        Rank=cells[0].text
        Team=cells[1].text.strip() #use strip to avoid \n and spaces
        Match=cells[2].text
        Points=cells[3].text
        Rating=cells[4].text
        c.execute("INSERT INTO team_rank VALUES ({},'{}','{}', '{}','{}')".format(Rank,Team,Match,Points,Rating))
conn.commit()       
c.execute("SELECT * FROM team_rank")
df = DataFrame(c.fetchall())
df.columns = ["Rank","Team","Match","Points","Rating"]
print ( c.fetchone()) 
print ( c.fetchall() )

