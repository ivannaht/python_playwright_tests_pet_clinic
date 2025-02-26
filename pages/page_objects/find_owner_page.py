from playwright.sync_api import Page

from pages.page_objects.base_page import BasePage


class FindOwnerPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.URL = super().URL + "owners/find"

    def load(self):
        self.page.goto(self.URL)

    def search_owner_by_last_name(self, last_name: str):
        search_input = self.page.locator('input[name="lastName"]')
        search_input.fill(last_name)
        self.page.locator('button[type="submit"]').click()

    def get_search_results(self):
        return self.page.locator('table.table tbody tr')

    def get_owner_details(self):
        details = {}
        details['firstName'] = self.page.locator('tr:has-text("First Name") td').inner_text()
        details['lastName'] = self.page.locator('tr:has-text("Last Name") td').inner_text()
        details['address'] = self.page.locator('tr:has-text("Address") td').inner_text()
        details['city'] = self.page.locator('tr:has-text("City") td').inner_text()
        details['telephone'] = self.page.locator('tr:has-text("Telephone") td').inner_text()
        return details
