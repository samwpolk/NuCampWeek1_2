from banking_pkg import account
import getpass


def atm_menu():

    account.screen_clear()

    print("          === Automated Teller Machine ===          \n")

    # name = input("Enter name to regiser: ")

    while True:

        fname = input("Enter your first name to regiser: ")

        if len(fname) < 1 or len(fname) > 9:

            account.screen_clear()
            print("Please input a first name with between 1 and 10 charactres")

        else:

            break

    while True:

        lname = input("Enter your last  name to regiser: ")

        if len(lname) < 1 or len(lname) > 9:

            account.screen_clear()
            print("Please input a last name with between 1 and 10 charactres")

        else:

            break

    name = fname + " " + lname

    while True:

        pin = getpass.getpass(
            "Enter PIN( PIN will not be written to the screen ): ")

        if len(pin) != 4:

            account.screen_clear()
            print("Please enter in a 4 digit PIN")

        else:

            break

    balance = 0.0

    print(name, "has been registerd with a begining balance of $"+str(balance))

    while True:

        print("LOGIN")

        nameIN = input("Enter first and last name ")
        pinIN = getpass.getpass("Enter PIN: ")

        if pinIN == pin and (nameIN == (fname + " " + lname)):

            print("successful")
            break

    while True:

        print("\033[1;32;40m \n")
        print("          === Automated Teller Machine ===          ")

        print("\033[1;34;40m User: " + name + "\033[1;32;40m")
        print("------------------------------------------")
        print("| 1.    Balance     | 2.    Deposit      |")
        print("------------------------------------------")
        print("------------------------------------------")
        print("| 3.    Withdraw    | 4.    Logout       |")
        print("------------------------------------------\033[0;37;40m")

        option = input("Choose an option: ")

        if option == "1":

            account.show_balance(balance)

        elif option == "2":

            balance = account.deposit(balance)
            account.show_balance(balance)

        elif option == "3":

            balance = account.withdraw(balance)
            account.show_balance(balance)

        elif option == "4":

            account.logout(name)

        else:

            input("Invalid Input, press any key to continue ")


atm_menu()
