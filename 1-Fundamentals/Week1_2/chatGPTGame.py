import random


class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def __str__(self):
        return self.name

    def attack(self, other):
        other.hp -= self.attack
        print(f"{self.name} attacks {other.name} for {self.attack} damage!")


class Human(Character):
    def __init__(self):
        super().__init__("Human", 100, 30)


1


class Elf(Character):
    def __init__(self):
        super().__init__("Elf", 80, 40)


class Wizard(Character):
    def __init__(self):
        super().__init__("Wizard", 60, 50)


class Orc(Character):
    def __init__(self):
        super().__init__("Orc", 120, 25)


class Dragon(Character):
    def __init__(self):
        super().__init__("Dragon", 100, 50)


def main():
    # create the characters
    human = Human()
    elf = Elf()
    wizard = Wizard()
    orc = Orc()
    dragon = Dragon()

    # display the menu and get the player's choice
    print("Choose your character:")
    print("1. Human (100 HP, 30 attack)")
    print("2. Elf (80 HP, 40 attack)")
    print("3. Wizard (60 HP, 50 attack)")
    print("4. Orc (120 HP, 25 attack)")
    choice = int(input("Enter your choice: "))

    # create the player character based on the player's choice
    if choice == 1:
        player = human
    elif choice == 2:
        player = elf
    elif choice == 3:
        player = wizard
    elif choice == 4:
        player = orc
    else:
        print("Invalid choice.")
        return

    # start the game loop
    while True:
        # player attacks first
        player.attack(dragon)
        if dragon.hp <= 0:
            print(f"{dragon.name} has been defeated!")
            break
        print(f"{dragon.name} has {dragon.hp} HP remaining.")

        # dragon attacks second
        dragon.attack(player)
        if player.hp <= 0:
            print(f"{player.name} has been defeated!")
            break
        print(f"{player.name} has {player.hp} HP remaining.")


if __name__ == "__main__":
    main()
