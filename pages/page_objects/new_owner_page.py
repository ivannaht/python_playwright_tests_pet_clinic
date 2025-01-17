from playwright.sync_api import Page

from pages.page_objects.base_page import BasePage


class NewOwnerPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.URL = super().URL + "owners/new"
        self.first_name_input = page.locator("#firstName")
        self.last_name_input = page.locator("#lastName")
        self.address_input = page.locator("#address")
        self.city_input = page.locator("#city")
        self.telephone_input = page.locator("#telephone")
        self.add_owner_button = page.get_by_role("button", name="Add Owner")
