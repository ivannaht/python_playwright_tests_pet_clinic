import pytest
from playwright.sync_api import expect
from pages.page_objects.find_owner_page import FindOwnerPage



@pytest.fixture(scope="function")
def load_page(find_owner_page: FindOwnerPage):
    find_owner_page.load()


def test_find_owner_ui(find_owner_page: FindOwnerPage, load_page, new_owner):
    find_owner_page.search_owner_by_last_name(new_owner['lastName'])
    search_results = find_owner_page.get_search_results()

    expect(search_results).to_contain_text(new_owner['lastName'])
    expect(search_results).to_contain_text(new_owner['firstName'])
    expect(search_results).to_contain_text(new_owner['address'])
    expect(search_results).to_contain_text(new_owner['city'])
    expect(search_results).to_contain_text(new_owner['telephone'])


def test_owner_details_ui(find_owner_page: FindOwnerPage, load_page, new_owner):
    find_owner_page.search_owner_by_last_name(new_owner['lastName'])
    search_results = find_owner_page.get_search_results()
    search_results.first().click()
    owner_details = find_owner_page.get_owner_details()

    assert owner_details['firstName'] == new_owner['firstName']
    assert owner_details['lastName'] == new_owner['lastName']
    assert owner_details['address'] == new_owner['address']
    assert owner_details['city'] == new_owner['city']
    assert owner_details['telephone'] == new_owner['telephone']
