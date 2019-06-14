

from functools import reduce

list1=[1,2,3,4,5,6,7] 
def productOfOdds(list):
    return reduce(lambda x,y:x*y, filter(lambda x:x%2==1, map(lambda x:x,list1)))
print(productOfOdds(list1))




def productOfOdds(list):
    result = 1
    for i in list:
        if i % 2 == 1:
            result *= i
    return result
    
#Rewrite the Python code using map, filter, and reduce:

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))



"""
from functools import reduce
mylist = input().split(',')
def m_func(n):
    return int(n)
    
def f_func(x):
    return x%2 == 1

def r_func(x,y):
    return x*y

def productOfOdds(mylist):
    return reduce(r_func, filter(f_func, (map(m_func, mylist))))

print(productOfOdds(mylist))


