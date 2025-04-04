from src.model.Pikeman import Pikeman
from src.model.Knight import Knight
from src.model.Archer import Archer
from src.model.Civilization import Civilization

class English(Civilization):
    def __init__(self):
        super().__init__("English")
        self.add_units(Pikeman, 10)
        self.add_units(Archer, 10)
        self.add_units(Knight, 10)