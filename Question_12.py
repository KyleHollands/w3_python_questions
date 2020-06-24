#!/bin/usr/env python

""" Write a Python function that checks whether a passed string is palindrome or not. """

# Method 1

def is_palindrome(word):
    if word == word[::-1]:
        print("Yes")
    else:
        print("No")
    
is_palindrome("malayalam")

# Method 2

def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1
    
    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True

print(isPalindrome('aza'))