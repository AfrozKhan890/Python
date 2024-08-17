# We are going to write a program that generates a random number and asks the user to
# guess it.

# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.

import random

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