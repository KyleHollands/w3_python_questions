#!/bin/env/usr python

import re

"""  Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. """

# Method 1

def findWords(words):
    items = [n for n in words.split('-')]
    items.sort()
    print('-'.join(items))
    
findWords("green-red-yellow-black-white")
findWords("hello-my-name-is-kyle")

# Method 2

words = "hello-my-name-is-john"
items = []

for i in words.split('-'):
    items.append(i)

items.sort()

print('-'.join(items))



