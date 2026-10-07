# 1. 3x3 matrix representing the game board initialized with dashes
matrix = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# 2. List of players (X goes first as per sample run)
players = ["X", "O"]

# 3. Variable to store the number of turns taken
turns = 0

# 4. Variable to store the winner of the game
winner = None

# 5. Main game loop (runs until 9 turns occur or a winner is found)
while turns < 9 and winner is None:
    # 6. Display the name of the game
    print("\nTIC-TAC-TOE")
    
    # 7. Print the 2-D matrix representing the game board
    for row in matrix:
        print(f"{row[0]} | {row[1]} | {row[2]}")
    print()

    # Determine current player based on turns
    current_player = players[turns % 2]
    
    # 8. Print a message informing whose turn it is
    print(f"{current_player}'s Turn")
    
    # 9 & 16. Prompt user and handle input validation gracefully
    try:
        row_input = input("Enter row (1-3): ")
        col_input = input("Enter column (1-3): ")
        
        # Convert to integers
        row_idx = int(row_input) - 1
        col_idx = int(col_input) - 1
        
        # Check if coordinates are within valid range
        if not (0 <= row_idx <= 2 and 0 <= col_idx <= 2):
            print("Invalid input! Please enter a number between 1 and 3.")
            input("Hit [enter] to continue.")
            continue
            
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
        input("Hit [enter] to continue.")
        continue

    # 10 & 11. Check if spot is occupied or overwrite it
    if matrix[row_idx][col_idx] != "-":
        print(f"\nSomeone has already claimed {row_input}:{col_input}!")
        input("Hit [enter] to continue.")
        continue  # Skip to the next iteration without incrementing turn
    else:
        matrix[row_idx][col_idx] = current_player

    # 12. Check for a horizontal, vertical, or diagonal win
    # Check rows and columns
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] == current_player:
            winner = current_player
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == current_player:
            winner = current_player
            
    # Check diagonals using enumerate to satisfy learning objectives if preferred, 
    # or direct indices for explicit clarity
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == current_player:
        winner = current_player
    if matrix[0][2] == matrix[1][1] == matrix[2][0] == current_player:
        winner = current_player

    # 13. Increment the turn counter at the end of a valid turn
    turns += 1

# Game Over Screen
# 14. Print final board matrix
print("\nTIC-TAC-TOE")
for row in matrix:
    print(f"{row[0]} | {row[1]} | {row[2]}")
print()

# 14 & 15. Check winner or specify a draw message
if winner:
    print(f"{winner} won!")
else:
    print("It's a draw! The board is full.")

print("Game Over!")
print("Thanks for playing!")