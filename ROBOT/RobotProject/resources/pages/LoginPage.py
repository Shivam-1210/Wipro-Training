import sys
import os
from typing import cast

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from SeleniumLibrary import SeleniumLibrary

from libraries.logger import LogGen
from libraries.screenshot_util import ScreenshotUtil

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from resources.locators.login_locators import (
    LOGIN_LINK,
    USERNAME_TEXTBOX,
    PASSWORD_TEXTBOX,
    LOGIN_BUTTON,
    WELCOME_USER
)

from resources.variables.config import config
from resources.variables.testdata import VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD

logger = LogGen.loggen()


class LoginPage:
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
    def click_login_link(self):
        logger.info('Clicking login link')
        self.selenium.click_element(LOGIN_LINK)

    @keyword
    def enter_username(self, username=VALID_USERNAME):
        logger.info(f'Entering Username: {username}')
        self.selenium.input_text(USERNAME_TEXTBOX, username)

    @keyword
    def enter_password(self, password=VALID_PASSWORD):
        logger.info(f'Entering Password: {password}')
        self.selenium.input_text(PASSWORD_TEXTBOX, password)

    @keyword
    def click_signin_button(self):
        logger.info('Clicking SignIn button')
        self.selenium.click_button(LOGIN_BUTTON)

    @keyword
    def verify_successful_login(self):
        logger.info('Verifying login success or handling unexpected alerts')
        try:
            # Check if an alert appears (like "Wrong password")
            alert = self.selenium.driver.switch_to.alert
            alert_text = alert.text
            logger.info(f"Unexpected alert during login: {alert_text}")
            ScreenshotUtil.capture_screenshot(self.selenium.driver, 'login_alert')
            alert.accept()
            raise AssertionError(f"Login failed due to alert: {alert_text}")
        except NoAlertPresentException:
            # No alert, continue to check welcome message
            WebDriverWait(self.selenium.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "nameofuser"))
            )
            welcome_text = self.selenium.get_text(WELCOME_USER)
            logger.info(f"Welcome text displayed: {welcome_text}")
            assert "Welcome" in welcome_text

    @keyword
    def enter_invalid_login_username(self):
        logger.info('Entering invalid username')
        self.enter_username(INVALID_USERNAME)

    @keyword
    def enter_invalid_login_password(self):
        logger.info('Entering invalid password')
        self.enter_password(INVALID_PASSWORD)

    @keyword
    def validate_invalid_login_alert(self):
        logger.info('Validating Invalid Login Alert')
        try:
            WebDriverWait(self.selenium.driver, 10).until(EC.alert_is_present())
            alert = self.selenium.driver.switch_to.alert
            logger.info(f'Alert text: {alert.text}')
            ScreenshotUtil.capture_screenshot(self.selenium.driver, 'invalid_login_alert')
            print(alert.text)
            alert.accept()
        except TimeoutException:
            ScreenshotUtil.capture_screenshot(self.selenium.driver, 'invalid_login_alert_timeout')
            raise AssertionError("Invalid login alert not displayed")