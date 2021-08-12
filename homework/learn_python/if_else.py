# -*- coding:utf-8 -*-
"""
@author:jingchen.li
@file: if_else.py
@date: 2020/09/28 20:21
"""


# 判断输入的边长能否构成三角形，如果能则计算出三角形的周长(三角形组成条件:两边之长大于第三边)
def trj_jud():
    a = float(input("请输入三角形的第一个边长:"))
    b = float(input("请输入三角形的第二个边长:"))
    c = float(input("请输入三角形的第三个边长:"))
    if a + b > c and a + c > b and b + c > a:
        print("这三个数能构成三角形，周长为{}".format(a + b + c))
    else:
        print("这三个数不能构成三角形")


# 如果输入的成绩在90分以上（含90分）输出A
# 80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
def num_jud():
    a = float(input("请输入你要判断的数字："))
    if a >= 90:
        print("A")
    elif 80 <= a < 90:
        print("B")
    elif 70 <= a < 80:
        print("C")
    elif 60 <= a < 70:
        print("D")
    elif a < 60:
        print("E")


# a = int(input("请输入你要判断的数字："))
def to_be_di():
    a = float(input("请输入你要判断的整数数字："))
    if a % 2 == 0:
        if a % 3 == 0:
            print("这个数能被2和3整除")
        else:
            print("这个数能被2整除但是不能被3整除")
    elif a % 3 == 0:
        print("这个数能被3整除但是不能被2整除")
    else:
        print("这个数不能被2和3整除")


if __name__ == '__main__':
    # trj_jud()
    # num_jud()
    to_be_di()
