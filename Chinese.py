from Pikeman import Pikeman
from Knight import Knight
from Archer import Archer
from Civilization import Civilization


class Chinese(Civilization):
    def __init__(self):
        super().__init__("Chinese")
        self.add_units(Pikeman, 2)
        self.add_units(Archer, 25)
        self.add_units(Knight, 2)




    
    