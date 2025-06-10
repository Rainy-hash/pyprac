"""
This module contains functions for solving geometric shapes and a temperature converter tool.
Temperature conversion requires the scale to be uppercase ('F' or 'C').
"""

import math

def circle_solver(radius):
    if radius <= 0:
        print("Radius must remain above 0")
        return
    area = math.pi * radius ** 2
    circumference = math.pi * radius * 2
    diameter = 2 * radius
    print(f"Area: {area}\nCircumference {circumference}\nDiameter {diameter}")

def square_solver (side):
    if side <= 0:
        print("Side length must remain above 0")
        return
    area = side * side
    perimeter = 4 * side
    diag = side * math.sqrt(2)
    diag = round(diag, 2)
    print(f"Square Measurements,\nArea: {area}\nPerimeter: {perimeter}\nDiagonal: {diag}")

def temp_convert(value, scale):
    fahrenheit = 'F'
    celsius = 'C'
    if scale == fahrenheit:
        celsius_value = (value - 32) * 5/9
        rounded_c = round(celsius_value, 2)
        print(f"{value} from Fahrenheit to Celsius is: {rounded_c}")
    elif scale == celsius:
        fahrenheit_value = (value * 9/5) + 32
        rounded_f = round(fahrenheit_value, 2)
        print(f"{value} from Celsius to Fahrenheit is: {rounded_f}")
    else:
        print("Please give a valid value and/or unit please")

square_solver(0)