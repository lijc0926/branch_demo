# -*- coding:utf-8 -*-
"""
@author:jingchen.li
@file: while_file.py
@date: 2020/09/29 20:43
"""
import random


# 计算机出一个1~100之间的随机数，人输入自己猜的数字，计算机给出对应的提示信息，直到人猜出计算机出的数字
def number_jud():
    answer = random.randint(1, 100)
    counter = 0
    while True:
        counter += 1
        number = int(input('请输入: '))
        if number < answer:
            print('你的数字得再大一点')
        elif number > answer:
            print('你的数字得在小一点')
        else:
            print('恭喜你猜对了!')
            break
    print('你总共猜了%d次' % counter)


#  2.使用while 循环,打印出 1到100之间 能被3 和 5 整除的数字
def number_3_5_jude():
    i = 1
    while i <= 100:
        if i % 3 == 0 or i % 5 == 0:
            print(i)
        i += 1


# 3. 使用while 循环,打印出 1到100之间 能被3 和 5 整除的数字,打印4个数字后就停止循环
def number_3_5_4_jude():
    i = 1
    p = 0
    while i <= 100 and p <= 3:
        if i % 3 == 0 or i % 5 == 0:
            p += 1
            print(i)
        i += 1


if __name__ == '__main__':
    number_3_5_4_jude()
