from Unit import Unit
from Archer import Archer

class Pikeman(Unit):
    def __init__(self):
        super().__init__("Pikeman", 5)

    def training(self, army):
        self.force +=3
        army.gold -= 10

    def transform(self, army):
        if army.gold>=30:
            army.gold -= 30
            new_archer=Archer()
            new_archer.force=self.force
            return new_archer
        
        return self

