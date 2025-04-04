from Unit import Unit
from Knight import Knight

class Archer(Unit):
    def __init__(self):
        super().__init__("Archer", 10)

    def training(self, army):
        self.force += 7
        army.gold -= 20

    def transform(self, army):
        if army.gold>=40:
            army.gold -= 40
            new_knight=Knight()
            new_knight.force=self.force
            return new_knight
        
        return self
