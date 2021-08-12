# -*- coding:utf-8 -*-
"""
@author:jingchen.li
@file: filter筛选函数.py
@date: 2020/10/09 22:19
"""


"""
filter按条件过滤,将元素在方法中执行,返回结果为True的保留下来。
返回的结果是 filter 对象, 可以使用list函数转换成list对象
filter(function, 数据)
"""


def f1():
    # 求大于2的元素
    result = filter(lambda x: x > 2, [1, 2, 3, 4])
    print(type(result))
    print(list(result))


v3 = [11, 22, 33, 'asd' ,44, 'xf']


def fun1(i):
    if type(i) == int:
        return True
    return False


def f2():
    result = filter(fun1, v3)
    print(list(result))  # [11,22,33,44]
    # 简化做法
    result = filter(lambda x: True if type(x) == int else False, v3)
    print(list(result))


# 求列表中的偶数
def f3():
    result = filter(lambda x: True if type(x) == int and x % 2 == 0 else False, v3)
    print(list(result))


# 简单写法
def f4():
    # 求列表中的数字
    print(list( filter(lambda x: type(x) == int, v3)))
    # 求列表中的 偶数
    print(list( filter(lambda x: type(x) == int and x % 2 == 0, v3)))


# 字段过滤
def f5():
    salaries = {'egon': 3000, 'alex': 100000000, 'wupeiqi': 10000, 'yuanhao': 2000}
    # 大于10000的键值对
    res = filter(lambda k: salaries[k] >= 10000, salaries)
    print(list(res))

    info = [
        {'name': 'egon', 'age': '18', 'salary': '3000'},
        {'name': 'wxx', 'age': '28', 'salary': '1000'},
        {'name': 'lxx', 'age': '38', 'salary': '2000'}
    ]
    # 工资大于1000 的字典
    res2 = filter(lambda x: int(x['salary']) > 1000, info)
    print(list(res2))


if __name__ == '__main__':
    f3()
