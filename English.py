from Pikeman import Pikeman
from Knight import Knight
from Archer import Archer
from Civilization import Civilization

class English(Civilization):
    def __init__(self):
        super().__init__("English")
        self.add_units(Pikeman, 10)
        self.add_units(Archer, 10)
        self.add_units(Knight, 10)