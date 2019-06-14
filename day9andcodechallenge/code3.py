#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 17:32:07 2019

@author: vikram
"""
"""
Code Challenge 3
In the Bid plus Code Challenege 

          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)

Store the information into a database mySQL Database on cloud 
"""
import mysql.connector 
# connect to  MySQL server along with Database name

conn = mysql.connector.connect(user='abc123_root', password='abc123_root',
                              host='db4free.net', database = 'abc123_root')
#, database = 'forsk_test'

# creating cursor
c = conn.cursor()

# STEP 0
#c.execute("DROP DATABASE employee;")

# STEP 1
#c.execute("CREATE DATABASE employee;")

# STEP 2
c.execute("DROP Table item_list;")

# STEP 3
c.execute ("""CREATE TABLE item_list(
          BidNO TEXT,
          items  TEXT,
          quantity TEXT,
          department_name TEXT,
          start_date TEXT,
          end_date TEXT
          )""")
from  selenium import webdriver
from time import sleep
item_list=[]
#from bs4 import BeautifulSoup as BS

#url = "http://keralaresults.nic.in/sslc2018rgr8364/swr_sslc.htm"
url =  "https://bidplus.gem.gov.in/bidlists"
browser = webdriver.Firefox(executable_path="/home/vikram/anaconda3/geckodriver")
browser.get(url)
#slbrowser.find_element_by_xpatheep(2)
download_file = browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[1]/p[1]/a')
download_file.click()
sleep(5)

for i in range(1,11):
        bidno=browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div['+str(i)+']/div[1]/p[1]/a')
        item=browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div['+str(i)+']/div[2]/p[1]/span')
        quan=browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div['+str(i)+']/div[2]/p[2]/span')
        address=browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div['+str(i)+']/div[3]/p[2]')
        start=browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div['+str(i)+']/div[4]/p[1]/span')
        End=browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div['+str(i)+']/div[4]/p[2]/span')
        print(bidno.text)
        c.execute("INSERT INTO item_list VALUES ('{}','{}', '{}','{}','{}','{}')".format(bidno.text,item.text,quan.text,address.text,start.text,End.text))
conn.commit()   
c.execute("SELECT * FROM item_list")
#print ( c.fetchall()) 
print ( c.fetchone()) 
conn.close()