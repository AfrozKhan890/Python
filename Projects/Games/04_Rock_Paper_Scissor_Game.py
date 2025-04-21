import random

# Rock = 1, Paper = 2, Scissors = 3
computer = random.choice([1, 2, 3])

userInput = input("Enter your choice: (r for Rock), (p for Paper), (s for Scissors): ").upper()

myDict = {"R": 1, "P": 2, "S": 3}
reverseDict = {1: "Rock", 2: "Paper", 3: "Scissors"}

user = myDict.get(userInput)

if user is None:
    print("Invalid input! Please enter 'r', 'p', or 's'.")
else:
    print(f"Computer chose {reverseDict[computer]}.")
    print(f"You chose {reverseDict[user]}.")

    if computer == user:
        print("It's a draw!")
    else:
        if computer == 1 and user == 2:
            print("You win! Paper beats Rock.")
        elif computer == 1 and user == 3:
            print("You lose! Rock beats Scissors.")
        elif computer == 2 and user == 3:
            print("You win! Scissors beats Paper.")
        elif computer == 2 and user == 1:
            print("You lose! Paper beats Rock.")
        elif computer == 3 and user == 1:
            print("You win! Rock beats Scissors.")
        elif computer == 3 and user == 2:
            print("You lose! Scissors beats Paper.")
        else:
            print("Something went wrong!")
