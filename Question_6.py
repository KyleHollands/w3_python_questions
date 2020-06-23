#!/bin/env/usr python

""" Write a Python function to check whether a number is in a given range. """

# Method 1

def given_range(min_num, max_num):
    num = int(input("Please enter a number: "))
    
    if min_num <= num <= max_num:
        print("Number entered is within range.")
    else:
        print("Number entered is not within range.")
    
given_range(1, 4)

# Method 2

def test_range(n):
    if n in range(3, 9):
        print( " %s is in the range"%str(n))
    else:
        print("The number is outside the given range.")
        
test_range(5)