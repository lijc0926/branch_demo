# -*- coding:utf-8 -*-
"""
@author:jingchen.li
@file: lambda.py
@date: 2020/10/09 21:12
"""


def max_demo():
    alist = [-9, -8, 1, 3, -4, 6]    # 求最大值
    print(max(alist))
    # 求绝对值的最大值
    tmp = max(alist, key=lambda x: abs(x))
    print(tmp)


salaries = {'egon': 3000, 'alex': 100000000, 'wupeiqi': 10000, 'yuanhao': 2000}

info = [
    {'name': 'egon', 'age': '18', 'salary': '3000'},
    {'name': 'wxx', 'age': '28', 'salary': '4000'},
    {'name': 'lxx', 'age': '38', 'salary': '2000'}
]


def get(k):
    return salaries[k]


def max_demo2():
    # 求salaries中工资最高的人
    print(max(salaries, key=get))
    # 'alex'
    print(max(salaries, key=lambda x: salaries[x]))
    # 求info中工资最高的人
    print(max(info, key=lambda dic: int(dic['age'])))


def max_demo3():
    # 求salaries中工资最低的人
    print(min(salaries, key=get))
    print(min(salaries, key=lambda x: salaries[x]))
    # 求info中工资最低的人
    print(min(info, key=lambda dic: int(dic['salary'])))


def sorted_demo():
    key_up = sorted(salaries)
    # 默认按照字典的键排序
    print(key_up)
    up = sorted(salaries, key=lambda x:salaries[x])
    # 默认是升序排
    print(up)
    down = sorted(salaries, key=lambda x:salaries[x], reverse=True)
    # 降序
    print(down)
    l = sorted(info, key=lambda dic: int(dic['salary']))
    print(l)


def map_demo():
    v1 = [11, 22, 33, 44]
    # 将元素的每个值加100
    result = map(lambda x: x + 100, v1)
    # 第一个参数为执行的函数,第二个参数为可迭代元素.
    print(list(result))  # [111,122,133,144]
    names = ['alex', 'wupeiqi', 'yuanhao', 'egon']
    # 给名字做拼接
    res = map(lambda x: x+'_A' if x == 'egon' else x + '_B', names)
    print(list(res))


def homework():
    blist = [1, 2, 3, 4, 5, 6, 7]
    # 使用匿名函数取出blist 列表中的偶数
    (lambda l: [print(i) for i in l if i % 2 == 0])(blist)
    # 使用匿名函数将blist 列表中的元素加10
    res = map(lambda l: l+10, blist)
    print(list(res))


# 十月八日作业
def homework1():
    info = [
        {'name': 'egon', 'age': '18', 'salary': '3000'},
        {'name': 'wxx', 'age': '28', 'salary': '1000'},
        {'name': 'lxx', 'age': '38', 'salary': '2000'}
    ]
    # 求info中年龄最大的人
    max_res = max(info, key=lambda x: int(x['salary']))
    print(max_res)
    # 求info中年龄最小的人
    min_res = min(info, key=lambda x: int(x['salary']))
    print(min_res)
    # 给info中的数据按年龄从小到大排序
    sor_res = sorted(info, key=lambda c: int(c['age']))
    print(sor_res)
    # 给info中每个人的工资加1000
    sum_res = map(lambda x: int(x['salary'])+1000, info)
    print(list(sum_res))


# 十月九日作业



if __name__ == '__main__':
    # max_demo()
    homework1()
    # a = get('egon')
    # print(a)
