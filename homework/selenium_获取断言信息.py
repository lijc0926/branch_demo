#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 20:53
# @Author  : jingchen
# @File    : selenium_获取断言信息.py


from selenium import webdriver

driver = webdriver.Chrome("D:\pythonfile\homework\driver_folder\chromedriver.exe")

driver.get("https://www.baidu.com/")

# 获取当前页面的title
print(driver.title)
# 获取当前页面的url
print(driver.current_url)
# 获取标签对的文本信息
#   标签内没有文本信息，返回结果为空
#   input之类的单标签没有文本信息
#   标签元素不展示在页面上，返回结果为空
print(driver.find_element_by_class_name("title-text").text)
# 获取元素的某个属性
ele = driver.find_element_by_id("kw")
print(ele.get_attribute("class"))

driver.quit()
