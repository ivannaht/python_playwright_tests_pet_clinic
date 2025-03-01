import pytest
from playwright.sync_api import expect
from pages.page_objects.find_owner_page import FindOwnerPage
from steps.api_steps import new_owner


@pytest.fixture(scope="function")
def load_find_owner_page(find_owner_page: FindOwnerPage):
    find_owner_page.load()


def test_find_owner_ui(find_owner_page: FindOwnerPage, load_find_owner_page, new_owner):
    find_owner_page.search_owner_by_last_name(new_owner['lastName'])

    assert find_owner_page.page.url.endswith('/12'), "Clicking should navigate to the owner details page"
