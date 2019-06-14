#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:57:39 2019

@author: vikram


Database handling using MySQL on Local Machine
"""


#use below command in anaconda prompt
# pip install mysql-connector-python

from pandas import DataFrame
import mysql.connector



# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = mysql.connector.connect ( user='root', password='', host='localhost')
# database = '' can be used if we want to connect to already defined database


# creating cursor
c = conn.cursor()

# STEP 0 if exists
c.execute("DROP DATABASE employee;")

# STEP 1
c.execute("CREATE DATABASE employee;")

# STEP 2
c.execute("USE employee;")

# STEP 3
c.execute ("""CREATE TABLE employees(
          id INTEGER,
          first  TEXT,
          last TEXT,
          pay INTEGER
          )""")


# STEP 4
c.execute("INSERT INTO employees VALUES (01,'Sylvester', 'Fernandes', 50000)")
c.execute("INSERT INTO employees VALUES (02,'Yogendra', 'Singh', 70000)")
c.execute("INSERT INTO employees VALUES (03,'Pradeep', 'Natani', 30000)")
c.execute("INSERT INTO employees VALUES (04,'Kunal', 'Vaid', 30000)")
c.execute("INSERT INTO employees VALUES (05,'Devendra', 'Shekhawat', 30000)")

# c.execute("INSERT INTO employee VALUES ({},'{}', '{}', {})".format(idd, first,last,pay))


c.execute("SELECT * FROM employees")

# STEP 5
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM employees")



# STEP 6
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["id","first","last","pay"]

# field_names = [i[0] for i in c.description]
# print field_names

conn.commit()
conn.close()

