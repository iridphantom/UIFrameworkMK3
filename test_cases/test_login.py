import os
import unittest

from selenium import webdriver

from page_object.login_page import LoginPage
from test_data import config


@unittest.skipUnless(os.getenv("RUN_UI_TESTS") == "1", "UI tests require RUN_UI_TESTS=1")
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.page = LoginPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login_success(self) -> None:
        self.page.open(config.BASE_URL)
        self.page.login(config.VALID_USER, config.VALID_PASSWORD)
        # Add assertion for post-login element here.


if __name__ == "__main__":
    unittest.main()
