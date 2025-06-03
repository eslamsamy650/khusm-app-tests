import time
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("logged_in_driver")
class TestHome:

    def test_nav_bar_buttons(self, logged_in_driver):
        home = HomePage(logged_in_driver)
        login_page = LoginPage(logged_in_driver)
        login_page.skip_user_tutorial()
        login_page.click_home_next()
        login_page.click_Skip_nav()
        
        
        time.sleep(5)
        home.tap_cart()
        time.sleep(2)
        home.tap_care_team()
        time.sleep(2)
        home.tap_account()
        time.sleep(2)
        home.tap_home()
        time.sleep(2)

    def test_search_bar_visible(self, logged_in_driver):
        home = HomePage(logged_in_driver)
        home.tap_search()
        login_page = LoginPage(logged_in_driver)
        login_page.skip_adding_service()
        login_page.skip_cart_tutorial()
        time.sleep(2)
        assert home.is_search_bar_visible(), "Search bar not visible"

    def test_search_functionality(self, logged_in_driver):
        home = HomePage(logged_in_driver)
        logged_in_driver.back()
        # Step 1: Tap the search bar
        home.tap_search()
        home.tap_search_bar()
        time.sleep(2)

        # Assert keyboard is open or input is focused
        assert home.is_search_input_focused(), "Search input is not focused after tapping."

        # Step 2: Type valid input and verify results
        valid_input = "cbc"
        home.type_in_search_bar(valid_input)
        time.sleep(2)
        assert home.are_search_results_visible(), "Expected search results not shown for valid input."

        # Step 3: Clear and type invalid input
        home.clear_search_bar()
        invalid_input = "asdfghjk"
        home.type_in_search_bar(invalid_input)
        time.sleep(2)
        assert home.is_empty_state_displayed(), "Empty state not shown for invalid input."

    def test_notifications_button(self, logged_in_driver):
        home = HomePage(logged_in_driver)
        logged_in_driver.back()
        logged_in_driver.back()
        time.sleep(2)
        home.tap_notifications_button()
        time.sleep(5)
        assert home.is_notifications_title_visible(), "Notifications Title visible"
        

    # def test_provider_list_visible(self, logged_in_driver):
    #     home = HomePage(logged_in_driver)
    #     logged_in_driver.back()
    #     time.sleep(2)
    #     assert home.is_provider_list_visible(), "Provider list not visible"
    
    

    def test_health_tips_visible(self, logged_in_driver):
        home = HomePage(logged_in_driver)
        logged_in_driver.back()
        assert home.is_health_tips_visible(), "Health tips not visible"

    def test_find_near_me_navigation(self, logged_in_driver):
        time.sleep(2)
        home = HomePage(logged_in_driver)
        home.tap_find_near_me_arrow()
        time.sleep(2)
        assert home.is_find_near_me_visible, "Find Near Me visible"

    def test_banners_visible(self, logged_in_driver):
        home = HomePage(logged_in_driver)
        logged_in_driver.back()
        # Dynamically scroll down (from 80% to 20% of screen height)
        window_size = logged_in_driver.get_window_size()
        width = window_size["width"]
        height = window_size["height"]

        start_x = width // 2
        start_y = int(height * 0.8)
        end_y = int(height * 0.2)

        logged_in_driver.swipe(start_x, start_y, start_x, end_y, 800)

        time.sleep(5)
        assert home.is_banners_visible(), "Banners not visible"


