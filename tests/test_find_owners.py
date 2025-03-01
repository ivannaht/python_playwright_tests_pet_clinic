import pytest

from pages.page_objects.find_owner_page import FindOwnerPage

@pytest.fixture(scope="function")
def owner():
    return {
        'firstName': 'Emma',
        'lastName': 'Catalog',
        'address': '123 Test Street',
        'city': 'New City',
        'phoneNumber': '1234567'
    }

@pytest.fixture(scope="function")
def load_find_owner_page(find_owner_page: FindOwnerPage):
    find_owner_page.load()


def test_find_owner_ui(find_owner_page: FindOwnerPage, load_find_owner_page, owner):
    find_owner_page.search_owner_by_last_name(owner['lastName'])

    assert find_owner_page.page.url.endswith('/12'), "Clicking should navigate to the owner details page"
