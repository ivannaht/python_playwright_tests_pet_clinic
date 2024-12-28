import pytest
from playwright.sync_api import Page

from pages.page_objects.base_page import BasePage
from pages.page_objects.new_owner_page import NewOwnerPage


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
