import pytest
from pages.profile_page import ProfilePage
from pages.data import ProfilePageData
import time


@pytest.mark.smoke
def test_edit_pet(browser, go_to_login):
    link = ProfilePageData.PROFILE_PAGE_LINK
    page = ProfilePage(browser, link)
    page.open()
    time.sleep(2)
    page.edit_pet()
    time.sleep(2)
    page.go_to_name_clear()
    time.sleep(2)
    page.go_to_save_btn()
    time.sleep(2)

    browser.save_screenshot('result_edit_pet.png')


@pytest.mark.regression
def test_add_pet(browser, go_to_login):
    link = ProfilePageData.PROFILE_PAGE_LINK
    page = ProfilePage(browser, link)
    page.open()
    time.sleep(2)
    page.add_pet()
    time.sleep(2)
    page.go_to_name()
    time.sleep(2)

    browser.save_screenshot('result_add_pet.png')


@pytest.mark.regression
def test_add_pet_and_cancel(browser, go_to_login):
    link = ProfilePageData.PROFILE_PAGE_LINK
    page = ProfilePage(browser, link)
    page.open()
    time.sleep(2)
    page.add_pet()
    time.sleep(2)
    page.go_to_cancel()
    time.sleep(2)

    browser.save_screenshot('result_add_pet_cancel.png')


@pytest.mark.smoke
def test_delete_pet(browser, go_to_login):
    link = ProfilePageData.PROFILE_PAGE_LINK
    page = ProfilePage(browser, link)
    page.open()
    time.sleep(2)
    page.delete_pet()
    time.sleep(2)

    browser.save_screenshot('result_delete_pet.png')


@pytest.mark.regression
def test_go_to_quit_after_login(browser, go_to_login):
    link = ProfilePageData.PROFILE_PAGE_LINK
    page = ProfilePage(browser, link)
    page.open()
    time.sleep(2)
    page.go_to_quit()
    time.sleep(2)

    browser.save_screenshot('result_quit.png')
