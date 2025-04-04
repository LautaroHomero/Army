from src.model.Pikeman import Pikeman
from src.model.Knight import Knight
from src.model.Archer import Archer
from src.model.Civilization import Civilization


class Chinese(Civilization):
    def __init__(self):
        super().__init__("Chinese")
        self.add_units(Pikeman, 2)
        self.add_units(Archer, 25)
        self.add_units(Knight, 2)




    
    