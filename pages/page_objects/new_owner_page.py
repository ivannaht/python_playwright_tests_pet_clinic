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
