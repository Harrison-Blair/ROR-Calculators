"""
Utility functions and varibles used across files

Mainly repetative tasks like clearing screen & generating menu headers

Variables are ones used across files, like troop names/types, etc.

"""
import json
import os

# FILE READ/WRITE RELATED FUNCTIONS

def LoadRecentBattles():
    try:
        cdir = os.path.dirname(__file__)
        rdir = "data/playerdata/rbattles.json"
        absdir = os.path.join(cdir, rdir)
        f = open(absdir, 'r')
        data = json.load(f)
        f.close()

        return data
    except Exception as e:
        PrintErrorMenu(str(e))
        return None

def LoadUnitTypes():
    try:
        cdir = os.path.dirname(__file__)
        rdir = "data/units.json"
        absdir = os.path.join(cdir, rdir)
        f = open(absdir, 'r')
        data = json.load(f)
        f.close()

        return data['unit_types']
    except Exception as e:
        PrintErrorMenu(str(e))
        return None

# MENU/VISUAL RELATED FUNCTIONS

def CLS(numlines=100):
    """Clears screen depending on OS"""

    # Thanks to Steven D'Aprano, http://www.velocityreviews.com/forums
    if os.name == "posix":
    # Unix, Linux, macOS, BSD, etc.
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
    # DOS/Windows
        os.system('CLS')
    else:
    # Fallback for other operating systems.
        print('\n' * numlines)

def PrintMenu(name="MENU NAME", length=80):
    """ Prints a given menu name at a given length with bars surrounding """
    print("=" * length)
    n = name.center(18)
    print(f"|{n}|" * 4)
    print("=" * length)

def PrintSubheader(name="Subheading", length=80):
    """Prints a subheading at a given length"""
    print(name)
    print("*" * length)

def PrintErrorMenu(error=None):
    """ Prints an error message, and then returns the player to the previous menu 
    
        print("\n\x1B[3m(italicized!)\x1B[0m") -> Italics in console
    """
    PrintMenu("ERROR MENU")
    print("\nAn error has occured!")
    if (error != None):
        print(f"\n{error}")
    print("\n\x1B[3mPress enter to continue...\x1B[0m")
    input()

def PrintUnitInfoMenu():
    """ Prints the Unit Type data to the console """
    types = LoadUnitTypes()

    if (types == None):
        return

    CLS()
    PrintMenu("UNIT INFO MENU")

    for i in types:
        if (i['id'] > 0):
            print("-" * 65)
            print(f"Unit Name : {i['name'].upper()}")
            print(f"\nStats : ")
            print(f"\t{format("Max Health", "<25")} : {i['hps']}")
            print(f"\t{format("Dammage/Attack", "<25")} : {i['dmg']}")
            print(f"\t{format("Speed", "<25")} : {i['spd']}")
            print(f"\nUpkeep : ")
            for j in i['ukp']:
                print(f"\t- {j[0]} {j[1]}")

    print("\n\x1B[3mPress enter to continue...\x1B[0m")
    input()
            
    