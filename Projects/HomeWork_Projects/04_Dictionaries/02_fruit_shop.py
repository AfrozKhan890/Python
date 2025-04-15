"""
There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.
Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.
"""


def fruit_shop():
    fruits = {'apple': 2, 'durian': 5, 'jackfruit': 10, 'kiwi': 8, 'rambutan': 9, 'mango': 5.5}
    
    cost = 0
    for fruit in fruits:
        price = fruits[fruit]
        while True:
            try:
                buy_amount = int(input("How many (" + fruit + ") do you want to buy?: "))
                if buy_amount < 0:
                    print("Please Enter a non-negative value.")
                else:
                    break
            except ValueError:
                print("Please enter a valid Number.")
        cost += (price * buy_amount)
    
    print(f"Your total cost is ${cost}")


fruit_shop()
