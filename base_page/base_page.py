from __future__ import annotations

from typing import Tuple

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """Encapsulate Selenium operations used by page objects."""

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.timeout = timeout

    def open(self, url: str) -> None:
        self.driver.get(url)

    def find(self, locator: Tuple[str, str]):
        return self.driver.find_element(*locator)

    def finds(self, locator: Tuple[str, str]):
        return self.driver.find_elements(*locator)

    def click(self, locator: Tuple[str, str]) -> None:
        self.wait_visible(locator)
        self.find(locator).click()

    def input_text(self, locator: Tuple[str, str], text: str, clear: bool = True) -> None:
        self.wait_visible(locator)
        element = self.find(locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator: Tuple[str, str]) -> str:
        self.wait_visible(locator)
        return self.find(locator).text

    def wait_visible(self, locator: Tuple[str, str]):
        return WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(locator))
