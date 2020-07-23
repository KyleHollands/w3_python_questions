#!/bin/usr/env python

"""  Write a Python class which has two methods get_String and print_String. get_String accepts a string from the user and print_String print the string in upper case. """

# Method 1

class convert_lower_to_upper:
    def __init__(self):
        self.input_string = ""
        
    def get_string(self):
        self.input_string = input("Please enter a string to be converted to upper-case: ")
        
    def print_string(self):
        print("The string converted to upper-case: " + self.input_string.upper())
        
output_string = convert_lower_to_upper()
output_string.get_string()
output_string.print_string()