# -*- coding:utf-8 -*-
"""
@author:jingchen.li
@file: 列表推导式.py
@date: 2020/10/13 21:24
"""


# 列表推导式
# 推导式（又称解析器），是 Python 独有的一种特性。使用推导式可以快速生成列表、元组、字典以及集合类型的数据
# ，因此推导式又可细分为列表推导式、元组推导式、字典推导式以及集合推导式
"""
a_range = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
b_list = [x * x for x in a_range if x % 2 == 0]
print(b_list)
"""


# 使用列表推导式生成一个[0,5,10,15,20,…50]的列表
def homework():
    a_list = [x for x in range(51) if x % 5 == 0]
    return a_list


# 使用列表推导式生成一个[page1,page2,page3…page10]的列表
def homework2():
    b_list = ['page' + str(i) for i in range(1, 11)]
    return b_list


if __name__ == '__main__':
    a = homework()
    print(a)
