# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : epo模式.py
# @ide     : PyCharm
# @time    : 2020/12/21 21:21
"""
po模式，简单来说，就是page object
页面对象
我们做ui自动化的时候，会遇到很多的页面
为了维护方面，我们可以将每一个页面封装成一个class

po模式，其实没有任何新的知识点融入，只不过是将面向对象的思想融入进来了
"""
"""
selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
陈旧的元素引用异常
这个异常发生在
    获取元素赋值给变量，再通过变量操作元素，两个步骤之间，若产生了界面刷新
    则会在通过变量操作元素的时候，抛出此异常
解决方案：
    每次操作元素前，实时获取元素赋值给变量
    也就是说，若在获取元素赋值给变量，与通过变量操作元素之间发生了页面刷新
    则在界面刷新后，元素操作前，重新获取元素赋值给变量
"""
from selenium import webdriver


class loginPage:
    def __init__(self, url):
        # 创建浏览器驱动对象，这里是打开浏览器
        self.driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
        # 访问网址
        self.driver.get(url)

    # 用户名输入框
    def user_name_input_box(self):
        return self.driver.find_element_by_name("username")

    # 密码输入框
    def password_input_box(self):
        return self.driver.find_element_by_name("password")

    # 登录按钮
    def login_button_box(self):
        return self.driver.find_element_by_css_selector("button")

    def logn(self):
        self.driver.refresh()
        self.user_name_input_box().send_keys("libai")
        self.password_input_box().send_keys("opmsopms123")
        self.login_button_box().click()


LP = loginPage("http://127.0.0.1:8088/login")
LP.logn()
