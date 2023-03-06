def get_name(person):
    return person["name"]


def get_favourite_tv_show(tvshow):
    return tvshow["favourites"]["tv_show"]


def likes_to_eat(person, food):
    # snacks is a list within a dic within another dic
    found_snacks = False
    for each_snack in person["favourites"]["snacks"]:
        if each_snack == food:
            found_snacks = (
                True  # Q1 -- if I write "return True" does it means the same?
            )
    #  Q2 - The reason I cannot write below is because person is not a list?
    # for each_snack in person:
    #     if each_snack["favourites"]["snacks"] == food:
    #         found_snacks = True
    #   TpeError: string indices must be integers
    return found_snacks
    # Q3 Why not: return False, do we have to return sth?
    # if I do not add the return line, it says: AssertionError: True != None


#  Mar's example:
# def likes_to_eat(person_whose_fav_food_we_will_look_through, snack_to_be_searched_for):
#     all_persons_snacks = person_whose_fav_food_we_will_look_through["favourites"][
#         "snacks"
#     ]
#     found_food = False
#     for each_snack in all_persons_snacks:
#         if each_snack == snack_to_be_searched_for:
#             found_food = True
#     return found_food


def add_friend(person, new_friend):
    person["friends"].append(new_friend)


def remove_friend(person, removed_friend):
    friend_index = person["friends"].index(removed_friend)
    person["friends"].pop(friend_index)


def total_money(person):
    count_amount = 0

    for each_money in person:
        count_amount += each_money["monies"]
    return count_amount


def lend_money(lender, lendee, amount):
    # no need to return anything but "doing" sth!
    lender["monies"] -= amount
    lendee["monies"] += amount


def all_favourite_foods(people):
    favourite_foods = []
    # Why I have to use extend not append? - because snack is a string not a list
    # for food in people["favourites"]["snacks"]:
    #     favourite_foods.extend(food)
    for person in people:
        for snack in person["favourites"]["snacks"]:
            favourite_foods.append(snack)
    # Q7 - why I have to return this value?
    return favourite_foods


def find_no_friends(people):
    no_mates = []
    # Q8 -I did this and I got error:list indices must be integers or slices, not str
    # friends = people["friends"]
    # people_has_no_friends = people["name"]
    # for friend in friends:
    #     if friend == False:
    #         no_mate.append(people_has_no_friends)

    for person in people:
        # Q9 - Why not - if len(people["friends"]) == 0:
        # A: people is a list; person is a dic within the list; check the Q self.people
        if len(person["friends"]) == 0:
            no_mates.append(person)
            # is "person" the item a string and people a list?

    return no_mates


def unique_favourite_tv_shows(people):
    # solution 1: use "not in"
    # def unique_favourite_tv_shows(people):
    #     unique_tv_shows = []
    #     for person in people:
    #         if person["favourites"]["tv_show"] not in unique_tv_shows:
    #             unique_tv_shows.append(person["favourites"]["tv_show"])
    #     return unique_tv_shows

    all_tv_shows = []
    # Q10- why my code won't get the result?
    # for person in people:
    #     for each_tv in person["favourites"]["tv_show"]:
    #         # set(favourite_TV.append(each_tv))
    #         all_tv_shows.append(each_tv)
    # return list(set(all_tv_shows))
    # Q11 - see solu 2 "all_favourite_foods"; why different? Why here use extend not append?
    #  I cannot pass the test!
    for person in people:
        all_tv_shows.extend(person["favourites"]["tv_show"])

    return set(all_tv_shows)
