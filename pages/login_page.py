from .base_page import BasePage
from .locators import LoginPageLocators
from pages.data import LoginPageData


class LoginPage(BasePage):
    def go_to_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(*LoginPageData.EMAIL_DATA)

    def go_to_pass(self):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS).send_keys(*LoginPageData.PASSWORD_DATA)

    def go_to_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).submit()

