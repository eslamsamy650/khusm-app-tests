import os
import sys
import pytest
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from pages.active_card_page import ActivePage
from utilities.appium_driver import get_driver

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

from utilities.otp_utils import fetch_otp  # ⬅️ import the new function
import random

def generate_egyptian_phone():
    prefixes = ["010", "011", "012", "015"]
    prefix = random.choice(prefixes)
    number = ''.join(random.choices('0123456789', k=8))  # 11 - 3 = 8 digits
    return prefix + number

@pytest.mark.order(1)
def test_successful_registration(driver):
    registration = ActivePage(driver)

    time.sleep(3)
    registration.allow_permission_popup()
    registration.skip_onbarding_page()
    registration.navigate_to_active_card_screen()
    registration.click_card_id()
    registration.enter_card("25001241")
    registration.hide_keyboard_if_visible()
    registration.click_name()
    registration.enter_name("Eslam")
    registration.hide_keyboard_if_visible()
    registration.click_last_name()
    registration.enter_last_name("Tester")
    registration.hide_keyboard_if_visible()
    registration.click_phone()
    phone_number = generate_egyptian_phone()
    registration.enter_phone(phone_number)
    registration.hide_keyboard_if_visible()
    registration.click_password()
    registration.enter_password("123e321")
    registration.hide_keyboard_if_visible()
    registration.click_confirm_password()
    registration.confirm_password("123e321")
    registration.hide_keyboard_if_visible()
    
    registration.submit_registration()

    time.sleep(5)
    otp = fetch_otp(phone_number)
    assert otp is not None, "Failed to fetch OTP via API."
    # registration.allow_permission_popup 
    # tap on screen at x=149, y=1101 with 1 tap
    driver.tap([(149, 1101)])
    time.sleep(2)
    driver.execute_script("mobile: type", {"text": otp})
    registration.allow_permission_popup_location()
    assert registration.is_registration_successful(), "Registration failed: Success message not found."






def test_invalid_otp_registration(driver):
    registration = ActivePage(driver)

    time.sleep(3)
    registration.allow_permission_popup()
    registration.skip_onbarding_page()
    registration.navigate_to_active_card_screen()
    registration.click_card_id()
    registration.enter_card("25001237")
    registration.hide_keyboard_if_visible()
    registration.click_name()
    registration.enter_name("Eslam")
    registration.hide_keyboard_if_visible()
    registration.click_last_name()
    registration.enter_last_name("Tester")
    registration.hide_keyboard_if_visible()
    registration.click_phone()
    phone_number = "01116599586"
    registration.enter_phone(phone_number)
    registration.hide_keyboard_if_visible()
    registration.click_password()
    registration.enter_password("123e321")
    registration.hide_keyboard_if_visible()
    registration.click_confirm_password()
    registration.confirm_password("123e321")
    registration.hide_keyboard_if_visible()
    
    registration.submit_registration()

    
    otp = fetch_otp(phone_number)
    assert otp is not None, "Failed to fetch OTP via API."
    driver.tap([(149, 1101)])
    time.sleep(2)
    driver.execute_script("mobile: type", {"text": 123456})
    # registration.click_otp_verify()
    assert registration.is_registration_invalid_otp(), "Registration failed: Success message not found."

def test_registration_with_existing_phone(driver):
    registration = ActivePage(driver)

    time.sleep(5)
    registration.allow_permission_popup()
    registration.skip_onbarding_page()
    registration.navigate_to_active_card_screen()
    registration.click_card_id()
    registration.enter_card("25001236")
    registration.hide_keyboard_if_visible()
    registration.click_name()
    registration.enter_name("Eslam")
    registration.hide_keyboard_if_visible()
    registration.click_last_name()
    registration.enter_last_name("Tester")
    registration.hide_keyboard_if_visible()
    registration.click_phone()
    registration.enter_phone("01116590586")
    registration.hide_keyboard_if_visible()
    registration.click_password()
    registration.enter_password("123e321")
    registration.hide_keyboard_if_visible()
    registration.click_confirm_password()
    registration.confirm_password("123e321")
    registration.hide_keyboard_if_visible()
    
    registration.submit_registration()
    

    assert  registration.is_registration_mobile_warning_exist(), "Registration succeeded with existing_phone."


