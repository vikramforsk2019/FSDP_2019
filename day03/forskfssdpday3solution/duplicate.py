"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values
    with original order reserved  
"""


# version 1


# given list
given_list =  [12,24,35,24,88,120,155,88,120,155]

# parsing given list into set to remove duplicate entries
# then again parsing it back to list
output_list = list(set(given_list))

# reversing the new list
output_list.sort()

print(output_list)




# version 2


# given list
given_list =  [12,24,35,24,88,120,155,88,120,155]
output_list  = []

# loop to remove duplicate values
for item in given_list:
    if item in output_list:
        pass
    else:
        output_list.append(item)


print(output_list)





