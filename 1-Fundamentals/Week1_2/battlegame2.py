import sys

# Placecode in a function


def game():

    # Declare three variables with the following names:

    wizard = 'Wizard'
    elf = "Elf"
    human = "Human"
    orc = "Orc"

    # Declare three variables, set to Integer values that indicate the health points of each character

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    orc_hp = 170
    dragon_hp = 300

    # Declare variables having Integer values that indicate the damage of each character (how hard they hit)

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 33
    dragon_damage = 30

    # Setup infinite loop

    inpt = ""

    while True:

        # set a flag to help with logic

        flag = False

        print("-----------------")
        print("1).....Wizard")
        print("2).....Elf")
        print("3).....Human")
        print("4).....Orc")
        print("0).....Quit")
        print("-----------------\n")

        # if else elif logic

        inpt = input("Choose your character ").lower()

        if inpt == "0":
            break

        if inpt == "1" or inpt == "wizard":

            flag = True
            character = "wizard"
            my_hp = wizard_hp
            my_damage = wizard_damage

        elif inpt == "2" or inpt == "elf":

            flag = True
            character = "elf"
            my_hp = elf_hp
            my_damage = elf_damage

        elif inpt == "3" or inpt == "human":

            flag = True
            character = "human"
            my_hp = human_hp
            my_damage = human_damage

        elif inpt == "4" or inpt == "orc":
            flag = True
            character = "Orc"
            my_hp = orc_hp
            my_damage = orc_damage

        if flag == False:

            print("\n" + inpt + " Please choose a valid Character\n")

        else:

            print("\nYour choice was " + inpt + " the " + character+"\n")
            print("Health: " + str(my_hp))
            print("Damage: " + str(my_damage))
            print()

        # temporaily store orginal hp valuse

        temp_my_hp = my_hp
        temp_dragon_hp = dragon_hp

        while True:

            my_hp -= dragon_damage

            if my_hp > 0:

                print("The Dragon hit's the " + character +
                      " with damage " + str(dragon_damage))
                print()
                print(character + "'s health is " + str(my_hp))
                print()

            else:

                print("The " + character + " has health of 0 and has lost")
                print()

                # restore hp values

                my_hp = temp_my_hp
                dragon_hp = temp_dragon_hp

                break

            dragon_hp -= my_damage

            if dragon_hp > 0:
                print("The " + character +
                      " hits the dragon with damge of " + str(my_damage))
                print()
                print("Dragon's health is " + str(dragon_hp))
                print()
            else:
                print(
                    "The Dragon has a health of 0 and has lost the batte to " + character)
                print()

                # restore hp values

                my_hp = temp_my_hp
                dragon_hp = temp_dragon_hp

                break

    # Game over section

    for i in range(5):

        print("\n0GAME OVER, Thanks For Playing")

    ply = input("\nWould you like to play again? ").lower()

    # Check to see if user wants to play agian

    if ply == "yes" or ply == "y":
        game()
    else:
        # Terminate program

        print('BYE')
        sys.exit()


game()
