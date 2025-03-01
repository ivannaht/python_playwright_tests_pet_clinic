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

    def get_owner_name(self) -> str:
        return self.owner_name.text_content()

    def get_owner_address(self) -> str:
        return self.owner_address.text_content()

    def get_owner_city(self) -> str:
        return self.owner_city.text_content()

    def get_owner_telephone(self) -> str:
        return self.owner_telephone.text_content()

    def click_edit_owner(self) -> None:
        self.edit_owner_button.click()

    def click_add_new_pet(self) -> None:
        self.add_new_pet_button.click()
