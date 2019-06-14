

from bs4 import BeautifulSoup
import requests

#Get Source Code of page
url = "https://www.icc-cricket.com/rankings/mens/team-rankings/t20i"
source = requests.get(url).text

#Parsing of HTML data
soup = BeautifulSoup(source,"lxml")

#Get table from html data
ranking_table = soup.find('table', class_='table')


import sqlite3
from pandas import DataFrame
# connecting database
conn = sqlite3.connect ( 'ICC_cricket.db' )
# creating cursor
c = conn.cursor()
c.execute("DROP Table ranking")
# creating table of student
c.execute ("""CREATE TABLE ranking(
              rank INTEGER,
              team TEXT,
              weighted_matches INTEGER,
              points INTEGER,
              rating INTEGER
          )""")
conn.commit()

for row in ranking_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        rank = int(cells[0].text.strip())
        team = cells[1].text.strip()
        weighted_matches = int(cells[2].text.strip())
        points = int(cells[3].text.strip().replace(",",""))
        rating = int(cells[4].text.strip().replace(",",""))
        c.execute("INSERT INTO ranking VALUES({},'{}',{},{},{})".format(rank,team,weighted_matches,points,rating))
        conn.commit()
        
# Retriving data from database
c.execute("SELECT * FROM ranking")

df = DataFrame(c.fetchall())  
df.columns = ["Rank","Team","Weighted Matches","Points","Rating"]

conn.close()
