import unittest 
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Donald Trump", 1000.00)
        self.drink = Drink("Trumpinator", 5.00)

    def test_buy_a_drink(self):
        self.customer.buy_a_drink(self.drink)
        self.assertEqual(1, len(self.customer.drinks_list))

    def test_remove_money_wallet(self):
        self.customer.remove_money_wallet(self.drink.price)
        self.assertEqual(995, self.customer.wallet)
        

    # def test_wallet(self):
    #     self.assertEqual():