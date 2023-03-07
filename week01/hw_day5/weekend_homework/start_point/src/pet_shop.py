# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount


# pet_shop["admin"]["total_cash"] = pet_shop["admin"]["total_cash"] + amount
# Same case as lender & lendee in hw_day_4
# Look at the assert clause and figure out what it’s actually testing.
# If it’s a thing, then return that thing.
# If it’s a variable from having run a different function (like in this case),
# then we’re not actually returning anything, but *doing* something.


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, sold_amount):
    pet_shop["admin"]["pets_sold"] += sold_amount


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


# 7. get_pets_by_breed
def get_pets_by_breed(pet_shop, breed):
    # breed name is in a dic within a list within another dic
    # pdb.set_trace()
    found_pets = []
    # here should be pet_shop["pets"] as "pets" is the list we are using
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_pets.append(pet)  # here we get a list of dic[{},{}..]
    # Q: if we want a list of the breed_name:
    # breed.append(breed_name) is the same as breed.append(pet_breed["breed"])?
    return found_pets


# 8. find_pet_by_name
def find_pet_by_name(pet_shop, pet_name):
    found_pet = None
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            found_pet = pet
    return found_pet


# solution by CodeClan:
# def find_pet_by_name(pet_shop, name):
#     for pet in pet_shop["pets"]:
#         if pet["name"] == name:
#             return pet
#     return None


def remove_pet_by_name(pet_shop, name):
    # for pet in pet_shop["pets"]:
    #     if pet["name"] == pet_name:
    #         index = pet_shop["pets"]["name"].index(pet_name)
    # pet_shop["pets"].pop(index) - need index
    # pet_shop["pets"]["name"].remove(pet_name) - to remove an item
    #  del pet_shop["pets"]["name"].index(pet_name)

    # solution: call the previous function to get the pet dic
    pet_to_delete = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(pet_to_delete)
    # .remove() to remove an item from a list


def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)


def get_customer_cash(customer):
    return customer["cash"]


# do not over complicate things -
# get a value of a dic within a list: list["key_of_a_dic"]


def remove_customer_cash(customer, cash):
    customer["cash"] -= cash


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    #  Here we do not need to return a value


def customer_can_afford_pet(customer, pet):
    can_buy_pet = False
    if customer["cash"] >= pet["price"]:
        can_buy_pet = True
        # return can_buy_pet
    return can_buy_pet


# why this works:
#  return customer["cash"] >= pet["price"]


def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet):
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        # increase_pets_sold(pet_shop, 1)
