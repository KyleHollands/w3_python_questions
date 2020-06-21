#!/bin/env/usr python

""" Write a Python function to find the Max of three numbers. """

# Method 1

def max_of_three(x, y, z):
    if x > y and x > z:
        return x
    if y > x and y > z:
        return y
    if z > x and z > y:
        return z
        
print(max_of_three(3, 6, -5))

# Method 2

def max_of_two(x, y):
    if x > y:
        return x
    return y
def max_of_three_(x, y, z):
    return max_of_two(x, max_of_two(y, z))

print(max_of_three_(3, 6 ,-5))