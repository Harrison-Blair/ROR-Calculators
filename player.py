import json
import utils
import comodity

class Player:
    def __init__(self, info, IndustrialScores, Resources, PublicIndustry, ImportExport, Stockpile, Consumption):
        # Country Info
        self.info = info

        # Resource lists
        self.Resources = Resources

        # Industry, Agriculture, Mining Scores
        self.IndustrialScores = IndustrialScores

        # Public Industry
        self.PublicIndustry = PublicIndustry

        # Private Industry
        self.PrivateIndustry = self.CalculatePrivateIndustry()

        # Imports and Exports
        self.ImportExport = ImportExport

        self.Stockpile = Stockpile

        # Consumption
        self.Consumption = Consumption
        self.CalculateIndustryConsumption()

        self.SavePlayer()

    def SavePlayer(self):
        PlayerData = {}

        # Country Info
        PlayerData['info'] = self.info

        # Industry, Agriculture, Mining Scores
        PlayerData['IndustrialScores'] = self.IndustrialScores

        # Industry, Agriculture, Mining assignments/allocations
        PlayerData['PublicIndustry'] = self.PublicIndustry

        # Imports, Exports
        PlayerData['ImportExport'] = self.ImportExport

        # Stockpile
        PlayerData['Stockpile'] = self.Stockpile

        # Consumption [Pop] [Ind] [Gov]
        PlayerData['Consumption'] = self.Consumption

        with open('player.json', 'w') as file:
            json.dump(PlayerData, file)

        resources = []
        for s in self.Resources:
            for r in s:
                resources.append(r.__dict__)

        with open('resources.json', 'w') as file:
            json.dump(resources, file)
                

    def PrintInfo(self):
        for key, value in self.info.items():
            if key == "population":
                print(f"{key.upper()}: {value} Million")
                continue
            if key == "policy":
                print(f"POLICIES:")
                for k, v in value.items():
                    print(f"\t{k}: {v}")
                continue
            print(f"{key.upper()}: {value}")

    def main(self):
        while True:
            utils.CLS()
            utils.PrintMenu("Main Menu")
            self.PrintInfo()

            print("Menu")
            print("-" * 45)
            options = [
                "View Detailed Industry Overview",
                "Increase Industry",
                "Allocate Industry",
                "Manage Imports/Exports",
                "Modify Country Info"
            ]
            for num, opt in enumerate(options):
                print(f"{num}. {opt}")
            print("[O/o] Game Options")
            print("[E/e] Save and Exit")

            c = input(f"\nEnter a number [0-{len(options) - 1}]: ")

            if c.lower() == "b":
                continue

            if c.lower() == "o":
                self.GameOptions()
                continue

            if c.lower() == "e":
                self.SavePlayer()
                return
            
            try:
                c = int(c)

                match c:
                    case 0:
                        self.ViewDetailedIndustryOverview()
                    case 1:
                        self.IncreaseIndustry()
                    case 2:
                        self.AllocateIndustry()
                        self.CalculateIndustryConsumption()
                        self.PrivateIndustry = self.CalculatePrivateIndustry()
                    case 3:
                        self.ManageImportsExports()
                    case 4:
                        self.ModifyPlayerInfo()
                        self.PrivateIndustry = self.CalculatePrivateIndustry()
                    case _: # Default
                        raise Exception("Invalid input")
            except Exception as e:
                utils.PrintErrorMenu(e) 

    def PrintResources(self, type=None, id=None, perpop=False):
        popmod = 1.0
        if not perpop:
            popmod = self.info["population"]

        #"| # | NAME | INGREDIENTS | SP | P-CON | I-REQ | GOV | EXP | IMP | PRI-I | PUB-I | ISA | ISC | Q | M-V | FACILILITY |"
        #"  5    25        25         7      7       7     7      7     7      7       7      7     7    5    7        20    "
        columns = ["#", "NAME", "INGREDIENTS", "SP", "P-CON", "I-REQ", "GOV", "EXP", "IMP", "PRI-I", "PUB-I", "ISA", "ISC", "Q", "M-V", "FACILITY"]
        widths = [5, 25, 25, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 5, 7, 20]
        industries = [type] if type is not None else range(3)
        for i in industries: # Headers
            match i:
                case 0:
                    print("Agriculture".center(sum(widths) + len(widths) - 1))
                case 1:
                    print("Mining".center(sum(widths) + len(widths) - 1))
                case 2:
                    print("Industry".center(sum(widths) + len(widths) - 1))
            print("+" + "-" * (sum(widths) + len(widths) - 1) + "+")
            
            print("|", end="") # Table Header
            for col in columns: 
                print(col.center(widths[columns.index(col)]) + "|", end="")
            
            print("\n+", end="")
            for col in columns: # Header Divider
                print("-" * widths[columns.index(col)] + "+", end="")

            for rid, res in enumerate(self.Resources[i]):
                res : comodity.Comodity = res
                if id is not None and rid != id:
                    continue

                try: # Attempt to get recipies
                    for recid, recipie in enumerate(res.Ingredients):
                        if recid != 0:
                            print(f"\n|"+ " ".center(widths[0]) + "|", end="")
                            print(f" ".center(widths[1]) + "|", end="")
                            print(f"OR".center(widths[2]) + "|", end="")
                            print(f" ".center(widths[3]) + "|", end="")
                            print(f" ".center(widths[4]) + "|", end="")
                            print(f" ".center(widths[5]) + "|", end="")
                            print(f" ".center(widths[6]) + "|", end="")
                            print(f" ".center(widths[7]) + "|", end="")
                            print(f" ".center(widths[8]) + "|", end="")
                            print(f" ".center(widths[9]) + "|", end="")
                            print(f" ".center(widths[10]) + "|", end="")
                            print(f" ".center(widths[11]) + "|", end="")
                            print(f" ".center(widths[12]) + "|", end="")
                            print(f" ".center(widths[13]) + "|", end="")
                            print(f" ".center(widths[14]) + "|", end="")
                            print(f" ".center(widths[15]), end="")
                        for resid, resource in enumerate(recipie):
                            if resid == 0:
                                print(f"\n|{str(rid).center(widths[0])}|", end="")
                                print(f"{res.name.center(widths[1])}|", end="")
                                print(f"{str(resource[1]).center(5)},{resource[0].center(widths[2] - 6)}|", end="")
                                print(f"{str(self.Stockpile[i][rid][1][recid]).center(widths[3])}|", end="")
                                print(f"{str(self.Consumption[0][i][rid][1][recid] * popmod).center(widths[4])}|", end="")
                                print(f"{str(self.Consumption[1][i][rid][1][recid]).center(widths[5])}|", end="")
                                print(f"{str(self.Consumption[2][i][rid][1][recid]).center(widths[6])}|", end="")
                                print(f"{str(self.ImportExport[i][rid][1][1][recid]).center(widths[7])}|", end="")
                                print(f"{str(self.ImportExport[i][rid][1][0][recid]).center(widths[8])}|", end="")
                                print(f"{str(self.PrivateIndustry[i][rid][1][recid]).center(widths[9])}|", end="")
                                print(f"{str((self.PublicIndustry[i][rid][1][recid] / res.ISC) * res.Quantity).center(widths[10])}|", end="")
                                print(f"{str(self.PublicIndustry[i][rid][1][recid]).center(widths[11])}|", end="")
                                if recid == 0:
                                    print(f"{str(res.ISC).center(widths[12])}|", end="")
                                    print(f"{str(res.Quantity).center(widths[13])}|", end="")
                                    print(f"{str(res.Cost).center(widths[14])}|", end="")
                                    print(f"{res.Facility.center(widths[15])}", end="")
                                else:
                                    print(f" ".center(widths[12]) + "|", end="")
                                    print(f" ".center(widths[13]) + "|", end="")
                                    print(f" ".center(widths[14]) + "|", end="")
                                    print(f" ".center(widths[15]), end="")
                            else:
                                print(f"\n|{str(rid).center(widths[0])}|", end="")
                                print(f"".center(widths[1]) + "|", end="")
                                print(f"{str(resource[1]).center(5)},{resource[0].center(widths[2] - 6)}|", end="")
                                print(f" ".center(widths[3]) + "|", end="")
                                print(f" ".center(widths[4]) + "|", end="")
                                print(f" ".center(widths[5]) + "|", end="")
                                print(f" ".center(widths[6]) + "|", end="")
                                print(f" ".center(widths[7]) + "|", end="")
                                print(f" ".center(widths[8]) + "|", end="")
                                print(f" ".center(widths[9]) + "|", end="")
                                print(f" ".center(widths[10]) + "|", end="")
                                print(f" ".center(widths[11]) + "|", end="")
                                print(f" ".center(widths[12]) + "|", end="")
                                print(f" ".center(widths[13]) + "|", end="")
                                print(f" ".center(widths[14]) + "|", end="")
                                print(f" ".center(widths[15]), end="")
                except: # No recipies
                    print(f"\n|{str(rid).center(widths[0])}|", end="")
                    print(f"{res.name.center(widths[1])}|", end="")
                    print(f"{"-".center(widths[2])}|", end="")
                    print(f"{str(self.Stockpile[i][rid][1]).center(widths[3])}|", end="")
                    print(f"{str(self.Consumption[0][i][rid][1] * popmod).center(widths[4])}|", end="")
                    print(f"{str(self.Consumption[1][i][rid][1]).center(widths[5])}|", end="")
                    print(f"{str(self.Consumption[2][i][rid][1]).center(widths[6])}|", end="")
                    print(f"{str(self.ImportExport[i][rid][1][1]).center(widths[7])}|", end="")
                    print(f"{str(self.ImportExport[i][rid][1][0]).center(widths[8])}|", end="")
                    print(f"{str(self.PrivateIndustry[i][rid][1]).center(widths[9])}|", end="")
                    print(f"{str((self.PublicIndustry[i][rid][1] / res.ISC) * res.Quantity).center(widths[10])}|", end="")
                    print(f"{str(self.PublicIndustry[i][rid][1]).center(widths[11])}|", end="")
                    print(f"{str(res.ISC).center(widths[12])}|", end="")
                    print(f"{str(res.Quantity).center(widths[13])}|", end="")
                    print(f"{str(res.Cost).center(widths[14])}|", end="")
                    print(f"{res.Facility.center(widths[15])}", end="")
                print("\n+", end="")
                for col in columns: # Header Divider
                    print("-" * widths[columns.index(col)] + "+", end="")
            print()

    def SortResources(self):
        # Alphabetically
        for i in range(len(self.Resources)):
            self.Resources[i].sort(key=lambda x: x.name)
            self.PublicIndustry[i].sort(key=lambda x: x[0])
            self.PrivateIndustry[i].sort(key=lambda x: x[0])
            self.ImportExport[i].sort(key=lambda x: x[0])
            self.Stockpile[i].sort(key=lambda x: x[0])
            for j in range(3):
                self.Consumption[j][i].sort(key=lambda x: x[0])

        

        self.SavePlayer()

    def ViewDetailedIndustryOverview(self): # TODO: I feel this could be better/more descriptive somehow
        utils.CLS()
        utils.PrintMenu("Det. Ind. Overview")

        self.PrintResources(0)
        self.PrintResources(1)
        self.PrintResources(2)

        print(f"Agriculture Score (ISA/AS): {sum(i[1] for i in self.PublicIndustry[0])}/{self.IndustrialScores[0]}")
        print(f"Mining Score (ISA/MS): {sum(i[1] for i in self.PublicIndustry[1])}/{self.IndustrialScores[1]}")
        print(f"Industry Score (ISA/IS): {sum(sum(i[1]) for i in self.PublicIndustry[2])}/{self.IndustrialScores[2]}")

        input("\nPress Enter to continue...")

    def IncreaseIndustry(self):
        while True:
            try:
                utils.CLS()
                utils.PrintMenu("Increase Industry")
                options = [
                    "Agriculture",
                    "Mining",
                    "Industry"
                ]
                for num, opt in enumerate(options):
                    print(f"{num}. {opt}: ", end="")
                    if num == 2:
                        print(f"({sum(sum(i[1]) for i in self.PublicIndustry[num])}/{self.IndustrialScores[num]})")
                    else:
                        print(f"({sum(i[1] for i in self.PublicIndustry[num])}/{self.IndustrialScores[num]})")
                print("[E/e] Exit")
                
                print("\nWhich Industry would you like to invest in?")

                c = input(f"Enter a number [0-{len(options) - 1}]: ")

                if c.lower() == "e":
                    break

                c = int(c)

                if c in {0, 1, 2}:
                    print("\nHow much would you like to invest?")
                    print("\n5 Budget = 1 Industry Score")
                    print("\n[E/e] Exit")

                    b = input("Enter a number: ")

                    if b.lower() == "e":
                        break

                    if b.isdigit():
                        self.IndustrialScores[c] += int(b) / 5

                    else:
                        raise Exception("Invalid input")
                else:
                    raise Exception("Invalid input")
            except Exception as e:
                utils.PrintErrorMenu(e)
        
    def AllocateIndustry(self):
        while True:
            utils.CLS()
            utils.PrintMenu("Allocate Industry")

            self.PrintResources()

            print("Which industry would you like to allocate resources to?")
            options = [
                "Agriculture",
                "Mining",
                "Industry"
            ]
            for num, opt in enumerate(options):
                print(f"{num}. {opt}")

            print("[E/e] Exit")

            s = input(f"\nEnter a number [0-{len(options)}]: ")

            if s.lower() == "e":
                break

            try:
                s = int(s)

                if s not in {0, 1, 2}:
                    raise Exception("Invalid input")
                
                utils.CLS()
                utils.PrintMenu(f"Alloc. {options[s]} Ind.")
                self.PrintResources(s)

                print("[E/e] Exit")

                rid = input(f"\nEnter the number of the resource you would like to allocate Industrial Score to [1-{len(self.PublicIndustry[s]) - 1}]: ")

                if rid.lower() == "e":
                    break

                rid = int(rid)

                if rid not in range(0, len(self.PublicIndustry[s]) + 1):
                    raise Exception("Invalid input")
                
                utils.CLS()
                utils.PrintMenu(f"Alloc. {self.PublicIndustry[s][rid][0]} Ind.")
                self.PrintResources(s, rid)

                print("\n[E/e] Exit")

                if s == 2:
                    while True:
                        # Only one recipie case
                        if len(self.PublicIndustry[s][rid][1]) == 1:
                            indscore = float(input(f"\nEnter the amount of Industrial Score you would like to allocate to {self.PublicIndustry[s][rid][0]}: "))
                            self.PublicIndustry[s][rid][1][0] = indscore
                            return

                        r = input(f"\nWhich recipie of {self.PublicIndustry[s][rid][0]} would you like to allocate Industrial Score to? [0-{len(self.PublicIndustry[s][rid][1]) - 1}]: ")
                        
                        if r == "e":
                            break

                        try:
                            r = int(r)
                            
                            if r not in range(0, len(self.PublicIndustry[s][rid][1])):
                                raise Exception("Invalid input")    
                            
                            indscore = float(input(f"\nEnter the amount of Industrial Score you would like to allocate to recipie #{r} of {self.PublicIndustry[s][rid][0]}: "))
                            self.PublicIndustry[s][rid][1][r] = indscore
                            return
                        except Exception as e:
                            utils.PrintErrorMenu(e)
                            utils.CLS()
                            utils.PrintMenu(f"Alloc. {self.PublicIndustry[s][rid][0]} Ind.")
                            self.PrintResources(s, rid)
                            print("\n[E/e] Exit")
                else:
                    indscore = float(input(f"\nEnter the amount of Industrial Score you would like to allocate to {self.PublicIndustry[s][rid][0]}: "))

                if indscore < 0:
                    raise Exception("Invalid input")
                
                self.PublicIndustry[s][rid][1] = indscore
            except Exception as e:
                utils.PrintErrorMenu(e)

    def CalculatePrivateIndustry(self):
        PrivateIndustry = [[],[],[]]
        for i in range(3):
            match i:
                case 0 | 1:
                    for comodity, allocation in self.PublicIndustry[i]:
                        for res in self.Resources[i]:
                            if comodity == res.name: 
                                PrivateIndustry[i].append([comodity, ((allocation / res.ISC) * res.Quantity) * (100 - self.info['policy']["PublicIndustryShare"]) / self.info['policy']["PublicIndustryShare"]])
                case 2:
                    for comodity, allocation in self.PublicIndustry[i]:
                        for res in self.Resources[i]:
                            if comodity == res.name:
                                PrivateIndustryProduction = []
                                for rid, recipie in enumerate(res.Ingredients):
                                    PrivateIndustryProduction.append(((allocation[rid] / res.ISC) * res.Quantity) * (100 - self.info['policy']["PublicIndustryShare"]) / self.info['policy']["PublicIndustryShare"])
                                PrivateIndustry[i].append([comodity, PrivateIndustryProduction])
        return PrivateIndustry

    def CalculateIndustryConsumption(self):
        for s in self.Consumption[1]:
            for r in s:
                try:
                    for a in r[1]:
                        a = 0.0
                except:
                    r[1] = 0.0
        
        # Get allocation of each item in the Public Industry
        for cid, ca in enumerate(self.PublicIndustry[2]):
            comodity = ca[0]
            allocation = ca[1]
            # Get the resource from the resource list to get info
            for rid, res in enumerate(self.Resources[2]):
                if comodity == res.name:
                    # Get the recepies
                    for rcid, recipie in enumerate(res.Ingredients):
                        for input, cost in recipie:
                            for sid, sector in enumerate(self.Consumption[1]):
                                for rid, rescon in enumerate(sector):
                                    resource = rescon[0]
                                    consumption = rescon[1]
                                    if resource == input:
                                        try:
                                            for aid, a in enumerate(consumption):
                                                self.Consumption[1][sid][rid][1][aid] += (allocation[rcid] / res.ISC) * cost
                                        except: 
                                            self.Consumption[1][sid][rid][1] += (allocation[rcid] / res.ISC) * cost

    def ManageImportsExports(self):
        while True:
            utils.CLS()
            utils.PrintMenu("Manage Imports/Exports")
            for i in range(3):
                self.PrintResources(i)
            
            options = [
                "Agriculture",
                "Mining",
                "Industry"
            ]
            for num, opt in enumerate(options):
                print(f"{num}. {opt}")

            print("[E/e] Exit")

            s = input(f"\nEnter a number [0-{len(options)}]: ")

            if s.lower() == "e":
                break

            try:
                s = int(s)

                if s not in {0, 1, 2}:
                    raise Exception("Invalid input")
                
                utils.CLS()
                utils.PrintMenu(f"Manage {options[s]} Imp/Exp")
                self.PrintResources(s)

                print("[E/e] Exit")

                rid = input(f"\nEnter the id of the resource you would like to manage the Imports/Exports of [0-{len(self.ImportExport[s]) - 1}]: ")

                if rid.lower() == "e":
                    break

                rid = int(rid)

                if rid not in range(0, len(self.ImportExport[s]) + 1):
                    raise Exception("Invalid input")
                
                utils.CLS()
                utils.PrintMenu(f"Manage {self.ImportExport[s][rid][0]} Imp/Exp")
                self.PrintResources(s, rid)

                print("\n[E/e] Exit")

                match s:
                    case 0 | 1:
                        exp = float(input(f"\nEnter the amount of exports of {self.ImportExport[s][rid][0]}: "))
                        imp = float(input(f"\nEnter the amount of imports of {self.ImportExport[s][rid][0]}: "))
                        self.ImportExport[s][rid][1][1] = exp
                        self.ImportExport[s][rid][1][0] = imp
                    case 2:
                        for recid, recipie in enumerate(self.Resources[s][rid].Ingredients):
                            for resid, resource in enumerate(recipie):
                                exp = float(input(f"\nEnter the amount of exports of recipie #{recid} for {self.Resources[s][rid].name}: "))
                                imp = float(input(f"\nEnter the amount of imports of recipie #{recid} for {self.Resources[s][rid].name}: "))
                                self.ImportExport[s][rid][1][1][recid] = exp
                                self.ImportExport[s][rid][1][0][recid] = imp
            except Exception as e:
                utils.PrintErrorMenu(e)

    def SurplusToStockpile(self):
        # Add resourse surplus to stockpile
        for sid, s in enumerate(self.Stockpile):
            for rid, r in enumerate(s):
                try:
                    for aid, a in enumerate(r[1]):
                        pcons = (self.Consumption[0][sid][rid][1][aid] * self.info['population']) - (self.PrivateIndustry[sid][rid][1][aid] * self.Resources[sid][rid].Quantity)
                        if pcons < 0:
                            pcons = 0
                        a += ((self.PublicIndustry[sid][rid][1][aid] / self.Resources[sid][rid].ISC) * self.Resources[sid][rid].Quantity) + self.ImportExport[sid][rid][1][0][aid] - self.ImportExport[sid][rid][1][1][aid] - self.Consumption[1][sid][rid][1][aid] - self.Consumption[2][sid][rid][1][aid] - pcons
                except:
                    pcons = (self.Consumption[0][sid][rid][1] * self.info['population']) - (self.PrivateIndustry[sid][rid][1] * self.Resources[sid][rid].Quantity)
                    if pcons < 0:
                        pcons = 0
                    r[1] += ((self.PublicIndustry[sid][rid][1] / self.Resources[sid][rid].ISC) * self.Resources[sid][rid].Quantity) + self.ImportExport[sid][rid][1][0] - self.ImportExport[sid][rid][1][1] - self.Consumption[1][sid][rid][1] - self.Consumption[2][sid][rid][1] - pcons

        # Add Budget from Exports to info['budget']
        for sid, s in enumerate(self.ImportExport):
            for rid, r in enumerate(s):
                try:
                    for aid, a in enumerate(r[1][1]):
                        self.info['budget'] += a * self.Resources[sid][rid].Cost
                except:
                    self.info['budget'] += r[1][1] * self.Resources[sid][rid].Cost

        utils.CLS()
        utils.PrintMenu("Surplus to Stockpile")
        print("\nSurplus Added!")
        input("\nPress Enter to continue...")

    def GameOptions(self):
        while True:
            utils.CLS()
            utils.PrintMenu("Game Options")
            options = [
                "Add Resource", #0
                "Edit Resource",
                "Remove Resource", 
                "Reload Resource Prices", #3
                "Sort Resources",
                "Modify Population Consumption",
                "Add Industry Surplus to Stockpile" #6
            ]
            for num, opt in enumerate(options):
                print(f"{num}. {opt}")

            print("[E/e] Exit")

            c = input(f"\nEnter a number [0-{len(options) - 1}]: ")

            if c.lower() == "e":
                break

            try:
                c = int(c)

                match c:
                    case 4:
                        self.SortResources()
                    case 5:
                        self.ModifyPopulationConsumption()
                    case 6:
                        self.SurplusToStockpile()
                    case _: # Default
                        raise Exception("Invalid input")
                    
            except Exception as e:
                utils.PrintErrorMenu(e)

    def ModifyPopulationConsumption(self):
        while True:
            utils.CLS()
            utils.PrintMenu("Mod. Pop. Con.")
            for i in range(3):
                self.PrintResources(i, perpop=True)

            print("Which industry would you like to modify the Population Resource Consumption of?")
            options = [
                "Agriculture",
                "Mining",
                "Industry"
            ]
            for num, opt in enumerate(options):
                print(f"{num}. {opt}")

            print("[E/e] Exit")

            s = input(f"\nEnter a number [0-{len(options)}]: ")

            if s.lower() == "e":
                break

            try:
                s = int(s)

                if s not in {0, 1, 2}:
                    raise Exception("Invalid input")
                
                utils.CLS()
                utils.PrintMenu(f"Mod. Pop. {options[s]} Con.")
                self.PrintResources(s)

                print("[E/e] Exit")

                rid = input(f"\nEnter the id of the resource you would like to modify the Population Consumption of [0-{len(self.Consumption[0][s]) - 1}]: ")

                if rid.lower() == "e":
                    break

                rid = int(rid)

                if rid not in range(0, len(self.Consumption[0][s]) + 1):
                    raise Exception("Invalid input")
                
                utils.CLS()
                utils.PrintMenu(f"Mod. Pop. {self.Consumption[0][s][rid][0]} Con.")
                self.PrintResources(s, rid)

                print("\n[E/e] Exit")

                if s == 2:
                    for recid, recipie in enumerate(self.Resources[s][rid].Ingredients):
                        for resid, resource in enumerate(recipie):
                            con = float(input(f"\nEnter the Per-Million-Pop Consumption rate of recipie #{recid} for {self.Resources[s][rid].name}: "))
                            if con < 0:
                                raise Exception("Invalid input")
                            self.Consumption[0][s][rid][1][recid] = con
                else:
                    con = float(input(f"\nEnter the Per-Million-Pop Consumption rate of {self.Resources[s][rid].name}: "))
                    if con < 0:
                        raise Exception("Invalid input")
                    self.Consumption[0][s][rid][1] = con
                return
            except Exception as e:
                utils.PrintErrorMenu(e)

    def ModifyPlayerInfo(self):
        while True:
            utils.CLS()
            utils.PrintMenu("Modify Player Info")

            options = []
            types = []

            for k, v in self.info.items():
                options.append(k)
                types.append(type(v))
            
            for num, opt in enumerate(options):
                print(f"{num}. {opt}:")
                if types[num] == dict:
                    for k, v in self.info[opt].items():
                        print(f"\t{k}: {v}")
                else:
                    if opt == "population":
                        print(f"\t{self.info[opt]} Million")
                        continue
                    print(f"\t{self.info[opt]}")
            print("[E/e] Exit")

            c = input(f"\nEnter an item to modify [0-{len(options) - 1}]: ")

            if c.lower() == "e":
                break

            try:
                c = int(c)

                if c not in range(0, len(options)):
                    raise Exception("Invalid input")

                if types[c] == dict:
                    utils.CLS()
                    utils.PrintMenu(f"Modify {options[c]}")
                    keys = []
                    for k, v in self.info[options[c]].items():
                        keys.append(k)
                        print(f"{k}: {v}")
                    print("[E/e] Exit")

                    key = input(f"\nEnter an item to modify: ")

                    if key.lower() == "e":
                        break

                    try:
                        if key not in keys:
                            raise Exception("Policy Does Not Exist")

                        value = input(f"\nEnter a new value for {key}: ")

                        if type(self.info[options[c]][key]) == float:
                            value = float(value)
                        elif type(self.info[options[c]][key]) == int:
                            value = int(value)
                        elif type(self.info[options[c]][key]) == str:
                            value = str(value)

                        self.info[options[c]][key] = value
                    except Exception as e:
                        utils.PrintErrorMenu(e)
                else:
                    value = input(f"\nEnter a new value for {options[c]}: ")

                    if type(self.info[options[c]]) == float:
                        value = float(value)
                    elif type(self.info[options[c]]) == int:
                        value = int(value)
                    elif type(self.info[options[c]]) == str:
                        value = str(value)

                    self.info[options[c]] = value
            except Exception as e:
                utils.PrintErrorMenu(e)