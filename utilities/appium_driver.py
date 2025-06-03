from appium import webdriver
# from appium.webdriver.common.mobileby import MobileBy
from appium.options.android import UiAutomator2Options  # Import the correct options class
import yaml
import os

# Function to load capabilities from the YAML file located in the 'config' folder
def load_capabilities():
    config_path = os.path.join(os.getcwd(), 'config', 'appium_config.yaml')
    with open(config_path, "r") as file:
        capabilities = yaml.safe_load(file)
    return capabilities

def get_driver():
    capabilities = load_capabilities()

    # Create UiAutomator2Options or AndroidOptions instance
    options = UiAutomator2Options()

    # Add each capability from the loaded dictionary to the options instance
    for key, value in capabilities.items():
        options.set_capability(key, value)
    
    # Initialize the Appium driver with the correct options
    driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4723",  # ✅ No /wd/hub in Appium 2
    options=options
    )

    return driver
