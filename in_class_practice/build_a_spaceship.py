import random

#1 destination wordlist
destination_wordlist = ["mars", "venus", "jupiter", "saturn", "uranus", "neptune",]

#2 select a random destination from the wordlist
random_number = random.randint(0, len(destination_wordlist) -1)
secret_destination =destination_wordlist[random_number]

#3 structural failures
structural_failures = []

#4 visible destination board
destination_board = ["_"] * len(secret_destination)

# Spaceship destruction stages (Each exactly 8 lines tall)
spaceship_assembly = [
    #0 mistakes - Clean ship ready for flight
    """
         /\\
        /__\\
        
       |    |
       |    |
      /|    |\\
     /_|____|_\\
       ///\\\\\\""",
       
    #1 mistake - Structural short circuit! Sparks appear on the left wall
    """
         /\\
        /__\\
        
     ⚡|    |
     ⚡|    |
      /|    |\\
     /_|____|_\\
       ///\\\\\\""",
       
    #2 mistakes - Left engine thruster snaps off and explodes underneath
    """
         /\\
        /__\\
        
     ⚡|    |
     ⚡|    |
      /|    |\\
     /_|____|_\\
      💥💥\\\\\\""",
       
    #3 mistakes - The hull plate structural integrity fails, splitting the fuselage down the center
    """
         /\\
        /__\\
        
      ⚡ \\  / |
      ⚡  X  |
      /| / \\|\\
     /_|/___|_\\
      💥//\\\\\\""",
       
    #4 mistakes - The nosecone canopy shatters completely, exposing internal wiring
    """
       💥  💥
        /__\\
        
      ⚡ \\  / |
      ⚡  X  |
      /| / \\|\\
     /_|/___|_\\
      💥//\\\\\\""",
       
    #5 mistakes - The entire starship snaps clean in half right before complete systems failure
    """
       💥    💥
        /_ ⚡  _\\
           ⚡
      ⚡  ⚡   |
      ⚡  ⚡   |
      /|  ⚡   |\\
     /_|  ⚡   |_\\
       💥💥💥  """,
       
    #6 Final mistake - The ship violently rips apart at the seams!
    """
         /  💥
        ⚡  \\
      *  | 💥  |
    💥   |    |   *
      / ⚡    💥 \\
     /__|💥___|__\\
       ⚡   💥 """
]

# Helper function to print clean display
def print_cockpit_display():
    print("=== STARSHIP LAUNCH OPERATIONS ===")
    print(destination_board)
    print(spaceship_assembly[len(structural_failures)])
    print(f"System Faults Logged: {structural_failures}\n")

# 5. Main Game loop
while True:
    print_cockpit_display()
    guess = input("Decrypt coordinate letter: ").lower()

    # 6. Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Decryption Error! Please input a single structural letter.")
        input("\nPress [enter] to cycle system tools.")
        continue

    elif guess in structural_failures or guess in destination_board:
        print("⚠️ Systems warning: Frequency sector already decoded!")
        input("\nPress [enter] to cycle system tools.")
        continue

    # 8. Correct Sector Alignment
    if guess in secret_destination:
        for index in range(len(secret_destination)):
            if secret_destination[index] == guess:
                destination_board[index] = guess 
        
        # 9. Warp Flight Victory Condition
        if "_" not in destination_board:
            print(f"✅ Frequency alignment sector '{guess}' synchronized!")
            input("Press [enter] to engage warp drive.")
            
            print_cockpit_display()
            print(f"🚀 WARP DRIVE ENGAGED! Successfully arrived at '{secret_destination.upper()}'")
            print(f"Safe travels to {secret_destination}, Captain!")
            break

    # 7. Engineering Fault Encountered
    else:
        structural_failures.append(guess)
        print(f"❌ Critical system feedback! Sector '{guess}' rejected.")
        input("\nPress [enter] to bypass short circuit.")

    # 10. Destruction/Loss Condition
    if len(structural_failures) == 6:
        print_cockpit_display()
        print(f"💀 MISSION FAILED! The engines ruptured. The destination was '{secret_destination.upper()}'")
        print("Critical systems destroyed.")
        break