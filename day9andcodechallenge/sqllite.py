#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:56:33 2019

@author: vikram
"""

"""

Code Challenge 1
Write a python code to insert records to a sqlite
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""

import sqlite3
from pandas import DataFrame


# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'db_University' )


# creating cursor
c = conn.cursor()


# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE Table student_data(
          Student_Name TEXT,
           Student_Age INTEGER,
          Student_Roll_no INTEGER,
          Student_Branch TEXT
          )""")


# STEP 2
c.execute("INSERT INTO student_data VALUES ('vikram',22, 16492,'computer science')")



# STEP 3
c.execute("SELECT * FROM student_data")
# "SELECT * FROM employees WHERE last = 'Fernandes' "



# STEP 4
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )



# STEP 6
# commits the current transaction 
conn.commit()

# STEP 7
# closing the connection 
conn.close()
