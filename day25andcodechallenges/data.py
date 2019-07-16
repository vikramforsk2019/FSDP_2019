#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:46:56 2019

@author: vikram
"""

Q3. """Code Challenge -
Data: "data.csv"

This data is provided by The Metropolitan Museum of Art Open Access
1. Visualize the various countries from where the artworks are coming.
2. Visualize the top 2 classification for the artworks
3. Visualize the artist interested in the artworks
4. Visualize the top 2 culture for the artworks
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('data.csv')

b=dataset['Country'].value_counts()

import matplotlib.pyplot as plt
p1=list(b.index)
p2=list(b.values)
plt.pie(p2,labels=p1, autopct='%.0f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


b=dataset['Classification'].value_counts()
p1=list(b.index[0:2])
p2=list(b.values[0:2])
plt.pie(p2,labels=p1, autopct='%.0f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

b=dataset['Artist Role'].value_counts()
import matplotlib.pyplot as plt
p1=list(b.index)
p2=list(b.values)
plt.pie(p2,labels=p1, autopct='%.0f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


b=dataset['Culture'].value_counts()
p1=list(b.index[0:2])
p2=list(b.values[0:2])
plt.pie(p2,labels=p1, autopct='%.0f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

