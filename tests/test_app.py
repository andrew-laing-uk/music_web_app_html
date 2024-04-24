from playwright.sync_api import Page, expect


"""
We can get album details from the /albums page using the album id. 
E.g., /albums/1
"""
def test_get_single_album_details(db_connection, page, test_web_address): 
    db_connection.seed("seeds/music_library_1.sql")
    page.goto(f"http://{test_web_address}/albums/1")

    # We look at the <h1> tag
    h1_tag = page.locator("h1")

    # We assert that it has the text "Doolittle"
    expect(h1_tag).to_have_text("Doolittle")


def test_click_album_link_on_albums_page(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library_1.sql")

    page.goto(f"http://{test_web_address}/albums")

    # Click the link with the text 'Doolittle'
    page.click("text=Doolittle")

    # We assert that it has the text "Doolittle"
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Doolittle")

"""
We can get artist details from the /artist page using the artist id. 
E.g., /artists/1
"""
def test_get_single_artist_details(db_connection, page, test_web_address): 
    db_connection.seed("seeds/music_library_1.sql")
    page.goto(f"http://{test_web_address}/artists/1")

    # We look at the <h1> tag
    h1_tag = page.locator("h1")

    # We assert that it has the text "Doolittle"
    expect(h1_tag).to_have_text("Pixies")

"""
We can click on a link on the artists page, and open
a page of info on that artist.
"""
def test_click_artist_link_on_artists_page(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library_1.sql")

    page.goto(f"http://{test_web_address}/artists")

    # Click the link with the text 'Pixies'
    page.click("text=Pixies")

    # We assert that it has the text "Pixies"
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Pixies")

"""
When we create a new artist
We see it in the artists index
"""
def test_create_artist(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library_1.sql")
    page.goto(f"http://{test_web_address}/artists")

    page.click("text=Add a new artist")

    # Then we fill out the fields
    page.fill("input[name='name']", "Altan")
    page.fill("input[name='genre']", "Irish Traditional")

    page.click("text=Create Artist")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Altan")

    genre_element = page.locator(".t-artist-genre")
    expect(genre_element).to_have_text("Genre: Irish Traditional")

"""
When we create a new album
We see it in the albums index
"""
def test_create_album(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library_1.sql")
    page.goto(f"http://{test_web_address}/albums")

    page.click("text=Add a new album")

    # Then we fill out the fields
    page.fill("input[name='title']", "Greatest Hits")
    page.fill("input[name='release_year']", "2001")
    page.fill("input[name='artist_id']", "1")

    page.click("text=Create Album")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Greatest Hits")
