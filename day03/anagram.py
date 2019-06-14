#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:02:32 2019

@author: vikram
"""
def anagram_fun(input_word1,input_word2):
    if(len(input_word1)==len(input_word2)):
        if(sorted(input_word1)==sorted(input_word2)):
            return 'True'
        else:
            return 'False'
    else:
     return 'False'
input_word1=input('enter first word>')
input_word2=input('enter second word>')
result=anagram_fun(input_word1,input_word2)
if result == 'True' :
    print ("Its Anagram")
else:
    print ("Not Anagram")