# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 下拉框选择.py
# @ide     : PyCharm
# @time    : 2020/12/21 20:02
from selenium.webdriver.support.select import Select
from selenium import webdriver

# 创建浏览器驱动对象，这里是打开浏览器
driver = webdriver.Chrome("D:\\tool\selenium\chromedriver.exe")
# 访问网址
driver.get("file:///D:/Users/lenovo/PycharmProjects/script/study/seleniumStu/day5/test.html")

# 定位到下拉框元素
ele = driver.find_element_by_id("abc")
# # 根据下拉框文本选择
# Select(ele).select_by_visible_text("月薪三千")
# # 根据下标选择
# Select(ele).select_by_index(0)
# 根据 value 属性选择
Select(ele).select_by_value("p3")
