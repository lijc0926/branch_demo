# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : ccookie操作.py
# @ide     : PyCharm
# @time    : 2020/12/21 20:37
"""
cookie 是服务端存在我们本地客户端的一些信息
并且是不涉及隐私的信息（这个通常要程序员自我约束
cookie 里边要存那些内容也不是固定的，完全按照开发者的心意去实现
"""

from selenium import webdriver
import pprint

# 创建浏览器驱动对象，这里是打开浏览器
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("http://127.0.0.1:8088/")

# 登录一下
driver.find_element_by_name("username").send_keys("libai")
driver.find_element_by_name("password").send_keys("opmsopms123")
driver.find_element_by_css_selector("button").click()

# 获取所有的 cookie
cookieSli = driver.get_cookies()
pprint.pprint(cookieSli)
# # 根据name，获取某个cookie
# cookie = driver.get_cookie("beegosessionID")
# print(cookie)
