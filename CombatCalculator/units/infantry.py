"""
Infantry Unit Class

Inherits from Class {unit} in unit.py
"""

from units import unit

class Infantry(unit.Unit):

    def __init__(self):
        self.type = 0
        super().__init__()
    