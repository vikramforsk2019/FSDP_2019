#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 17:12:37 2019

@author: vikram
"""
"""
Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.
"""
import pymongo
#import dns # required for connecting with SRV

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
client = pymongo.MongoClient("mongodb://vikram:abc123%5Froot@clusterfirst-shard-00-00-lwlpc.mongodb.net:27017,clusterfirst-shard-00-01-lwlpc.mongodb.net:27017,clusterfirst-shard-00-02-lwlpc.mongodb.net:27017/test?ssl=true&replicaSet=Clusterfirst-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb = client.demo


def add_student(idd, first, last, pay):
    unique_employee = mydb.employees.find_one({"id":idd})
    if unique_employee:
       return "Employee already exists"
    else:
     mydb.demo.insert_one(
            {
            "Student_name" : idd,
            "Student_age" :first ,
            "Student_roll" :last ,
            "Student_branch" :pay
            })
    return "Student added successfully"


def fetch_all_student():
    user = mydb.demo.find()
    for i in user:
        print (i)




add_student('Pandit',22, '16478', 'computer science')


fetch_all_student()