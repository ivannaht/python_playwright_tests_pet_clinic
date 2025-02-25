import pytest
from playwright.sync_api import expect
from pages.page_objects.base_page import BasePage

@pytest.fixture(scope="function")
def load_base_page(base_page: BasePage):
    base_page.load()

def test_navbar_home_link(base_page: BasePage, load_base_page) -> None:
    base_page.go_to_home()
    expect(base_page.page).to_have_url(base_page.URL)

def test_navbar_find_owners_link(base_page: BasePage, load_base_page) -> None:
    base_page.find_owners()
    expect(base_page.page).to_have_url(base_page.URL + "owners/find")

def test_navbar_veterinarians_link(base_page: BasePage, load_base_page) -> None:
    base_page.go_to_veterinarians()
    expect(base_page.page).to_have_url(base_page.URL + "vets.html")

def test_navbar_links_visible(base_page: BasePage, load_base_page) -> None:
    expect(base_page.home_link).to_be_visible()
    expect(base_page.find_owners_link).to_be_visible()
    expect(base_page.veterinarians_link).to_be_visible()
