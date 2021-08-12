# -*- coding:utf-8 -*-
"""
@author:jingchen.li
@file: 递归函数.py
@date: 2020/10/11 21:26
"""


"""
递归函数:在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
必须有一个明确的结束条件；
每次进入更深一层递归时，问题规模相比上次递归都应有所减少
相邻两次重复之间有紧密的联系，前一次要为后一次做准备（通常前一次的输出就作为后一次的输入）。
递归效率不高，递归层次过多会导致栈溢出（在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，
递归调用的次数过多，会导致栈溢出）
"""
# 计算1到100之间相加之和；通过循环和递归两种方式实现
# 循环方式


def f1(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    print(sum)


# 递归方式
def recu(n):
    if n > 0:
       return n + recu(n-1)
    else:
       return 0


# 尾递归,计算1到100之间相加之和
def recu1(n, count):
    if n > 0:
        return recu1(n-1, count+n)
    else:
        return count


def wrecu(n):
    return recu1(n, 0)


# 使用递归方式实现阶乘：n=7
# 普通递归
def func1(n):
    if n == 1:
        return 1
    else:
        return n * func1(n-1)


# 尾递归
def fact1(n):
    return fact_iter(n, 1)


def fact_iter(num, total):
    if num == 1:
        return total
    return fact_iter(num - 1, num * total)


# 作业
alist = [[3, 5, 8], 10, [[13, 14, ], 15, 18], 20]
# 使用 递归函数 打印 alist所有元素


def homework(list_a):
    for i in list_a:
        if type(i) == list:
            homework(i)
        else:
            print(i)


# 使用 递归函数 求 alist所有元素 的 和
def homework2(b_list):
    sum = 0
    for i in b_list:
        if type(i) == list:
            sum += homework2(i)
        else:
            sum += i
    return sum


if __name__ == '__main__':
    a = homework2(alist)
    print(a)
