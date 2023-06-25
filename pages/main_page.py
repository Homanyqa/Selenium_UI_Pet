from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()

    def firter_by_type(self):
        filter_type_link = self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE).click()

    def choose_hamster_type(self):
        pet_type = self.browser.find_element(*MainPageLocators.HAMSTER_TYPE).click()

    # Дописать, добавить enter
    def firter_by_name(self):
        filter_name_link = self.browser.find_element(*MainPageLocators.FILTER_BY_NAME).send_keys('hommy')

    def view_details(self):
        details = self.browser.find_element(*MainPageLocators.DETAILS).click()

    def view_picture(self):
        picture = self.browser.find_element(*MainPageLocators.PICTURE).click()

    def pet_has_name(self):
        pet_name = self.browser.find_element(*MainPageLocators.PET_NAME)
        return pet_name
