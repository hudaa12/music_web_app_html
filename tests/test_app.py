from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    h2_tags = page.locator("h2")
    p_tags = page.locator("p")
    expect(h2_tags).to_have_text([
        "Doolittle",
        "Surfer Rosa",
    ])
    expect(p_tags).to_have_text([
        "Released: 1989",
        "Released: 1988"
    ])


def test_single_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa'")
    h1_tags = page.locator("h1")
    expect(h1_tags).to_have_text("Album: Doolittle")
    p_tags = page.locator("p")
    expect(p_tags).to_have_text("Released: 1989")
