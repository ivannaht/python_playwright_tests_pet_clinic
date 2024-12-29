import pytest
from playwright.sync_api import expect

from pages.page_objects.new_owner_page import NewOwnerPage

from faker import Faker


@pytest.fixture(scope="function")
def owner_data():
    fake = Faker()

    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'address': fake.address(),
        'city': fake.city(),
        'phone_number': fake.phone_number()
    }


def test_add_owner(new_owner_page: NewOwnerPage, owner_data) -> None:
    new_owner_page.load()
    new_owner_page.first_name_input.fill(owner_data['first_name'])
    new_owner_page.last_name_input.fill(owner_data['last_name'])
    new_owner_page.address_input.fill(owner_data['address'])
    new_owner_page.city_input.fill(owner_data['city'])
    new_owner_page.telephone_input.fill(owner_data['phone_number'])
    new_owner_page.add_owner_button.click()

    expect(new_owner_page.success_message).to_be_visible()
    expect(new_owner_page.success_message).to_have_text("New Owner Created")
