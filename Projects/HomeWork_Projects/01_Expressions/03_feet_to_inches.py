"""
Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.
"""

inch_to_foot = 12

def inch_to_feet():
    feet = float(input("Enter value of feet: "))
    inches = feet * inch_to_foot
    print(f"{feet} feet is {inches:.2f} inches")
    

inch_to_feet()