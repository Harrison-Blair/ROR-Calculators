"""
Main File for the Reform or Revolution (ROR) Combat Calculator

Holds main menu logic, and the actual main function.
"""

import utils
import battle

def main():
    while True:
        utils.CLS()
        utils.PrintMenu("MAIN MENU")
        print("Welcome to the RoR Combat Calculator!")
        print("\x1B[3mcoded by penguin-thing\x1B[0m")
        print("\nWhat would you like to do?\n")
        print("\t1. Simulate a \x1B[3mnew\x1B[0m Battle")
        print("\t2. Load a \x1B[3mprevious\x1B[0m battle")
        print("\t3. View saved & recent battles")
        print("\t4. View unit types")
        print("\t5. Options")
        
        print("\n\t[e]xit")
        choice = input("\n> ")

        try:
            if (choice.lower() == "e"):
                exit()

            if (0 < int(choice) < 6):
                match int(choice):
                    case 1:
                        battle.Battle()
                    case 4:
                        utils.PrintUnitInfoMenu()
            else:
                raise Exception("Invalid Choice")
        except Exception as e:
            utils.PrintErrorMenu(str(e))
    

if __name__ == "__main__":
    main()