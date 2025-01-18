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

    def PrintResources(self, type, id=None, pop=True):
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
        print(f"{type + " Sector"}".center(idw + namew + inputw + conw + reqw + govw + pw + isaw + iscw + qw + mvw + fw))
        print(f"|{"*" * idw}|{"*" * namew}|{"*" * inputw}|{"*" * conw}|{"*" * reqw}|{"*" * govw}|{"*" * pw}|{"*" * isaw}|{"*" * iscw}|{"*" * qw}|{"*" * mvw}|{"*" * fw}")
        print(f"|{"#".center(idw)}|{"Name".center(namew)}|{"Inputs".center(inputw)}|{"Con".center(conw)}|{"Req".center(reqw)}|{"Gov".center(govw)}|{"P".center(pw)}|{"ISA".center(isaw)}|{"ISC".center(iscw)}|{"Q".center(qw)}|{"M.V.".center(mvw)}|{"Facility".center(fw)}")
        print(f"|{"=" * idw}|{"=" * namew}|{"=" * inputw}|{"=" * conw}|{"=" * reqw}|{"=" * govw}|{"=" * pw}|{"=" * isaw}|{"=" * iscw}|{"=" * qw}|{"=" * mvw}|{"=" * fw}")
        if type == "Agriculture":
            if id != None:
                c = self.PublicIndustry[0][id][0]
                isa = self.PublicIndustry[0][id][1]
                print(f"|{str(id).center(idw)}|{str(c.name).center(namew)}|{"-".center(inputw)}|{str(self.Consumption[0][0][id][1] * popmod).center(conw)}|{str(self.Consumption[1][0][id][1]).center(reqw)}|{str(self.Consumption[2][0][id][1]).center(govw)}|{str((isa / c.ISC) * c.Quantity).center(pw)}|{str(isa).center(isaw)}|{str(c.ISC).center(iscw)}|{str(c.Quantity).center(qw)}|{str(c.Cost).center(mvw)}|{str(c.Facility).center(fw)}")
                print(f"|{"-" * idw}|{"-" * namew}|{"-" * inputw}|{"-" * conw}|{"-" * reqw}|{"-" * govw}|{"-" * pw}|{"-" * isaw}|{"-" * iscw}|{"-" * qw}|{"-" * mvw}|{"-" * fw}")
                return
            for num, com in enumerate(self.PublicIndustry[0]):
                c = com[0]
                isa = com[1]
                print(f"|{str(num).center(idw)}|{str(c.name).center(namew)}|{"-".center(inputw)}|{str(self.Consumption[0][0][num][1] * popmod).center(conw)}|{str(self.Consumption[1][0][num][1]).center(reqw)}|{str(self.Consumption[2][0][num][1]).center(govw)}|{str((isa / c.ISC) * c.Quantity).center(pw)}|{str(isa).center(isaw)}|{str(c.ISC).center(iscw)}|{str(c.Quantity).center(qw)}|{str(c.Cost).center(mvw)}|{str(c.Facility).center(fw)}")
                print(f"|{"-" * idw}|{"-" * namew}|{"-" * inputw}|{"-" * conw}|{"-" * reqw}|{"-" * govw}|{"-" * pw}|{"-" * isaw}|{"-" * iscw}|{"-" * qw}|{"-" * mvw}|{"-" * fw}")
        elif type == "Mining":
            if id != None:
                c = self.PublicIndustry[1][id][0]
                isa = self.PublicIndustry[1][id][1]
                print(f"|{str(id).center(idw)}|{str(c.name).center(namew)}|{"-".center(inputw)}|{str(self.Consumption[0][1][id][1] * popmod).center(conw)}|{str(self.Consumption[1][1][id][1]).center(reqw)}|{str(self.Consumption[2][1][id][1]).center(govw)}|{str((isa / c.ISC) * c.Quantity).center(pw)}|{str(isa).center(isaw)}|{str(c.ISC).center(iscw)}|{str(c.Quantity).center(qw)}|{str(c.Cost).center(mvw)}|{str(c.Facility).center(fw)}")
                print(f"|{"-" * idw}|{"-" * namew}|{"-" * inputw}|{"-" * conw}|{"-" * reqw}|{"-" * govw}|{"-" * pw}|{"-" * isaw}|{"-" * iscw}|{"-" * qw}|{"-" * mvw}|{"-" * fw}")
                return
            for num, com in enumerate(self.PublicIndustry[1]):
                c = com[0]
                isa = com[1]
                print(f"|{str(num).center(idw)}|{str(c.name).center(namew)}|{"-".center(inputw)}|{str(self.Consumption[0][1][num][1] * popmod).center(conw)}|{str(self.Consumption[1][1][num][1]).center(reqw)}|{str(self.Consumption[2][1][num][1]).center(govw)}|{str((isa / c.ISC) * c.Quantity).center(pw)}|{str(isa).center(isaw)}|{str(c.ISC).center(iscw)}|{str(c.Quantity).center(qw)}|{str(c.Cost).center(mvw)}|{str(c.Facility).center(fw)}")
                print(f"|{"-" * idw}|{"-" * namew}|{"-" * inputw}|{"-" * conw}|{"-" * reqw}|{"-" * govw}|{"-" * pw}|{"-" * isaw}|{"-" * iscw}|{"-" * qw}|{"-" * mvw}|{"-" * fw}")
        if type == "Industry":
            if id != None:
                c = self.PublicIndustry[2][id][0]
                isa = self.PublicIndustry[2][id][1]
                for r, recipie in enumerate(c.Ingredients):
                    if r != 0:
                        print(f"|{" ".center(idw)}|{" ".center(namew)}|{"OR".center(inputw)}|{" ".center(conw)}|{" ".center(reqw)}|{" ".center(govw)}|{" ".center(pw)}|{" ".center(isaw)}|{" ".center(iscw)}|{" ".center(qw)}|{" ".center(mvw)}|{" ".center(fw)}")
                        print(f"|{" ".center(idw)}|{" ".center(namew)}|{str(recipie[0][1]).rjust(3)}, {str(recipie[0][0]).ljust(inputw - 5)}|{str(self.Consumption[0][2][id][1][r] * popmod).center(conw)}|{str(self.Consumption[1][2][id][1][r]).center(reqw)}|{str(self.Consumption[2][2][id][1][r]).center(govw)}|{str((isa[r] / c.ISC) * c.Quantity).center(pw)}|{str(isa[r]).center(isaw)}|{" ".center(iscw)}|{" ".center(qw)}|{" ".center(mvw)}|{" ".center(fw)}")
                    else:
                        print(f"|{str(id).center(idw)}|{str(c.name).center(namew)}|{str(recipie[0][1]).rjust(3)}, {str(recipie[0][0]).ljust(inputw - 5)}|{str(self.Consumption[0][2][id][1][r] * popmod).center(conw)}|{str(self.Consumption[1][2][id][1][r]).center(reqw)}|{str(self.Consumption[2][2][id][1][r]).center(govw)}|{str((isa[r] / c.ISC) * c.Quantity).center(pw)}|{str(isa[r]).center(isaw)}|{str(c.ISC).center(iscw)}|{str(c.Quantity).center(qw)}|{str(c.Cost).center(mvw)}|{str(c.Facility).center(fw)}")

                for i, ingredient in enumerate(recipie):
                    if i == 0:
                        continue
                    print(f"|{" ".center(idw)}|{" ".center(namew)}|{str(ingredient[1]).rjust(3)}, {str(ingredient[0]).ljust(inputw - 5)}|{" ".center(pw)}|{" ".center(isaw)}|{" ".center(iscw)}|{" ".center(qw)}|{" ".center(mvw)}|{" ".center(fw)}")
                print(f"|{"-" * idw}|{"-" * namew}|{"-" * inputw}|{"-" * conw}|{"-" * reqw}|{"-" * govw}|{"-" * pw}|{"-" * isaw}|{"-" * iscw}|{"-" * qw}|{"-" * mvw}|{"-" * fw}")
                return
            for num, c in enumerate(self.PublicIndustry[2]):
                isa: int = c[1]
                c: comodity.Comodity = c[0]
                for r, recipie in enumerate(c.Ingredients):
                    if r != 0:
                        print(f"|{" ".center(idw)}|{" ".center(namew)}|{"OR".center(inputw)}|{" ".center(conw)}|{" ".center(reqw)}|{" ".center(govw)}|{" ".center(pw)}|{" ".center(isaw)}|{" ".center(iscw)}|{" ".center(qw)}|{" ".center(mvw)}|{" ".center(fw)}")
                        print(f"|{" ".center(idw)}|{" ".center(namew)}|{str(recipie[0][1]).rjust(3)}, {str(recipie[0][0]).ljust(inputw - 5)}|{str(self.Consumption[0][2][num][1][r] * popmod).center(conw)}|{str(self.Consumption[1][2][num][1][r]).center(reqw)}|{str(self.Consumption[2][2][num][1][r]).center(govw)}|{str((isa[r] / c.ISC) * c.Quantity).center(pw)}|{str(isa[r]).center(isaw)}|{" ".center(iscw)}|{" ".center(qw)}|{" ".center(mvw)}|{" ".center(fw)}")
                    else:
                        print(f"|{str(num).center(idw)}|{str(c.name).center(namew)}|{str(recipie[0][1]).rjust(3)}, {str(recipie[0][0]).ljust(inputw - 5)}|{str(self.Consumption[0][2][num][1][r] * popmod).center(conw)}|{str(self.Consumption[1][2][num][1][r]).center(reqw)}|{str(self.Consumption[2][2][num][1][r]).center(govw)}|{str((isa[r] / c.ISC) * c.Quantity).center(pw)}|{str(isa[r]).center(isaw)}|{str(c.ISC).center(iscw)}|{str(c.Quantity).center(qw)}|{str(c.Cost).center(mvw)}|{str(c.Facility).center(fw)}")

                for i, ingredient in enumerate(recipie):
                    if i == 0:
                        continue
                    print(f"|{" ".center(idw)}|{" ".center(namew)}|{str(ingredient[1]).rjust(3)}, {str(ingredient[0]).ljust(inputw - 5)}|{" ".center(conw)}|{" ".center(reqw)}|{" ".center(govw)}|{" ".center(pw)}|{" ".center(isaw)}|{" ".center(iscw)}|{" ".center(qw)}|{" ".center(mvw)}|{" ".center(fw)}")

                print(f"|{"-" * idw}|{"-" * namew}|{"-" * inputw}|{"-" * conw}|{"-" * reqw}|{"-" * govw}|{"-" * pw}|{"-" * isaw}|{"-" * iscw}|{"-" * qw}|{"-" * mvw}|{"-" * fw}")
        
    def ViewDetailedIndustryOverview(self):
        utils.CLS()
        utils.PrintMenu("Det. Ind. Overview")

        self.PrintResources("Agriculture")
        self.PrintResources("Mining")
        self.PrintResources("Industry")

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

                if c in {"1", "2", "3"}:
                    c = int(c)
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
            self.CalculateIndustryConsumption()
            utils.CLS()
            utils.PrintMenu("Allocate Industry")
            print(f"1. Agriculture Score (ISA/AS): {sum(i[1] for i in self.PublicIndustry[0])}/{self.IndustrialScores[0]}")
            print(f"2. Mining Score (ISA/MS): {sum(i[1] for i in self.PublicIndustry[1])}/{self.IndustrialScores[1]}")
            print(f"3. Industry Score (ISA/IS): {sum(sum(i[1]) for i in self.PublicIndustry[2])}/{self.IndustrialScores[2]}")
            print("[E/e] Exit")
            print("\nWhich Industry would you like to allocate resources in")
            i = input("\n Enter a number [1-3]: ")

            if i.lower() == "e":
                break

            try:
                i = int(i)
                max = 0
                if i in {1, 2, 3}:
                    match i:
                        case 1:
                            self.PrintResources("Agriculture")
                            max = len(self.PublicIndustry[0]) - 1
                        case 2:
                            self.PrintResources("Mining")
                            max = len(self.PublicIndustry[1]) - 1
                        case 3:
                            self.PrintResources("Industry")
                            max = len(self.PublicIndustry[2]) - 1
                else:
                    raise Exception("Invalid input")
                print("\nEnter the ID# of the resource you would like to allocate resources to.")
                print("\n[E/e] Exit")

                id = input(f"\nEnter a number [1-{str(max)}]: ")

                if id == "e":
                    break

                id = int(id)

                resource: comodity.Comodity = None
                if 0 <= id < max + 1:
                    match i:
                        case 1:
                            self.PrintResources("Agriculture", id) 
                            resource = self.PublicIndustry[0][id][0]
                        case 2:
                            self.PrintResources("Mining", id)
                            resource = self.PublicIndustry[1][id][0]
                        case 3:
                            self.PrintResources("Industry", id)
                            resource = self.PublicIndustry[2][id][0]
                    recipie = None
                    if resource.Ingredients != None and len(resource.Ingredients) > 1:
                        print("\nWhich recipie would you like to allocate resources to?")
                        print("\n[E/e] Exit")

                        recipie = input(f"Enter a number[1-{len(resource.Ingredients)}]: ")

                        if recipie == "e":
                            break

                        recipie = int(recipie)

                        if not 0 < recipie < len(resource.Ingredients) + 1:
                            raise Exception("Invalid input")
                        
                        recipie -= 1
                    
                    print("\nHow much would you like to allocate?")

                    match i:
                        case 1:
                            print(f"You are currently producing: { (self.PublicIndustry[0][id][1]/ resource.ISC) * resource.Quantity}")
                        case 2:
                            print(f"You are currently producing: { (self.PublicIndustry[1][id][1]/ resource.ISC) * resource.Quantity}")
                        case 3:
                            print(f"You are currently producing: { (sum(self.PublicIndustry[2][id][1])/ resource.ISC) * resource.Quantity}")
                    
                    print("\n[E/e] Exit")

                    ind = input("Enter a number: ")

                    if ind.lower() == "e":
                        break

                    ind = int(ind)

                    if recipie == None:
                        self.PublicIndustry[i][id][1] = ind
                    else:
                        self.PublicIndustry[i][id][1][recipie] = ind
                else:
                    raise Exception("Invalid input")
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

    def ModifyPopulationConsumption(self): # Really gotta fix this
        while True:
            utils.CLS()
            utils.PrintMenu("Mod. Pop. Con.")
            self.PrintResources("Agriculture", pop=False)
            self.PrintResources("Mining", pop=False)
            self.PrintResources("Industry", pop=False)

            print("\n[E/e] Exit")

            print("\nNOTE: Consumption is displayed in *PER MILLION POP*")

            try:
                s = input("\nWhich sector would you like to modify? [1-3]: ")

                if s.lower() == "e":
                    break

                s = int(s)

                if not 0 < s < 4:
                    raise Exception("Invalid input")
                
                s -= 1

                utils.CLS()
                utils.PrintMenu("Mod. Pop. Con.")
                match s:
                    case 0:
                        self.PrintResources("Agriculture")
                        max = len(self.PublicIndustry[s]) - 1
                    case 1:
                        self.PrintResources("Mining")
                        max = len(self.PublicIndustry[s]) - 1
                    case 2:
                        self.PrintResources("Industry")
                        max = len(self.PublicIndustry[s]) - 1

                print("\nNOTE: Consumption is displayed in *PER MILLION POP*")

                n = int(input(f"\nWhich resource would you like to modify? [0-{max}]: "))

                if not -1 < n < max + 1:
                    raise Exception("Invalid input")
                
                if s != 2:
                    val = self.Consumption[0][s][n][1]
                else:
                    val = sum(self.Consumption[0][s][n][1])

                val = float(input(f"\nInput the new value in *PER MILLION POP* [Current = {val}]: "))
                
                if s != 2:
                    self.Consumption[0][s][n][1] = val
                    continue

                if sum(self.Consumption[0][s][n][1]) == val:
                    for i, c in enumerate(self.Consumption[0][s][n][1]):
                        self.Consumption[0][s][n][1][i] = 0

                while sum(self.Consumption[0][s][n][1]) != val:
                    utils.CLS()
                    utils.PrintMenu("Mod. Pop. Con.")
                    print(f"\nYou must manually assign the TYPE of resources allocated for {self.Consumption[0][s][n][0].name} consumption.")
                    
                    self.PrintResources("Industry", n)

                    print(f"\nYou have {sum(self.Consumption[0][s][n][1])}/{val} assigned.")

                    r = int(input(f"\nWhich recipie would you like to allocate resources from? [1-{len(self.Consumption[0][s][n][0].Ingredients)}]: "))

                    if not 0 < r < len(self.Consumption[0][s][n][0].Ingredients) + 1:
                        raise Exception("Invalid input")
                    
                    r -= 1

                    amt = float(input(f"\nAmount to allocate: "))

                    if amt < 0:
                        raise Exception("Invalid input")
                    
                    self.Consumption[0][s][n][1][r] = amt

            except Exception as e:
                utils.PrintErrorMenu(e)

    def CalculateIndustryConsumption(self): # This too
        for res, isa in self.Industry:
            for i, recipie in enumerate(res.Ingredients):
                for r, q in recipie:
                    for s, sector in enumerate(self.Consumption[1]):
                        for n, comodity in enumerate(sector):
                            if comodity[0].name == r:
                                try:
                                    while sum(self.Consumption[1][s][n][1]) != q * (isa[i] / res.ISC):
                                        utils.CLS()
                                        utils.PrintMenu("Ind. Con. Allocation")
                                        print(f"An item requires manual assignment of the TYPE of resource.")
                                        
                                        print(f"Creating {res.name}(s) requires *{q}, {r.upper()}*")
                                        print(f"\nSince you can make multiple kinds of pipes, you must choose which ones to use to create the {res.name}(s)")
                                        
                                        match s:
                                            case 0:
                                                self.PrintResources("Agriculture", n)
                                            case 1:
                                                self.PrintResources("Mining", n)
                                            case 2:
                                                self.PrintResources("Industry", n)

                                        print(f"\nYou have {sum(self.Consumption[1][s][n][1])} {r.upper()} assigned.")
                                        print(f"\nYou need {q * (isa[i] / res.ISC)} {r.upper()} assigned.")

                                        print()

                                        try:
                                            recipie = int(input(f"\nWhich recipie would you like to allocate resources from? [1-{len(res.Ingredients)}]:"))

                                            if not 0 < recipie < len(res.Ingredients) + 1:
                                                raise Exception("Invalid input")
                                            
                                            recipie -= 1

                                            amt = float(input(f"\nHow much would you like to allocate?"))

                                            if amt < 0:
                                                raise Exception("Invalid input")
                                            
                                            self.Consumption[1][s][n][1][recipie] = amt
                                        except Exception as e:
                                            utils.PrintErrorMenu(e)
                                except:
                                    self.Consumption[1][s][n][1] = q * (isa[i] / res.ISC)

    def CreateResource(self): # yikes
        while True:
                utils.CLS()
                utils.PrintMenu("Add Resource")
                print("What type of resource would you like to add?")
                print("1. Agriculture")
                print("2. Mining")
                print("3. Industry")
                print("[E/e] Exit")

                c = input("\nEnter a number [1-3]: ")

                if c.lower() == "e":
                    break

                try:
                    c = int(c)

                    if not c in {1, 2, 3}:
                        raise Exception("Invalid input")
                    
                    n = input("\nEnter the name of the resource: ")
                    isc = int(input("\nEnter the Industry Score Cost: "))
                    q = int(input("\nEnter the Quantity produced: "))
                    cost = float(input("\nEnter the cost: "))

                    match c: # Append to resource list, imports, exports, and save to resources.json
                        case 1: # Agriculture
                            facility = f"{n} Farm"
                            com = comodity.Comodity(n, isc, q, cost, facility)
                            self.Agriculture.append([com, 0])
                            break
                        case 2: # Mining
                            facility = f"{n} Mine"
                            com = comodity.Comodity(n, isc, q, cost, facility)
                            self.Mining.append([com, 0])
                            break
                        case 3: # Industry
                            facility = input("\nEnter the facility the item is produced in: ")
                            recipies = []

                            while True:
                                print("\nWould you like to add a recipie? [Y/n]")
                                i = input("\nEnter a letter: ")

                                if i.lower() == "n":
                                    break
                                
                                recipie = []
                                while True:
                                    print("\nWould you like to add an input? [Y/n]")
                                    i = input("\nEnter a letter: ")

                                    if i.lower() == "n":
                                        recipies.append(recipie)
                                        break
                                    
                                    name = input("\nEnter the name of the input: ")
                                    quantity = int(input("\nEnter the quantity of the input: "))

                                    recipie.append([name, quantity])
                            
                            com = comodity.Comodity(n, isc, q, cost, facility, recipies)
                            com = self.Industry.append([com, [0]])
                    self.Imports[c - 1].append([com, 0])
                    self.Exports[c - 1].append([com, 0])
                    
                    with open('resources.json', 'r') as file:
                        resources = json.load(file)

                    resources.append({"name": n, "ISC": isc, "Quantity": q, "Cost": cost, "type": ["Agriculture", "Mining", "Industry"][c - 1], "Facility": facility, "Input": recipies})

                    with open('resources.json', 'w') as file:
                        json.dump(resources, file)

                except Exception as e:
                    utils.PrintErrorMenu(e)
                return

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
