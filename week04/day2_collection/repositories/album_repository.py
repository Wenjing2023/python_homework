from db.run_sql import run_sql

from models.albums import Album
import repositories.artist_repository as artist_repository


# create album - save()
def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
#  Here is to create an object, must have all elements but not id as db will assign it an id
    values = [album.title, album.genre, album.artist.id]
# Q1 - why not album.artist_id since we are giving it an artist_id into db; 
# Q2 - I assume here has nothing to do with Album class? album.genre - are these values of the table dic value? 3 %s, 3 values

    results = run_sql(sql, values)
    id = results[0]["id"]
    # getting the assigned id, result is a list, checking the 1st item's (in this case the only item) id 
    album.id = id
    return album
# Q3- album is an object, so we know it's title, genre and artist_id but didn't know its id first; when we get id we return the whole info

# select_all()
def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row["artist_id"])
# Q3 - still why we use artist_repository.select() while we could just use row["artist_id"]?
        album = Album(row["title"], row["genre"], artist, row["id"])
        albums.append(album)
    return albums

# delete_all()
def delete_all():
    sql = "DELETE * FROM albums"
    run_sql(sql)


# find_album_by_id -  select(id)
def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        selected_album = results[0]
        artist = artist_repository.select(selected_album["artist_id"])
        album = Album(
            selected_album["title"],
            selected_album["genre"],
            artist,
            selected_album["id"]
        )
    return album

# list all the albums by an artist
def album_for_artist(artist):
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)
    album_artist = []
    for row in results:
        album = Album(row["title"], row["genre"],artist, row["id"])
        album_artist.append(album)
    return album_artist

# edit album
def update(album):
    sql = "UPDATE albums SET (title, genre, artist_id) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.genre, album.artist_id]
    run_sql(sql, values)
# Q4 - so here we do not need to call album.artist.id? Does this have anything to do with artist_repository
# if we only update genre, do we need to get all values or just the genre one

# delete album
def delete(album):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)