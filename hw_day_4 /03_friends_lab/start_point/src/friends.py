def get_name(person):
    return person["name"]


def get_favourite_tv_show(tvshow):
    return tvshow["favourites"]["tv_show"]


def likes_to_eat(person, yoursnacks):
    found_snacks = False
    # I have to specify snack_list["favourites"]["snacks"]
    for each_snack in person["favourites"]["snacks"]:
        if each_snack == yoursnacks:
            found_snacks = True  # Q -- why not: return Trun

    #   if each_snack["favourites"]["snacks"] == yoursnacks:
    #   TpeError: string indices must be integers

    return found_snacks  # Q Why not: return False, do we have to return sth?
    # if I do not add the next line, it says: AssertionError: True != None


#  Mar's example:
# def likes_to_eat(person_whose_fav_food_we_will_look_through, snack_to_be_searched_for):
#     all_persons_snacks = person_whose_fav_food_we_will_look_through["favourites"][
#         "snacks"
#     ]
#     found_food = False
#     for each_snack in all_persons_snacks:
#         if each_snack == snack_to_be_searched_for:
#             found_food = True
#     # if I do not add the next line, it says: AssertionError: True != None - why is that?
#     return found_food


def add_friend(person, new_friend):
    person["friends"].append(new_friend)
