# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1: int = random.randint(1, 6)
    die2: int = random.randint(1, 6)
    return die1,die2


def main():
    for i in range(3):
        die1 ,die2 = roll_dice()
        print("Die1 is",die1 , "and Die2 is", die2)
        total: int = die1 + die2
        print(f"Total of two dices: {total} \n")

main()