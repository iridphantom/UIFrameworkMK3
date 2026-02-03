
from selenium import webdriver
from base_page.basepage import BasePage

class open_url(BasePage):
    # 页面URL
    url = 'http://39.101.122.147:3000/user/login'

    # 页面核心元素(需要操作的核心元素)
    # 元素核心内容包括定位方法、对应的value值
    login_input_username = ('id', 'loginName')  # 获取用户名输入框的元素定位信息
    login_input_password = ('id', 'password')
    login_input_code = ('id', 'inputCode')
    login_code_img = ('xpath', '//img[@data-v-4f5798c5]')  # 获取验证码图片的元素定位信息
    login_button = ('xpath', '//button[@data-v-4f5798c5]')

    # 页面的子流程封装
    def login(self, username, password):
        self.open(self.url)
        # self.input(*self.login_input_username, content= username)  # *：解元组。   由于浏览器已导入缓存，会自动填充，这里就不输入了
        # self.input(*self.login_input_password, content= password)
        self.input(*self.login_input_code, content=self.get_code(*self.login_code_img))
        self.click(*self.login_button)
        self.wait(15)
