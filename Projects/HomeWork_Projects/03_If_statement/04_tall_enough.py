"""
Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.
In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like
Here's two sample runs (user input is in bold italics):
How tall are you? 100
You're tall enough to ride!
How tall are you? 10
You're not tall enough to ride, but maybe next year!
"""


def tell_enough():
    
    height = float(input("Enter your Height: "))
    if height >=50:
        print("You are tall enough to ride.")
    else:
        print("You're not tall enough to ride, but maybe next year!")

tell_enough()