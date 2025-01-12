import utils as u
import unit as Unit

class Player:
    def __init__(self):
        try:
            self.LoadPlayerData()
        except Exception as e:
            u.PrintErrorMenu(e)
            self.CreatePlayerData()

    def LoadPlayerData(self):
        raise NotImplementedError("LoadPlayerData() not implemented")

    def SavePlayerData(self):
        pass

    def CreatePlayerData(self):
        u.CLS()
        u.PrintMenu("CREATE PLAYER")
        print("\nWelcome to the Reform or Revolution Combat Calculator!")
        print("\nYou are about to create a new player profile.")
        print("\nPlease enter your country or username, this is how the Calculator will refer to you.")
        print("\nYou can change this later.\n")
        self.name = input("Enter your country or username: ")
        self.units = []
        self.unit_ids = []

        for unit in u.UNIT_DEFAULTS:
            self.unit_ids.append((unit['type'], 0))

        print(self.unit_ids)
        print(self.unit_ids[0][1])
        input()
        

    def ManageUnits(self):
        while True:
            u.CLS()
            u.PrintMenu("UNIT MANAGER")

            # Units Overview
            if len(self.units) != 0:
                u.PrintSubheader("Units Overview")
                # Print all units
                print(f"Units: {len(self.units)}")

            u.PrintSubheader("Manage Units")
            print("1. View Delployed Units Overview")
            print("2. Edit A Unit")
            print("3. Deploy A New Unit")
            print("4. Disband A Unit")
            print("5. View Unit Types")
            print("e. Return to Main Menu")

            try:
                c = input("\nEnter your choice: ")

                if c.lower() == "e":
                    break

                c = int(c)

                match c:
                    case 1:
                        self.UnitDetails()
                    case 2:
                        self.EditUnit()
                    case 3:
                        self.DeployUnit()
                    case 4:
                        self.DisbandUnit()
                    case 5:
                        u.CLS()
                        u.PrintMenu("UNIT TYPES")
                        u.PrintUnitStats()
                        input("\n\x1B[3mPress enter to continue...\x1B[0m")
                    case _:
                        raise Exception("Invalid input, please try again.")
            except:
                u.PrintErrorMenu(Exception("Invalid input, please try again."))

    def UnitDetails(self):
        if len(self.units) == 0:
            u.PrintErrorMenu(Exception("No units to display."))
            return
        
        u.CLS()
        u.PrintMenu("UNIT DETAILS")
        # ID | Army | S TYPE S | HPS | DMG | SPD | UKP
        for unit in enumerate(self.units):
            print(f"{unit.type}")

        input()

    def EditUnit(self):
        pass

    def DeployUnit(self):
        while True:
            u.CLS()
            u.PrintMenu("DEPLOY UNIT")
            u.PrintUnitStats(numbered=True)
            print("\x1B[3mEnter 'e' to return to the previous menu.\x1B[0m")

            try:
                t = input("\nSelect a unit type to deploy: ")

                if t.lower() == "e":
                    return
                
                t = int(t)
                
                if t < 0 or t >= len(u.UNIT_DEFAULTS):
                    raise Exception("Invalid input, please try again.")
                else:
                    self.units.append(Unit.Unit(u.UNIT_DEFAULTS[t]['type'],u.UNIT_DEFAULTS[t]['symbol'],u.UNIT_DEFAULTS[t]['hps'],u.UNIT_DEFAULTS[t]['dmg'], u.UNIT_DEFAULTS[t]['spd'], u.UNIT_DEFAULTS[t]['ukp']))
                    return
            except Exception as e:
                u.PrintErrorMenu(e)

    def DisbandUnit(self):
        pass  
    
        

        
        