#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:01:04 2019

@author: vikram
"""
my_dict={}
list=[]
list2=[]
count=0
count1=0
input_str=input('enter a file name>')
print(input_str)
with open(input_str, mode='rt') as file :
   for line in file:
       list.append(line)
       value=line.split(" ") #create list with seperate
       temp=' '.join(value) #without list join all
       temp2=''.join(value) #without whitespace
       list2=temp2[::]
       print(temp)
       print(value)
       count+=len(temp)
       count1+=len(value)
       if temp2[:] not in my_dict:
           my_dict[temp2[:]]=1
       else:
           my_dict[temp2[:]]+=1
       
      
       
print("words:",count1)       
print("letter(include whitespace):",count)      
print("lines:",len(list))      
       