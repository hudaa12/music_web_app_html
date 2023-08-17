import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route("/albums")
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums.html", albums=albums)

@app.route("/albums_id")
def get_single_albums(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)
    album = repository.find(id)
    artist = artist_repository.find(album.artist_id)
    return render_template("single_albums.html", album=album, artist=artist)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
