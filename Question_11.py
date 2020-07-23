#!/bin/usr/env python

import math

""" Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle. """

# Method 1

class Circle:
    radius = int(input("Enter the radius: "))
        
    def circle_area(self):
        return '{:.2f}'.format((self.radius ** 2 * math.pi))
    
    def circle_circumference(self):
        return '{:.2f}'.format((2 * self.radius * math.pi))
    
print("The area of the circle is: " + str(Circle().circle_area()))
print("The circumference of the circle is: " + str(Circle().circle_circumference()))

# Method 2

class Circle:
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius**2*3.14
    def perimter(self):
        return 2 * self.radius*3.14
    
NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimter())

        

        
        
""" A = pi*r^2
C = 2*pi*r """