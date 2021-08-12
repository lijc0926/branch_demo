# -*- coding:utf-8 -*-
"""
@author:jingchen.li
@file: practice_练习.py
@date: 2020/10/02 19:40
"""
"""
篮子拿鸡蛋
有一篮鸡蛋
每次拿 4 个 最后剩1个,
每次拿5个剩4个,
每次拿6个 最后剩3个,
每次拿7个最后剩5个,
每次拿8个最后剩1个,
每次拿9个 刚好拿完, 篮子最多放1000个鸡蛋,求有多少鸡蛋
"""


def egg():
    num = 0
    while True:
        num += 1
        if num % 4 == 1 and num % 5 == 4 and num % 6 == 3 and num % 7 == 5 and \
                num % 8 == 1 and num % 9 == 0:
            print(num)
            break


# 输入两个数字,并求两个数之间的偶数和
def two_num_oushu_sum():
    num1 = int(input("请输入第一个数字："))
    num2 = int(input("请输入第二个数字："))
    sum = 0
    if num1 > num2:
        for i in range(num2, num1 + 1):
            if i % 2 == 0:
                sum += i
    elif num2 > num1:
        for i in range(num1, num2 + 1):
            if i % 2 == 0:
                sum += i
    elif num1 == num2:
        print("这两个数相等")
    print(sum)


# 判断是否是质数/素数
def sushu():
    num = int(input("请输入一个正整数："))
    num2 = int(num/2 + 1)
    if num <= 1 or num <= 2 or num == 0:
        print("这几个数不在质数的判断范围内")
    else:
        a = False
        for i in range(2, num2):
            if num % i == 0:
                a = True
                print("这个数不是质数")
        if not a:
            print("这个数是质数")


if __name__ == '__main__':
    # egg()
    # two_num_oushu_sum()
    sushu()
