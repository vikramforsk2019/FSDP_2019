#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:04:23 2019

@author: vikram
"""


"""
Database handling using MongoDB locally 
"""

#use below command in anaconda prompt
#pip install pymongo


from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# create the database if does not exists
mydb = client.employee2



# adding the employee in the employee collection
def add_employee(idd, first, last, pay):
    unique_employee = mydb.employees.find_one({"id":idd})
    if unique_employee:
        return "Employee already exists"
    else:
        mydb.employees.insert(
                {
                "id" : idd,
                "first" : first,
                "last" : last,
                "pay" : pay
                })
        return "Employee added successfully"

def fetch_all_employee():
    user = mydb.employees.find()
    for i in user:
        print (i)



add_employee('01','Sylvester', 'Fernandes', 50000)
add_employee('02','Yogendra', 'Singh', 70000)
add_employee('03','Rohit', 'Mishra', 30000)
add_employee('04','Kunal', 'Vaid', 30000)
add_employee('05','Devendra', 'Shekhawat', 30000)


fetch_all_employee()
    

