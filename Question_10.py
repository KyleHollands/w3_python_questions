#!/bin/env/usr python

""" Write a Python program to print the even numbers from a given list. """

# Method 1

def even_numbers(numbers):
    
    even_list = []
    
    for i in numbers:
        if i % 2 == 0:
            if i not in even_list:
                even_list.append(i)
    print(even_list)

even_numbers([1,2,3,4,5,6,7,8,9])
            
# Method 2

def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum

print(is_even_num([1,2,3,4,5,6,7,8,9]))


