import unittest

from classes.customer import Customer
from classes.pet import Pet


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jack Jarvis", 1000)
        self.pet = Pet("Blue", "cat", "British Shorthair", 500)

    def test_customer_has_name(self):
        self.assertEqual("Jack Jarvis", self.customer.name)

    def test_customer_has_cash(self):
        self.assertEqual(1000, self.customer.cash)

    def test_customer_can_reduce_cash(self):
        self.customer.reduce_cash(500)
        self.assertEqual(500, self.customer.cash)

    # self.customer.cash is an attribute not a method; has things not does things

    # @unittest.skip("delete this line to run the test")
    def test_pets_start_at_0(self):
        self.assertEqual(0, self.customer.pet_count())
        # pet_count() is a method
        # there is no parameters as pet_count() is empty
        # there is sth to return: 0 - is what we are expecting
        # we will need to use len(), so we need to create a list

    # @unittest.skip("delete this line to run the test")
    def test_can_add_pet(self):
        self.customer.add_pet(self.pet)
        self.assertEqual(1, self.customer.pet_count())

    # @unittest.skip("delete this line to run the test")
    def test_can_get_total_pet_cost(self):
        self.customer.add_pet(self.pet)
        self.customer.add_pet(self.pet)
        self.customer.add_pet(self.pet)
        #  we are adding Blue 3 times
        self.assertEqual(1500, self.customer.get_total_value_of_pets())
