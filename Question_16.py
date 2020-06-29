#!/bin/env/usr python

""" Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included). """

# Method 1

square_values = []
i = 1
counter = 1
    
while counter <= 30:
    counter += 1
    square_values.append(counter ** counter)
print(square_values)
    
    
# Method 2

def printValues():
    l = list()
    for i in range(1,21):
        l.append(i**2)
    print(l)
    
printValues()