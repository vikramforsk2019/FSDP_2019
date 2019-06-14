#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 12:37:10 2019

@author: vikram
"""

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
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
for i in range(1,11):
        bidno=browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div['+str(i)+']/div[1]/p[1]/a')
        item=browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div['+str(i)+']/div[2]/p[1]/span')
        quan=browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div['+str(i)+']/div[2]/p[2]/span')
        address=browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div['+str(i)+']/div[3]/p[2]')
        start=browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div['+str(i)+']/div[4]/p[1]/span')
        End=browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div['+str(i)+']/div[4]/p[2]/span')
        A.append(bidno.text.strip())
        print(A)
        B.append(item.text.strip())#cells[0] remove bcoz it is se no. it take automaticly
        C.append(quan.text.strip())
        D.append(address.text.strip())
        E.append(start.text.strip())
        F.append(End.text.strip())
        

sleep(3)

import pandas as pd
from collections import OrderedDict

col_name = ["BID NO","ITEM","QUANTITY","ADDRESS","START TIME","END TIME"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))
df = pd.DataFrame(col_data) 
df.to_csv("former4.csv")

sleep(2)


browser.quit()
