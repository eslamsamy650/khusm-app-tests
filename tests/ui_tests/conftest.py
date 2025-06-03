import pytest
from utilities.appium_driver import get_driver
from pages.login_page import LoginPage
import time

@pytest.fixture(scope="session")
def logged_in_driver():
    driver = get_driver()
    login_page = LoginPage(driver)

    time.sleep(5)  # wait for app load

    login_page.allow_permission_popup()
    login_page.skip_onbarding_page()
    login_page.go_to_login_screen()
    login_page.click_phone_login()
    login_page.enter_phone("01116590586")
    login_page.click_password_login()
    login_page.enter_password("123e321")
    login_page.submit_login()
    login_page.allow_permission_popup_location()

    yield driver
    driver.quit()
