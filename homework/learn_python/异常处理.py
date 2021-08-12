# -*- coding:utf-8 -*-
"""
@author:jingchen.li
@file: 异常处理.py
@date: 2020/10/11 21:50
"""


# try except
def try_demo():
    try:
        num = 5/0
    except Exception as e:
        print('除数异常{}'.format(e))


# try/except…else
def try_demo1():
    try:
        num = 5/2
    except:
        print('除数异常')
    else:
        print('未发生异常')


# finally
def try_demo11():
    try:
        num = 5/2
    except:
        print('除数异常')
    else:
        print('未发生异常')
    finally:
        print('finally分支')


# 作业
def homework(a, b):
    try:
        num = a/b
    except:
        print('除数异常')
    else:
        print('未发生异常')
    finally:
        print('finally分支')
# try_demo1(1,2): 控制台输出(未发生异常，finally分支)
# try_demo1(1,0): 控制台输出(除数异常)


if __name__ == '__main__':
    try_demo()
