import os
import json
import comodity

def CLS():
    # Thanks to Steven D'Aprano, http://www.velocityreviews.com/forums
    if os.name == "posix":
    # Unix, Linux, macOS, BSD, etc.
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
    # DOS/Windows
        os.system('CLS')
    else:
    # Fallback for other operating systems.
        print('\n' * 100)

def PrintMenu(name="MENU NAME", length=140):
    """ Prints a given menu name at a given length with bars surrounding """
    print()
    print("=" * length)
    n = name.center(18)
    print(f"|{n}|" * 7)
    print("=" * length)

def PrintErrorMenu(error=None):
    """ Prints an error message, and then returns """
    PrintMenu("ERROR MENU")
    print("\nAn error has occured!")
    if (error != None):
        print(f"\n{error}")
    input("\n\x1B[3mPress enter to continue...\x1B[0m")

def CreatePlayerData():
    CLS()
    PrintMenu("Create Player")
    # Player Info
    info = {}
    
    name = input("Enter your name: ")
    
    info['name'] = name

    # Policy | TODO: Allow user to define policy from character creation?
    policy = {}

    policy["PublicIndustry"] = 10.0

    # Industry Scores
    agrs = float(input("Enter your Agricultural Score: "))
    mins = float(input("Enter your Mining Score: "))
    inds = float(input("Enter your Industrial Score: "))

    # Industry
    Industry = []
    Agriculture = []
    Mining = []

    # Import/Export
    ImpExpCon = []

    AgricultureImpExp = []
    MiningImpExp = []
    IndustryImpExp = []

    # Consumption
    Consumption = [[[],[],[]],[[],[],[]],[[],[],[]]]

    with open('resources.json', 'r') as file:
        resources = json.load(file)

    for resource in resources:
        print(f"{resource}")

        if resource['type'] == 'Agriculture':
            res = comodity.Comodity(resource['name'], resource['ISC'], resource['Quantity'], resource['Cost'], f"{resource['name']} Farm")
            AgricultureImpExp.append([res, 0.0])
            Agriculture.append([res, 0.0])
            for i in range(3):
                Consumption[i][0].append([res, 0.0])
        elif resource['type'] == 'Mining':
            res = comodity.Comodity(resource['name'], resource['ISC'], resource['Quantity'], resource['Cost'], f"{resource['name']} Mine")
            MiningImpExp.append([res, 0.0])
            Mining.append([res, 0.0])
            for i in range(3):
                Consumption[i][1].append([res, 0.0])
        elif resource['type'] == 'Industry':
            res = comodity.Comodity(resource['name'], resource['ISC'], resource['Quantity'], resource['Cost'], resource['Facility'], resource['Input'])
            IndustryImpExp.append([res, 0.0])
            isa = []
            for i in resource['Input']:
                isa.append(0)
            Industry.append([res, isa])
            for i in range(3):
                Consumption[i][2].append([res, isa])

    ImpExpCon.append(AgricultureImpExp)
    ImpExpCon.append(MiningImpExp)
    ImpExpCon.append(IndustryImpExp)
    
    return info, policy, inds, agrs, mins, Industry, Agriculture, Mining, ImpExpCon, ImpExpCon, Consumption

def LoadPlayerData(): 
    with open('player.json', 'r') as file:
        data = json.load(file)
        if len(data) == 0:
            raise Exception
        
        Industry = []
        Agriculture = []
        Mining = []

        IndustryImports = []
        AgricultureImports = []
        MiningImports = []

        IndustryExports = []
        AgricultureExports = []
        MiningExports = []

        Imports = []
        Exports = []

        Consumption = [[[],[],[]],[[],[],[]],[[],[],[]]]

        with open('resources.json', 'r') as file:
            resources = json.load(file)

        for resource in resources:
            print(f"{resource}")
            imp = next((com[1] for com in data['Imports'] if com[0] == resource['name']), 0)
            exp = next((com[1] for com in data['Exports'] if com[0] == resource['name']), 0)


            if resource['type'] == 'Agriculture':
                ind = next((com[1] for com in data['Agriculture'] if com[0] == resource['name']), 0)
                res = comodity.Comodity(resource['name'], resource['ISC'], resource['Quantity'], resource['Cost'], f"{resource['name']} Farm")
                Agriculture.append([res, ind])
                AgricultureImports.append([res, imp])
                AgricultureExports.append([res, exp])

                PopCon = next((com[1] for com in data['Consumption'][0][0] if com[0] == resource['name']), 0)
                IndCon = next((com[1] for com in data['Consumption'][1][0] if com[0] == resource['name']), 0)
                ActCon = next((com[1] for com in data['Consumption'][2][0] if com[0] == resource['name']), 0)

                Consumption[0][0].append([res, PopCon])
                Consumption[1][0].append([res, IndCon])
                Consumption[2][0].append([res, ActCon])
            elif resource['type'] == 'Mining':
                ind = next((com[1] for com in data['Mining'] if com[0] == resource['name']), 0)
                res = comodity.Comodity(resource['name'], resource['ISC'], resource['Quantity'], resource['Cost'], f"{resource['name']} Mine")
                Mining.append([res, ind])
                MiningImports.append([res, imp])
                MiningExports.append([res, exp])

                PopCon = next((com[1] for com in data['Consumption'][0][1] if com[0] == resource['name']), 0)
                IndCon = next((com[1] for com in data['Consumption'][1][1] if com[0] == resource['name']), 0)
                ActCon = next((com[1] for com in data['Consumption'][2][1] if com[0] == resource['name']), 0)

                Consumption[0][1].append([res, PopCon])
                Consumption[1][1].append([res, IndCon])
                Consumption[2][1].append([res, ActCon])
            elif resource['type'] == 'Industry':
                res = comodity.Comodity(resource['name'], resource['ISC'], resource['Quantity'], resource['Cost'], resource['Facility'], resource['Input'])
                isa = []
                for i, r in enumerate(resource['Input']):
                    isa.append(next((com[1][i] for com in data['Industry'] if com[0] == resource['name']), 0))
                Industry.append([res, isa])
                IndustryImports.append([res, imp])
                IndustryExports.append([res, exp])

                PopCon = next((com[1] for com in data['Consumption'][0][2] if com[0] == resource['name']), 0)
                IndCon = next((com[1] for com in data['Consumption'][1][2] if com[0] == resource['name']), 0)
                ActCon = next((com[1] for com in data['Consumption'][2][2] if com[0] == resource['name']), 0)

                Consumption[0][2].append([res, PopCon])
                Consumption[1][2].append([res, IndCon])
                Consumption[2][2].append([res, ActCon])

        Imports.append(AgricultureImports)
        Imports.append(MiningImports)
        Imports.append(IndustryImports)

        Exports.append(AgricultureExports)
        Exports.append(MiningExports)
        Exports.append(IndustryExports)

        return data['info'], data['policy'], data['IS'], data['AS'], data['MS'], Industry, Agriculture, Mining, Imports, Exports, Consumption