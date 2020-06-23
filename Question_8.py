#!/bin/env/usr python

""" Write a Python function that takes a list and returns a new list with unique elements of the first list. """

# Method 1

def create_list(l):
    
    unique_list = []
    
    for i in l:
        if i not in unique_list:
            unique_list.append(i)
            
    print(unique_list)
    
create_list([1,2,3,3,3,3,4,5])
create_list([5,5,5,3,4,1,3])

# Method 2

def unique_list(l):
    x = []
    
    for a in l:
        if a not in x:
            x.append(a)
    return x
    
print(unique_list([1,2,3,3,3,4,5]))