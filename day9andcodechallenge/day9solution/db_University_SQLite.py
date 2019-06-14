
import sqlite3
from pandas import DataFrame
# connecting database
conn = sqlite3.connect ( 'University.db' )
# creating cursor
c = conn.cursor()
# creating table of student
c.execute ("""CREATE TABLE students(
              student_name TEXT,
              student_age INTEGER,
              student_roll_no TEXT,
              student_branch TEXT
          )""")
conn.commit()
# inserting data into table students
c.execute("INSERT INTO students VALUES('Himanshu',21,'A045','CS')")
c.execute("INSERT INTO students VALUES('Ashish',20,'A019','CS')")
c.execute("INSERT INTO students VALUES('Kritika',19,'A053','CS')")
c.execute("INSERT INTO students VALUES('Divya',19,'A036','CS')")
c.execute("INSERT INTO students VALUES('Hitesh',20,'A046','CS')")
c.execute("INSERT INTO students VALUES('Lakshya',20,'A056','CS')")
c.execute("INSERT INTO students VALUES('Aditya',21,'A08','CS')")
c.execute("INSERT INTO students VALUES('Akshay',20,'A06','CS')")
c.execute("INSERT INTO students VALUES('Abhishek',21,'A01','CS')")
c.execute("INSERT INTO students VALUES('Kushal',21,'A052','CS')")
conn.commit()
# fetching the data
c.execute("SELECT * FROM students")
# putting the result into Dataframe
df = DataFrame(c.fetchall())  
df.columns = ["Name","Age","Roll No.","Branch"]
