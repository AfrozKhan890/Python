# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

def remainder():
    num1 = int(input("Enter the value of an integer to be divided: "))
    num2 = int(input("Enter the value of an integer to divided by: "))

    if num2 != 0:
        remainder = num1 % num2
        quotient = num1 / num2
        print(f"The result of the division: {quotient}\nThe Remainder is {remainder}")
    else:
        print("Error! Division by zero is not allowed.")
    
remainder()