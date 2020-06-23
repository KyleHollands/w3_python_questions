#!/bin/env/usr python

""" Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. """

# Method 1

def calcUpperLower(s):
    lower = 0
    upper = 0
    
    for i in s:
        if i.isalpha():
            if i.isupper():
                upper += 1
            elif i.islower():
                lower += 1
            else:
                pass
    print("Original string: ", s)
    print("# of Upper case characters: ", upper)
    print("# of Lower case characters: ", lower)
        
calcUpperLower("The quick Brown Fox")

# Method 2

def string_test(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass
        
    print("Original string: ", s)
    print("No. of Upper case characters: ", d["UPPER_CASE"])
    print("No. of Lower case characters: ", d["LOWER_CASE"])
    
string_test("The quick Brown Fox")
