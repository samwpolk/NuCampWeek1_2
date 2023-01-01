import random

# Set the size of the game board
board_size = 15

# Set the number of ships
num_ships = 3

# Initialize the game board with all '-' characters
board = [['-' for _ in range(board_size)] for _ in range(board_size)]

# Place the ships on the board at random locations
for _ in range(num_ships):
    x = random.randint(0, board_size - 1)
    y = random.randint(0, board_size - 1)
    board[x][y] = 'S'

# Print the initial game board
print("Initial game board:")
for row in board:
    print(' '.join(row))

# Initialize the number of guesses and hits
num_guesses = 0
num_hits = 0

# Loop until all ships have been hit
while num_hits < num_ships:
    # Prompt the user to enter a guess
    x = int(input("Enter x coordinate of your guess: "))
    y = int(input("Enter y coordinate of your guess: "))

    # Check if the guess is valid
    if x < 0 or x >= board_size or y < 0 or y >= board_size:
        print("Invalid guess. Please try again.")
        continue

    # Check if the guess is a hit or miss
    if board[x][y] == 'S':
        print("HIT!")
        board[x][y] = 'H'
        num_hits += 1
    else:
        print("MISS!")
        board[x][y] = 'M'

    # Increment the number of guesses
    num_guesses += 1

    # Print the updated game board
    print("Updated game board:")
    for row in board:
        print(' '.join(row))

# Print the final game stats
print("You took {} guesses to sink all {} ships.".format(num_guesses, num_ships))5
