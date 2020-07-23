#!/bin/usr/env python

""" Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle. """

# Method 1

class my_solution:
    def area_of_rectangle(area):
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        
        area = length * width
        
        print("The area of the rectangle is: " + str(area))
        
my_solution().area_of_rectangle()

# Method 2

class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w
        
    def rectangle_area(self):
        return self.length * self.width
    
newRectangle = Rectangle(12, 10)

print(newRectangle.rectangle_area())