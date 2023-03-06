# WRITE YOUR FUNCTIONS HERE
# 1. get_pet_shop_name
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


# 2. get_total_cash
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


# 3. add_or_remove_cash
def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount


# Same case as lender & lendee in hw_day_4
# Look at the assert clause and figure out what it’s actually testing.
# If it’s a thing, then return that thing.
# If it’s a variable from having run a different function (like in this case),
# then we’re not actually returning anything, but *doing* something.


# 4. get_pets_sold
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


# 5. increase_pets_sold
def increase_pets_sold(pet_shop, sold_anount):
    pet_shop["admin"]["pets_sold"] += sold_anount


# 6. get_stock_count
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


# 7. get_pets_by_breed
def get_pets_by_breed(pet_shop, breed_name):
    # breed name is in a dic within a list within another dic
    breed = []
    # here should be pet_shop["pets"] as "pets" is the list we are using
    for pet_breed in pet_shop["pets"]:
        if pet_breed["breed"] == breed_name:
            breed.append(breed_name)
    return breed


# 8. find_pet_by_name
def find_pet_by_name(pet_shop, pet_name):
    found_pet = None
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            found_pet = pet
    return found_pet


# # 9. remove_pet_by_name - Q
# def remove_pet_by_name(pet_shop, pet_name):
#     # for pet in pet_shop["pets"]:
#     #     if pet["name"] == pet_name:
#     #         index = pet_shop["pets"]["name"].index(pet_name)

#     # pet_shop["pets"].pop(index)
#     # pet_shop["pets"]["name"].remove(pet_name)
#      del pet_shop["pets"]["name"].index(pet_name)


# 10. add_pet_to_stock
def add_pet_to_stock(pet_shop, pet_name):
    pet_shop["pets"].append(pet_name)


# 11. get_customer_cash -
def get_customer_cash(customer):
    cash = customer["cash"]
    return cash


# 12. remove_customer_cash
def remove_customer_cash(customer, cash):
    customer["cash"] -= cash


# 13. get_customer_pet_count
def get_customer_pet_count(customer):
    return customer["pets"]


# 14. add_pet_to_customer
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


# 15. customer_can_afford_pet
def customer_can_afford_pet(customer, new_pet):
    customer_cash = customer["cash"]
    pet_value = new_pet["price"]
    if customer_cash >= pet_value:
        return True
