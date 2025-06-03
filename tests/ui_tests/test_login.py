import os
import sys
import pytest
import time

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from pages.login_page import LoginPage
from utilities.appium_driver import get_driver

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_login_flow(driver):
    login_page = LoginPage(driver)

    

    login_page.allow_permission_popup()
    login_page.skip_onbarding_page()
    login_page.go_to_login_screen()
    login_page.click_phone_login()
    login_page.enter_phone("01116590586")
    login_page.click_password_login()
    login_page.enter_password("123e321")
    login_page.hide_keyboard_if_visible()
    login_page.submit_login()
    login_page.allow_permission_popup_location()
    login_page.skip_user_tutorial()
    assert login_page.is_login_successful(), "Login failed: Account button not found."

def test_invalid_phone_number(driver):
    login_page = LoginPage(driver)

    

    login_page.allow_permission_popup()
    login_page.skip_onbarding_page()
    login_page.go_to_login_screen()
    login_page.click_phone_login()
    login_page.enter_phone("01416590586")  # Invalid phone
    login_page.click_password_login()
    login_page.enter_password("123e321")  # Valid password
    login_page.hide_keyboard_if_visible()
    login_page.submit_login()

    assert  login_page.is_login_invalid_phone(), "Unexpected login success with invalid phone number."

def test_invalid_password(driver):
    login_page = LoginPage(driver)

    

    login_page.allow_permission_popup()
    login_page.skip_onbarding_page()
    login_page.go_to_login_screen()
    login_page.click_phone_login()
    login_page.enter_phone("01116590586")  # Valid phone
    login_page.click_password_login()
    login_page.enter_password("wrongpass")  # Invalid password
    login_page.hide_keyboard_if_visible()
    login_page.submit_login()

    assert  login_page.is_invalid_password(), "Unexpected login success with invalid password."

def test_empty_fields(driver):
    login_page = LoginPage(driver)

   

    login_page.allow_permission_popup()
    login_page.skip_onbarding_page()
    login_page.go_to_login_screen()
    login_page.click_phone_login()
    login_page.enter_phone("")  # Empty phone
    login_page.click_password_login()
    login_page.enter_password("")  # Empty password
    login_page.hide_keyboard_if_visible()
    login_page.submit_login()

    assert  login_page.is_empty_filed(), "Unexpected login success with empty credentials."
