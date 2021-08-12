#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 21:16
# @Author  : jingchen
# @File    : selenium_第二次作业.py
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 鼠标事件
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(r"D:\pythonfile\homework\driver_folder\chromedriver.exe")
driver.get("https://www.vmall.com/")
# 最大化窗口
driver.maximize_window()
# 显示等待，知道列表中的手机元素出现
WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, "//ol[@class='category-list']/li")))
# 获取列表中的所有的以及标签的元素位置
elLi = driver.find_elements_by_xpath("//ol[@class='category-list']/li")
# 遍历所有的一级标签，获取每个标签下的展示页的内容，并且将他们打印出来
for ele in elLi:
    yiji = ele.find_elements_by_xpath(".//input[@type='hidden']")
    if yiji:
        print("一级标签:{}".format(yiji[1].get_attribute("value")))
    # ele.click()
    ActionChains(driver).move_to_element(ele).perform()
    eleText = ele.find_elements_by_xpath(".//p/span")
    for i in eleText:
        Text = i.text
        print("    {}".format(Text))
# 页面滑动到热销单品页所在位置
target = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[@class='title change-title' and text()='热销单品']")))
driver.execute_script("arguments[0].scrollIntoView();", target)
time.sleep(3)
# 获取热销单品页中展示的手机的信息
eleAllP = driver.find_element_by_xpath("//div[@class='span-968 fl']")
eveP = eleAllP.find_elements_by_xpath('.//a[@class="thumb"]')
# 遍历热销单品页面的所有手机的名字和价格
for e in eveP:
    phone_name = e.find_element_by_xpath('.//div[@class="grid-title"]').text
    phone_money = e.find_element_by_xpath('.//p[@class="grid-price"]').text
    print("爆款：{}，价格：{}".format(phone_name, phone_money))
driver.quit()
