from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums.sql")
    page.goto(f"http://{test_web_address}/albums")
    div_tags = page.locator("div")
    expect(div_tags.to_have_text([
        "Title: Doolittle\nReleased: 1989",
        "Title: Surfer Rosa\nReleased: 1988"
    ]))