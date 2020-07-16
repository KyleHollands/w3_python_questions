#!/bin/usr/env python

import re

""" Write a Python class to reverse a string word by word. """

# Method 1

class my_solution:
    def reverse_sentence(self, sentence):
    
        r = ' '.join(reversed(sentence.split(' ')))
        
        print(r)
            
    
my_solution().reverse_sentence("This is a test sentence.")

# Method 2

class my_solution:
    def reverse_sentence(self, sentence):
        punctuations = ':;,.!?'
        match = re.search(r'([:;,.!?]+)$', sentence)
        
        end_puncs = match.group(1) if match is not None else ''
        rev = ' '.join(reversed(re.findall('[\w:;,.!?]+', sentence.rstrip(punctuations)))) + end_puncs
        
        print(rev)
            
    
my_solution().reverse_sentence("This is a test sentence.")

# Method 3

class my_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))
    
print(my_solution().reverse_words('hello .py'))

