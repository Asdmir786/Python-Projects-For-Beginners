import random

def hangman():
    # List of words to choose from
    words = ["python", "hangman", "programming", "developer", "code"]
    # Randomly select a word
    word = random.choice(words)
    guessed_word = ["_"] * len(word)  # Create a list to hold the guessed letters
    attempts = 6  # Number of attempts before losing
    guessed_letters = []  # Store guessed letters

    print("Welcome to Hangman!")
    
    while attempts > 0 and "_" in guessed_word:
        print("\nCurrent word: " + " ".join(guessed_word))
        print(f"Attempts left: {attempts}")
        print("Guessed letters: " + ", ".join(guessed_letters))
        
        guess = input("Guess a letter: ").lower()

        # Check if the input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            # Update guessed_word with correct guesses
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print("Incorrect guess.")

    # Game Over
    if "_" not in guessed_word:
        print("\nCongratulations! You've guessed the word: " + word)
    else:
        print("\nGame Over! The word was: " + word)

# Start the game
hangman()
