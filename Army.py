from Battle import Battle

class Army:
    def __init__(self, civilization):
        self.civilization = civilization
        self.gold = 1000
        self.battles = []
        self.unit=civilization.unit

    def attack(self, ejercito):
        battle=Battle()
        battle.battleBetween(self, ejercito)
        
    def loseUnits(self):
        if len(self.unit)<2:
            self.unit=[]
            return
        
        for _ in range(2):
            max_unit = max(self.unit, key=lambda x: x.force)
            self.unit.remove(max_unit)