class Unit:
    def __init__(self, type, force):
        self.type=type
        self.force = force
        
    
    def training(self, army):
        self.type.training(army)

    def transform(self, army):
        self.type.transform()

    
    
    
