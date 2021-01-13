import unittest 
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Trumpinator", 5.00)

    # def test_drink(self):
    #     self.assertEqual():