#!/bin/env/usr python

""" Write a Python program to reverse a string. """

# Method 1

def reverse_string(value):
    txt = value[::-1]
    return txt
 
print(reverse_string("Hello."))
print(reverse_string("1234abcd"))

# Method 2

def string_reverse(str1):
    
    rstr1 = ""
    index = len(str1)
    
    while index > 0:
        rstr1 += str1[index - 1]
        index = index - 1
    return rstr1

print(string_reverse('1234abcd'))