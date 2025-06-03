import os
import sys
import pytest
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from pages.login_page import LoginPage
from utilities.appium_driver import get_driver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_logout_flow(driver):
    login_page = LoginPage(driver) 
    wait = WebDriverWait(driver, 20)

    time.sleep(5)
    login_page.allow_permission_popup()
    login_page.skip_onbarding_page()
    login_page.go_to_login_screen()
    login_page.click_phone_login()
    login_page.enter_phone("01116590586")
    login_page.click_password_login()
    login_page.enter_password("123e321")
    login_page.submit_login()
    login_page.allow_permission_popup_location()

    assert login_page.is_login_successful(), "Login failed."
    login_page.skip_user_tutorial()
    login_page.click_home_next()
    login_page.click_Skip_nav()

    # === START Logout Steps ===
    account_btn = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, login_page.account_button_xpath)))
    account_btn.click()

    # Optional: Scroll/swipe to bottom if needed (depending on layout)
    # Dynamically scroll down (from 80% to 20% of screen height)
    window_size = driver.get_window_size()
    width = window_size["width"]
    height = window_size["height"]

    start_x = width // 2
    start_y = int(height * 0.8)
    end_y = int(height * 0.1)

    driver.swipe(start_x, start_y, start_x, end_y, 800)


    # Find and click logout button
    logout_btn = wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Log Out"]')
    ))
    logout_btn.click()

    # Optional: Confirm logout if there's a confirmation dialog
    confirm_btn = wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, '//android.view.View[@content-desc="Log Out"]')
    ))
    confirm_btn.click()

    # === Verify login screen is shown again ===
    login_screen_btn = wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, login_page.login_nav_button_xpath)
    ))
    assert login_screen_btn.is_displayed(), "Logout failed: Login screen not shown."
