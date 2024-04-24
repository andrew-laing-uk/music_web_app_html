from lib.album import Album

"""
Album constructs with an id, title, release_year and artist_id
"""
def test_albums_construct():
    album = Album(1, "Test Title", 2024, 4)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 2024
    assert album.artist_id == 4

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Test Title", 2024, 4)
    assert str(album) == "Album(1, Test Title, 2024, 4)"


"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album_1 = Album(1, "Test Title", 2024, 4)
    album_2 = Album(1, "Test Title", 2024, 4)
    assert album_1 == album_2


def test_artist_validity():
    assert Album(1, "", "", "").is_valid() == False
    assert Album(1, "Album", "", "").is_valid() == False
    assert Album(1, "", "Genre", "").is_valid() == False
    assert Album(1, "Album", None, "").is_valid() == False
    assert Album(1, None, "Genre", "").is_valid() == False
    assert Album(1, "Album", "Genre", 1).is_valid() == True
    assert Album(None, "Album", "Genre", 1).is_valid() == True

"""
We can generate errors for an invalid album
"""
def test_album_errors():
    assert Album(1, "", "", "").generate_errors() == "Title can't be blank, Release Year can't be blank, Artist ID can't be blank"
    assert Album(1, "Album", "", 1).generate_errors() == "Release Year can't be blank"
    assert Album(1, "", "Genre", 1).generate_errors() == "Title can't be blank"
    assert Album(1, "Album", "Genre", None).generate_errors() == "Artist ID can't be blank"
    assert Album(1, "Album", None, 1).generate_errors() == "Release Year can't be blank"
    assert Album(1, "Album", "Genre", 1).generate_errors() == None
    assert Album(None, "Album", "Genre", 1).generate_errors() == None