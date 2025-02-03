import json

from scripts import commodity
from scripts import utils

class Economy: 
    def __init__(self):
        self.resources = self.load_resources()

        self.menu()

    def load_resources(self):
        resources = []
        try:
            with open('game_data/resources.json') as f:
                data = json.load(f)
            with open('game_data/player_economy_data.json') as f:
                player_economy_data = json.load(f)
            for resource in data:
                resources.append(commodity.Resource(resource, player_economy_data[resource['name']]))
        except Exception as e:
            utils.PrintErrorMenu(str(e) + "\n\nReturning empty list.")
        return resources
        
    def menu(self):
        options = [
            "View Economy Overview",
        ]
        utils.CLS()
        utils.PrintMenu("ECONOMY MENU", options)
    