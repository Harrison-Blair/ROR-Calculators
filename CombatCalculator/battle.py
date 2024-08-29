"""
Battle interaction handler for the Reform or Revolution (ROR) Combat Calculator
"""
import unit
import utils

class Battle:

    def __init__(self, attacker=None, defedner=None):
        if(attacker==None):
            self.atkr = self.CreateUnit("Attacker")
        else:
            self.atkr = self.CreateUnit(stats=attacker.GetStats())

        if(defedner==None):
            self.defr = self.CreateUnit("Defender")
        else:
            self.defr = self.CreateUnit(stats=defedner.GetStats())

        self.SimulateCombat(self.atkr, self.defr)

    def CreateUnit(self, pos=None, stats=None):
        while True:
            if (stats != None):
                return unit.Unit(stats[0][1], stats[1][1], stats[2][1], stats[3][1], stats[4][1], stats[5][1], stats[6][1], stats[7][1])
            
            utils.CLS()
            utils.PrintMenu("UNIT CREATION MENU")
            print(f"What is the unit type of the {pos}?\n")
            utils.PrintUnitInfo(True)

            try:
                choice = int(input("\n\nDesired Unit Type ID# : "))

                stats = self.GetBaseUnitStats(choice)

                u = unit.Unit(stats[0][1], stats[1][1], stats[2][1], stats[3][1], stats[4][1], stats[5][1], stats[6][1], stats[7][1])

                u.ModifiersMenu()

                return u

            except Exception as e:
                utils.PrintErrorMenu(str(e))

    def GetBaseUnitStats(self, type=None):
        stats = []
        for i in utils.LoadUnitTypes():
            if (i['id'] == type):
                stats.append(['name', i['name']])
                stats.append(['cname', i['name']])
                stats.append(['cid', i['id']])
                stats.append(['hps', i['hps']])
                stats.append(['max_hps', i['hps']])
                stats.append(['dmg', i['dmg']])
                stats.append(['spd', i['spd']])
                stats.append(['ukp', i['ukp']])
        
        return stats
    
    def CalcUnitTotalMod(self, unit):
        stats = unit.GetStats()
        print(stats)
        total = 0.0

        if stats[8][1] == None:
            print("fc")
            input()
            return 0

        for i in stats[8][1]:
            total += i[1]

        print(total)
        input()

        return round(total, 2)

    def SimulateCombat(self, atkr, defr):
        m_atkr = 1 + self.CalcUnitTotalMod(atkr)
        m_defr = 1 + self.CalcUnitTotalMod(defr)

        a_p_hp = atkr.health
        d_p_hp = defr.health

        a_atk = atkr.damage * m_atkr
        d_atk = defr.damage * m_defr

        defr.TakeDamage(a_atk)
        atkr.TakeDamage(d_atk)

        utils.CLS()
        utils.PrintMenu("BATTLE RESULT")
        utils.PrintSubheader(f"{format(atkr.name, "<37")} v.s. {format(atkr.name, ">37")}")
        print(f"{format(atkr.cname, "<38")} || {format(defr.cname, ">38")}")
        print(f"{format(f"{a_p_hp} / {atkr.max_health}", "<18")}->{format(f"{atkr.health} / {atkr.max_health}", ">18")} || {format(f"{defr.health} / {defr.max_health}", "<18")}<-{format(f"{d_p_hp} / {defr.max_health}", ">18")}")
        print(f"{format(f"- {d_atk}", ">38")} || {format(f"- {a_atk}", "<38")}")

        utils.PrintSubheader("Stats".center(80))
        print(f"{format(atkr.speed, ">27")} |{"Speed".center(22)}| {format(atkr.speed, "<27")}")
        print(f"{format(atkr.damage, ">27")} |{"Attack".center(22)}| {format(atkr.damage, "<27")}")
        print(f"{"MODS".center(80, "-")}")


        if (atkr.mods == None):
            def_mod_values = []
            for i in range(len(atkr.mod_names)):
                def_mod_values.append([i, 0])
            atkr.mods = def_mod_values

        if (defr.mods == None):
            def_mod_values = []
            for i in range(len(defr.mod_names)):
                def_mod_values.append([i, 0])
            defr.mods = def_mod_values

        for i in range(len(atkr.mod_names)):
            print(f"{format(f"{"+" if atkr.mods[i][1] > 0 else ""}{atkr.mods[i][1] * 100} %", ">27")} |{f"{atkr.mod_names[i]}".center(22)}| {format(f"{"+" if defr.mods[i][1] > 0 else ""}{defr.mods[i][1] * 100} %", "<27")}")
        print(f"{format(f"{round(m_atkr * 100, 2)} %", ">27")} |{"Total Efficacy".center(22)}| {format(f"{round(m_defr * 100, 2)} %", "<27")}")

        utils.PrintSubheader("\n\n\tMenu")
        print("\t\t1. Save Battle")
        print("\t\t2. Flip Attacker & Defender")

        input("\n\t> ")


