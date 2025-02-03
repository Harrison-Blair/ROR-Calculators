import os

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

def PrintMenu(name="MENU NAME", options=[], length=150):
    """ Prints a given menu name at a given length with bars surrounding """
    print("=" * (length + 1))
    if len(name) < 25:
        for i in range(int(length / 25)):
            print(f"/" + name.center(24), end="")
    elif len(name) < 30:
        for i in range(int(length / 30)):
            print(f"/" + name.center(29), end="")
    elif len(name) < 50:
        for i in range(int(length / 50)):
            print(f"/" + name.center(49), end="")
    else:
        print(f"/" + name.center(length - 1), end="")
    print("/")
    print("=" * (length + 1))

    if len(options) > 0:
        for i, option in enumerate(options):
            print(f"\t{i}. {option}")

def PrintErrorMenu(error=None):
    """ Prints an error message, and then returns """
    PrintMenu("ERROR MENU")
    print("\nAn error has occured!")
    if (error != None):
        print(f"\n{error}")
    input("\n\x1B[3mPress enter to continue...\x1B[0m")