# -*- coding:utf-8 -*-
"""
@author:jingchen.li
@file: 异常处理2.py
@date: 2020/10/12 20:44
"""


def ex2():
    try:
        a = int(input("输入被除数："))
        b = int(input("输入除数："))
        c = a / b
        print("您输入的两个数相除的结果是：", c)
    except ValueError:
        print("程序发生了数字格式异常")
    except ArithmeticError:
        print("程序发生了算术异常")
    except:
        print("未知异常")
    print("程序继续运行")


# 捕获异常
def ex3():
    try:
        1 / 0
    except Exception as e:  # 访问异常的错误编号和详细信息
        print(e.args)
        print(str(e))
        print(repr(e))


# 抛出异常
def ex4():
    a1 = input("输入名字(2-5位)：")
    if len(a1) < 2:
        raise ValueError("名字小于2位")
    elif len(a1) > 5:
        raise ValueError("名字大于5位")
    else:
        print('已输入')


# 作业
def homework():
    try:
        a = int(input("输入被除数："))
        b = int(input("输入除数："))
        c = a / b
        print("您输入的两个数相除的结果是：", c)
    except ValueError:
        print("程序发生了数字格式异常")
    except ArithmeticError:
        print("程序发生了算术异常")
    except:
        print("未知异常")
    print("程序继续运行")
# 1当 a输入test 时 控制台输出:程序：发生了数字格式异常
# 2当 a输入1 ,b输入0 时 控制台输出：程序发生了算术异常


if __name__ == '__main__':
    ex4()
