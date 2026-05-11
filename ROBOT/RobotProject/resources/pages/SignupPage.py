import sys
import os
import time
from typing import cast

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from SeleniumLibrary import SeleniumLibrary

from libraries.logger import LogGen
from libraries.screenshot_util import ScreenshotUtil

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from resources.locators.signup_locators import SIGNUP_LINK, USERNAME_TEXTBOX, PASSWORD_TEXTBOX, SIGNUP_BUTTON
from resources.variables.config import config
from resources.variables.testdata import SIGNUP_PASSWORD

logger = LogGen.loggen()


class SignupPage:
    def __init__(self):
        self.selenium = cast(
            SeleniumLibrary,
            BuiltIn().get_library_instance("SeleniumLibrary")
        )

    @keyword
    def launch_demoblaze_application(self):
        self.selenium.open_browser(config.base_url, browser=config.browser)
        logger.info('Opening Browser and launching Demoblaze application')
        self.selenium.maximize_browser_window()
        self.selenium.set_selenium_implicit_wait(config.implicit_wait)

    @keyword
    def click_signup_link(self):
        logger.info('Clicking signup link')
        self.selenium.click_element(SIGNUP_LINK)

    @keyword
    def enter_username(self, username=None):
        # Generate a unique username if none provided
        if username is None:
            username = f"user_{int(time.time())}"
        self.username = username  # Save for later verification if needed
        logger.info(f'Entering Signup Username: {username}')
        self.selenium.input_text(USERNAME_TEXTBOX, username)

    @keyword
    def enter_password(self, password=SIGNUP_PASSWORD):
        logger.info(f'Entering Signup Password: {password}')
        self.selenium.input_text(PASSWORD_TEXTBOX, password)

    @keyword
    def click_register_button(self):
        logger.info('Clicking register button')
        self.selenium.click_button(SIGNUP_BUTTON)

    @keyword
    def verify_signup_success_alert(self):
        logger.info('Verifying Signup Success Alert')
        try:
            WebDriverWait(self.selenium.driver, 10).until(EC.alert_is_present())
            alert = self.selenium.driver.switch_to.alert
            logger.info(f'Alert text: {alert.text}')
            ScreenshotUtil.capture_screenshot(self.selenium.driver, 'signup_alert')
            print(alert.text)
            alert.accept()
            # Optionally assert for success message
            if "already exist" in alert.text.lower():
                raise AssertionError(f"Signup failed: {alert.text}")
        except TimeoutException:
            ScreenshotUtil.capture_screenshot(self.selenium.driver, 'signup_alert_timeout')
            raise AssertionError("Signup alert did not appear")