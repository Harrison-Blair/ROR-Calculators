"""
Battle Class
"""
import utils
from units import infantry
from units import unit
class Battle:

    def __init__(self):
        self.name = ""
        self.attacker = self.CreateUnit("Attacking")
        self.defender = self.CreateUnit("Defending")
        self.guy = unit.Unit()

    def CreateUnit(self, action):
        while True:
            utils.cls()
            utils.PrintMenu("UNIT SELECTION")
            print(f"\nWhat kind of unit is {action}?")
            print("1. Infantry")
            print("2. Armor")
            print("3. Mobile")
            print("4. Artillery")
            print("5. Shock Troops")
            print("6. Paratrooper")
            print("7. Partisan")
            print("8. Marine")
            print("9. Spec Ops")
            
            try:
                unit = int(input())
                return infantry.Infantry()
                
            except:
                utils.ErrorInput()