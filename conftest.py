import pytest
from playwright.sync_api import Playwright, APIRequestContext
from playwright.sync_api import Page

from pages.page_objects.base_page import BasePage
from pages.page_objects.find_owner_page import FindOwnerPage
from pages.page_objects.new_owner_page import NewOwnerPage
from faker import Faker
import re


@pytest.fixture(scope='session')
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,

        'viewport': {
            'width': 1920,
            'height': 1080,
        },
    }

@pytest.fixture()
def base_page(page: Page):
    return BasePage(page)


@pytest.fixture()
def new_owner_page(page: Page):
    return NewOwnerPage(page)

@pytest.fixture()
def find_owner_page(page: Page):
    return FindOwnerPage(page)

@pytest.fixture(scope='session')
def api_context(playwright: Playwright, base_url: str) -> APIRequestContext:
    api_context = playwright.request.new_context(base_url=base_url)
    yield api_context
    api_context.dispose()

@pytest.fixture
def new_owner(api_context: APIRequestContext):
    fake = Faker('en_US')

    digit_only_phone_number = re.sub(r'\D', '', fake.phone_number())[:10]

    new_owner = {
        'firstName': fake.first_name(),
        'lastName': fake.last_name(),
        'address': fake.address(),
        'city': fake.city(),
        'telephone': digit_only_phone_number
    }

    api_context.post(
        '/owners/new',
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        form=new_owner
    )

    return new_owner
