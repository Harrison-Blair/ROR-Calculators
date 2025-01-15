import json
import utils
import comodity

class Player:
    def __init__(self, name, IS, AS, MS, Industry, Agriculture, Mining, Imports, Exports, Consumption):
        # Country Info
        self.name = name

        # Industry, Agriculture, Mining Scores
        self.IndustryScore = IS
        self.AgricultureScore = AS
        self.MiningScore = MS

        # Industry, Agriculture, Mining assignments/allocations
        self.Industry = Industry
        self.Agriculture = Agriculture
        self.Mining = Mining

        # Imports, Exports
        self.Imports = Imports
        self.Exports = Exports

        # Consumption
        self.Consumption = Consumption

        self.SavePlayer()

    def SavePlayer(self):
        PlayerData = {}

        # Country Info
        PlayerData['name'] = self.name

        # Industry, Agriculture, Mining Scores
        PlayerData['IS'] = self.IndustryScore
        PlayerData['AS'] = self.AgricultureScore
        PlayerData['MS'] = self.MiningScore

        # Industry, Agriculture, Mining assignments/allocations
        PlayerData['Industry'] = []
        PlayerData['Agriculture'] = []
        PlayerData['Mining'] = []

        # Imports, Exports
        PlayerData['Imports'] = [[],[],[]]
        PlayerData['Exports'] = [[],[],[]]

        # Consumption
        PlayerData['Consumption'] = [[[],[],[]],[[],[],[]],[[],[],[]]]

        for c in self.Industry:
            PlayerData['Industry'].append((c[0].name, c[1]))

        for c in self.Agriculture:
            PlayerData['Agriculture'].append((c[0].name, c[1]))

        for c in self.Mining:
            PlayerData['Mining'].append((c[0].name, c[1]))

        for i in range(len(self.Imports)):
            for c in self.Imports[i]:
                PlayerData['Imports'][i].append((c[0].name, c[1]))

        for i in range(len(self.Exports)):
            for c in self.Exports[i]:
                PlayerData['Exports'][i].append((c[0].name, c[1]))

        with open('player.json', 'w') as file:
            json.dump(PlayerData, file)

    def main(self):
        while True:
            utils.CLS()
            utils.PrintMenu("Main Menu")
            print(f"Name: {self.name}")
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
                    case 4:
                        self.ManageImportsExports()
                    case 5:
                        self.ModifyPolicy()
                    case _: # Default
                        raise Exception("Invalid input")

            except Exception as e:
                utils.PrintErrorMenu(e)

    def PrintResources(self, type, id=None):
        #"| # | Name | Inputs | Imp | Exp | reqw | P | ISA | ISC | Q | M.V. | Facility |"
        #"  5    25      25      5     5      7    5    5     5    5    7         19    "
        idw = 5
        namew = 23
        inputw = 23
        impw = 5 # Not used yet
        expw = 5 # Not used yet
        reqw = 7 # Not used yet
        pw = 7
        isaw = 5
        iscw = 5
        qw = 5
        mvw = 7
        fw = 19
        print(f"|{"#".center(idw)}|{"Name".center(namew)}|{"Inputs".center(inputw)}|{"P".center(pw)}|{"ISA".center(isaw)}|{"ISC".center(iscw)}|{"Q".center(qw)}|{"M.V.".center(mvw)}|{"Facility".center(fw)}")
        print(f"|{"=" * idw}|{"=" * namew}|{"=" * inputw}|{"=" * pw}|{"=" * isaw}|{"=" * iscw}|{"=" * qw}|{"=" * mvw}|{"=" * fw}")
        if type == "Agriculture":
            if id != None:
                c = self.Agriculture[id][0]
                isa = self.Agriculture[id][1]
                print(f"|{str(id).center(idw)}|{str(c.name).center(namew)}|{"-".center(inputw)}|{str((isa / c.ISC) * c.Quantity).center(pw)}|{str(isa).center(isaw)}|{str(c.ISC).center(iscw)}|{str(c.Quantity).center(qw)}|{str(c.Cost).center(mvw)}|{str(c.Facility).center(fw)}")
                print(f"|{"-" * idw}|{"-" * namew}|{"-" * inputw}|{"-" * pw}|{"-" * isaw}|{"-" * iscw}|{"-" * qw}|{"-" * mvw}|{"-" * fw}")
                return
            for num, com in enumerate(self.Agriculture):
                c = com[0]
                isa = com[1]
                print(f"|{str(num).center(idw)}|{str(c.name).center(namew)}|{"-".center(inputw)}|{str((isa / c.ISC) * c.Quantity).center(pw)}|{str(isa).center(isaw)}|{str(c.ISC).center(iscw)}|{str(c.Quantity).center(qw)}|{str(c.Cost).center(mvw)}|{str(c.Facility).center(fw)}")
                print(f"|{"-" * idw}|{"-" * namew}|{"-" * inputw}|{"-" * pw}|{"-" * isaw}|{"-" * iscw}|{"-" * qw}|{"-" * mvw}|{"-" * fw}")
        elif type == "Mining":
            if id != None:
                c = self.Mining[id][0]
                isa = self.Mining[id][1]
                print(f"|{str(id).center(idw)}|{str(c.name).center(namew)}|{"-".center(inputw)}|{str((isa / c.ISC) * c.Quantity).center(pw)}|{str(isa).center(isaw)}|{str(c.ISC).center(iscw)}|{str(c.Quantity).center(qw)}|{str(c.Cost).center(mvw)}|{str(c.Facility).center(fw)}")
                print(f"|{"-" * idw}|{"-" * namew}|{"-" * inputw}|{"-" * pw}|{"-" * isaw}|{"-" * iscw}|{"-" * qw}|{"-" * mvw}|{"-" * fw}")
                return
            for num, com in enumerate(self.Mining):
                c = com[0]
                isa = com[1]
                print(f"|{str(num).center(idw)}|{str(c.name).center(namew)}|{"-".center(inputw)}|{str((isa / c.ISC) * c.Quantity).center(pw)}|{str(isa).center(isaw)}|{str(c.ISC).center(iscw)}|{str(c.Quantity).center(qw)}|{str(c.Cost).center(mvw)}|{str(c.Facility).center(fw)}")
                print(f"|{"-" * idw}|{"-" * namew}|{"-" * inputw}|{"-" * pw}|{"-" * isaw}|{"-" * iscw}|{"-" * qw}|{"-" * mvw}|{"-" * fw}")
        if type == "Industry":
            if id != None:
                c = self.Industry[id][0]
                isa = self.Industry[id][1]
                for r, recipie in enumerate(c.Ingredients):
                    if r != 0:
                        print(f"|{" ".center(idw)}|{" ".center(namew)}|{"OR".center(inputw)}|{" ".center(pw)}|{" ".center(isaw)}|{" ".center(iscw)}|{" ".center(qw)}|{" ".center(mvw)}|{" ".center(fw)}")
                        print(f"|{" ".center(idw)}|{" ".center(namew)}|{str(recipie[0][1]).rjust(3)}, {str(recipie[0][0]).ljust(inputw - 5)}|{str((isa[r] / c.ISC) * c.Quantity).center(pw)}|{str(isa[r]).center(isaw)}|{" ".center(iscw)}|{" ".center(qw)}|{" ".center(mvw)}|{" ".center(fw)}")
                    else:
                        print(f"|{str(id).center(idw)}|{str(c.name).center(namew)}|{str(recipie[0][1]).rjust(3)}, {str(recipie[0][0]).ljust(inputw - 5)}|{str((isa[r] / c.ISC) * c.Quantity).center(pw)}|{str(isa[r]).center(isaw)}|{str(c.ISC).center(iscw)}|{str(c.Quantity).center(qw)}|{str(c.Cost).center(mvw)}|{str(c.Facility).center(fw)}")

                for i, ingredient in enumerate(recipie):
                    if i == 0:
                        continue
                    print(f"|{" ".center(idw)}|{" ".center(namew)}|{str(ingredient[1]).rjust(3)}, {str(ingredient[0]).ljust(inputw - 5)}|{" ".center(pw)}|{" ".center(isaw)}|{" ".center(iscw)}|{" ".center(qw)}|{" ".center(mvw)}|{" ".center(fw)}")
                print(f"|{"-" * idw}|{"-" * namew}|{"-" * inputw}|{"-" * pw}|{"-" * isaw}|{"-" * iscw}|{"-" * qw}|{"-" * mvw}|{"-" * fw}")
                return
            for num, c in enumerate(self.Industry):
                isa: int = c[1]
                c: comodity.Comodity = c[0]
                for r, recipie in enumerate(c.Ingredients):
                    if r != 0:
                        print(f"|{" ".center(idw)}|{" ".center(namew)}|{"OR".center(inputw)}|{" ".center(pw)}|{" ".center(isaw)}|{" ".center(iscw)}|{" ".center(qw)}|{" ".center(mvw)}|{" ".center(fw)}")
                        print(f"|{" ".center(idw)}|{" ".center(namew)}|{str(recipie[0][1]).rjust(3)}, {str(recipie[0][0]).ljust(inputw - 5)}|{str((isa[r] / c.ISC) * c.Quantity).center(pw)}|{str(isa[r]).center(isaw)}|{" ".center(iscw)}|{" ".center(qw)}|{" ".center(mvw)}|{" ".center(fw)}")
                    else:
                        print(f"|{str(num).center(idw)}|{str(c.name).center(namew)}|{str(recipie[0][1]).rjust(3)}, {str(recipie[0][0]).ljust(inputw - 5)}|{str((isa[r] / c.ISC) * c.Quantity).center(pw)}|{str(isa[r]).center(isaw)}|{str(c.ISC).center(iscw)}|{str(c.Quantity).center(qw)}|{str(c.Cost).center(mvw)}|{str(c.Facility).center(fw)}")

                for i, ingredient in enumerate(recipie):
                    if i == 0:
                        continue
                    print(f"|{" ".center(idw)}|{" ".center(namew)}|{str(ingredient[1]).rjust(3)}, {str(ingredient[0]).ljust(inputw - 5)}|{" ".center(pw)}|{" ".center(isaw)}|{" ".center(iscw)}|{" ".center(qw)}|{" ".center(mvw)}|{" ".center(fw)}")

                print(f"|{"-" * idw}|{"-" * namew}|{"-" * inputw}|{"-" * pw}|{"-" * isaw}|{"-" * iscw}|{"-" * qw}|{"-" * mvw}|{"-" * fw}")
        
    def ViewDetailedIndustryOverview(self):
        utils.CLS()
        utils.PrintMenu("Det. Ind. Overview")

        self.PrintResources("Agriculture")
        self.PrintResources("Mining")
        self.PrintResources("Industry")

        print(f"Agriculture Score (ISA/AS): {sum(i[1] for i in self.Agriculture)}/{self.AgricultureScore}")
        print(f"Mining Score (ISA/MS): {sum(i[1] for i in self.Mining)}/{self.MiningScore}")
        print(f"Industry Score (ISA/IS): {sum(sum(i[1]) for i in self.Industry)}/{self.IndustryScore}")

        input("\nPress Enter to continue...")

    def IncreaseIndustry(self):
        while True:
            try:
                utils.CLS()
                utils.PrintMenu("Increase Industry")
                print(f"1. Agriculture Score (ISA/AS): {sum(i[1] for i in self.Agriculture)}/{self.AgricultureScore}")
                print(f"2. Mining Score (ISA/MS): {sum(i[1] for i in self.Mining)}/{self.MiningScore}")
                print(f"3. Industry Score (ISA/IS): {sum(sum(i[1]) for i in self.Industry)}/{self.IndustryScore}")
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
                        match c:
                            case 1:
                                self.AgricultureScore += int(b) / 5
                            case 2:
                                self.MiningScore += int(b) / 5
                            case 3:
                                self.IndustryScore += int(b) / 5
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
            print(f"1. Agriculture Score (ISA/AS): {sum(i[1] for i in self.Agriculture)}/{self.AgricultureScore}")
            print(f"2. Mining Score (ISA/MS): {sum(i[1] for i in self.Mining)}/{self.MiningScore}")
            print(f"3. Industry Score (ISA/IS): {sum(sum(i[1]) for i in self.Industry)}/{self.IndustryScore}")
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
                            max = len(self.Agriculture) - 1
                        case 2:
                            self.PrintResources("Mining")
                            max = len(self.Mining) - 1
                        case 3:
                            self.PrintResources("Industry")
                            max = len(self.Industry) - 1
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
                            resource = self.Agriculture[id][0]
                        case 2:
                            self.PrintResources("Mining", id)
                            resource = self.Mining[id][0]
                        case 3:
                            self.PrintResources("Industry", id)
                            resource = self.Industry[id][0]
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
                            print(f"You are currently producing: { (self.Agriculture[id][1]/ resource.ISC) * resource.Quantity}")
                        case 2:
                            print(f"You are currently producing: { (self.Mining[id][1]/ resource.ISC) * resource.Quantity}")
                        case 3:
                            print(f"You are currently producing: { (sum(self.Industry[id][1])/ resource.ISC) * resource.Quantity}")
                    
                    print("\n[E/e] Exit")

                    ind = input("Enter a number: ")

                    if ind.lower() == "e":
                        break

                    ind = int(ind)

                    if recipie == None:
                        match i:
                            case 1:
                                self.Agriculture[id][1] = ind
                            case 2:
                                self.Mining[id][1] = ind
                            case 3:
                                self.Industry[id][1][0] = ind
                    else:
                        self.Industry[id][1][recipie] = ind
                else:
                    raise Exception("Invalid input")
            except Exception as e:
                utils.PrintErrorMenu(e)

    def ManageImportsExports(self):
        pass

    def GameOptions(self):
        while True:
            utils.CLS()
            utils.PrintMenu("Game Options")
            print("1. Add Resource")

            print("[E/e] Exit")

            c = input("\nEnter a number [1-x]: ")

            if c.lower() == "e":
                break

            try:
                c = int(c)

                match c:
                    case 1:
                        self.CreateResource()
                    case _: # Default
                        raise Exception("Invalid input")
                    
            except Exception as e:
                utils.PrintErrorMenu(e)


    def CreateResource(self):
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
        pass