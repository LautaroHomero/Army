from Pikeman import Pikeman
from Knight import Knight
from Archer import Archer
from Civilization import Civilization

class Byzantines(Civilization):
    def __init__(self):
        super().__init__("Byzantines")
        self.add_units(Pikeman, 5)
        self.add_units(Archer, 8)
        self.add_units(Knight, 15)