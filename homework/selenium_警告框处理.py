#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/20 21:57
# @Author  : jingchen
# @File    : selenium_警告框处理.py


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 鼠标事件
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(r"D:\pythonfile\homework\driver_folder\chromedriver.exe")
driver.get("https://www.vmall.com/")


driver.find_element_by_xpath('kw').click()
# 操作对话框
a = driver.switch_to.alert
# 确认对话框
a.accept()

# 确认确认框
a.accept()
# 取消确认框
a.dismiss()

# 文本输入
a.send_keys()
