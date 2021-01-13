class Customer:
    
    def __init__(self, name, wallet, age): # constructor function
        self.name = name 
        self.wallet = wallet
        self.age = age
        self.drinks_list = []
        
    def buy_a_drink(self, drink):
        self.drinks_list.append(drink)

    def remove_money_wallet(self, price):
        self.wallet -= price
        return self.wallet 