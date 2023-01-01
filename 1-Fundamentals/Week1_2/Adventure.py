# Adventure game in Python

# import the random module
import random

# list of possible locations
locations = ['desert', 'forest', 'mountain', 'swamp']

# choose a random starting location
current_location = random.choice(locations)

# set the player's initial health
health = 100

# set the player's initial inventory (empty)
inventory = []

# set the player's initial score
score = 0

# set the game to continue until the player quits
playing = True

while playing:
    # display the current location and available actions
    print(f"You are currently in the {current_location}.")
    print("What do you want to do?")
    print("1. Look for items")
    print("2. Travel to a new location")
    print("3. Quit the game")

    # get the player's input
    choice = input("> ")

    # look for items
    if choice == "1":
        # choose a random item to find
        found_item = random.choice(['food', 'water', 'medicine', 'weapon'])
        # add the item to the inventory
        inventory.append(found_item)
        print(f"You found a {found_item}!")

    # travel to a new location
    elif choice == "2":
        # choose a new random location
        current_location = random.choice(locations)
        print(f"You are now in the {current_location}.")
1
   # quit the game
   elif choice == "3":
        playing = False

    # invalid input
    else:
        print("Invalid input. Please try again.")

# display the final score
print(f"Your final score is {score}.")
