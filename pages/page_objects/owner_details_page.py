from playwright.sync_api import Page

from pages.page_objects.base_page import BasePage


class OwnerDetailsPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.owner_name = page.locator('table.table-striped >> text=Name').locator('..').locator('td')
        self.owner_address = page.locator('table.table-striped >> text=Address').locator('..').locator('td')
        self.owner_city = page.locator('table.table-striped >> text=City').locator('..').locator('td')
        self.owner_telephone = page.locator('table.table-striped >> text=Telephone').locator('..').locator('td')
        self.edit_owner_button = page.locator('a.btn.btn-primary', has_text='Edit Owner')
        self.add_new_pet_button = page.locator('a.btn.btn-primary', has_text='Add New Pet')
