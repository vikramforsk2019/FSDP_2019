#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:08:27 2019

@author: vikram
"""

"""
Code Challenge
  Filename: 
    map2.py
  Problem Statement:
 

      names = ['Mary', 'Isla', 'Sam']

    for i in range(len(names)):
        names[i] = hash(names[i])

    print (names)
    
(Hopefully, the secret agents will have good memories and won’t forget each other’s secret code names during the secret mission.)

Rewrite the above code using map.
    

"""
username = ['Mary', 'Isla', 'Sam']
result =list(map(lambda name:hash(name),username))
 