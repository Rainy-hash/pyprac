"""
This file acts as a test, providing numerous inputs for each funciton to prove they are accurate.
"""
from units import *
#For the cases I have hardcoded the correct answers.
circle_cases = [
    (2, (12.57, 12.57, 4.0)),
    (43, (5808.80, 270.18, 86.0)),
    (12, (452.39, 75.40, 24.00))
]

square_cases = [
    (32, (1024, 128, 45.25)),
    (5, (25, 20, 7.07)),
    (8, (64, 32, 11.31))
]

triangle_cases = [
    (4, 3, (6.0, 5.0, 12.0)),
    (10, 20, (100.0, 22.36, 52.36)),
    (16, 4, (32.0, 16.49, 36.49))
]

def circle_test(radius, expected_output): 
    print(f"Your input is...: {radius}\nExpecting: {expected_output}")
    result =  (tuple(round(x, 2) for x in circle_solver(radius)))
    print(f"Result for area, circumference, and diameter are {result}")
    if result == expected_output:
        print("---")
        print("SUCCESS")
        return True
    print("FAIL")
    return False

def square_test(side, expected_output):
    print(f"Your input is...: {side}\nExpecting: {expected_output}")
    result = tuple(round(x, 2) for x in square_solver(side))
    print(f"Result for area, perimeter, and diagonal are {result}")
    if result == expected_output:
        print("---")
        print("SUCCESS")
        return True
    print("FAIL")
    return False

def triangle_test(base, height, expected_output):
    print(f"Your inputs are...: {base, height}\nExpecting: {expected_output}")
    result = tuple(round(x, 2) for x in triangle_solver(base, height))
    print(f"Result for area, hypotenuse, and perimeter are {result}")
    if result == expected_output:
        print("---")
        print("SUCCESS")
        return True
    print("FAIL")
    return False

#Below the for loops will run and display the tests using the functions above

def main():
    passed = 0
    failed = 0

    for radius, expected_output in circle_cases:
        correct = circle_test(radius, expected_output)
        if correct:
            passed += 1
        else:
            failed += 1

    for side, expected_output in square_cases:
        correct = square_test(side, expected_output)
        if correct:
            passed += 1
        else:
            failed += 1
    
    for base, height, expected_output in triangle_cases:
        correct = triangle_test(base, height, expected_output)
        if correct:
            passed += 1
        else:
            failed += 1

    if failed == 0:
        print("ALL TESTS HAVE PASSED")
    else:
        print("FAIL, PLEASE CHECK AGAIN")

main()
