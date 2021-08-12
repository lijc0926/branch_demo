# -*- coding:utf-8 -*-
"""
@author:jingchen.li
@file: for循环.py
@date: 2020/10/02 19:14
"""


# for循环
# 求 1到50之间的偶数和
def oushu_sum():
    sum = 0
    for i in range(1, 51):
        if i % 2 == 0:
            sum += i
    print(sum)


# 求 1到100之间的奇数和
def qishu_sum():
    sum = 0
    for i in range(1, 51):
        if i % 2 != 0:
            sum += i
    print(sum)


#  3. 使用for 循环,打印出 1到100之间 能被3 和 5 整除的数字
def shuzi_3_5_sum():
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            print(i)


#    4.使用for 循环,打印出 1到100之间 能被3 和 5 整除的数字,打印4个数字后就停止循环
def shuzi_3_5_4_sum():
    j = 0
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            print(i)
            j += 1
        if j > 3:
            break


if __name__ == '__main__':
    # oushu_sum()
    # qishu_sum()
    # shuzi_3_5_sum()
    shuzi_3_5_4_sum()
