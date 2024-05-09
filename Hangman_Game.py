import random

# List of words for the game
words = ["apple", "banana", "orange", "grape", "melon", "strawberry", "kiwi"]

def choose_word(words_list):
    """Choose a random word from the given list."""
    return random.choice(words_list)

def display_word(word, guessed_letters):
    """Display the word with placeholders for unguessed letters."""
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word

def hangman():
    print("Welcome to Hangman!")
    
    # Choose a random word
    secret_word = choose_word(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6  # Set the maximum number of incorrect guesses allowed
    
    while True:
        print("\n" + display_word(secret_word, guessed_letters))
        print(f"Incorrect guesses remaining: {max_attempts - incorrect_guesses}")
        
        if "_" not in display_word(secret_word, guessed_letters):
            print("\nCongratulations! You guessed the word correctly!")
            break
        
        if incorrect_guesses >= max_attempts:
            print("\nSorry, you ran out of guesses. The word was:", secret_word)
            break
        
        guess = input("Guess a letter or type 'exit' to quit: ").lower()
        
        if guess == "exit":
            print("\nGoodbye!")
            break
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in secret_word:
            print("Incorrect guess!")
            incorrect_guesses += 1

# Run the game
hangman()
