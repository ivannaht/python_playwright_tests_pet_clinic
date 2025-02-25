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
        self.first_name_empty_error = page.locator('xpath=//*[@class="form-group has-error"][1]//span[2]')
        self.last_name_empty_error = page.locator('xpath=//*[@class="form-group has-error"][2]//span[2]')
        self.address_empty_error = page.locator('xpath=//*[@class="form-group has-error"][3]//span[2]')
        self.city_empty_error = page.locator('xpath=//*[@class="form-group has-error"][4]//span[2]')
        self.telephone_empty_error = page.locator('xpath=//*[@class="form-group has-error"][5]//span[2]')

    def load(self) -> None:
        self.page.goto(self.URL)

    def fill_owner_details(self, first_name: str, last_name: str, address: str, city: str, telephone: str) -> None:
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.address_input.fill(address)
        self.city_input.fill(city)
        self.telephone_input.fill(telephone)

    def submit_form(self) -> None:
        self.add_owner_button.click()

    def is_add_owner_button_enabled(self) -> bool:
        return self.add_owner_button.is_enabled()
