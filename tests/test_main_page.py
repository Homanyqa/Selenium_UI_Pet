import time
import pytest
from pages.main_page import MainPage
from pages.data import MainPageData


@pytest.mark.regression
def test_go_to_login_page(browser):
    link = MainPageData.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    time.sleep(2)
    page.open()
    time.sleep(2)
    page.go_to_login_page()
    browser.save_screenshot('result_go_to_login.png')


@pytest.mark.smoke
def test_filter_type(browser):
    link = MainPageData.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.firter_by_type()
    page.choose_hamster_type()
    time.sleep(1)
    browser.save_screenshot('result_choose_type.png')


@pytest.mark.smoke
def test_filter_name(browser):
    link = MainPageData.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.firter_by_name()
    time.sleep(1)
    browser.save_screenshot('result_choose_name.png')


@pytest.mark.regression
def test_view_details(browser):
    link = MainPageData.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.view_details()
    time.sleep(1)
    browser.save_screenshot('result_details.png')


@pytest.mark.regression
def test_view_picture(browser):
    link = MainPageData.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.view_details()
    page.view_picture()
    time.sleep(1)
    browser.save_screenshot('result_picture.png')


@pytest.mark.smoke
def test_pet_has_name(browser):
    link = MainPageData.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.view_details()
    pet_name = page.pet_has_name()

    assert pet_name.text != ''
