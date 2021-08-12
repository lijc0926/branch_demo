#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/22 22:04
# @Author  : jingchen
# @File    : selenium_下拉框选择.py


import win32com.client
# 下拉框的类
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(r"D:\pythonfile\homework\driver_folder\chromedriver.exe")
driver.get("https://www.vmall.com/")

# 定位到下拉框元素
ele = driver.find_element_by_css_selector("下拉框元素的位置")
# 根据下拉框文本选择
Select(ele).select_by_visible_text("下拉框中的文本内容")
# 根据下拉框索引选择  下标从0开始
Select(ele).select_by_index("标签的索引")
# 根据下拉框的value属性进行选择，必须要有value属性
Select(ele).select_by_value("value的值")
