import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase): # << in brackets is inheriting from another class.
    

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink = Drink ("Trumpinator", 5.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_money_till(self):
        self.pub.increase_money_till(5.00)
        self.assertEqual(105.00, self.pub.till)
