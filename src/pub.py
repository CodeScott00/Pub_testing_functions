class Pub:
    
    def __init__(self, name, till): # constructor function
        self.name = name 
        self.till = till
        self.drinks = []

    def increase_money_till(self, drink):
        self.till += drink

    