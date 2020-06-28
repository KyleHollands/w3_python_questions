#!/bin/env/usr python

import string, sys

""" Write a Python function to check whether a string is a pangram or not. """

""" # Method 1

def pangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
        
string = "The quick brown fox jumps over the lazy dog"

if(pangram(string) == True):
    print("Yes.")
else:
    print("No.") """
    
# Method 2

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

print( ispangram("The quick brown fox jumps over the lazy dog"))


