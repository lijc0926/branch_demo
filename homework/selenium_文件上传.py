#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/21 20:25
# @Author  : jingchen
# @File    : selenium_文件上传.py


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 鼠标事件
from selenium.webdriver.common.action_chains import ActionChains
# 文件上传
import win32com.client
driver = webdriver.Chrome(r"D:\pythonfile\homework\driver_folder\chromedriver.exe")
driver.get("https://tinypng.com/")

# 对于input标签进行上传时，直接用send_keys方式进行文件上传
time.sleep(3)
# driver.find_element_by_css_selector('input[type="file"]').send_keys(r"d:\a.txt")
driver.find_element_by_css_selector('figure[class="icon"]').click()
# 模拟键盘敲击，不管不顾的敲击，只要代码运行到此处，就进行敲击的操作
time.sleep(3)
sh = win32com.client.Dispatch("WScript.shell")
# 最后的\r\n是回车操作
sh.SendKeys("d:\\a.txt\r\n")

