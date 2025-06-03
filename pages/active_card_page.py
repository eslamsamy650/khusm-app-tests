from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ActivePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    # Locators (you need to inspect the app to find the real ones)
    otp_input_xpath='//android.view.View[@clickable="true"]'
    allow_permission_notifications = "com.android.permissioncontroller:id/permission_allow_button"
    allow_permission_location = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
    onboarding_xpath= '//android.view.View[@content-desc="SKIP"]'
    active_button_xpath = '//android.widget.Button[@content-desc="Active Khusm Card"]'
    card_input_xpath= '//android.widget.ScrollView/android.widget.EditText[1]'
    phone_input_xpath = '//android.widget.ScrollView/android.widget.EditText[4]'
    password_input_xpath = '//android.widget.ScrollView/android.widget.EditText[5]'
    confirm_password_input_xpath = '//android.widget.ScrollView/android.widget.EditText[5]'
    name_input_xpath = '//android.widget.ScrollView/android.widget.EditText[2]'
    last_input_xpath='//android.widget.ScrollView/android.widget.EditText[3]'
    otp_warning_message ='//android.view.View[@content-desc="Incorrect code. Please re-enter the code."]'
    submit_button_xpath = '//android.widget.Button[@content-desc="Sign Up"]'
    NAV_HOME = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[1]'
    card_tap_xpath = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]'
    name_tap_xpath='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]'
    last_tap_xpath='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[3]'
    phone_tap_xpath='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[4]'
    password_tap_xpath='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[5]'
    confirm_password_tap_xpath='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[6]'
    otp_confirm_click='//android.widget.Button[@resource-id="com.google.android.gms:id/negative_button"]'
    duplicate_mobile_number='//android.view.View[@content-desc="Mobile number already exists for another member."]'
    duplicate_card_number='//android.view.View[@content-desc="Card Already Activated"]'
    invalid_card_nunber='//android.view.View[@content-desc="Invalid card Id"]'
    mismatch_password='//android.view.View[@content-desc="Passwords do not match. Please ensure both passwords are identical"]'
    confirm_password_is_empty ='//android.view.View[@content-desc="Please confirm password"]'
    first_name_is_empty='//android.view.View[@content-desc="Enter your first name"]'
    last_name_is_empty='//android.view.View[@content-desc="Enter your last name"]'
    phone_is_empty ='//android.view.View[@content-desc="Enter your phone number"]'
    password_is_empty='//android.view.View[@content-desc="Please enter your password"]'
    click_verify='//android.widget.Button[@content-desc="Verify"]'
    
    
    # Actions
    def allow_permission_popup(self):
        try:
            allow_btn = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.ID, self.allow_permission_notifications)
            ))
            allow_btn.click()
        except TimeoutException:
            print("Permission popup not found or already dismissed.")

    def allow_permission_popup_location(self):
        try:
            allow_btn = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.ID, self.allow_permission_location)
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

    def navigate_to_active_card_screen(self):
        try:
            active_card_btn = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, self.active_button_xpath)
            ))
            active_card_btn.click()
        except TimeoutException:
            raise TimeoutException("Register button not found.")

    def enter_card(self, card):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.card_input_xpath))).send_keys(card)

    def enter_phone(self, phone):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.phone_input_xpath))).send_keys(phone)

    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.password_input_xpath))).send_keys(password)

    def confirm_password(self, password):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.confirm_password_input_xpath))).send_keys(password)

    def enter_name(self, name):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.name_input_xpath))).send_keys(name)

    def enter_last_name(self, lname):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.last_input_xpath))).send_keys(lname)

    def click_phone(self):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.phone_tap_xpath))).click()

    def click_otp(self):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.phone_tap_xpath))).click()

    def click_password(self):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.password_tap_xpath))).click()

    def click_confirm_password(self):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.confirm_password_tap_xpath))).click()

    def click_name(self):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.name_tap_xpath))).click()

    def click_last_name(self):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.last_tap_xpath))).click()

    def click_card_id(self):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.card_tap_xpath))).click()

    def click_otp_confirmation(self):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.otp_confirm_click))).click()

    def click_otp_verify(self):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.click_verify))).click()

    def submit_registration(self):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.submit_button_xpath))).click()

    def enter_otp_code(self, otp):
        for i, digit in enumerate(otp):
            otp_input_xpath = f'//android.widget.EditText[{i + 1}]'  # Adjust to your real XPath
            self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, otp_input_xpath))).send_keys(digit)


    def hide_keyboard_if_visible(self):
        try:
            self.driver.hide_keyboard()
        except:
            pass


    def is_registration_successful(self):
        try:
            self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, self.NAV_HOME)))
            return True
        except TimeoutException:
            return False
        
    def is_registration_invalid_otp(self):
        try:
            self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, self.otp_warning_message)))
            return True
        except TimeoutException:
            return False
    
    def is_registration_mobile_warning_exist (self):
        try:
            self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, self.duplicate_mobile_number)))
            return True
        except TimeoutException:
            return False
        
    def is_registration_card_warning_exist (self):
        try:
            self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, self.duplicate_card_number)))
            return True
        except TimeoutException:
            return False
        
    def is_registration_invalid_card_warning_exist (self):
        try:
            self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, self.invalid_card_nunber)))
            return True
        except TimeoutException:
            return False
        
    def is_registration_mismatch_warning_exist (self):
        try:
            self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, self.mismatch_password)))
            return True
        except TimeoutException:
            return False
    def are_all_registration_warnings_displayed(self):
        try:
            self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, self.first_name_is_empty)))
            self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, self.last_name_is_empty)))
            self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, self.phone_is_empty)))
            self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, self.password_is_empty)))
            self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, self.confirm_password_is_empty)))
            return True
        except TimeoutException:
            return False

    