
class Comodity:
    def __init__(self, name, sector, ISC, Quantity, Cost, Facility=None, Ingredients=None):
        self.name = name
        self.type = sector
        self.ISC = ISC
        self.Quantity = Quantity
        self.Cost = Cost
        self.Facility = Facility
        self.Ingredients = Ingredients