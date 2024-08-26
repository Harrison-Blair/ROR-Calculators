"""
Unit Template Class
"""
import utils

class Unit:

    def __init__(self):
        # Defaults
        self.active_ability = False
        self.passive_ability = False
        self.modifiers = [0, 0, 0, 0, 0]

        # Get User Input
        self.health = self.GetHealth()
        self.attack = self.GetAttack()
        self.modifiers = self.GetModifiers()
        
    def GetHealth(self):
        utils.cls()
        utils.PrintMenu("HEALTH MENU")
        if (hasattr(self, 'type')):
            match self.type:
                # Infantry
                case 0:
                    max_health = 100
                # Armor
                case 1:
                    max_health = 200
                # Mobile
                case 3:
                    max_health = 100
                # Artillery
                case 4:
                    max_health = 30
                # Shock Troops
                case 5:
                    max_health = 150
                # Paratrooper
                case 6:
                    max_health = 100
                # Partisan
                case 7:
                    max_health = 80
                # Marine
                case 8:
                    max_health = 80
                # Spec Ops
                case 9:
                    max_health = 75
                # Fuck
                case _:
                    max_health = 9999

            while True: 
                print(f"Input the current health of the Unit [1-{max_health}]")

                try:
                    health = int(input())

                    if (0 < health < max_health):
                        return [health, max_health]
                    else:
                        raise TypeError
                except:
                    utils.ErrorInput()

        else:
            print("What the. I have shat the bed.")
            input()
            return [42069, 42069]
        
    def GetAttack(self):
        if (hasattr(self, 'type')):
            match self.type:
                # Infantry
                case 0:
                    return 60
                # Armor
                case 1:
                    return 200
                # Mobile
                case 3:
                    return 50
                # Artillery
                case 4:
                    return 80
                # Shock Troops
                case 5:
                    return 50
                # Paratrooper
                case 6:
                    return 60
                # Partisan
                case 7:
                    return 40
                # Marine
                case 8:
                    return 40
                # Spec Ops
                case 9:
                    return 75
                # Fuck
                case _:
                    return -1
        return -1
    
    def GetModifiers(self):
        # The Number of elements in {modifiers} is equal to the number of options in the list below
        modifiers = self.modifiers
        while True:
            utils.cls()
            utils.PrintMenu("MODIFIER MENU")
            print(type(self))
            print(self.health)
            self.PrintModifiers()
            print(f"Total = {sum(modifiers) * 100}%")
            utils.PrintLine()
            print("1. Aeriel Bombardment (-25%)")
            print("2. No Supply (-50%)")
            print("3. Outdated Tech (-10% PER YEAR)")
            print("4. Terrain dis/advantage (+/- 5-15%)")
            print("5. Well Equiped (+5%)")
            print("6. Reset Modifiers")
            print("7. None/Exit")

            try:
                selection = int(input())
                if not (0 < selection < 8):
                    raise TypeError

                match selection:
                    # Aeriel Bombardment (-25%)
                    case 1:
                        modifiers[0] += -0.25
                    # No Supply (-50%)
                    case 2:
                        modifiers[1] = -0.5
                    # Outdated Tech (-10% PER YEAR)
                    case 3:
                        modifiers[2] = self.GetTechModifier()
                    # Terrain dis/advantage (+/- 5-15%)
                    case 4:
                        modifiers[3] = self.GetTerrainModifier()
                    # Well Equiped (+5%)
                    case 5:
                        modifiers[4] += 0.05
                    # Reset Modifier
                    case 6:
                        if (self.ResetModifier()):
                            modifiers = [0, 0, 0, 0, 0]
                    # No modifier
                    case 7:
                        return modifiers
            except:
                utils.ErrorInput()
        
    def GetTechModifier(self):
        while True:
            utils.cls()
            utils.PrintMenu("TECH-MOD MENU")
            print("\n\033[3m[e] to exit...\033[0m")
            print("\nEnter the # of years outdated this unit is: ")

            try:
                years = input()

                if (years.lower() == "e"):
                    return 0

                years = int(years)
                return (years * -0.1)
            except:
                utils.ErrorInput()

    def GetTerrainModifier(self):
        while True:
            utils.cls()
            utils.PrintMenu("TERRAIN-MOD MENU")
            print("\n\033[3m[e] to exit...\033[0m")
            print("\nIs this a terrain bonus [y/n]?")

            try:
                bonus = input()
                if (bonus.lower() == "y" or bonus.lower() == "n"):
                    while True:
                            print("\nWhat % is the 'bonus' [5-15]?" )
                            try:
                                percent = int(input())

                                if (4 < percent < 16):
                                    if (bonus.lower() == "y"):
                                        return percent/100
                                    else:
                                        return percent/100 * -1
                                else:
                                    raise TypeError
                            except:
                                utils.ErrorInput()
                                break
                elif (bonus.lower() == "e"):
                    return 0
                else:
                    raise TypeError
            except:
                utils.ErrorInput()

    def ResetModifier(self):
        utils.cls()
        utils.PrintMenu("RESET MOD MENU")
        print("\nAre you sure you want to reset the modifiers on this unit?")
        print("\nIf you are sure, input [Y/y] (Any other input will go back to the | MOD MENU |)")

        reset = input()

        if (reset.lower() == "y"):
            return True
        else:
            return False

    def PrintModifiers(self):
        print("CURRENT MODIFIERS:")
        if (sum(self.modifiers) == 0):
            print("\tNone!")
            return
        if (self.modifiers[0] != 0):
            print(f"\tAeriel Bombardment Modifier: {self.modifiers[0] * 100}%")
        if (self.modifiers[1] != 0):
            print(f"\tSupply Modifier: {self.modifiers[1] * 100}%")
        if (self.modifiers[2] != 0):
            print(f"\tTech Modifier: {self.modifiers[2] * 100}%")
        if (self.modifiers[3] != 0):
            print(f"\tTerrain Modifier: {self.modifiers[3]* 100}%")
        if (self.modifiers[4] != 0):
            print(f"\tSupply Modifier: {self.modifiers[4]* 100}%")
    
    def UseAbility(self):
        self.active_ability = not self.active_ability

    def hasPassive(self):
        self.passive_ability = True
    
    def TakeDamage(self, dmg):
        self.health -= dmg

        if (self.health < 0):
            self.health = 0