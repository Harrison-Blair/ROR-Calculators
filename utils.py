import os
import json
import shutil

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

def PrintMenu(name="MENU NAME", length=150):
    """ Prints a given menu name at a given length with bars surrounding """
    print("=" * (length + 1))
    if len(name) < 25:
        for i in range(int(length / 25)):
            print(f"/" + name.center(24), end="")
    elif len(name) < 30:
        for i in range(int(length / 30)):
            print(f"/" + name.center(29), end="")
    elif len(name) < 50:
        for i in range(int(length / 50)):
            print(f"/" + name.center(49), end="")
    else:
        print(f"/" + name.center(length - 1), end="")
    print("/")
    print("=" * (length + 1))

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
    # Try to backup the player.json file if exists
    try:
        shutil.move('player.json', 'player.json.bak')
    except:
        pass

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

    IndustrialScores = [agrs, mins, inds]

    Resources = [[],[],[]]

    PublicIndustry = [[],[],[]]

    # Import/Export
    ImpExp = [[],[],[]]

    # Consumption
    Consumption = [[[],[],[]],[[],[],[]],[[],[],[]]]

    with open('resources.json', 'r') as file:
        resources = json.load(file)

    for resource in resources:
        print(f"{resource}")

        if resource['type'] == 'Agriculture':
            res = comodity.Comodity(resource['name'], resource['ISC'], resource['Quantity'], resource['Cost'], f"{resource['name']} Farm")
            Resources[0].append(res)
            ImpExp[0].append([res.name, [0.0, 0.0]])
            PublicIndustry[0].append([res.name, 0.0])
            for i in range(3):
                Consumption[i][0].append([res.name, 0.0])
        elif resource['type'] == 'Mining':
            res = comodity.Comodity(resource['name'], resource['ISC'], resource['Quantity'], resource['Cost'], f"{resource['name']} Mine")
            Resources[1].append(res)
            ImpExp[1].append([res.name, [0.0, 0.0]])
            PublicIndustry[1].append([res.name, 0.0])
            for i in range(3):
                Consumption[i][1].append([res.name, 0.0])
        elif resource['type'] == 'Industry':
            res = comodity.Comodity(resource['name'], resource['ISC'], resource['Quantity'], resource['Cost'], resource['Facility'], resource['Input'])
            Resources[2].append(res)
            isa = []
            for i in resource['Input']:
                isa.append(0.0)
            ImpExp[2].append([res.name, isa * 2])
            PublicIndustry[2].append([res.name, isa])
            for i in range(3):
                Consumption[i][2].append([res.name, isa])
    
    return info, policy, IndustrialScores, Resources, PublicIndustry, ImpExp, Consumption

def LoadPlayerData(): 
    with open('player.json', 'r') as file:
        data = json.load(file)
        if len(data) == 0:
            raise Exception
        
        Resources = [[],[],[]]

        with open('resources.json', 'r') as file:
            resources = json.load(file)

        for resource in resources:
            print(f"{resource}")

            match resource['type']:
                case 'Agriculture':
                    res = comodity.Comodity(resource['name'], resource['ISC'], resource['Quantity'], resource['Cost'], f"{resource['name']} Farm")
                    Resources[0].append(res)
                case 'Mining':
                    res = comodity.Comodity(resource['name'], resource['ISC'], resource['Quantity'], resource['Cost'], f"{resource['name']} Mine")
                    Resources[1].append(res)
                case 'Industry':
                    res = comodity.Comodity(resource['name'], resource['ISC'], resource['Quantity'], resource['Cost'], resource['Facility'], resource['Input'])
                    Resources[2].append(res)

        return data['info'], data['policy'], data['IndustrialScores'], Resources, data['PublicIndustry'], data['ImportExport'], data['Consumption']