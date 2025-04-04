from src.model.Battle import Battle

class Army:
    def __init__(self, civilization):
        self.civilization = civilization
        self.gold = 1000
        self.battles = []
        self.unit=civilization.unit

    def attack(self, enemy_army):
        if len(self.unit) < 1:
            raise Exception(f"{self.civilization.name} army can't attack — not enough units.")
        
        battle = Battle()
        new_battle=battle.battleBetween(self, enemy_army)

        self.battles.append(new_battle)
        enemy_army.battles.append(new_battle)

    def unitTrain(self, unitToTrain):
        if(unitToTrain in self.unit):
            unitToTrain.training(self)
        else:
            raise ValueError("This unit does not belong to the army.")

    def unitTransf(self, unitToTransform):
        if(unitToTransform in self.unit):
            new_unit=unitToTransform.transform(self)

            if(new_unit not in self.unit):
                index=self.unit.index(unitToTransform)
                self.unit[index]=new_unit

        else:
            raise ValueError("This unit does not belong to the army.")    

        
    def loseUnits(self):
        if len(self.unit)<=2:
            self.unit=[]
            return
        
        for _ in range(2):
            max_unit = max(self.unit, key=lambda x: x.force)
            self.unit.remove(max_unit)