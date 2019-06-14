#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:52:12 2019

@author: vikram
"""

"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""
import requests
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Udaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"
url = url1 + url2 + url3
print (url)
response = requests.get(url)
response.content
print (type(response.content))s
jsondata = response.json()
print (type(jsondata))
print(jsondata)
print(jsondata['coord'])
print(jsondata['wind']['speed'])
