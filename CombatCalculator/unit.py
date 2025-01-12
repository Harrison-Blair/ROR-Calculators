class Unit:
    def __init__(self, type, symbol, hps, dmg, spd, ukp):
        self.type = type

        self.symbol = eval(r"'\N" + symbol + "'")
        
        self.hps = hps
        self.max_hps = hps
        
        self.dmg = dmg
        self.spd = spd
        
        self.ukp = []

        self.main_res = None
        self.ammo = None

        self.fuel = None # Only Vehicle units

        for resource in ukp:
            self.ukp.append((resource[0], float(resource[1])))

            if self.main_res == None:
                self.main_res = resource[0]

            if self.ammo == None and "Ammo" in resource[0]:
                self.ammo = resource[0]

            if self.fuel == None and "Fuel" in resource[0]:
                self.fuel = resource[0]
