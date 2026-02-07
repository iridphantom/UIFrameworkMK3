import unittest

from ddt import file_data, ddt
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from page_object.add_material import add_product
from page_object.logout import Logout
from page_object.open_page import open_url
from utils.browser.browser_options import firefox_options
from utils.browser.driver_factory import create_firefox_options


@ddt
class TestErp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('所有测试用例执行前的初始化操作')

        cls.driver = create_firefox_options()
        cls.login_page = open_url(cls.driver)
        cls.add_material = add_product(cls.driver)
        cls.logout = Logout(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print('所有测试用例执行后的收尾操作')
        cls.driver.quit()

    @file_data('../test_data/login.yaml')
    def test_01_login(self, username, password):
        self.login_page.login(username, password)

    # 添加商品
    @file_data('../test_data/material.yaml')
    def test_02_add_product(self, name, standard, unit, stock):
        self.add_material.add_product(name, standard, unit, stock)

    def test_03_logout(self):
        self.logout.logout()


if __name__ == '__main__':
    unittest.main()