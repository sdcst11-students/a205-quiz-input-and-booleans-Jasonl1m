"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math
a = float(input("Enter a number = "))
b = float(input("Enter another number = "))
x = input("Are one of the numbers the hypotenuse of a right triangle? ")
if x == "yes":
    if a > b:
        c = (a**2 - b**2)**0.5
        print(f"The missing side is {round(c, 1)}")
    else:
        c = (b**2 - a**2)**0.5
        print(f"The missing side is {round(c, 1)}")
else:
    c = (a**2 + b**2)**0.5
    print(f"The missing side is {round(c, 1)}")
         