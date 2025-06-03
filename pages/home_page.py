from appium.webdriver.common.appiumby import AppiumBy

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # ---------- Locators ----------
    NAV_HOME = (AppiumBy.ACCESSIBILITY_ID, "Home")
    NAV_CART = (AppiumBy.ACCESSIBILITY_ID, "Cart")
    NAV_CARE_TEAM = (AppiumBy.ACCESSIBILITY_ID, "Care Team")
    NAV_ACCOUNT = (AppiumBy.ACCESSIBILITY_ID, "Account")
    HOME_SEARCH_BAR= (AppiumBy.XPATH, '//android.widget.EditText')
    SEARCH_BAR = (AppiumBy.XPATH, '//android.widget.EditText')
    NOTIFICATIONS_BUTTON = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.ImageView')
    NOTIFICATIONS_PAGE = (AppiumBy.XPATH, '//android.view.View[@content-desc="Notifications"]')
    PROVIDER_LIST = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="lab"]')
    HEALTH_TIPS = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[3]/android.view.View/android.widget.ImageView')
    BANNERS = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[3]/android.view.View/android.widget.ImageView')
    FIND_NEAR_ME_ARROW = (AppiumBy.XPATH, '//android.view.View[@content-desc="Find Near Me"]/android.widget.Button')
    FIND_NEAR_ME_ARROW_Title = (AppiumBy.XPATH, '//android.view.View[@content-desc="Find Near Me"]')
    SEARCH_INPUT =(AppiumBy.XPATH, '//android.widget.EditText')
    SEARCH_RESULTS_LIST = (AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View')
    EMPTY_STATE_LABEL=(AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.ImageView')

    # ---------- Actions ----------
    def tap_home(self):
        self.driver.find_element(*self.NAV_HOME).click()
    def tap_search(self):
        self.driver.find_element(*self.HOME_SEARCH_BAR).click()

    def tap_cart(self):
        self.driver.find_element(*self.NAV_CART).click()

    def tap_care_team(self):
        self.driver.find_element(*self.NAV_CARE_TEAM).click()

    def tap_account(self):
        self.driver.find_element(*self.NAV_ACCOUNT).click()

    def tap_notifications_button(self):
        self.driver.find_element(*self.NOTIFICATIONS_BUTTON).click()

    def tap_find_near_me_arrow(self):
        self.driver.find_element(*self.FIND_NEAR_ME_ARROW).click()
    

    def tap_search_bar(self):
        self.driver.find_element(*self.SEARCH_INPUT).click()

    def is_search_input_focused(self):
        # Could use driver.execute_script("mobile: isKeyboardShown") for Android
     return self.driver.is_keyboard_shown()

    def type_in_search_bar(self, text):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(text)

    def clear_search_bar(self):
        self.driver.find_element(*self.SEARCH_INPUT).clear()

    


    # ---------- Validations ----------
    def is_home_screen_displayed(self):
        return self.driver.find_element(*self.SEARCH_BAR).is_displayed()

    def is_search_bar_visible(self):
        return self.driver.find_element(*self.SEARCH_BAR).is_displayed()
    
    def is_notifications_title_visible(self):
        return self.driver.find_element(*self.NOTIFICATIONS_PAGE).is_displayed()

    def is_provider_list_visible(self):
        return self.driver.find_element(*self.PROVIDER_LIST).is_displayed()

    def is_health_tips_visible(self):
        return self.driver.find_element(*self.HEALTH_TIPS).is_displayed()

    def is_banners_visible(self):
        return self.driver.find_element(*self.BANNERS).is_displayed()
    
    def is_find_near_me_visible(self):
        return self.driver.find_element(*self.FIND_NEAR_ME_ARROW_Title).is_displayed()
    
    def are_search_results_visible(self):
     return len(self.driver.find_elements(*self.SEARCH_RESULTS_LIST)) > 0

    def is_empty_state_displayed(self):
     return self.driver.find_element(*self.EMPTY_STATE_LABEL).is_displayed()
