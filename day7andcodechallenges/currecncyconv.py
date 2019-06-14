#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:21:31 2019

@author: vikram
"""

"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
    https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=ba6f3bf34658b1491f00
"""
import requests
url1="https://free.currconv.com/api/v7/convert"
url2="?q=USD_INR&compact=ultra"
url3="&apiKey=ba6f3bf34658b1491f00"
url=(url1+url2+url3)
print(url)
response = requests.get(url)
response.content
print (type(response.content))
jsondata = response.json()
print (type(jsondata))
print(jsondata)

