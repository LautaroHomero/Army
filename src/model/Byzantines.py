from src.model.Pikeman import Pikeman
from src.model.Knight import Knight
from src.model.Archer import Archer
from src.model.Civilization import Civilization

class Byzantines(Civilization):
    def __init__(self):
        super().__init__("Byzantines")
        self.add_units(Pikeman, 5)
        self.add_units(Archer, 8)
        self.add_units(Knight, 15)