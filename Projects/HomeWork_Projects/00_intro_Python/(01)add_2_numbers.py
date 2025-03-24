# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:
# Prompt the user to enter the first number.
# Read the input and convert it to an integer.
# Prompt the user to enter the second number.
# Read the input and convert it to an integer.
# Calculate the sum of the two numbers.
# Print the total sum with an appropriate message.


def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    addition = num1 + num2
    print(f"The sum of {num1} and {num2} is equal to {addition}. ")
 

# Ap function ko __name__ kr k if condition use kr k call kr skty ho 
if __name__ =='__main__':
    main()

