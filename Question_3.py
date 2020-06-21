#!/bin/env/usr python

""" Write a Python function to multiply all the numbers in a list. """

# Method 1

def mult_num(numbers):
    
    total = 1
    
    for x in numbers:
        total *= x
    return total
    
print(mult_num((8, 2, 3, -1, 7)))