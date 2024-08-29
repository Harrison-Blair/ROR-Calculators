"""
Battle interaction handler for the Reform or Revolution (ROR) Combat Calculator
"""

import utils

class Battle:

    def __init__(self, attacker=None, defedner=None):
        if(attacker==None or defedner==None):
            self.atkr = self.CreateUnit("Attacker")
            self.defr = self.CreateUnit("Defender")

    def CreateUnit(self, name=None, type=None):
        while True:
            utils.CLS()
            utils.PrintMenu("UNIT CREATION MENU")
            
            input()