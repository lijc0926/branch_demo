# -*- coding:utf-8 -*-
"""
@author:jingchen.li
@file: reduce.py
@date: 2020/10/09 22:14
"""

from functools import reduce

"""
reduce函数
reduce() 函数会对参数序列中元素进行累积。
"""
v1 = ['wo', 'hao', 'e']
v2 = [1, 2, 3]


def func(x, y):
    return x+y


def redus_demo():
    r1 = reduce(func, v1)
    print(r1)
    # wohaoe
    r2 = reduce(lambda x, y: x+y, v1)
    print(r2)
    # wohaoe


def redus_demo2():
    r3 = reduce(lambda x, y: x + y, v2)
    print(r3)

    r4 = reduce(lambda x, y: x * y, v2)
    print(r4)


# 计算0到100的和
def redus_demo3():
    # 计算0到100的和
    print( reduce(lambda x, y: x + y, range(101)) )


if __name__ == '__main__':
    redus_demo3()
