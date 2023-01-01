

# Declare three variables with the following names:
wizard = 'Wizard'
elf = "Elf"
human = "Human"

# Declare three variables, set to Integer values that indicate the hp of eacH character. (hp stands for hitpoints, which means remaining health.)"""

wizard_hp = 70
elf_hp = 100
human_hp = 1501
dragon_hp = 200


# Declare three more variables having Integer values that indicate the damage of each character (how hard they hit).

wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 30


while True:

    flag = False
    print("-----------------")
    print("1).....Wizard")
    print("2).....Elf")
    print("3).....Human")
    print("-----------------\n")

    inpt = input("Choose your character ").lower()
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

    if flag == False:

        print("\n" + inpt + " Please choose a valid Character\n")

    else:

        print("\nYour choice was " + inpt + " the " + character+"\n")
        print("Health: " + str(my_hp))
        print("Damage: " + str(my_damage))
        print()

    temp_my_hp = my_hp
    temp_dragon_hp = dragon_hp

    while flag:

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

            my_hp = temp_my_hp
            dragon_hp = temp_dragon_hp

            break

        dragon_hp -= my_damage
        if dragon_hp > 0:
            print("The " + c3
                  haracter +
                  " hits the dragon with damge of " + str(my_damage))
            print()
            print("Dragon's health is " + str(dragon_hp))
            print()
        else:
            print(
                "The Dragon has a health of 0 and has lost the batte with the " + character)
            print()

            my_hp = temp_my_hp
            dragon_hp = temp_dragon_hp

            break
