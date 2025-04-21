def computer_guesses_number():
    low = 1
    high = 100
    attempts = 0

    print("🤖 Think of a number between 1 and 100, and I’ll try to guess it!")

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it too high (H), too low (L), or correct (C)? ").strip().lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"🎉 Yay! I guessed your number in {attempts} tries.")
            break
        else:
            print("Please enter 'H', 'L', or 'C'.")
            
computer_guesses_number()