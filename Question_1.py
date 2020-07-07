#!/usr/bin/env python

import logging

log = logging.getLogger(__name__)

""" Write a Python class to convert an integer to a roman numeral. """

# Method 1

class py_solution:
    def int_to_roman(self, num):
        
        val = [1000, 900, 500, 400,
               100, 90, 50, 40,
               10, 9, 5, 4, 1]
        symb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"]
        
        roman_num = ""
        i = 0
        
        while num > 0:
            log.debug("Doing something.")
            for _ in range(num // val[i]):
                roman_num += symb[i]
                num -= val[i]
            i += 1
        return roman_num
        
print(py_solution().int_to_roman(1))
print(py_solution().int_to_roman(4000))
print(py_solution().int_to_roman(15))

print(log)
            