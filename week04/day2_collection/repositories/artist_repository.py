from db.run_sql import run_sql

from models.artists import Artist
from models.albums import Album

# create artist - save()
def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    artist.id = id
    return artist

# select_all()
def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row["name"], row["id"])
        artists.append(artist)
    return artists

# delete_all()
def delete_all():
    sql ="DELETE * FROM artist"
    run_sql(sql)


# find_artist_by_id -  select(id)
def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        artist = Artist(result["name"], result["id"])
        # Q -  instead of  result["id"] can we use id?
    return artist     

