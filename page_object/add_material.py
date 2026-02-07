"""
    商品管理——商品信息，添加商品
"""

from base_page.basepage import BasePage

class add_product(BasePage):
    url = 'http://39.101.122.147:3000/material/material'

    add_material_button = ('xpath', '//div[@class="table-operator"]/button[1]')
    skip_button = ('xpath', '//a[@class="introjs-skipbutton"]') # 点击叉号，关闭提示信息     这个得看有没有第一次访问 第一次访问的话就要注释掉

    material_name = ('xpath', '//*[@placeholder="请输入名称"]')  # 名称
    material_standard = ('xpath', '//*[@placeholder="请输入规格"]')    # 规格
    material_unit = ('xpath', '//*[@placeholder="输入单位"]')    # 单位

    # 点击库存数量--->然后找到对应的仓库，添加库存
    stock_title = ('xpath', '//div[text()="库存数量"]')
    material_stock = ('xpath', '//span[@title="中图涿州库"]/../../div[3]')

    # 保存按钮
    material_save_button = ('xpath', '//span[text()="保 存"]')



    def add_product(self, name, standard, unit, stock):
        self.open(self.url)
        self.wait(1)
        self.click(*self.add_material_button)
        self.wait(1)
        # self.click(*self.skip_button)
        self.wait(1)
        self.input(*self.material_name, content = name)
        self.wait(1)
        self.input(*self.material_standard, content = standard)
        self.wait(1)
        self.input(*self.material_unit, content = unit)
        # 点击“库存数量”标签
        self.wait(1)
        self.click(*self.stock_title)
        self.wait(1)
        self.input(*self.material_stock, content=stock)
        self.wait(1)
        self.click(*self.material_save_button)
        self.wait(2)
