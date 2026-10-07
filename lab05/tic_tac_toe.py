# game board
matrix = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# list of players
players = ["X", "O"]

turns = 0

winner = None

# Main game loop
while turns < 9 and winner is None:
    print("\nTIC-TAC-TOE")
    
    for row in matrix:
        print(f"{row[0]} | {row[1]} | {row[2]}")
    print()

    # Determine current player based on turns
    current_player = players[turns % 2]
    
    # whose turn it is
    print(f"{current_player}'s Turn")
    
    # input validation
    try:
        row_input = input("Enter row (1-3): ")
        col_input = input("Enter column (1-3): ")
        
        # Convert to integers
        row_idx = int(row_input) - 1
        col_idx = int(col_input) - 1
        
        # Check if input is 1-3
        if not (0 <= row_idx <= 2 and 0 <= col_idx <= 2):
            print("Invalid input! Please enter a number between 1 and 3.")
            input("Hit [enter] to continue.")
            continue
            
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
        input("Hit [enter] to continue.")
        continue

    # Check if spot is occupied
    if matrix[row_idx][col_idx] != "-":
        print(f"\nSomeone has already claimed {row_input}:{col_input}!")
        input("Hit [enter] to continue.")
        continue
    else:
        matrix[row_idx][col_idx] = current_player

# Check for winner
    # Check rows and columns
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] == current_player:
            winner = current_player
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == current_player:
            winner = current_player
            
    # Check diagonals  
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == current_player:
        winner = current_player
    if matrix[0][2] == matrix[1][1] == matrix[2][0] == current_player:
        winner = current_player

    # turn counter
    turns += 1

# Game Over Screen
# Print final board matrix
print("\nTIC-TAC-TOE")
for row in matrix:
    print(f"{row[0]} | {row[1]} | {row[2]}")
print()

# Check winner or specify a draw message
if winner:
    print(f"{winner} won!")
else:
    print("It's a draw! The board is full.")

print("Game Over!")
print("Thanks for playing!")