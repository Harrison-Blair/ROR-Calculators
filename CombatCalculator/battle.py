"""
Battle Class
"""

from units import infantry

class Battle:

    def __init__(self):
        self.name = ""
        self.attacker = infantry.Infantry()
        self.defender = infantry.Infantry()
