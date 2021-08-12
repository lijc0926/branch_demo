#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/20 23:06
# @Author  : jingchen
# @File    : selenium_标签页面切换.py


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
driver.get("127.0.0.1:8088")
# driver.get("https://www.baidu.com/")
# # 获取当前所有的标签页的句柄
# all_handle = driver.window_handles
#
# # 循环遍历所有的标签页，切换到自己想要的标签页
# for handle in all_handle:
#     if driver.title == "1":
#         driver.switch_to.window(handle)
