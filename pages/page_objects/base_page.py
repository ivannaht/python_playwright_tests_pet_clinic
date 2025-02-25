from playwright.sync_api import Page, expect


class BasePage:
    URL = "https://spring-petclinic-clone-2024.azurewebsites.net/"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.find_owners_link = page.get_by_role("link", name="Find owners")
        self.home_link = page.get_by_role("link", name="Home")
        self.veterinarians_link = page.get_by_role("link", name="Veterinarians")
        self.error_message = page.locator(".error")
        self.success_message = page.locator("#success-message")

    def load(self) -> None:
        self.page.goto(self.URL)

    def find_owners(self) -> None:
        self.find_owners_link.click()

    def go_to_home(self) -> None:
        self.home_link.click()

    def go_to_veterinarians(self) -> None:
        self.veterinarians_link.click()

    def get_error_message(self) -> str:
        return self.error_message.text_content()

    def get_success_message(self) -> str:
        return self.success_message.text_content()

    def wait_for_element(self, locator: str) -> None:
        self.page.wait_for_selector(locator)

    def is_element_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()

    def is_element_enabled(self, locator: str) -> bool:
        return self.page.locator(locator).is_enabled()

    def assert_text(self, locator: str, expected_text: str) -> None:
        element = self.page.locator(locator)
        expect(element).to_have_text(expected_text)
