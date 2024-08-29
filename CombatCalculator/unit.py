"""
Unit Class File for the Reform or Revolution (ROR) Combat Calculator

Holds base class and allows for the creation of a class if no args provided.

Class stats that are tracked officially are as follows:
    - DMG (DAMAGE)              -> Damage dealt over the course of a year
    - HPS (HEALTH)              -> Amount of damage a unit can sustain until it is destroyed
    - SPD (SPEED)               -> Number of cells a unit can move per combat action
    - UKP (UPKEEP)              -> Amount of resources a unit must use to maintain thier combat effectiveness / maximum capacity of resources

Additional/Replacement stats that this calculator will use are as follows:
    - TYPE                      -> The unit's designated type, which will make creating units much easier using a predermined list of units.
    - ABL (ABILITIES)           -> Abilities either active or passive change how damage is dealt in a battle
    - MOD (MODIFIERS)           -> Modifiers given based on resources/terrain/events that dictate combat effectiveness


"""

class Unit:
    
    def __init__(self, name=None, hps=None, dmg=None, spd=None, ukp=None):
        self.name = name
        self.health = hps
        self.damage = dmg
        self.speed = spd
        self.ukp = ukp