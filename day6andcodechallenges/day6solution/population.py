# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:42:05 2019

@author: Hitesh

      The given input has a number of rows, each with four fields from a table, containing:

          Rank,City,Population,State or union territory
          1,Mumbai,"12,442,373",Maharashtra


    You are required to output:

        Country, State, Population of the state (obtained by summing up the population of each city in that state)  


    Sample Input

    1,Mumbai,"12,442,373",Maharashtra
    9,Pune,"3,124,458",Maharashtra
    13,Nagpur,"2,405,665",Maharashtra
    6,Chennai,"4,646,732",Tamil Nadu
    59,Salem,"831,038",Tamil Nadu


    Sample Output

    {"key":"India,Tamil Nadu","value":5477770}
    {"key":"India,Maharashtra","value":17972496}

    Explanation

    The population of India,Tamil Nadu is obtained by adding the population of 
    Chennai and Salem. 
    This process is repeated for India,Maharashtra and India,Maharashtra. 

    Refer to population.csv
"""

import csv
with open('population.csv') as pop:
    r = csv.reader(pop, delimiter=',')
    next(r)
    dict1 = {}
    for record in r:
        if dict1.get(record[3]):
            value = record[2].replace(',','')
            dict1["India,"+record[3]] += int(value)
        else:
            value = record[2].replace(',','')
            dict1["India,"+record[3]] =  int(value)
    print(dict1)
    