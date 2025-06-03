import os
import sys
import pytest
import time

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from pages.forget_password_page import ForgetPage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from utilities.appium_driver import get_driver
from utilities.otp_utils import fetch_otp  
@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    
    yield driver
    driver.quit()

def test_forget_password_flow(driver):

    login_page = ForgetPage(driver)
    login_page2=  LoginPage(driver)
    registration =RegistrationPage(driver)

    time.sleep(5)

    login_page.allow_permission_popup()
    login_page.skip_onbarding_page()
    login_page.go_to_login_screen()
    login_page.click_forget_password()
    login_page.click_phone_forget()
    phone_number = "01116590586"
    login_page.enter_phone_forget(phone_number)
    login_page.hide_keyboard_if_visible()
    login_page.submit_phone_forget()
    time.sleep(5)
    # registration.click_otp_confirmation()
    otp = fetch_otp(phone_number)
    assert otp is not None, "Failed to fetch OTP via API."
    registration.allow_permission_popup 
    # tap on screen at x=149, y=1101 with 1 tap
    driver.tap([(149, 1101)])
    time.sleep(2)
    driver.execute_script("mobile: type", {"text": otp})
    login_page.click_new_password()
    login_page.enter_new_password("123e321")
    # login_page.hide_keyboard_if_visible()
    login_page.click_confirm_password()
    login_page.enter_confirm_password("123e321")
    # login_page.hide_keyboard_if_visible()
    login_page.submit_reset_password()
    login_page2.click_phone_login()
    login_page2.enter_phone("01116590586")
    login_page2.click_password_login()
    login_page2.enter_password("123e321")
    login_page.hide_keyboard_if_visible()
    login_page2.submit_login()
    login_page.allow_permission_popup_location()
    login_page2.skip_user_tutorial()
    

    assert login_page.is_login_successful(), "Login failed: Account button not found."


