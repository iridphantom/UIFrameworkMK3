"""
    浏览器参数设置
"""

from selenium import webdriver


def chrome_options():
    option = webdriver.ChromeOptions()
    # 页面最大化.在浏览器启动时就会最大化
    option.add_argument('start-maximized')
    # 加载本地缓存
    # option.add_argument(r'--user-data-dir=C:\Users\1\AppData\Local\Google\Chrome\User Data')
    # option.add_argument('--headless')
    return option


def firefox_options():
    options = webdriver.FirefoxOptions()

    # Firefox个人资料路径
    profile_path = r"C:\Users\1\AppData\Roaming\Mozilla\Firefox\Profiles\vby4egfz.default-release"
    options.add_argument("-profile")
    options.add_argument(profile_path)
    
    # kiosk 模式：最大化并隐藏浏览器 UI（推荐用于测试）
    options.add_argument('-kiosk')

    # 设置初始窗口大小（当非 kiosk/fullscreen 时有效）
    # options.add_argument("--width=1920")
    # options.add_argument("--height=1080")



    return options