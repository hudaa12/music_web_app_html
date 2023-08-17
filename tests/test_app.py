from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        "Title: 1989\nReleased: 2014",
        "Title: Voyage\nReleased: 2022"
    ])


def test_single_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    h1_tags = page.locator("h1")
    p_tags = page.locator("p")
    expect(p_tags).to_have_text("Release year: 2014\nArtist: Pixies")
    expect(h1_tags).to_have_text("1989")