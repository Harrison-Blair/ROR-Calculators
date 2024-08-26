"""
Uitlity functions for the CombatCalculator python project
"""
import os

bar_size = 80

def cls():
    # For easier shorthand screen clearing
    os.system("cls")

def PrintLine():
    print("-" * bar_size)

def PrintMenu(menu_name):
    print("=" * bar_size)

    #^18 to fit the other two pipe characters, *4 to fill out bar_size chars
    print(f"|{menu_name:^18}|"*4)

    print("=" * bar_size)

def ErrorInput():
    print("\n" * 1)
    print("=" * bar_size)
    print(f"|{"ERRONIOUS INPUT":^18}|"*4)
    print("=" * bar_size)
    print("\nInvalid input, try again.")
    print("\n\n\033[3mpress anything to continue...\033[0m")
    input()
