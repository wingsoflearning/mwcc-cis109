# gameboard
matrix = [ 
    ["-", "-", "-"], 
    ["-", "-", "-"], 
    ["-", "-", "-"]
]

players= ["X", "O"]

number_of_turns = 0

winner = None

while number_of_turns < 9 and not winner:
    print("\nTIC-TAC-TOE")

    for row in matrix:
        print(f"{row[0]} | {row[1]} | {row[2]}")
    print()
    current_player = players[number_of_turns % 2]
    print(f"{current_player}'s turn")

    #input validation
    try:
        row_input = input("Enter row (1-3): ")
        col_input = input("Enter column (1-3): ")
        # convert to integers
        row_idx = int(row_input) - 1
        col_idx = int(col_input) -1

        if not (0 <= row_idx <= 2 and 0 <= col_idx <=2):
            print("Invalid placement! Please enter a number between 1 and 3.")
            input("Press [enter] to continue.")
            continue
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
        input("Press [enter] to continue.")
        continue

# check if spot is occupied
    if matrix[row_idx][col_idx] != "-":
        print(f"\nSomeone has already claimed {row_input}:{col_input}!")
        input("Press [enter] to continue.")
        continue
    else:
        matrix[row_idx][col_idx] = current_player
        
# check for wins
    # column win
    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == current_player:
            winner = current_player
    # row win
        if matrix[i][0] == matrix[i][1] == matrix[i][2] == current_player:
            winner = current_player
    # diagonal win
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == current_player:
            winner = current_player
    if matrix[0][2] == matrix[1][1] == matrix[2][0] == current_player:
            winner = current_player
    # turn counter at end of turn
    number_of_turns += 1

# Game over screen
print("\nTIC-TAC-TOE")
for row in matrix:
    print(f"{row[0]} | {row[1]} | {row[2]}")
print()

if winner:
    print(f"{winner} won!")
else:
    print("It's a draw! The board is full.")

print("Game Over!")
print("Thanks for playing!")