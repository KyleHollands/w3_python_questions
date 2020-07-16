#!/bin/usr/env python

""" Write a Python class to implement pow(x, n) """

# Method 1

class my_solution:
    def pow_of_two(self, num1, num2):
        result = (num1 ** num2)

        print(result)
        
my_solution().pow_of_two(2,-3)
my_solution().pow_of_two(3,5)

# Method 2

def power(x, y): 
  
    if (y == 0): return 1
    elif (int(y % 2) == 0): 
        return (power(x, int(y / 2)) *
               power(x, int(y / 2))) 
    else: 
        return (x * power(x, int(y / 2)) *
                   power(x, int(y / 2))) 
  
# Driver Code 
x = 0; y = 4
print(power(x, y))

