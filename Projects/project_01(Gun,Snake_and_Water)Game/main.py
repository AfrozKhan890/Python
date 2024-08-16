import random
'''
Snake = 1 
Water = 2 
Gun = 3
'''

computer = random.choice([1, 2, 3])
userInput = input("Enter your word: (s for Snake), (w for Water) and (g for Gun): ").upper()
myDict = {"S": 1, "W": 2, "G": 3}
reverseDict = {1: "Snake", 2: "Water", 3: "Gun"}

user = myDict.get(userInput)

if user is None:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    print(f"Computer chose {reverseDict[computer]}.")
    print(f"You chose {reverseDict[user]}.")


if(computer == user):
    print("It is a draw.")
    
else:
    if(computer == 1 and user == 2):
        print("You lose!")
    elif(computer == 1 and user == 3):
        print("You Win!")
        
    elif(computer == 2 and user == 3):
        print("You lose!")
    elif(computer == 2 and user == 1):
        print("You Win!")
        
    elif(computer == 3 and user == 1):
        print("You lose!")
    elif(computer == 3 and user == 2):
        print("You Win!")
        
    else:
        print("Something went wrong!")