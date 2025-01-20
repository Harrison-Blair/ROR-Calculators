import json
import utils
import comodity

class Player:
    def __init__(self, info, policy, IndustrialScores, Resources, PublicIndustry, ImportExport, Consumption):
        # Country Info
        self.info = info
        self.population = 105.0 # in millions
        self.policy = policy

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

        # Consumption
        self.Consumption = Consumption
        self.CalculateIndustryConsumption()

        self.SavePlayer()

    def SavePlayer(self):
        PlayerData = {}

        # Country Info
        PlayerData['info'] = self.info

        # Country Policy
        PlayerData['policy'] = self.policy

        # Industry, Agriculture, Mining Scores
        PlayerData['IndustrialScores'] = self.IndustrialScores

        # Industry, Agriculture, Mining assignments/allocations
        PlayerData['PublicIndustry'] = self.PublicIndustry

        # Imports, Exports
        PlayerData['ImportExport'] = self.ImportExport

        # Consumption [Pop] [Ind] [Gov]
        PlayerData['Consumption'] = self.Consumption

        with open('player.json', 'w') as file:
            json.dump(PlayerData, file)

    def main(self):
        while True:
            utils.CLS()
            utils.PrintMenu("Main Menu")
            print(f"Name: {self.info['name']}")
            # Swag overview

            print("Menu")
            print("-" * 45)
            print(f"1. View Detailed Industry Overview")
            print(f"2. Increase Industry")
            print(f"3. Allocate Industry")
            print(f"4. Manage Imports/Exports")
            print(f"5. Modify Policy")
            print("[O/o] Game Options")
            print("[E/e] Save and Exit")

            c = input("\nEnter a number [1-4]: ")

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
                    case 1:
                        self.ViewDetailedIndustryOverview()
                    case 2:
                        self.IncreaseIndustry()
                    case 3:
                        self.AllocateIndustry()
                        self.CalculateIndustryConsumption()
                        self.PrivateIndustry = self.CalculatePrivateIndustry()
                    case 4:
                        self.ManageImportsExports()
                    case 5:
                        self.ModifyPolicy()
                        self.PrivateIndustry = self.CalculatePrivateIndustry()
                    case _: # Default
                        raise Exception("Invalid input")

            except Exception as e:
                utils.PrintErrorMenu(e) 

    def PrintResources(self, type=None, id=None, perpop=False):
        popmod = 1.0
        if not perpop:
            popmod = self.population

        #"| # | NAME | INPUTS | CON | REQ | GOV | PROD | ISA | ISC | Q | M.V. | FACILILITY |"
        #"  5    25      25      7     7     7      7    7     7    5    7         20    "
        columns = ["#", "NAME", "INPUTS", "CON", "REQ", "GOV", "PROD", "ISA", "ISC", "Q", "M.V.", "FACILITY"]
        widths = [5, 25, 25, 7, 7, 7, 7, 7, 7, 5, 7, 20]
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
                            print(f" ".center(widths[11]), end="")
                        for resid, resource in enumerate(recipie):
                            if resid == 0:
                                print(f"\n|{str(rid).center(widths[0])}|", end="")
                                print(f"{res.name.center(widths[1])}|", end="")
                                print(f"{str(resource[1]).center(5)},{resource[0].center(widths[2] - 6)}|", end="")
                                print(f"{str(self.Consumption[0][i][rid][1][recid] * popmod).center(widths[3])}|", end="")
                                print(f"{str(self.Consumption[1][i][rid][1][recid]).center(widths[4])}|", end="")
                                print(f"{str(self.Consumption[2][i][rid][1][recid]).center(widths[5])}|", end="")
                                print(f"{str((self.PublicIndustry[i][rid][1][recid] / res.ISC) * res.Quantity).center(widths[6])}|", end="")
                                print(f"{str(self.PublicIndustry[i][rid][1][recid]).center(widths[7])}|", end="")
                                if recid == 0:
                                    print(f"{str(res.ISC).center(widths[8])}|", end="")
                                    print(f"{str(res.Quantity).center(widths[9])}|", end="")
                                    print(f"{str(res.Cost).center(widths[10])}|", end="")
                                    print(f"{res.Facility.center(widths[11])}", end="")
                                else:
                                    print(f" ".center(widths[8]) + "|", end="")
                                    print(f" ".center(widths[9]) + "|", end="")
                                    print(f" ".center(widths[10]) + "|", end="")
                                    print(f" ".center(widths[11]), end="")
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
                                print(f" ".center(widths[11]), end="")
                except: # No recipies
                    print(f"\n|{str(rid).center(widths[0])}|", end="")
                    print(f"{res.name.center(widths[1])}|", end="")
                    print(f"{"-".center(widths[2])}|", end="")
                    print(f"{str(self.Consumption[0][i][rid][1] * popmod).center(widths[3])}|", end="")
                    print(f"{str(self.Consumption[1][i][rid][1]).center(widths[4])}|", end="")
                    print(f"{str(self.Consumption[2][i][rid][1]).center(widths[5])}|", end="")
                    print(f"{str((self.PublicIndustry[i][rid][1] / res.ISC) * res.Quantity).center(widths[6])}|", end="")
                    print(f"{str(self.PublicIndustry[i][rid][1]).center(widths[7])}|", end="")
                    print(f"{str(res.ISC).center(widths[8])}|", end="")
                    print(f"{str(res.Quantity).center(widths[9])}|", end="")
                    print(f"{str(res.Cost).center(widths[10])}|", end="")
                    print(f"{res.Facility.center(widths[11])}", end="")
                print("\n+", end="")
                for col in columns: # Header Divider
                    print("-" * widths[columns.index(col)] + "+", end="")
            print()
                        
    def ViewDetailedIndustryOverview(self):
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
                print(f"1. Agriculture Score (ISA/AS): {sum(i[1] for i in self.PublicIndustry[0])}/{self.IndustrialScores[0]}")
                print(f"2. Mining Score (ISA/MS): {sum(i[1] for i in self.PublicIndustry[1])}/{self.IndustrialScores[1]}")
                print(f"3. Industry Score (ISA/IS): {sum(sum(i[1]) for i in self.PublicIndustry[2])}/{self.IndustrialScores[2]}")
                print("[E/e] Exit")
                
                print("\nWhich Industry would you like to invest in?")

                c = input("Enter a number [1-3]: ")

                if c.lower() == "e":
                    break

                c = int(c)

                if c in {1, 2, 3}:
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
                                PrivateIndustry[i].append([comodity, ((allocation / res.ISC) * res.Quantity) * (100 - self.policy["PublicIndustry"]) / self.policy["PublicIndustry"]])
                case 2:
                    for comodity, allocation in self.PublicIndustry[i]:
                        for res in self.Resources[i]:
                            if comodity == res.name:
                                PrivateIndustryProduction = []
                                for rid, recipie in enumerate(res.Ingredients):
                                    PrivateIndustryProduction.append(((allocation[rid] / res.ISC) * res.Quantity) * (100 - self.policy["PublicIndustry"]) / self.policy["PublicIndustry"])
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
        pass

    def GameOptions(self):
        while True:
            utils.CLS()
            utils.PrintMenu("Game Options")
            print("1. Add Resource")
            print("2. Modify Population Consumption")

            print("[E/e] Exit")

            c = input("\nEnter a number [1-x]: ")

            if c.lower() == "e":
                break

            try:
                c = int(c)

                match c:
                    case 1:
                        self.CreateResource()
                    case 2:
                        self.ModifyPopulationConsumption()
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

    def ModifyPolicy(self):
        while True:
            utils.CLS()
            utils.PrintMenu("Modify Policy")
            opt = []
            opt.append("Modify Tax Policy")

            for i, o in enumerate(opt):
                print(f"{i + 1}. {o}")

            print("[E/e] Exit")

            c = input(f"\nEnter a number [1-{len(opt)}]: ")

            if c.lower() == "e":
                break

            try:
                c = int(c)

                match c:
                    case 1:
                        self.ModifyTaxPolicy()
                    case _: # Default
                        raise Exception("Invalid input")
            except Exception as e:
                utils.PrintErrorMenu(e)

    def ModifyTaxPolicy(self):
        while True:
            utils.CLS()
            utils.PrintMenu("Modify Tax Policy")

            try:
                print(f"The current ratio of [Public : Private] Industry ownership is: [{self.policy['PublicIndustry']} : {100 - self.policy['PublicIndustry']}]")
                
                pub = float(input("\nEnter the percentage of INDUSTRY that is PUBLIC: "))

                if not 0 < pub < 100:
                    raise Exception("Invalid input")

                self.policy['PublicIndustry'] = pub

                return
            except Exception as e:
                utils.PrintErrorMenu(e)
