# -*- coding:utf-8 -*-
"""
@author:jingchen.li
@file: 字典推导式.py
@date: 2020/10/14 21:59
"""


mcase = {'a': 10, 'b': 34, 'y': 7, 'Z': 3}


# 使用推导式将mcase字典的key全部换成大写
def homework():
    h_mcase = {k.upper(): v for k, v in mcase.items()}
    print(h_mcase)


# 使用推导式将mcase字典中 value大于9的键值对提取出来
def homework1():
    h_mcase = {k: v for k, v in mcase.items() if v > 9}
    print(h_mcase)


if __name__ == '__main__':
    homework1()
