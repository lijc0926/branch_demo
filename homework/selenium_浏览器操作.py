#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 20:02
# @Author  : jingchen
# @File    : selenium_浏览器操作.py


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 鼠标事件
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(r"D:\pythonfile\homework\driver_folder\chromedriver.exe")
driver.get("https://www.vmall.com/")
driver.get("https://www.baidu.com/")



# 返回上一个网址
driver.back()
time.sleep(3)
# 退回上个网址
driver.forward()
time.sleep(3)
# 刷新界面
driver.refresh()
time.sleep(3)
# 控制浏览器大小
driver.set_window_size(700, 700)

# 最大化窗口
driver.maximize_window()

driver.quit()
