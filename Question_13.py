#!/bin/usr/env python

""" Write a Python function that prints out the first n rows of Pascal's triangle. """

""" # Method 1
 
n = int(input("Enter number of rows: "))
a = []

for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1, i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(n != 0):
        a[i].append(1)
        
for i in range(n):
    print("    "*(n-i), end="  ", sep="   ")
    for j in range(0, i+1):
        print('{0:6}'.format(a[i][j]), end="  ", sep="  ")
    print() """
    
# Method 2

def pascal_triangle(n):
    trow = [1]
    y = [0]
    
    for x in range(max(n, 0)):
        print(trow)
        trow = [l+r for l, r in zip(trow + y, y + trow)]
    return n >= 1

pascal_triangle(6)