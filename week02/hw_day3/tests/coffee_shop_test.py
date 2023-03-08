#     def setUp(self):
#         self.coffee_shop = CoffeeShop("Sky's Coffee Shop", 100.00)

#     def test_coffee_shop_has_name(self):
#         self.assertEqual("Sky's Coffee Shop", self.coffee_shop.name)

#     def test_can_increase_till(self):
#         # Arrange: self.coffee_shop = CoffeeShop()
#         # Act:
#         self.coffee_shop.increase_till(5.99)
#         # Assert
#         # expected = 105.99
#         # actual = self.coffee_shop.till
#         # self.assertEqual(expected, actual)
#         self.assertEqual(105.99, self.coffee_shop.till)


import unittest
from src.drinks import Drinks
from src.customer import Customer
from src.coffee_shop import CoffeeShop
from src.food import Food


class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.coffee_shop = CoffeeShop(
            "L and W Cafe", 500, ["coffee”, “tea”, “latte”, “espresso”, “water"]
        )
        self.drink = Drinks("coffee", 4, 5)
        self.customer = Customer("Mar", 50, 18, 10)
        self.food = Food("cake", 5, 5)

    def test_shop_name(self):
        self.assertEqual("L and W Cafe", self.coffee_shop.shop_name())

    def test_has_drinks(self):
        self.assertEqual(
            ["coffee”, “tea”, “latte”, “espresso”, “water"],
            self.coffee_shop.shop_drinks(),
        )

    def test_reduce_money(self):
        self.customer.reduce_money(self.drink)
        self.assertEqual(46, self.customer.wallet)

    def test_increase_till(self):
        self.coffee_shop.increase_till(self.drink)
        self.assertEqual(504, self.coffee_shop.till)

    def test_check_age(self):
        self.assertEqual("Here is your coffee", self.customer.check_age())

    def test_energy_increase(self):
        self.customer.energy_increase(self.drink)
        self.assertEqual(15, self.customer.energy)

    def test_refuse_service(self):
        self.assertEqual("What would you like?", self.customer.refuse_service())

    def test_rejuvenation_decrease(self):
        self.customer.rejuvenation_decrease(self.food)
        self.assertEqual(5, self.customer.energy)
