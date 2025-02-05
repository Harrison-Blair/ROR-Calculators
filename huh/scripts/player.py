import json

from scripts import economy
from scripts import utils

class Player:
    def __init__(self):
        self.economy = economy.Economy()

    def menu(self):
        options = [
            "Manage Economy",
        ]
        while True:
            utils.CLS()
            utils.PrintMenu("Main Menu", options)

            print("\t[O/o] Player Options")
            print("\n\t[Q/q] Save and Quit")
            choice = input("\n> ")

            if choice.lower() == "o":
                continue #self.playeroptions
            elif choice.lower() == "q":
                self.economy.save_resources()
                break

            try: 
                choice = int(choice)

                match choice:
                    case 0:
                        self.economy.menu()
            except Exception as e:
                utils.PrintErrorMenu(str(e) + "\n\nInvalid input.")


        
