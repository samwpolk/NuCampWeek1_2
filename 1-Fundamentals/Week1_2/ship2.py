import random

# Set the size of the game board
board_size = 10

# Set the number and sizes of the ships
ships = [('Aircraft Carrier', 5), ('Battleship', 4),
         ('Submarine', 3), ('Cruiser', 3), ('Patrol Boat', 2)]

# Initialize the game board with all '-' characters
board = [['-' for _ in range(board_size)] for _ in range(board_size)]

# Place the ships on the board at random locations
for name, size in ships:
    # Generate a random starting position for the ship
    x = random.randint(0, board_size - size)
    y = random.randint(0, board_size - 1)

    # Place the ship on the board
    for i in range(size):
        board[x+i][y] = name[0]

# Print the initial game board
print("Initial game board:")
for row in board:
    print(' '.join(row))

# Initialize the number of guesses and hits
num_guesses = 0
num_hits = 0

# Initialize a dictionary to keep track of the ships that have been hit
ships_hit = {name: 0 for name, size in ships}

# Loop until all ships have been hit
while num_hits < sum(size for name, size in ships):
    # Prompt the user to enter a guess
    x = int(input("Enter x coordinate of your guess: "))
    y = int(input("Enter y coordinate of your guess: "))

    # Check if the guess is valid
    if x < 0 or x >= board_size or y < 0 or y >= board_size:
        print("Invalid guess. Please try again.")
        continue

    # Check if the guess is a hit or miss
    if board[x][y] != '-':
        print("HIT!")
        board[x][y] = 'H'
        num_hits += 1

        # Update the number of times the ship has been hit
        ships_hit[board[x][y]] = "H"

        # Check if the ship has been sunk
        for name, size in ships:
            if name[0] == board[x][y] and ships_hit[board[x][y]] == size:
                print("You sank the {}!".format(name))
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
print("You took {} guesses to sink all {} ships.".format(num_guesses, len(ships)))
