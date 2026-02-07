"""
    封装页面级通用操作
"""
import time
import ddddocr

from utils.logger.get_logger import get_logger

class BasePage:

    # 构造方法
    def __init__(self, driver):
        self.driver = driver
        # self.logger = get_logger(self.__class__.__name__)
        # self.logger = get_logger()
        self.logger = get_logger("uiLogger")

    # 封装访问URL：
    def open(self, url):
        self.logger.info(f"打开页面{url}")
        self.driver.get(url)

    # 封装定位元素
    def locator(self, by, value):
        return self.driver.find_element(by, value)

    # 封装输入
    def input(self, by, value, content):
        self.locator(by, value).send_keys(content)

    # 封装点击
    def click(self, by, value):
        self.locator(by, value).click()

    # 封装关闭
    def quit(self):
        self.driver.quit()

    # 封装强制等待
    def wait(self, wait_time):
        time.sleep(int(wait_time))

    # 验证码处理
    def get_code(self, by, value):
        file = self.locator(by, value).screenshot_as_png
        return ddddocr.DdddOcr(show_ad=False).classification(file)

    # 断言
    def assert_text(self, by, value, expected):
        # 1. 首先定位到元素
        element = self.locator(by, value)  # 这里返回的是 WebElement 对象

        # 2. 从元素对象中获取文本
        reality = element.text  # 调用 .text 属性获取文本内容

        # 3. 比较获取到的文本和预期文本
        assert reality == expected, f'''
        预期结果不匹配，请检查！
        预期结果为：{expected}
        实际结果为：{reality}  # 现在显示的是文本，而不是对象
        断言结果：{expected} != {reality}'''
