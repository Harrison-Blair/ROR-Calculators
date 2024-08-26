"""
Uitls for the CombatCalculator python project
"""

def cls():
    # For easier shorthand screen clearing
    print(chr(27) + "[2J")

def PrintMenu(menu_name):
    bar_size = 80
    
    print("=" * bar_size)

    #^18 to fit the other two pipe characters, *4 to fill out bar_size chars
    print(f"|{menu_name:^18}|"*4)

    print("=" * bar_size)
