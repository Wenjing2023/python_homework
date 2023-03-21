class Album:
    def __init__(self,title, genre, artist, id=None,):
        self.title = title
        self.genre = genre
        self.artist = artist
        self.id = id

 # in db albums there is a artist_id cause by clicking the id we can see artist object(id, name); 
 # here in the class is artist name not id