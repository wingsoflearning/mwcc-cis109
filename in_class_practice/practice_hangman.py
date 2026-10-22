import random

wordlist = ["hangman", "llama", "python", "programming", "computer", "software"]
word = random.randint(0, len(wordlist) - 1) 
board = list["_"] * len(word)
bad_guesses = []
max_wrong = 6

while(len(bad_guesses) <=max_wrong and "_" in board):
    print("\nWelcome to Hangman!\n")
    print(f"{board}\n")

    match len(bad_guesses):
        case 0:
            print("\n" *6)
        case 1:
            print("""
+---+
|
|
|
|
======""".strip())
        case 2:
            print("""
+---+
|   |
|
|
|
======""".strip)
        case 3:
            print("""
+---+
|   |
|   O
|
|
======""".strip)
        case 4:
            print("""
+---+
|   |
|   O
|   |
|
======""")
        case 5:
            print("""
+---+
|   |
|   O
|  /|\\
|
======""")
        case 6:
            print("""
+---+
|   |
|   O
|  /|\\
|  / \\""".strip())
            break

    #validation Input
    guess = input("Guess a letter: ") #input guess from user
    if len(guess) != 1 or not guess.isalpha():
        print("\n⚠️ Please enter exactly one letter.\n")
        input("Press [enter] to continue.")
        continue
    if guess in bad_guesses or guess in board:
        print("\n⚠️ You've already guessed that letter!\n")
        input("Press [enter] to continue.")
        continue

    is_found = False
    for i, letter in enumerate(word, start=0):
        if letter == guess:
            board[i] = word[i]
            is_found = True

    if not is_found:
        bad_guesses.append(guess)
        print(f"\n "{guess}" is in the word")