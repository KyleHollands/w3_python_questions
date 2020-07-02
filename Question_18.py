#!/bin/env/usr python

import sys
import os
import re

""" Write a Python program to execute a string containing Python code. """

# Method 1

def exec_string(code):
    i = 0
    return exec(code)
    
exec_string("while(i < 10): i += 1; print(i)")

# Method 2

def exec_string(code):
    ans = int(input("How many variables are required? (Max of 3) "))
    if ans == 1:
        var1 = int(input("Declare 'var1' variable value to be used with code: "))
    if ans == 2:
        var1 = int(input("Declare 'var1' variable value to be used with code: "))
        var2 = int(input("Declare 'var2' variable value to be used with code: "))
    if ans == 3:
        var1 = int(input("Declare 'var1' variable value to be used with code: "))
        var2 = int(input("Declare 'var2' variable value to be used with code: "))
        var3 = int(input("Declare 'var3' variable value to be used with code: "))
    
    exec(code)
    
    return code

exec_string(input("Enter code here: "))

# Method 3

mycode = 'print("hello world")'
code = """
def multiply(x,y):
    return x*y
    
print('Multiple of 2 and 3 is:',multiply(2,3))
"""

exec(mycode)
exec(code)