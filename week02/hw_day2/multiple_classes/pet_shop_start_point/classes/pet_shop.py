class PetShop:
    def __init__(self, name, pet_list, total_cash):
        self.name = name
        self.pet_list = pet_list
        self.total_cash = total_cash
        self.pets_sold = 0

    def stock_count(self):
        return len(self.pet_list)

    def increase_pets_sold(self):
        self.pets_sold += 1

    def increase_total_cash(self, amount):
        self.total_cash += amount

    def remove_pet(self, removed_pet):
        self.pet_list.remove(removed_pet)

    def find_pet_by_name(self, name):
        # pet_list is a list, I have to use for loop
        for pet in self.pet_list:
            if pet.name == name:
                return pet

    # here to return pet not pet name because in the Q it needs a list:
    # it is already using pet.name to get the name

    def sell_pet_to_customer(self, pet_name, customer):
        pet = self.find_pet_by_name(pet_name)
        customer.reduce_cash(pet.price)
        self.increase_total_cash(pet.price)
        self.increase_pets_sold()
        self.remove_pet(pet)
        self.stock_count()
        customer.add_pet(pet)
        customer.pet_count()
