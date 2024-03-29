#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 08:33:05 2019

@author: vikram
"""


"""
Code Challenge
  Name: 
    IGN Analysis
  Filename: 
    ign.py
  Problem Statement:
    Read the ign.csv file and perform the following task :
   
   Let's say we want to find games released for the Xbox One 
   that have a score of more than 7.
   
   review distribution for the Xbox One vs the review distribution 
   for the PlayStation 4.We can do this via a histogram, which will plot the 
   frequencies for different score ranges.
   
   
   
  Hint:

    The columns contain information about that game:

    score_phrase — how IGN described the game in one word. 
                   This is linked to the score it received.
    title — the name of the game.
    url — the URL where you can see the full review.
    platform — the platform the game was reviewed on (PC, PS4, etc).
    score — the score for the game, from 1.0 to 10.0.
    genre — the genre of the game.
    editors_choice — N if the game wasn't an editor's choice, Y if it was. This is tied to score.
    release_year — the year the game was released.
    release_month — the month the game was released.
    release_day — the day the game was released.



xbox_one_filter = (reviews["score"] > 7) & (reviews["platform"] == "Xbox One")
filtered_reviews = reviews[xbox_one_filter]
filtered_reviews.head()
      
%matplotlib inline
reviews[reviews["platform"] == "Xbox One"]["score"].plot(kind="hist")

reviews[reviews["platform"] == "PlayStation 4"]["score"].plot(kind="hist")

filtered_reviews["score"].hist()
        
"""
from matplotlib import pyplot as plt
import pandas as pd
#Read csv file
df = pd.read_csv("ign.csv")

# 1.find game name 
filtered_review=df['title'][(df['platform']=='Xbox One') & ( df['score'] > 7) ]

#find

df_xbox = df[df['platform'] == 'Xbox One' ][['score','platform']]

df_play4 = df[df['platform'] == 'PlayStation 4' ][['score','platform']]

xbox_score=df_xbox['score'].tolist()
play4_score=df_play4['score'].tolist()

plt.hist(xbox_score,[0,2,4,6,8,10],label='Xbox One') 

plt.hist(play4_score,[0,2,4,6,8,10],alpha=0.5, histtype='stepfilled', color='pink',edgecolor='black') 
plt.xlabel('Score range')
plt.ylabel('Xbox One and play4')
plt.show()
