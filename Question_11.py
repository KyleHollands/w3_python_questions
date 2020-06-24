#!/bin/env/usr python

""" Write a Python function to check whether a number is perfect or not. """

# Method 1

def check_perfect_num(number):
    total = 0
    
    for i in range(1, number):
        if number % i == 0:
            total += i
            
    if (total * 2) / 2 == number:
        print(number, "is a perfect number.")
    else:
        print(number, "is not a perfect number.")
        
check_perfect_num(6)

# Method 2

def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

print(perfect_number(6))