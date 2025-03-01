import pytest
from playwright.sync_api import Playwright, APIRequestContext
from pages.page_objects.base_page import BasePage
import re
from faker import Faker


@pytest.fixture(scope='session')
def base_url() -> str:
    return BasePage.URL


@pytest.fixture(scope="session")
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


@pytest.fixture(scope='session')
def api_context(playwright: Playwright, base_url: str) -> APIRequestContext:
    api_context = playwright.request.new_context(base_url=base_url)
    yield api_context
    api_context.dispose()


@pytest.fixture(scope='session')
def new_owner(api_context: APIRequestContext, valid_owner_data):
    api_context.post(
        '/owners/new',
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        form=valid_owner_data
    )

    return valid_owner_data
