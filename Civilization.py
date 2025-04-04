class Civilization:
    def __init__(self, name):
        self.name = name
        self.unit = []
        
    def add_units(self, unit_class, quantity):
        self.unit.extend([unit_class() for _ in range(quantity)])
