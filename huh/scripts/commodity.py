class Resource:
    def __init__(self, info, player_data):
        # Somewhat constant values 
        self.NAME = info['name']
        self.ISC = info['ISC']
        self.AMOUNT = info['amount']
        self.MARKET_VALUE = info['market_value']
        self.FACILITY = info['facility']
        self.RECIPIES = info['recipies']

        # Player data
        self.isa = player_data['isa']
        self.om_imports = player_data['om_imports']
        self.om_exports = player_data['om_exports']
        self.dir_imports = player_data['dir_imports'] # (val, source)
        self.dir_exports = player_data['dir_exports']
        self.stockpile = player_data['stockpile']
        self.private_sector_share = player_data['private_sector_share']

        # Calculated values
        self.public_sector = self.calculate_public_sector()
        self.private_sector = self.calculate_private_sector()

    def calculate_public_sector(self):
        return (self.isa / self.ISC) * self.AMOUNT
    
    def calculate_private_sector(self):
        return ((self.isa/self.ISC) * self.AMOUNT) * (self.private_sector_share / (100 - self.private_sector_share))
    
