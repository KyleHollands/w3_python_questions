#!/usr/bin/env python

""" Write a Python program to access a function inside a function. """

# Method 1

def outer_function(msg):

    def inner_function():
        print(msg)
        
    inner_function()
    
outer_function("Hello")
        
# Method 2

def print_msg(msg):
    def printer():
        print(msg)
        
    return printer()

another = print_msg("Hello")

# Method 3

def test(a):
    def add(b):
        nonlocal a
        a += 1
        return a + b
    return add

func = test(4)
print(func(4))