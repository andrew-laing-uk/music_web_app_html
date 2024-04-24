import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)


@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    albums = album_repository.all()
    return render_template('music/albums.html', albums=albums)

# GET /books/<id>
# Returns a single book
@app.route('/albums/<int:id>', methods=['GET'])
def get_single_album(id):
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)
    album = album_repository.find(id)
    artist = artist_repository.find(album.artist_id)
    print(f"The name of the artist is {artist.name}")
    return render_template('music/show_album.html', artist=artist, album=album)


@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artists = artist_repository.all()
    return render_template('music/artists.html', artists=artists)


# GET /artists/<id>
# Returns a single book
@app.route('/artists/<int:id>', methods=['GET'])
def get_single_artist(id):
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artist = artist_repository.find(id)
    return render_template('music/show_artist.html', artist=artist)


# GET /artists/new
# Returns a form to create a new artist
@app.route('/artists/new', methods=['GET'])
def get_new_artist():
    return render_template('music/new_artist.html')


# POST /artists
# Creates a new artist
@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)

    # Get the fields from the request form
    name = request.form['name']
    genre = request.form['genre']

    artist = Artist(None, name, genre)

    if not artist.is_valid():
        return render_template('artists/new_artist.html', artist=artist, errors=artist.generate_errors()), 400

    # Save the artist to the database
    artist = artist_repository.create(artist)

    return redirect(f"/artists/{artist.id}")


# GET /albums/new
# Returns a form to create a new album
@app.route('/albums/new', methods=['GET'])
def get_new_book():
    return render_template('music/new_album.html')


# POST /albums
# Creates a new album
@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)

    # Get the fields from the request form
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']

    album = Album(None, title, release_year, artist_id)

    if not album.is_valid():
        return render_template('albums/new_album.html', album=album, errors=album.generate_errors()), 400

    # Save the artist to the database
    album = album_repository.create(album)

    return redirect(f"/albums/{album.id}")



if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
