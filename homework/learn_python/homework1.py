#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 22:11
# @Author  : jingchen
# @File    : homework1.py


import math


class Triangle(object):
    """
    求三角形的周长和面积
    """
    def __init__(self, side_length1, side_length2, side_length3):
        """
        :param side_length1: 三角形的第一个边长
        :param side_length2: 三角形的第二个边长
        :param side_length3: 三角形的第三个边长
        """
        self.side_length1 = side_length1
        self.side_length2 = side_length2
        self.side_length3 = side_length3

    def perimeter(self):
        """
        计算三角形的周长
        :return: 返回三角形的周长
        """
        per = self.side_length3 + self.side_length2 + self.side_length1
        return int(per)

    def area(self):
        """
        计算三角形的面积
        :return: 返回三角形的面积
        """
        # 三角形一半的周长
        half_per = self.perimeter()/2
        print(half_per)
        # 海伦公式
        s = (half_per*(half_per-self.side_length1)*(half_per-self.side_length2)*(half_per-self.side_length3)) ** 0.5
        return s


if __name__ == '__main__':
    tri = Triangle(3, 3, 3)
    print(tri.perimeter())
    print(tri.area())
