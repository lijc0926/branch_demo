#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/20 21:53
# @Author  : jingchen
# @File    : selenium_窗口截图.py



from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 鼠标事件
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(r"D:\pythonfile\homework\driver_folder\chromedriver.exe")
driver.get("https://www.vmall.com/")

# 窗口截图
driver.get_screenshot_as_file("文件地址")

# 单个元素截图
ele = driver.find_element_by_xpath("kw")
ele.screenshot("截图文件地址")