def test_registration_with_(driver):
    registration = ActivePage(driver)

    time.sleep(5)
    registration.allow_permission_popup()
    registration.skip_onbarding_page()
    registration.navigate_to_active_card_screen()
    registration.click_card_id()
    registration.enter_card("25001236")
    registration.hide_keyboard_if_visible()
    registration.click_name()
    registration.enter_name("Eslam")
    registration.hide_keyboard_if_visible()
    registration.click_last_name()
    registration.enter_last_name("Tester")
    registration.hide_keyboard_if_visible()
    registration.click_phone()
    registration.enter_phone("01116590586")
    registration.hide_keyboard_if_visible()
    registration.click_password()
    registration.enter_password("123e321")
    registration.hide_keyboard_if_visible()
    registration.click_confirm_password()
    registration.confirm_password("123e321")
    registration.hide_keyboard_if_visible()
    
    registration.submit_registration()
    

    assert  registration.is_registration_mobile_warning_exist(), "Registration succeeded with existing_phone."


def test_registration_with_existing_card(driver):
    registration = ActivePage(driver)

    time.sleep(5)
    registration.allow_permission_popup()
    registration.skip_onbarding_page()
    registration.navigate_to_active_card_screen()
    registration.click_card_id()
    registration.enter_card("25001235")
    registration.hide_keyboard_if_visible()
    registration.click_name()
    registration.enter_name("Eslam")
    registration.hide_keyboard_if_visible()
    registration.click_last_name()
    registration.enter_last_name("Tester")
    registration.hide_keyboard_if_visible()
    registration.click_phone()
    registration.enter_phone("01116599586")
    registration.hide_keyboard_if_visible()
    registration.click_password()
    registration.enter_password("123e321")
    registration.hide_keyboard_if_visible()
    registration.click_confirm_password()
    registration.confirm_password("123e321")
    registration.hide_keyboard_if_visible()
    
    registration.submit_registration()
    

    assert  registration.is_registration_card_warning_exist(), "Registration succeeded with existing_phone."



def test_registration_with_invalid_card(driver):
    registration = ActivePage(driver)

    time.sleep(5)
    registration.allow_permission_popup()
    registration.skip_onbarding_page()
    registration.navigate_to_active_card_screen()
    registration.click_card_id()
    registration.enter_card("25005555")
    registration.hide_keyboard_if_visible()
    registration.click_name()
    registration.enter_name("Eslam")
    registration.hide_keyboard_if_visible()
    registration.click_last_name()
    registration.enter_last_name("Tester")
    registration.hide_keyboard_if_visible()
    registration.click_phone()
    registration.enter_phone("01116599586")
    registration.hide_keyboard_if_visible()
    registration.click_password()
    registration.enter_password("123e321")
    registration.hide_keyboard_if_visible()
    registration.click_confirm_password()
    registration.confirm_password("123e321")
    registration.hide_keyboard_if_visible()
    
    registration.submit_registration()
    

    assert  registration.is_registration_invalid_card_warning_exist(), "Registration succeeded with existing_phone."




def test_mismatched_passwords(driver):
    registration = ActivePage(driver)

    time.sleep(5)

    registration.allow_permission_popup()
    registration.skip_onbarding_page()
    registration.navigate_to_active_card_screen()
    registration.click_card_id()
    registration.enter_card("25001236")
    registration.hide_keyboard_if_visible()
    registration.click_name()
    registration.enter_name("Eslam")
    registration.hide_keyboard_if_visible()
    registration.click_last_name()
    registration.enter_last_name("Tester")
    registration.hide_keyboard_if_visible()
    registration.click_phone()
    registration.enter_phone("01116599580")
    registration.hide_keyboard_if_visible()
    registration.click_password()
    registration.enter_password("Test@123")
    registration.hide_keyboard_if_visible()
    registration.click_confirm_password()
    registration.confirm_password("Test@321")
    registration.hide_keyboard_if_visible()
    registration.submit_registration()
    

    assert  registration.is_registration_mismatch_warning_exist(), "Registration succeeded with mismatched passwords."



def test_empty_fields(driver):
    registration = ActivePage(driver)

    time.sleep(5)

    registration.allow_permission_popup()
    registration.skip_onbarding_page()
    registration.navigate_to_active_card_screen()
    registration.click_card_id()
    registration.enter_card("")
    registration.hide_keyboard_if_visible()
    registration.click_name()
    registration.enter_name("")
    registration.hide_keyboard_if_visible()
    registration.click_last_name()
    registration.enter_last_name("")
    registration.hide_keyboard_if_visible()
    registration.click_phone()
    registration.enter_phone("")
    registration.hide_keyboard_if_visible()
    registration.click_password()
    registration.enter_password("")
    registration.hide_keyboard_if_visible()
    registration.click_confirm_password()
    registration.confirm_password("")
    registration.hide_keyboard_if_visible()
    registration.submit_registration()
   

    assert  registration.are_all_registration_warnings_displayed(), "Registration succeeded with empty fields."
