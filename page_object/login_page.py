from selenium.webdriver.common.by import By

from base_page.base_page import BasePage


class LoginPage(BasePage):
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    submit_button = (By.CSS_SELECTOR, "button[type='submit']")

    def login(self, username: str, password: str) -> None:
        self.input_text(self.username_input, username)
        self.input_text(self.password_input, password)
        self.click(self.submit_button)
