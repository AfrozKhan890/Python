"""
Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!
The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.
"""
from math import sqrt
def Pythagorean():
    AB = float(input("Enter the length of AB: "))
    AC = float(input("Enter the length of AC: "))

    BC = (AB ** 2) + (AC ** 2)
    print(f"The length of BC(the hypothenus) is: {BC:.2f}")
    

Pythagorean()
