class Guest:
    def __init__(self, name, money, favourite_song):
        self.name = name
        self.money = money
        self.favourite_song = favourite_song

    def sufficient_funds_to_enter(self, room):
        return self.money >= room.entry_fee

    def enter(self, room):
        if self.sufficient_funds_to_enter(room):
            self.money -= room.entry_fee
        # return self.money

    def sufficient_funds_for_bar(self, room, beer):
        self.enter(room)
        return self.money >= beer.price

    def buy_food(self, room, food):
        # Q: is this necessary:
        # if self.sufficient_funds_for_bar(room, food):
        self.enter(room)
        self.money -= food.price
