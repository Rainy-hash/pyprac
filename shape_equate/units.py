"""
This module contains functions for solving geometric shapes and a temperature converter tool.
"""
import math
#This along with the if side statement are to make sure negative numbers and 0 arent calculable
#This file is a set up for the test file which runs the tests and gives an output

def circle_solver (radius):
    if radius <= 0:
        print("Radius must remain above 0")
        return None

    area = math.pi * radius ** 2
    circumference = math.pi * radius * 2
    diameter = 2 * radius
    return area, circumference, diameter

def square_solver (side):
    if side <= 0:
        print("Side length must remain above 0")
        return None

    area = side * side
    perimeter = 4 * side
    diag = round(side * math.sqrt(2), 2) #This line is an effective way to combine round with sqrt, as shown below as well
    return area, perimeter, diag

def triangle_solver (base, height):
    if base <= 0 or height <= 0:
        print("Ensure both values are higher than 0")
        return None

    area = .5 * base * height 
    hypotenuse = round(math.sqrt(base**2 + height**2), 2) #Note to self, ** is for exponentiation, NOT ^
    perimeter = base + height + hypotenuse
    return area, hypotenuse, perimeter
