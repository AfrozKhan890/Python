# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).
# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):
# What's your favorite animal? cow
# My favorite animal is also cow!


def main():
    user = input("What is your favorite Animal? ")
    
    # ANSI code for bold and Italic 
    # 033[3;1m = Bold + Italic
    print(f"My favorite animal is \033[3;1m{user}\033[0m!")
    
 
# Ap function ko __name__ kr k if condition use kr k call kr skty ho 
if __name__ =='__main__':
    main()

