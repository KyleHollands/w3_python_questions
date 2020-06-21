#!/bin/env/usr python

""" Write a Python function to sum all the numbers in a list. """

# Method 1

sample_list = [8, 2, 3, 0, 7]

total = 0

for i in sample_list:
    total = total + i

print(total)

# Method 2

def sum(numbers):
    total = 0
    
    for x in numbers:
        total += x
    return total

print(sum((8, 2, 3, 0, 7)))