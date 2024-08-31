"""
Unit Class File for the Reform or Revolution (ROR) Combat Calculator

Holds base class and allows for the creation of a class if no args provided.

Class stats that are tracked officially are as follows:
    - DMG (DAMAGE)              -> Damage dealt over the course of a year
    - HPS (HEALTH)              -> Amount of damage a unit can sustain until it is destroyed
    - SPD (SPEED)               -> Number of cells a unit can move per combat action
    - UKP (UPKEEP)              -> Amount of resources a unit must use to maintain thier combat effectiveness / maximum capacity of resources

Additional/Replacement stats that this calculator will use are as follows:
    - TYPE                      -> The unit's designated type, which will make creating units much easier using a predermined list of units.
    - ABL (ABILITIES)           -> Abilities either active or passive change how damage is dealt in a battle
    - MOD (MODIFIERS)           -> Modifiers given based on resources/terrain/events that dictate combat effectiveness


"""

import utils

class Unit:

    mod_names  = [
                "No Supply", 
                "Ariel Bombardment", 
                "Outdated Technology",
                "Terrain Modifier",
                "Well Equipped"
        ]

    def __init__(self, name=None, cname=None, cid=None, hps=None, max_hps=None, dmg=None, spd=None, ukp=None, mods=None):
        self.name = name
        self.cname = cname
        self.cid = cid
        self.health = hps
        self.max_health = max_hps
        self.damage = dmg
        self.speed = spd
        self.ukp = ukp
        self.mods = mods
        

    def GetStats(self):
        stats = []
        stats.append(['name', self.name])
        stats.append(['cname', self.cname])
        stats.append(['cid', self.cid])
        stats.append(['hps', self.health])
        stats.append(['max_hps', self.max_health])
        stats.append(['dmg', self.damage])
        stats.append(['spd', self.speed])
        stats.append(['ukp', self.ukp])
        stats.append(['mods', self.mods])
        return stats

    def ModifiersMenu(self):
        while True:
            utils.CLS()
            utils.PrintMenu("MOD MENU")
            stats = self.GetStats()
            utils.PrintSubheader("Unit Stats", 65)
            print(f"\t{format("Name", "<10")} : {stats[0][1]}")
            print(f"\t{format("Class", "<10")} : {stats[1][1]}")
            print(f"\t{format("Health", "<10")} : {stats[3][1]} / {stats[4][1]}")
            print(f"\n\t{format("Damage", "<10")} : {stats[5][1]}\t{format("Move-Speed", "<10")} : {stats[6][1]}")
            utils.PrintSubheader("\nUnit Upkeep", 50)
            for i in stats[7][1]:
                print(f"- {i[0]} {i[1]}")
            utils.PrintSubheader("\nCurrent Modifiers", 50)

            mod_values = []
            for name in self.mod_names:
                mod_values.append(0)

            if(stats[8][1] == None or all([ v[1] == 0 for v in stats[8][1] ]) ):
                print("\tNo modifiers so far!")
            else:
                for i in stats[8][1]:
                    if (i[1] != 0.0):
                        print(f"\t- {self.mod_names[i[0]]} : {"+" if i[1] > 0 else ""}{i[1] * 100}%")
                        mod_values[i[0]] = i[1]
                
            utils.PrintSubheader("Menu", 35)
            print("1. No Supply (- 50%)")
            print("2. Increase Ariel Bombardment (- 25%)")
            print("3. Outdated Technology (- 10% PER Year)")
            print("4. Terrain dis/advantage (+/- 5-15%)")
            print("5. Well Equipped (+ 5%)")
            print("99. Reset Modifiers")
            print("\n[E/e] Exit")

            try:
                choice = input("\n>  ")

                if (choice.lower() == "e"):
                    return

                choice = int(choice)

                match choice:
                    case 1:
                        mod_values[choice-1] = round((mod_values[choice-1] - 0.5), 2)
                    case 2:
                        mod_values[choice-1] = round((mod_values[choice-1] - 0.25), 2)
                    case 3:
                        mod_values[choice-1] = round(self.TechModMenu(), 2)
                    case 4:
                        mod_values[choice-1] = round(self.TerrainModMenu(), 2)
                    case 5:
                        mod_values[choice-1] = round((mod_values[choice-1] + 0.05), 2)
                    case 99:
                        utils.PrintSubheader("\nAre you sure? [Y/y]")
                        confirm = input("\n> ")

                        if (confirm.lower() == "y"):
                            mod_values.clear()
                            for i in range(len(self.mod_names)):
                                mod_values.append(0)
                        else:
                            utils.PrintErrorMenu("Reset Cancelled")
                    case _:
                        pass

                mods = []
                for i in range(len(self.mod_names)):
                    mods.append([i, mod_values[i]])

                self.mods = mods

            except Exception as e:
                utils.PrintErrorMenu(str(e))
        
    def TechModMenu(self):
        print()
        utils.PrintSubheader("Tech Mod Menu")

        while True:
            print("How many years outdated is the unit? ")

            try:
                yr = int(input("> "))

                if ( yr >= 0):
                    m = (yr * 0.1)
                    return -m

            except:
                print("***Bad input, try again***")

    def TerrainModMenu(self):
        print()
        utils.PrintSubheader("Terrain Mod Menu")
        
        while True:
            print("Enter a number between - 15 & + 15")

            try:
                per = int(input("> "))

                if (-16 < per < 16):
                    return per / 100

            except:
                print("***Bad input, try again***")
    
