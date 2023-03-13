class Venue:
    def __init__(self, name, till):
        self.name = name
        self.room = []
        self.till = till
        self.guest = []

    def guests_count(self):
        return len(self.guest)

    def guest_can_afford_to_enter(self, guest, room):
        return guest.sufficient_funds_to_enter(room)

    def check_in_guest(self, guest, room):
        if self.guest_can_afford_to_enter(guest, room):
            self.guest.append(guest)
            self.till += room.entry_fee
            # self.increase_till_check_in(room)

    # Also need to check the room capacity

    def check_out_guest(self, guest):
        self.guest.remove(guest)

    # def increase_till_check_in(self, room):
    #     self.till += len(self.guest) * room.entry_fee
    #     # return checked_in_till

    def increase_till_bar_service(self, room, food):
        self.increase_till_check_in(room)
