"""
This file acts as a test, providing numerous inputs for each funciton to prove they are accurate.
"""

from units import *

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

def circle_test(input1, expected_output):
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = circle_solver(input1)
    rounded_result = tuple(round(x, 2) for x in result)
    print(f"Actual result {rounded_result}")
    if rounded_result == expected_output:
        print("SUCCESS")
        return True
    print("FAIL")
    return False

def square_test(input1, expected_output):
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = square_solver(input1)
    rounded_result = tuple(round(x, 2) for x in result)
    print(f"Actual result {rounded_result}")
    if rounded_result == expected_output:
        print("SUCCESS")
        return True
    print("FAIL")
    return False

#Below the function will run and display the tests using the functions above

def main():
    passed = 0
    failed = 0

    for case, expected_output in circle_cases:
        correct = circle_test(case, expected_output)
        if correct:
            passed += 1
        else:
            failed += 1

    for case, expected_output in square_cases:
        correct = square_test(case, expected_output)
        if correct:
            passed += 1
        else:
            failed += 1

    if failed == 0:
        print("ALL TESTS HAVE PASSED")
    else:
        print("FAIL, PLEASE CHECK AGAIN")

main()
