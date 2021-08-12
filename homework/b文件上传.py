# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : b文件上传.py
# @ide     : PyCharm
# @time    : 2020/12/21 20:15
"""
对于通过 input 实现的文件上传，我们可以将其看作是一个输入框
即通过 send_keys 的方式即可实现文件上传

对于非 input 标签实现的上传功能，我们可以通过模拟键盘敲击的方式去实现
"""
from selenium import webdriver
import win32com.client
import time

# 创建浏览器驱动对象，这里是打开浏览器
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("https://tinypng.com/")

# # 定位到文件上传的 input 标签
# ele = driver.find_element_by_css_selector("input[type=\"file\"]")
# ele.send_keys("D:\\Users\lenovo\PycharmProjects\script\study\seleniumStu\day4\ele.png")

# 对于非 input 标签实现的上传功能，我们通过模拟键盘敲击的方式实现

# 触发文件上传的功能
driver.find_element_by_css_selector("figure.icon").click()
time.sleep(3)

# 模拟键盘敲击，会不管不顾的敲击，只要代码运行到这里，就敲
sh = win32com.client.Dispatch("WScript.shell")
sh.Sendkeys("D:\\Users\lenovo\PycharmProjects\script\study\seleniumStu\day4\ele.png\r\n")

# 注意：代码运行过程不要操作鼠标
# 输入法要保持英文输入的状态
