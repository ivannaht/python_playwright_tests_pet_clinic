from playwright.sync_api import Page


class BasePage:
    URL = "https://spring-petclinic-clone-2024.azurewebsites.net/"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.find_owners_link = page.get_by_role("link", name="Find owners")
        self.success_message = page.locator("#success-message")

    def load(self) -> None:
        self.page.goto(self.URL)

    def find_owners(self) -> None:
        self.find_owners_link.click()
