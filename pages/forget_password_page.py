from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ForgetPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    # Locators
    allow_permission_notifications = "com.android.permissioncontroller:id/permission_allow_button"
    allow_permission_location = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
    login_nav_button_xpath = '//android.widget.Button[@content-desc="Log In"]'
    forget_nav_button_xpath= '//android.widget.Button[@content-desc="Forgot Password?"]'
    tap_phone_number_xpath= '//android.widget.EditText'
    submit_forget_password='//android.widget.Button[@content-desc="Continue"]'
    otp_input_xpath='//android.view.View[@clickable="true"]'
    account_button_xpath = '//android.widget.ImageView[@content-desc="Account"]'
    onboarding_xpath= '//android.view.View[@content-desc="SKIP"]'
    tap_new_pass_xpath= '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]'
    tap_confirm_pass_xpath='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]'
    reset_password_btn_xpath='//android.widget.Button[@content-desc="Reset Password"]'
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

    def click_phone_forget(self):
        try:
            phone_field = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.tap_phone_number_xpath)
            ))
            phone_field.click()
        except TimeoutException:
            print("Phone login field not clickable.")
            raise TimeoutException("Failed to click on phone login.")

    def enter_phone_forget(self, phone_number):
        try:
            phone_field = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.tap_phone_number_xpath)
            ))
            phone_field.send_keys(phone_number)
        except TimeoutException:
            print("Phone input field not clickable.")
            raise TimeoutException("Failed to enter phone number.")



    def click_new_password(self):
        try:
            phone_field = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.tap_new_pass_xpath)
            ))
            phone_field.click()
        except TimeoutException:
            print("Phone login field not clickable.")
            raise TimeoutException("Failed to click on phone login.")

    def enter_new_password(self, phone_number):
        try:
            phone_field = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.tap_new_pass_xpath)
            ))
            phone_field.send_keys(phone_number)
        except TimeoutException:
            print("Phone input field not clickable.")
            raise TimeoutException("Failed to enter phone number.")
        


    def click_confirm_password(self):
        try:
            phone_field = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.tap_confirm_pass_xpath)
            ))
            phone_field.click()
        except TimeoutException:
            print("Phone login field not clickable.")
            raise TimeoutException("Failed to click on phone login.")

    def enter_confirm_password(self, phone_number):
        try:
            phone_field = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.tap_confirm_pass_xpath)
            ))
            phone_field.send_keys(phone_number)
        except TimeoutException:
            print("Phone input field not clickable.")
            raise TimeoutException("Failed to enter phone number.")   




    def click_forget_password(self):
        try:
            password_field = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.forget_nav_button_xpath)
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

    def submit_phone_forget(self):
        try:
            login_btn = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.submit_forget_password)
            ))
            login_btn.click()
        except TimeoutException:
            print("Login button not clickable.")
            raise TimeoutException("Failed to click on login button.")
        
    def submit_reset_password(self):
        try:
            login_btn = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.reset_password_btn_xpath)
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
