#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:45:32 2019

@author: vikram
"""

"""
 Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
          7. Name of the PDF file
          
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""
import csv
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
item_list=[]
for i in range(1,11):
 for j in [1,2,3,4]:
    list_item=browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div['+str(i)+']/div['+str(j)+']')
    print(list_item.text)
    print('\n')
    item_list.append(list_item.text)
   # print(item_list)
sleep(3)


with open('item_list.csv', mode='a') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',')
    for row in item_list :
    #print(row)
      employee_writer.writerow([row])

sleep(5)


browser.quit()
