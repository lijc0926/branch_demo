# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : d使用cookie模拟登录.py
# @ide     : PyCharm
# @time    : 2020/12/21 21:02
import time
import pprint
from selenium import webdriver

# 创建浏览器驱动对象，这里是打开浏览器
driver = webdriver.Chrome(r"D:\pythonfile\homework\driver_folder\chromedriver.exe")
# 访问网址
driver.get("http://127.0.0.1:8088/")

# cookieSli = [{'domain': '127.0.0.1',
#               'httpOnly': False,
#               'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436',
#               'path': '/',
#               'secure': False,
#               'value': '1608555739'},
#              {'domain': '127.0.0.1',
#               # 'expiry': 1640091739,
#               'httpOnly': False,
#               'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436',
#               'path': '/',
#               'secure': False,
#               'value': '1608555739'},
#              {'domain': '127.0.0.1',
#               # 'expiry': 1640091738,
#               'httpOnly': True,
#               'name': 'beegosessionID',
#               'path': '/',
#               'secure': False,
#               'value': '06263987180ed7d51bc9f7014b31f03e'}]
#
# # 先清除所有的cookie
# driver.delete_all_cookies()
# for cookie in cookieSli:
#     # 添加 cookie
#     driver.add_cookie(cookie)
# time.sleep(4)
# driver.refresh()

driver.find_element_by_name("username").send_keys("libai")
driver.find_element_by_name("password").send_keys("opmsopms123")
driver.find_element_by_css_selector("button").click()
print(driver.get_cookies())

"""
关于ui自动化登录的问题
    1、若权限足够，则申请服务端权限，读取验证码
    2、也可以在权限足够的情况下，去修改服务端验证码的值
    3、若权限不足，则请开发将测试环境的验证码校验取消（此刻输入任何内容都能通过
    4、测试环境设置一个万能验证码
    需要注意的是，第三四种方法，必须在上线后，修正
"""
