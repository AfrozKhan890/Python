"""
Guess My Number
I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
Enter a new number: 25 Your guess is too low
Enter a new number: 40 Your guess is too low
Enter a new number: 45 Your guess is too low
Enter a new number: 48 Congrats! The number was: 48
"""

import random

def Guessing_Number():
    computer = random.randint(1,100)

    for i in range(1,11):
        user = int(input("Enter a number between 1 to 100: "))
        
        if(user>computer):
            print("Please write lower number")

        elif(user<computer):
            print("Please write higher number")

        else:
            print(f"Congratulations! You have guessed the number in {i} attempts. It is correct.")
            break
    else:
        print(f"Sorry, you've used all your guesses. The number was {computer}.")
    
Guessing_Number()