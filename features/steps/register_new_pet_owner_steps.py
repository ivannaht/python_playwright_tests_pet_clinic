import pytest
from behave import given, when, then
from faker import Faker
from playwright.sync_api import sync_playwright, expect
from pytest_playwright.pytest_playwright import page

from pages.page_objects.base_page import BasePage
from pages.page_objects.find_owner_page import FindOwnerPage
from pages.page_objects.new_owner_page import NewOwnerPage
import re


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


@given('I am on the pet clinic home page')
def load_base_page(base_page: BasePage):
    base_page.load()


@when('I navigate to the Find Owners page')
def navigate_find_owners_page(base_page: BasePage, page) -> FindOwnerPage:
    base_page.find_owners()
    return FindOwnerPage(page)


@when('I navigate to the Add Owner page')
def navigate_add_owner_page(find_owner_page: FindOwnerPage, page) -> NewOwnerPage:
    find_owner_page.click_add_owner()
    return NewOwnerPage(page)


@when('I enter owner valid data')
def add_owner_valid(new_owner_page: NewOwnerPage, valid_owner_data) -> None:
    new_owner_page.fill_owner_details(
        valid_owner_data['first_name'],
        valid_owner_data['last_name'],
        valid_owner_data['address'],
        valid_owner_data['city'],
        valid_owner_data['phone_number']
    )
    new_owner_page.submit_form()


@then('I see the owner is registered successfully')
def verify_success_registration(new_owner_page: NewOwnerPage):
    expect(new_owner_page.success_message).to_be_visible()
    expect(new_owner_page.success_message).to_have_text("New Owner Created")
