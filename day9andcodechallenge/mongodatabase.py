#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:53:04 2019

@author: vikram
"""

"""
Database handling using MongoDB on Cloud -  Mongo Atlas
"""
#copy cluster
"""


client = pymongo.MongoClient("mongodb://vikram:abc123%5Froot@clusterfirst-shard-00-00-lwlpc.mongodb.net:27017,clusterfirst-shard-00-01-lwlpc.mongodb.net:27017,clusterfirst-shard-00-02-lwlpc.mongodb.net:27017/test?ssl=true&replicaSet=Clusterfirst-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.demo



"""

import pymongo
#import dns # required for connecting with SRV

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
client = pymongo.MongoClient("mongodb://vikram:abc123%5Froot@clusterfirst-shard-00-00-lwlpc.mongodb.net:27017,clusterfirst-shard-00-01-lwlpc.mongodb.net:27017,clusterfirst-shard-00-02-lwlpc.mongodb.net:27017/test?ssl=true&replicaSet=Clusterfirst-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb = client.demo


def add_employee(idd, first, last, pay):
    #unique_employee = mydb.demo.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.demo.insert_one(
            {
            "id" : idd,
            "first" : first,
            "last" : last,
            "pay" : pay
            })
    return "Employee added successfully"


def fetch_all_employee():
    user = mydb.demo.find()
    for i in user:
        print (i)




add_employee(1,'Sylvester', 'Fernandes', '50000')
add_employee(2,'Yogendra', 'Singh', 70000)
add_employee(3,'Rohit', 'Mishra', 30000)
add_employee(4,'Kunal', 'Vaid', 30000)
add_employee(6,'Ram', 'Singh', '30000')

fetch_all_employee()