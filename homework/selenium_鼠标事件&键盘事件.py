#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/20 22:16
# @Author  : jingchen
# @File    : selenium_鼠标事件&键盘事件.py


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

"""
鼠标事件
ele = driver.find_element_by_xpath('a')
ele1 = driver.find_element_by_xpath('a')
# 右击元素
ActionChains(driver).context_click(ele).perform()
# 双击元素
ActionChains(driver).double_click(ele).perform()
# 单击元素
ActionChains(driver).click(ele).perform()
# 拖动元素
ActionChains(driver).drag_and_drop(ele, ele1).perform()
"""


# 键盘事件
ele = driver.find_element_by_xpath('a')
# 给输入框输入内容
ele.send_keys("给输入框输入内容")
# 删除掉最后的一个字
ele.send_keys(Keys.BACK_SPACE)
#
