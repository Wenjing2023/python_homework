class CoffeeShop:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def shop_name(self):
        return self.name

    def shop_drinks(self):
        return self.drinks

    def increase_till(self, drink):
        self.till += drink.price
