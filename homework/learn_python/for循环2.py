# -*- coding:utf-8 -*-
"""
@author:jingchen.li
@file: for循环2.py
@date: 2020/10/02 19:27
"""


def distenct():
    # list去重
    alist = [3, 2, 1, 5, 4, 4,5]
    blist= []
    for i in alist:
        if i not in blist:
            blist.append(i)
    print(blist)    # 去重方式 2
    s = set(alist)
    print(s)


# list 转 字典 , 索引作为key , 索引对应的值 作为 value
def list_dict():
    alist = [3, 2, 1, 5, 4, 4, 5]
    adict={}
    for i in range(len(alist)):
        v = alist[i]
        adict[i] = v
    print(adict)


# 请使用for循环遍历列表的方式
# 求出两个列表的 交集(两个列表都包含的元素)
# 和 差集(alist中有的元素blist中没有 和 blist中有的元素alist中没有 的元素)
def homework_1():
    alist = ['哈', '楼', 4, 5, 1, 2, 3]
    blist = ['哈', '楼', 'wo', 'de', 1, 2, 3]
    intersection = []
    dif_set = []
    for i in alist:
        if i in blist:
            intersection.append(i)
    for j in alist:
        if j not in blist:
            dif_set.append(j)
    for p in blist:
        if p not in alist:
            dif_set.append(p)
    print("两个列表的交集为{}".format(intersection))
    print("两个列表的差集为{}".format(dif_set))


if __name__ == '__main__':
    # distenct()
    # list_dict()
    homework_1()
