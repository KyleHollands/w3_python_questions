#!/usr/bin/env python

import re

""" Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 
These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid. """

# Method 1

class str_validity:
    def val_parantheses(self, s):
       pattern = r'(([{}]+)|([()]+)|([[]]+))+' 
       
       result = re.match(pattern, s)
       
       return result != None
        
print(str_validity().val_parantheses("(){}[]"))
print(str_validity().val_parantheses("()[{)}"))
print(str_validity().val_parantheses("()"))

# Method 2

class py_solution:
    def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0
    
print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))