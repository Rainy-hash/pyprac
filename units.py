"""
This module contains functions for solving geometric shapes and a temperature converter tool.
"""
import math
#This along with the if side statement are to make sure negative numbers and 0 arent calculable
def circle_solver(radius):
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
    diag = side * math.sqrt(2)
    diag_rounded = round(diag, 2)
    return area, perimeter, diag_rounded

def triangle_solver (base, height):
    pass