from models.artists import Artist
from models.albums import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist1 = Artist("Pink")
artist_repository.save(artist1)

artist2 = Artist("Adele")
artist_repository.save(artist2)

album1 = Album("I'm not dead","pop", artist1)
album_repository.save(album1)

album2 = Album("21", "R&B", artist2)
album_repository.save(album2)

result = album_repository.select_all()
for album in result:
    print(f"{album.artist} is {album.artist.name}")

result1 = album_repository.select(1)
print(result1.title)

artist1_album = album_repository.album_for_artist(artist1)
for album in artist1_album:
    print(f"{album.artist.name}")



