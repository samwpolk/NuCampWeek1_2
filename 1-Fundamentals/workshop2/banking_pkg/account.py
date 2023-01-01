import sys
import os


def show_balance(balance):

    print(f'\nYour current balance is ${balance}')

    return balance


def deposit(balance):

    d = input('\nHow much would like to deposit ')

    balance += float(d)

    return balance


def withdraw(balance):

    if balance <= 0:
        return balance

    w = input('\nHow much would like to withdraw ')

    if float(w) > balance:
        print("\nInsuffient funds")
        return balance

    balance -= float(w)

    return balance


def logout(name):

    print(f'\nGood Bye!  {name}\033[0;37;40m')
    sys.exit()

    return


def screen_clear():

    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':

        os.system('clear')

    else:

        os.system('cls')
