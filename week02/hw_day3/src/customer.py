class Customer:
    def __init__(self, name, wallet, age, energy):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy = energy

    def reduce_money(self, drink):
        self.wallet -= drink.price

    def check_age(self):
        if self.age < 16:
            return "You are too young!"
        else:
            return "Here is your coffee"

    def energy_increase(self, drink):
        self.energy += drink.caffeine

    def refuse_service(self):
        if self.energy > 10:
            return "Sorry nothing for you"
        else:
            return "What would you like?"

    def rejuvenation_decrease(self, food):
        self.energy -= food.rejuvenation
