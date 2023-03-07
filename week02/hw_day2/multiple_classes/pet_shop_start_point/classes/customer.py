class Customer:
    # write pass so at this stage we don't have to do anything
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self._pets = []

    # there is no need to add pets in def () because our pets start empty
    # add _ before _pets annoucing this is used only in this class
    # When adding a pet:
    # Instead of customer.pets.append(pets) we should use customer.pets.add_pet(pet)
    # This is because in this way we give responsibility to the customer
    # as maybe pets is a dic not a list; also makes the code more clear

    def reduce_cash(self, amount):
        self.cash -= amount

    def pet_count(self):
        return len(self._pets)

    def add_pet(self, pet):
        self._pets.append(pet)

    def get_total_value_of_pets(self):
        total = 0
        for pet in self._pets:
            total += pet.price
        #  we got pet.price here because .append(pet) we are adding pet info
        #  we do not need to import pet.py because that class's purpose is to create a pet
        #  if we need to add a pet we use customer_test.py
        return total
