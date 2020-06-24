#!/bin/env/usr python

import os
import sys
import math

""" Write a Python program to print the even numbers from a given list. """

# Method 1

def even_numbers(numbers):
    
    even_list = []
    
    for i in numbers:
        if isinstance(i, int): # Checks if value is an integer.
            if i % 2 == 0: # Checks if value is even.
                if i not in even_list: # Checks if value is in the list already.
                    even_list.append(i)
        else:
            print("Values must be numbers.")
            break
    # print(even_list)
    return even_list

print(even_numbers([1,2,3,4,5,6,7,8,9]))
print(even_numbers([1,5,"g",7,"e"]))
            
# Method 2

""" def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum

print(is_even_num([1,2,3,4,5,6,7,8,9])) """


