import unittest
from src.bar import Bar


class TestBar(unittest.TestCase):
    def setUp(self):
        self.beer = Bar("Beer", 5, 100)
        self.burger = Bar("Burger", 10, 20)

    def test_beer_has_name(self):
        self.assertEqual("Beer", self.beer.name)

    def test_burger_has_price(self):
        self.assertEqual(10, self.burger.price)

    def test_burger_has_stock(self):
        self.assertEqual(100, self.beer.stock)
