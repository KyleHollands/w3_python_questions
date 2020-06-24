#!/bin/env/usr python

""" Write a Python function that takes a number as a parameter and check the number is prime or not. """

# Method 1

def check_prime(number):

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number.")
                break
        else:
            print(number, "is a prime number.")
            
    else:
        print(number, "is not a prime number.")

check_prime(4)
        
# Method

def test_prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2, n):
            if (n % x == 0):
                return False
        return True
        
print(test_prime(9))
        
    
    
    