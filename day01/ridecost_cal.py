#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:15:08 2019

@author: vikram
"""
""" 
 Problem Statement:
    Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office.
"""
total_dis=80
cost_per_litre=80 
fuel_avg=18       #km/litre
one_km=(1/18) #1km=1/18 liter fuel

total_fuel= one_km*total_dis  #for 80km 
total_cost=total_fuel*cost_per_litre
print(total_cost)

