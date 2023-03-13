class Room:
    def __init__(self, name, capcacity, entry_fee):
        self.name = name
        self.songs = []
        self.guest = []
        self.capacity = capcacity
        self.entry_fee = entry_fee

    def guests_count(self):
        return len(self.guest)

    def add_guest(self, guest):
        self.guest.append(guest)

    def remove_guest(self, guest):
        self.guest.remove(guest)

    def songs_count(self):
        return len(self.songs)

    def add_songs(self, song):
        if song not in self.songs:
            self.songs.append(song)

    def too_many_guests(self):
        return len(self.guest) > self.capacity

    # same as: if len(self.guest) > self.capacity return Ture

    def fav_song(self, song):
        if song in self.songs:
            return "Whoo!"
        else:
            return "Boooo!"
