"""
    专门用于创建driver
"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from utils.browser.browser_options import chrome_options, firefox_options

def create_chrome_driver():
    service = Service(r"D:\DevelopmentEnvironment\BrowserDrivers\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options())
    driver.implicitly_wait(5)
    return driver


def create_firefox_options():
    service = Service(r"D:\DevelopmentEnvironment\BrowserDrivers\geckodriver.exe")
    driver = webdriver.Firefox(service=service, options = firefox_options())
    driver.implicitly_wait(5)
    return driver