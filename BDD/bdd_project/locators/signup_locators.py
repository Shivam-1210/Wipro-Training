from selenium.webdriver.common.by import By


class SignupLocators:
    SIGNUP_MENU = (By.LINK_TEXT, "Sign up")
    USERNAME_INPUT = (By.ID, "sign-username")
    USERNAME_password = (By.ID, "sign-password")

    SIGNUP_BUTTON = (By.XPATH, "//button[text()='Sign up']")
