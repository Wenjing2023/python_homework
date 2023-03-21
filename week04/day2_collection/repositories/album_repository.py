from db.run_sql import run_sql

from models.albums import Album
import repositories.artist_repository as artist_repository


# create album - save()
def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    album.id = id
    return album

# select_all()
def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row["artist_id"])
    # Q: here ["artist_id"] belongs to the table not the class?
        album = Album(row["title"], row["genre"], artist, row["id"])
        albums.append(album)
    return albums

# delete_all()
def delete_all():
    sql = "DELETE * from albums"
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
    #  line 42 ["artist_id"] is database element and line 44 is Album class element? 
        album = Album(
            selected_album["title"],
            selected_album["genre"],
            artist,
            selected_album["id"]
        )
    return album


