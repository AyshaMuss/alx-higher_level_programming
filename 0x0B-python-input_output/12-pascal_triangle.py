#!/usr/bin/python3
"""
A function that returns a lists of integers representing the Pascal's triangle of n
"""
def pascal_triangle(n):
    if (n <= 0)
        return []
lst=[1] 
for i in range(5): 
    print(lst) 
    mylist=[] 
    mylist.append(lst[0]) 
    for i in range(len(lst)-1): 
        mylist.append(lst[i]+lst[i+1]) 
    mylist.append(lst[-1]) 
    lst=mylist
