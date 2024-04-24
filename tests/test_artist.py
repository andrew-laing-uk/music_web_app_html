from lib.artist import Artist

"""
Artist constructs with an id, name and genre
"""
def test_artist_constructs():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert artist.id == 1
    assert artist.name == "Test Artist"
    assert artist.genre == "Test Genre"

"""
We can format artists to strings nicely
"""
def test_artists_format_nicely():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert str(artist) == "Artist(1, Test Artist, Test Genre)"

"""
We can compare two identical artists
And have them be equal
"""
def test_artists_are_equal():
    artist1 = Artist(1, "Test Artist", "Test Genre")
    artist2 = Artist(1, "Test Artist", "Test Genre")
    assert artist1 == artist2

"""
We can assess an artist for validity
"""
def test_artist_validity():
    assert Artist(1, "", "").is_valid() == False
    assert Artist(1, "Artist", "").is_valid() == False
    assert Artist(1, "", "Genre").is_valid() == False
    assert Artist(1, "Artist", None).is_valid() == False
    assert Artist(1, None, "Genre").is_valid() == False
    assert Artist(1, "Artist", "Genre").is_valid() == True
    assert Artist(None, "Artist", "Genre").is_valid() == True

"""
We can generate errors for an invalid artist
"""
def test_Artist_errors():
    assert Artist(1, "", "").generate_errors() == "Name can't be blank, Genre name can't be blank"
    assert Artist(1, "Artist", "").generate_errors() == "Genre name can't be blank"
    assert Artist(1, "", "Genre").generate_errors() == "Name can't be blank"
    assert Artist(1, "Artist", None).generate_errors() == "Genre name can't be blank"
    assert Artist(1, None, "Genre").generate_errors() == "Name can't be blank"
    assert Artist(1, "Artist", "Genre").generate_errors() == None
    assert Artist(None, "Artist", "Genre").generate_errors() == None
