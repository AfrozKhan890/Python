import random

def display_hangman(tries):
    stages = [
        '''
           ------
           |    |
                |
                |
                |
                |
         ---------
        ''',
        '''
           ------
           |    |
           O    |
                |
                |
                |
         ---------
        ''',
        '''
           ------
           |    |
           O    |
           |    |
                |
                |
         ---------
        ''',
        '''
           ------
           |    |
           O    |
          /|    |
                |
                |
         ---------
        ''',
        '''
           ------
           |    |
           O    |
          /|\\   |
                |
                |
         ---------
        ''',
        '''
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
         ---------
        ''',
        '''
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
         ---------
        '''
    ]
    return stages[tries]

def hangman():
    word_list = ["python", "java", "computer", "hangman", "developer", "programming", "algorithm"]
    word = random.choice(word_list).lower()
    word_length = len(word)
    guessed_word = ["_"] * word_length
    guessed_letters = []
    tries = 0
    max_tries = 7

    print("Welcome to Hangman!")
    
    # Main game loop
    while tries < max_tries:
        print(display_hangman(tries))
        print("Word to guess: ", " ".join(guessed_word))
        print(f"Guessed Letters: {', '.join(guessed_letters)}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(word_length):
                if word[i] == guess:
                    guessed_word[i] = guess
            print("Good guess!")
        else:
            tries += 1
            print(f"Wrong guess! You have {max_tries - tries} tries left.")

        if "_" not in guessed_word:
            print("Congratulations! You've guessed the word:", word)
            break
    else:
        print(display_hangman(tries))
        print(f"Sorry, you've lost! The word was: {word}")

hangman()
