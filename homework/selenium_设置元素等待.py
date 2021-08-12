#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 20:28
# @Author  : jingchen
# @File    : selenium_设置元素等待.py


import time
# 设置元素定位使用哪种方法
from selenium.webdriver.common.by import By
# 元素等待
from selenium.webdriver.support.ui import WebDriverWait
# 提供条件判断函数
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver

driver = webdriver.Chrome("D:\pythonfile\homework\driver_folder\chromedriver.exe")

driver.get("https://m.weibo.cn/")


driver.find_element_by_class_name("m-text-cut").click()
# 显示等待，直到某个元素出现，才进行下一步，元素不出现，默认等待0.5s，直到最大等待时间到了，还不出现，就抛出异常
# WebDriverWait(driver, 10, 0.5)
WebDriverWait(driver, 5, 0.5).until(EC.visibility_of_element_located((By.XPATH, "//h4[@class='m-text-cut' and contains(text(),'微博')]")))
# 然后点击元素
driver.find_element_by_xpath("//h4[@class='m-text-cut' and contains(text(),'微博')]").click()

WebDriverWait(driver, 5, 0.5).until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='card card11']/div/div[@class='card-list'])[1]/div")))

elelist = driver.find_elements_by_xpath("(//div[@class='card card11']/div/div[@class='card-list'])[1]/div")
for ele in elelist:
    # 对元素进行xpath定位操作的时候要加上.
    imgeleList = ele.find_elements_by_xpath(".//span[@class='m-link-icon']")
    if imgeleList:
        eleImg = imgeleList[0].find_element_by_tag_name('img')
        eleText = eleImg.get_attribute('src')
        if "hot" in eleText:
            textType = "热"
            text = ele.find_element_by_xpath(".//span[@class='main-text m-text-cut']").text
            print(f"{text}:{textType}")
        elif "fei" in eleText:
            textType = "沸"
            text = ele.find_element_by_xpath(".//span[@class='main-text m-text-cut']").text
            print(f"{text}:{textType}")
        elif "jian" in eleText:
            textType = "荐"
            text = ele.find_element_by_xpath(".//span[@class='main-text m-text-cut']").text
            print(f"{text}:{textType}")
        elif "new" in eleText:
            textType = "新"
            text = ele.find_element_by_xpath(".//span[@class='main-text m-text-cut']").text
            print(f"{text}:{textType}")
# 强制等待
time.sleep(6)


# 隐式等待，页面所有元素加载出之后，进行下一步
#  隐式等待之后所有的元素都要进行隐式等待的十秒
# driver.implicitly_wait(10)
driver.quit()
