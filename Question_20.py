#!/bin/usr/env python

""" Write a Python program to detect the number of local variables declared in a function. """

# Method 1

def fun():
    a = 1
    str = "Hello"
    doub = 44.23

print(fun.__code__.co_nlocals)

# Method 2

def geek():
    pass

def fun():
    a, b, c = 1, 2.25, 333
    str = "GeeksForGeeks"
    
print(geek.__code__.co_nlocals)
print(fun.__code__.co_nlocals)

# Method 3

def abc():
    x = 1
    y = 2
    str1 = "w3resource"
    print("Python Exercises")
    
print(abc.__code__.co_nlocals)
