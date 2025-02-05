import json

from scripts import commodity
from scripts import utils

class Economy: 
    def __init__(self):
        self.resources = self.load_resources()
        self.save_resources()

    def load_resources(self):
        resources = []
        try:
            with open('game_data/resources.json', 'r') as f:
                data = json.load(f)
            with open('game_data/player_economy_data.json', 'r') as f:
                player_economy_data = json.load(f)
            try:
                player_economy_data['private_sector_share']
            except:
                player_economy_data['private_sector_share'] = 90
            self.private_sector_share = player_economy_data['private_sector_share']
            for resource in data:
                try:
                    player_economy_data[resource['name']]
                except:
                    player_economy_data[resource['name']] = {
                        'isa': 0,
                        'om_imports': 0,
                        'om_exports': 0,
                        'dir_imports': [],
                        'dir_exports': [],
                        'stockpile': 0,
                    }
                resources.append(commodity.Resource(resource, player_economy_data[resource['name']], self.private_sector_share))
        except Exception as e:
            utils.PrintErrorMenu(str(e) + "\n\nReturning empty list of Resources.")
        return resources
        
    def save_resources(self):
        try:
            with open('game_data/player_economy_data.json', 'w') as f:
                player_economy_data = {}
                player_economy_data['private_sector_share'] = self.private_sector_share
                for resource in self.resources:
                    resource: commodity.Resource
                    player_economy_data[resource.NAME] = {
                        'isa': resource.isa,
                        'om_imports': resource.om_imports,
                        'om_exports': resource.om_exports,
                        'dir_imports': resource.dir_imports,
                        'dir_exports': resource.dir_exports,
                        'stockpile': resource.stockpile,
                    }
                json.dump(player_economy_data, f, indent=4)
        except Exception as e:
            utils.PrintErrorMenu(str(e) + "\n\nFailed to save player_economy_data.")
        
        try:
            with open('game_data/resources.json', 'w') as f: 
                json.dump([{
                    'name': resource.NAME,
                    'sector': resource.SECTOR,
                    'ISC': resource.ISC,
                    'amount': resource.AMOUNT,
                    'market_value': resource.MARKET_VALUE,
                    'facility': resource.FACILITY,
                    'recipies': resource.RECIPIES,
                } for resource in self.resources], f, indent=4) #Type: List[commodity.Resource] <- I want to make this typed if possible
        except Exception as e:
            utils.PrintErrorMenu(str(e) + "\n\nFailed to save resources.json.")

    def menu(self):
        options = [
            "View Economy Overview",
        ]
        while True:
            utils.CLS()
            utils.PrintMenu("ECONOMY MENU", options)
            print("\t[O/o] Economy Options")
            print("\n\t[E/e] Exit")
            choice = input("\n> ")

            if choice.lower() == "o":
                continue #self.economyoptions
            elif choice.lower() == "e":
                break

            try:
                choice = int(choice)

                match choice:
                    case 0:
                        self.view_economy_overview()
            except Exception as e:
                utils.PrintErrorMenu(str(e) + "\n\nInvalid input.")

    def view_economy_overview(self):
        pass