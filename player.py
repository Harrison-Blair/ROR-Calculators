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

    def PrintResources(self, type, id=None, pop=True): # Redo
        #"| # | Name | Inputs | Con | Req | Gov | P | ISA | ISC | Q | M.V. | Facility |"
        #"  5    25      25      7     7     7    5    5     5    5    7         19    "
        popmod = self.population
        if not pop:
            popmod = 1.0

        idw = 5
        namew = 23
        inputw = 23
        impw = 5 # Not used yet
        expw = 5 # Not used yet
        conw = 7
        reqw = 7 # Not used yet
        govw = 7 # Not used yet
        pw = 7
        isaw = 5
        iscw = 5
        qw = 5
        mvw = 7
        fw = 19

        
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
        
    def AllocateIndustry(self): # Redo
        while True:
            utils.CLS()
            utils.PrintMenu("Allocate Industry")

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

    def ModifyPopulationConsumption(self): # Redo
        while True:
            utils.CLS()
            utils.PrintMenu("Mod. Pop. Con.")


    def CalculateIndustryConsumption(self):
            for cid, comodity in enumerate(self.PrivateIndustry[2]):
                for res in self.Resources[2]:
                    if comodity[0] == res.name:
                        if sum(comodity[1]) == 0:
                            continue
                        for i, recipie in enumerate(res.Ingredients):
                            if i == 0:
                                self.Consumption[1][2][cid][1][i] = (comodity[1] / res.ISC) * res.Quantity
                            else:
                                self.Consumption[1][2][cid][1][i] = (comodity[1][i] / res.ISC) * res.Quantity


    def CreateResource(self): # yikes
        pass

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
