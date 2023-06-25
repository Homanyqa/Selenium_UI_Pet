from .base_page import BasePage
from .locators import ProfilePageLocators


class ProfilePage(BasePage):
    def go_to_quit(self):
        to_quit = self.browser.find_element(*ProfilePageLocators.PROFILE_QUIT).click()

    def edit_pet(self):
        edit = self.browser.find_element(*ProfilePageLocators.EDIT_PET).click()

    def go_to_name(self):
        input_name = self.browser.find_element(*ProfilePageLocators.INPUT_NAME).send_keys('kitty')

    def go_to_name_clear(self):
        clear_name = self.browser.find_element(*ProfilePageLocators.INPUT_NAME).clear()

    def go_to_save_btn(self):
        save_button = self.browser.find_element(*ProfilePageLocators.SAVE_BUTTON).click()

    def add_pet(self):
        add_btn = self.browser.find_element(*ProfilePageLocators.ADD_PET).click()

    def go_to_cancel(self):
        cancel_btn = self.browser.find_element(*ProfilePageLocators.CANCEL_BUTTON).click()

    def delete_pet(self):
        delete_btn = self.browser.find_element(*ProfilePageLocators.DELETE_PET).click()
