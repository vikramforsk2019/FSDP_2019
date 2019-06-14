"""
Code Challenge
  Name: 
    Centered Average
  Filename: 
    centered.py
  Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is
    the mean average of the values, except ignoring the largest and 
    smallest values in the array. If there are multiple copies of the 
    smallest value, ignore just one copy, and likewise for the largest value. 
    Use int division to produce the final average. You may assume that the 
    array is length 3 or more.
    Take input from user  
  Input: 
    1, 2, 3, 4, 100
  Output:
    3
"""

user_input = input("Enter comma seperated Numbers: ").split(",")

user_list = []

for i in user_input:
    user_list.append(int(i))

# Sorting the list of integers
user_list.sort()

# leaving out 1 smallest and 1 largest value
final_list = user_list[1:-1]

# Calculating average
average = sum( final_list ) / len( final_list )

print ("Average is :", int( average ))
