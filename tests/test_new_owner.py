from playwright.sync_api import expect

from pages.page_objects.new_owner_page import NewOwnerPage


def test_add_owner(new_owner_page: NewOwnerPage) -> None:
    new_owner_page.load()
    new_owner_page.first_name_input.fill("Emma")
    new_owner_page.last_name_input.fill("Roman")
    new_owner_page.address_input.fill("123 Street")
    new_owner_page.city_input.fill("New York")
    new_owner_page.telephone_input.fill("1234567")
    new_owner_page.add_owner_button.click()

    expect(new_owner_page.success_message).to_be_visible()
    expect(new_owner_page.success_message).to_have_text('New Owner Created')
