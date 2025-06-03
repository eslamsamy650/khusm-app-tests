from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    # Locators
    allow_permission_notifications = "com.android.permissioncontroller:id/permission_allow_button"
    allow_permission_location = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
    change_language_xpath ='//android.view.View[@content-desc="العربيه"]'
    login_nav_button_xpath = '//android.widget.Button[@content-desc="Log In"]'
    phone_click_xpath = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]'
    phone_input_xpath = '//android.widget.ScrollView/android.widget.EditText[1]'
    password_click_xpath = '//android.widget.ScrollView/android.widget.EditText[2]'
    password_input_xpath = '//android.widget.ScrollView/android.widget.EditText[2]'
    login_button_xpath = '//android.widget.Button[@content-desc="Log In"]'
    account_button_xpath = '//android.widget.ImageView[@content-desc="Account"]'
    onboarding_xpath= '//android.view.View[@content-desc="SKIP"]'
    user_tutorial_skip_btn='//android.widget.Button[@content-desc="Skip"]'
    invalid_phone_number='//android.view.View[@content-desc="Phone number must start with 010 or 011 or 012 or 015"]'
    invalid_password_xpath='//android.view.View[@content-desc="Phone or Password is incorrect!"]'
    empty_filed_waning='//android.view.View[@content-desc="Password is required"]'
    nxt_home_btn='//android.view.View[@content-desc="Next"]'
    skip_user_tutorial_nav='//android.widget.Button[@content-desc="Skip"]'
    search_user_tutorial='//android.view.View[@content-desc="Next"]'
    cart_user_tutorial = '//android.view.View[@content-desc="Finish"]'


    # Actions
    def allow_permission_popup(self):
        try:
            allow_btn = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.ID, self.allow_permission_notifications)
            ))
            allow_btn.click()
        except TimeoutException:
            print("Permission popup not found or already dismissed.")

    def skip_onbarding_page(self):
        try:
            skip_btn = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, self.onboarding_xpath)
            ))
            skip_btn.click()
        except TimeoutException:
            print("skip onbardingpage  not found or already dismissed.")

    def skip_adding_service(self):
        try:
            skip_btn = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, self.search_user_tutorial)
            ))
            skip_btn.click()
        except TimeoutException:
            print("skip onbardingpage  not found or already dismissed.")


    def skip_cart_tutorial(self):
        try:
            skip_btn = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, self.cart_user_tutorial)
            ))
            skip_btn.click()
        except TimeoutException:
            print("skip onbardingpage  not found or already dismissed.")

    def skip_user_tutorial(self):
        try:
            skip_btn = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, self.user_tutorial_skip_btn)
            ))
            skip_btn.click()
        except TimeoutException:
            print("skip onbardingpage  not found or already dismissed.")

    def go_to_login_screen(self):
        try:
            login_nav_btn = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.login_nav_button_xpath)
            ))
            login_nav_btn.click()
        except TimeoutException:
            print("Login navigation button not clickable.")
            raise TimeoutException("Failed to navigate to the login screen.")
        
    def Change_langauge_to_English(self):
            try:
                Change_lang_btn = self.wait.until(EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.change_language_xpath)
                ))
                Change_lang_btn.click()
            except TimeoutException:
                print("Login navigation button not clickable.")
                raise TimeoutException("Failed to navigate to the login screen.")    

    def click_phone_login(self):
        try:
            phone_field = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.phone_click_xpath)
            ))
            phone_field.click()
        except TimeoutException:
            print("Phone login field not clickable.")
            raise TimeoutException("Failed to click on phone login.")

    def enter_phone(self, phone_number):
        try:
            phone_field = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.phone_input_xpath)
            ))
            phone_field.send_keys(phone_number)
        except TimeoutException:
            print("Phone input field not clickable.")
            raise TimeoutException("Failed to enter phone number.")


    def click_password_login(self):
        try:
            password_field = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.password_click_xpath)
            ))
            password_field.click()
        except TimeoutException:
            print("Password login field not clickable.")
            raise TimeoutException("Failed to click on password login.")
        
    def click_home_next(self):
        try:
            password_field = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.nxt_home_btn)
            ))
            password_field.click()
        except TimeoutException:
            print("Password login field not clickable.")
            raise TimeoutException("Failed to click on password login.")


    def click_Skip_nav(self):
        try:
            password_field = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.skip_user_tutorial_nav)
            ))
            password_field.click()
        except TimeoutException:
            print("Password login field not clickable.")
            raise TimeoutException("Failed to click on password login.")



    def enter_password(self, password):
        try:
            password_field = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.password_input_xpath)
            ))
            password_field.send_keys(password)
        except TimeoutException:
            print("Password input field not found.")
            raise TimeoutException("Failed to enter password.")

    def submit_login(self):
        try:
            login_btn = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.login_button_xpath)
            ))
            login_btn.click()
        except TimeoutException:
            print("Login button not clickable.")
            raise TimeoutException("Failed to click on login button.")

    def allow_permission_popup_location(self):
        try:
            allow_btn = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.ID, self.allow_permission_location)
            ))
            allow_btn.click()
        except TimeoutException:
            print("Permission popup not found or already dismissed.")

    def hide_keyboard_if_visible(self):
        try:
            self.driver.hide_keyboard()
        except:
            pass

    def is_login_successful(self):
        try:
            self.wait.until(EC.visibility_of_element_located(
                (AppiumBy.XPATH, self.account_button_xpath)
            ))
            return True
        except TimeoutException:
            print("Account button not found after login attempt.")
            return False
    def is_login_invalid_phone(self):
        try:
            self.wait.until(EC.visibility_of_element_located(
                (AppiumBy.XPATH, self.invalid_phone_number)
            ))
            return True
        except TimeoutException:
            print("Account button not found after login attempt.")
            return False
        
    def is_invalid_password(self):
        try:
            self.wait.until(EC.visibility_of_element_located(
                (AppiumBy.XPATH, self.invalid_password_xpath)
            ))
            return True
        except TimeoutException:
            print("Account button not found after login attempt.")
            return False
        
    def is_empty_filed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(
                (AppiumBy.XPATH, self.empty_filed_waning)
            ))
            return True
        except TimeoutException:
            print("Account button not found after login attempt.")
            return False