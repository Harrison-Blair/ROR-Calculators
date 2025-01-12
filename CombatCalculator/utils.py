# Utility function file for the Reform or Revolution project

import os
import json

UNIT_DEFAULTS = []

def LoadDefaults():
    LoadUnitDefaults()

def CLS():
    # Thanks to Steven D'Aprano, http://www.velocityreviews.com/forums
    if os.name == "posix":
    # Unix, Linux, macOS, BSD, etc.
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
    # DOS/Windows
        os.system('CLS')
    else:
    # Fallback for other operating systems.
        print('\n' * 100)

def PrintMenu(name="MENU NAME", length=80):
    """ Prints a given menu name at a given length with bars surrounding """
    print()
    print("=" * length)
    n = name.center(18)
    print(f"|{n}|" * 4)
    print("=" * length)

def PrintSubheader(name="Subheading", length=80):
    """ Prints a subheading at a given length """
    print(name)
    print("*" * length)

def PrintErrorMenu(error=None):
    """ Prints an error message, and then returns """
    PrintMenu("ERROR MENU")
    print("\nAn error has occured!")
    if (error != None):
        print(f"\n{error}")
    input("\n\x1B[3mPress enter to continue...\x1B[0m")

def LoadUnitDefaults():
    """ Loads the default units from the JSON file """
    global UNIT_DEFAULTS
    with open("units.json", "r") as f:
        UNIT_DEFAULTS = json.load(f)

def PrintUnitStats(numbered=False):
    """ Prints the unit stats table from the loaded defaults """
    if len(UNIT_DEFAULTS) == 0:
        LoadUnitDefaults()

    type_width = 16
    symbol_width = 11
    stat_width = 7
    ukp_width = 25

    if numbered:
        print(f"|{"###".center(stat_width)}|{"TYPE".center(type_width)}|{"SYMBOL".center(symbol_width)}|{"HPS".center(stat_width)}|{"DMG".center(stat_width)}|{"SPD".center(stat_width)}|{"YEARLY UPKEEP".center(ukp_width)}|")
        for i, unit in enumerate(UNIT_DEFAULTS):
            print(f"|{"-" * stat_width}|{"-" * type_width}|{"-" * symbol_width}|{"-" * stat_width}|{"-" * stat_width}|{"-" * stat_width}|{"-" * ukp_width}|")
            if not unit['ukp']:
                print(f"|{str(i).center(stat_width)}|{str(unit['type']).center(type_width)}|{eval(r"'\N" + unit['symbol'] + "'").center(symbol_width)}|{str(unit['hps']).center(stat_width)}|{str(unit['dmg']).center(stat_width)}|{str(unit['spd']).center(stat_width)}|{"N/A".center(ukp_width)}|")
            else:
                print(f"|{str(i).center(stat_width)}|{str(unit['type']).center(type_width)}|{eval(r"'\N" + unit['symbol'] + "'").center(symbol_width)}|{str(unit['hps']).center(stat_width)}|{str(unit['dmg']).center(stat_width)}|{str(unit['spd']).center(stat_width)}|{unit['ukp'][0][1] : >5} {unit['ukp'][0][0].ljust(ukp_width - 6)}|")
                for resource in unit['ukp'][1:]:
                    print(f"|{" " * stat_width}|{" " * type_width}|{" " * symbol_width}|{" " * stat_width}|{" " * stat_width}|{" " * stat_width}|{resource[1] : >5} {resource[0].ljust(ukp_width - 6)}|")
        print(f"|{"-" * stat_width}|{"-" * type_width}|{"-" * symbol_width}|{"-" * stat_width}|{"-" * stat_width}|{"-" * stat_width}|{"-" * ukp_width}|")
    else:
        print(f"|{"TYPE".center(type_width)}|{"SYMBOL".center(symbol_width)}|{"HPS".center(stat_width)}|{"DMG".center(stat_width)}|{"SPD".center(stat_width)}|{"YEARLY UPKEEP".center(ukp_width)}|")
        for unit in UNIT_DEFAULTS:
            print(f"|{"-" * type_width}|{"-" * symbol_width}|{"-" * stat_width}|{"-" * stat_width}|{"-" * stat_width}|{"-" * ukp_width}|")
            if not unit['ukp']:
                print(f"|{str(unit['type']).center(type_width)}|{eval(r"'\N" + unit['symbol'] + "'").center(symbol_width)}|{str(unit['hps']).center(stat_width)}|{str(unit['dmg']).center(stat_width)}|{str(unit['spd']).center(stat_width)}|{"N/A".center(ukp_width)}|")
            else:
                print(f"|{str(unit['type']).center(type_width)}|{eval(r"'\N" + unit['symbol'] + "'").center(symbol_width)}|{str(unit['hps']).center(stat_width)}|{str(unit['dmg']).center(stat_width)}|{str(unit['spd']).center(stat_width)}|{unit['ukp'][0][1] : >5} {unit['ukp'][0][0].ljust(ukp_width - 6)}|")
                for resource in unit['ukp'][1:]:
                    print(f"|{" " * type_width}|{" " * symbol_width}|{" " * stat_width}|{" " * stat_width}|{" " * stat_width}|{resource[1] : >5} {resource[0].ljust(ukp_width - 6)}|")
        print(f"|{"-" * type_width}|{"-" * symbol_width}|{"-" * stat_width}|{"-" * stat_width}|{"-" * stat_width}|{"-" * ukp_width}|")
