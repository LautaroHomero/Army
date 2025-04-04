from Unit import Unit

class Knight(Unit):
    def __init__(self):
        super().__init__("Knight", 20)

    def training(self, army):
        self.force += 10
        army.gold -= 30

    def transform(self, army):
        
        return self  
