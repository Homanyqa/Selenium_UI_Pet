import pytest
from pages.login_page import LoginPage
from pages.data import LoginPageData


@pytest.mark.smoke
def test_go_to_login(browser):
    link = LoginPageData.LOGIN_PAGE_LINK
    page = LoginPage(browser, link)
    page.open()
    page.go_to_email()
    page.go_to_pass()
    page.go_to_button()
    browser.save_screenshot('result_login.png')
