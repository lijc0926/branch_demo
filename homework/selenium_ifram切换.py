#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/20 22:48
# @Author  : jingchen
# @File    : selenium_ifram切换.py


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 鼠标事件
from selenium.webdriver.common.action_chains import ActionChains
# 键盘事件
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"D:\pythonfile\homework\driver_folder\chromedriver.exe")
driver.get("https://www.vmall.com/")

# 先定位到ifram标签
a = driver.find_element_by_xpath('kw')
# 切入ifram标签
driver.switch_to.frame(a)
# 退出ifram标签回到主页面(无论有多少层的ifram)
driver.switch_to.default_content()
