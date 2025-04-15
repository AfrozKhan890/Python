"""
This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

An example run of the program looks like this (user input is in blue):

Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.
"""

def count_nums():
   
    positions = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh","eigth","ninth","tenth"]
    count_dict = {}
    for num in range(10):
        numbers = int(input(f"Enter {positions[num]} number: "))
        if numbers in count_dict:
            count_dict[numbers] += 1
        else:
            count_dict[numbers] = 1

    sorted_counts = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    
    for numbers, count in sorted_counts:
        print(f"{numbers} appears {count} times.")

count_nums()