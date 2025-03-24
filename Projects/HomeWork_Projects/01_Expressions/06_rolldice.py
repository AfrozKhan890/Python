# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

def roll_dice():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2
    
    print("Dice has 6 sides each.")
    print(f"Die1 is {die1}")
    print(f"Die2 is {die2}")
    print(f"The total of the 2 dices is {total}")
    
roll_dice()