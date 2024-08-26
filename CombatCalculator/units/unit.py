"""
Unit Template Class
"""
import utils

class Unit:

    def __init__(self):
        self.modifier = self.GetModifier()

    def GetModifier(self):
        mod = 0
        while True:
            mod = round(mod, 2)
            utils.cls()
            utils.PrintMenu("MODIFIER MENU")
            print("CURRENT MODIFIER: " + str(mod * 100) + "%")
            print("1. Aeriel Bombardment (-25%)")
            print("2. No Supply (-50%)")
            print("3. Outdated Tech (-10% PER YEAR)")
            print("4. Terrain dis/advantage (+/- 5-15%)")
            print("5. Well Equiped (+5%)")

            try:
                selection = int(input())
                if not (0 < selection < 6):
                    raise TypeError
                
                match selection:
                    # Aeriel Bombardment (-25%)
                    case 1:
                        mod += -0.25
                    # No Supply (-50%)
                    case 2:
                        mod += -0.5
                    # Outdated Tech (-10% PER YEAR)
                    case 3:
                        mod += self.GetTechModifier()
                    # Terrain dis/advantage (+/- 5-15%)
                    case 4:
                        mod += self.GetTerrainModifier()
                    # Well Equiped (+5%)
                    case 5:
                        mod += 0.05

            except:
                print("ERROR, INVALID INPUT")
                input()
        
    def GetTechModifier(self):
        while True:
            utils.PrintMenu("TECH-MOD MENU")
            print("Enter the # of years outdated this unit is: ")

            try:
                years = int(input())
                return (years * -0.1)
            except:
                print("ERROR, INVALID INPUT")
                input()

    def GetTerrainModifier(self):
        while True:
            utils.PrintMenu("TERRAIN-MOD MENU")
            print("Is this a terrain bonus [y/n]? ")
