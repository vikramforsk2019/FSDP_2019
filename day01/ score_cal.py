#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:31:34 2019

@author: vikram
"""

"""
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
    
    """
             ass_one=50
    ass_two=50
    ass_third=80
    exam_one=30
    exam_two=50
    ass_res_weight=(ass_one+ass_two+ass_third)*0.1
    
    exam_res_weight=(exam_one+exam_two)*0.35
    
    total_weight_score=  ass_res_weight + exam_res_weight
    print(total_weight_score)
    
    