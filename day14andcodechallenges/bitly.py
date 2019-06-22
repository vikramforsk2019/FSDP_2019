#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 09:59:38 2019

@author: vikram
"""

"""
Code Challenge
  Name: 
    URL shortening service Bitly
  Filename: 
    bitly.py
  Problem Statement:
    (usagov_bitly_data.json)
    In 2011, URL shortening service Bitly partnered with the US government website
    USA.gov to provide a feed of anonymous data gathered from users who shorten links
    ending with .gov or .mil. 
    In 2011, a live feed as well as hourly snapshots were available
    as downloadable text files. 
    This service is shut down at the time of this writing (2017),
    but we preserved one of the data files.
    In the case of the hourly snapshots, each line in each file contains a common form of
    web data known as JSON. (Use usagov_bitly_data.txt file from Resources)

    Replace the 'nan' values with 'Mising' and ' ' values with 'Unknown' keywords
    Print top 10 most frequent time-zones from the Dataset i.e. 'tz', with and without Pandas
    Count the number of occurrence for each time-zone
    Plot a bar Graph to show the frequency of top 10 time-zones (using Seaborn)
    From field 'a' which contains browser information and separate out browser capability(i.e. the first token in the string eg. Mozilla/5.0)
    Count the number of occurrence for separated browser capability field and plot bar graph for top 5 values (using Seaborn)
    Add a new Column as 'os' in the dataset, separate users by 'Windows' for the values in  browser information column i.e. 'a' that contains "Windows" and "Not Windows" for those who don't

Hint:
    http://1usagov.measuredvoice.com/2011/

"""

#use regular expression for windows in os





import numpy as np
import pandas as pd
data =[]
import json
with open('usagov_bitly_data.json') as infile:
    temp_data = infile.readlines()
    for var in temp_data:
        data.append(json.loads(var))

df =  pd.DataFrame(data)
df.info()

#    Replace the 'nan' values with 'Mising' and ' ' values with 'Unknown' keywords

df=df.replace(r'^\s*$', 'UnKnown', regex=True)

#print(df['c'].replace(r'[NaN]', 'UnKnown', regex=True))


# fill all the records with missing values, with mean of that column

#new=df[df.replace(np.nan,'0')]

#df[df.replace([' ','nan'],['Missing','UnKnown'])]


# Print top 10 most frequent time-zones from the Dataset i.e. 'tz', with and without Pandas

#with pandas
df_time=df.groupby('tz')['tz']
list2=df_time.count()
list4=list2.sort_values(ascending=False)
print(list4.index[1:11])
print(list4.values[1:11])


#without pandas by using counter function
#num = np.bincount(incomes).argmax()
list3=df['tz'].values.tolist()
list_array=np.array(list3)
my_dict={}
for i in list_array:
    if i in my_dict:
        my_dict[i]+=1
    else:
        my_dict[i]=1
  

print(sorted(my_dict.items(), key = 
             lambda kv:(kv[1]))) 
      
#num = np.bincount(list_array).argmax()
#mc = MultiComparison(df['Score'].astype('float'), df['Group'])


# Plot a bar Graph to show the frequency of top 10 time-zones (using Seaborn)

import matplotlib.pyplot as plt
import seaborn as sns 
ax = sns.stripplot(list4.index[1:11], list4.values[1:11])
ax.set(xlabel ='Time-Zones', ylabel ='Frequency') 
plt.show()


"""
  From field 'a' which contains browser information and separate out browser capability(i.e. the first token in the string eg. Mozilla/5.0)
    Count the number of occurrence for separated browser capability field and plot bar graph for top 5 values (using Seaborn)
"""

df_time=df.groupby('a')['a']
list5=df_time.count()

list6=list5.sort_values(ascending=False)
print(list6.index[0:5])
print(list6.values[0:5])

import matplotlib.pyplot as plt
import seaborn as sns 
ax = sns.stripplot(list6.index[0:5], list6.values[0:5])
ax.set(xlabel ='Browser', ylabel ='Frequency') 
plt.show()

"""
Add a new Column as 'os' in the dataset, separate users by 'Windows' for the values
 in  browser information column i.e. 
 'a' that contains "Windows" and "Not Windows" for those who don't

"""


















"""
in temp data={ "a": "Mozilla\/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.25) Gecko\/20111212 Firefox\/3.6.25 ( .NET CLR 3.5.30729; .NET4.0E)", 
"c": "ID", 
"nk": 0, 
"tz": "Asia\/Jakarta", 
"gr": "04", 
"g": "taTNtd",
 "h": "w5jL6k", 
"l": "twitterfeed", 
"al": "en-us,en;q=0.5",
 "hh": "1.usa.gov", 
"r": "http:\/\/t.co\/gybB0nJk", "u": "http:\/\/www.whitehouse.gov\/blog\/2011\/12\/31\/weekly-address-working-together-new-year?utm_source=twitterfeed&utm_medium=twitter", "t": 1325330987, 
"hc": 1325329208,
 "cy": "Jakarta",
 "ll": [ -6.174400, 106.829399 ] 
}

"""