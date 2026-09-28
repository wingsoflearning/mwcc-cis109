import random

# 1. Wordlist
wordlist = ["hangman", "llama", "python", "programming", "computer", "software"]

# 2. Select a random word from the wordlist
random_number = random.randint(0, len(wordlist) - 1)
secret_word = wordlist[random_number]

# 3. Incorrect letters
bad_guesses = []

# 4. Visible letter board
letter_board = ["_"] * len(secret_word)

# ASCII Gallows Artwork
gallows = [
    # 0 Mistakes
    """+---+
|
|
|
| 
=======""",
    # 1st Mistake: Ready the Gallows!
    """+---+
|   
|
|
| 
=======""",
    # 2nd Mistake: Add the Rope!
    """+---+
|   |
|   
|
| 
=======""",
    # 3rd Mistake: Add the Head.
    """+---+
|   |
|   0
|   
| 
=======""",
    # 4th Mistake: Add the Torso.
    """+---+
|   |
|   0
|   |
| 
=======""",
    # 5th Mistake: Add the Arms.
    """+---+
|   |
|   0
|  /|\\
| 
=======""",
    # 6th Mistake: Add the Legs.
    """+---+
|   |
|   0
|  /|\\
|  / \\
======="""
]

# Helper function to print the clean current game layout
def print_game_screen():
    print("Welcome to HANGMAN!")
    print(letter_board)
    if len(bad_guesses) == 0:
        print("\n\n\n\n\n")  # Blank spacing matching gallows height
    else:
        print(gallows[len(bad_guesses)])
    print(f"Bad Guesses: {bad_guesses}\n")

# 5. Main Game loop
while True:
    print_game_screen()
    guess = input("Guess a letter: ").lower()

    # 6. Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Invalid input! Please enter a single letter.")
        input("\nPress [enter] to continue.")
        continue

    elif guess in bad_guesses or guess in letter_board:
        print("⚠️ You already guessed that letter!")
        input("\nPress [enter] to continue.")
        continue

    # 8. Correct Guess
    if guess in secret_word:
        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                letter_board[index] = guess 

    # 7. Bad Guess
    else:
        bad_guesses.append(guess)
        print(f"❌ '{guess}' is not in the word.")
        input("\nPress [enter] to continue.")

    # 9. Win Condition
    if "_" not in letter_board:
        print(f"✅ '{guess}' is in the word!")
        input("Press [enter] to continue.")
        
        print_game_screen()
        print(f"🎉 YOU WON! The word was '{secret_word}'")
        print("Thank you for playing!")
        break

    # 10. Loss Condition
    if len(bad_guesses) == 6:
        print_game_screen()
        print(f"💀 YOU LOST! The word was '{secret_word}'")
        print("Thank you for playing!")
        break