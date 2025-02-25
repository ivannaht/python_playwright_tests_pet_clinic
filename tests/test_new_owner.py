import pytest

from playwright.sync_api import expect

from pages.page_objects.new_owner_page import NewOwnerPage

import re
from faker import Faker


@pytest.fixture(scope="function")
def load_page(new_owner_page: NewOwnerPage):
    new_owner_page.load()


@pytest.fixture(scope="function")
def valid_owner_data():
    fake = Faker('en_US')

    digit_only_phone_number = re.sub(r'\D', '', fake.phone_number())[:10]

    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'address': fake.address(),
        'city': fake.city(),
        'phone_number': digit_only_phone_number
    }


@pytest.fixture(scope="function")
def invalid_empty_owner_data():
    return {
        'first_name': ' ',
        'last_name': ' ',
        'address': ' ',
        'city': ' ',
        'phone_number': ' '
    }


def test_add_owner_positive(new_owner_page: NewOwnerPage, load_page, valid_owner_data) -> None:
    new_owner_page.fill_owner_details(
        valid_owner_data['first_name'],
        valid_owner_data['last_name'],
        valid_owner_data['address'],
        valid_owner_data['city'],
        valid_owner_data['phone_number']
    )
    new_owner_page.submit_form()

    expect(new_owner_page.success_message).to_be_visible()
    expect(new_owner_page.success_message).to_have_text("New Owner Created")

def test_add_owner_negative(new_owner_page: NewOwnerPage, load_page, invalid_empty_owner_data) -> None:
    new_owner_page.fill_owner_details(
        invalid_empty_owner_data['first_name'],
        invalid_empty_owner_data['last_name'],
        invalid_empty_owner_data['address'],
        invalid_empty_owner_data['city'],
        invalid_empty_owner_data['phone_number']
    )
    new_owner_page.submit_form()

    expect(new_owner_page.first_name_empty_error).to_have_text("must not be blank")
    expect(new_owner_page.last_name_empty_error).to_have_text("must not be blank")
    expect(new_owner_page.address_empty_error).to_have_text("must not be blank")
    expect(new_owner_page.city_empty_error).to_have_text("must not be blank")
    expect(new_owner_page.telephone_empty_error).to_contain_text("must not be blank")
