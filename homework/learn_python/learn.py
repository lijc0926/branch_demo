#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 21:46
# @Author  : jingchen
# @File    : learn.py

# ```python
#201206_第9次课编程题
#梳理编程思路
#1.把老虎的类建好
#2.把羊的类建好
#3.把房间的类建好
#4.把老虎或羊放入房间
#5.写游戏的相关代码
class Tiger:
    def __init__(self):
        self.name='老虎'
        self.weight=200

    def eat(self,food):
        if food=='meat':
            print('喂食正确,体重+10')
            self.weight+=10
        elif food=='grass':
            print('喂食错误,体重-10')
            self.weight-=10

    def roar(self):
        print('Wow!!')
        self.weight-=5


class Sheep:
    def __init__(self):
        self.name='羊'
        self.weight=100
    def eat(self,food):
        if food=='grass':
            print('喂食正确,体重+10')
            self.weight+=10
        elif food=='meat':
            print('喂食错误,体重-10')
            self.weight-=10
    def roar(self):
        print('mie~~')
        self.weight-=5

#新建一个房间的类
from random import randint
class Room:
    def __init__(self,category):
        self.category=category

roomlist=[]  #新建一个列表,等下用来放10个房间的实例
for i in range(1,11):
    if randint(1,2)==1:
        category=Tiger()  #实例化一个老虎
    else:
        category=Sheep()  #实例化一个羊
    rm=Room(category)  #将动物放入房间的实例中
    roomlist.append(rm)  #将房间的实例放到列表中

import time
start_time=time.time()  #返回当前时间距离1970年1月1日的秒数
while time.time()-start_time<=180:
    num1=randint(0,9)
    fangjian=roomlist[num1]  #随机选择一个房间
    a=input(f'当前访问的是{num1+1}号房间,请问是否需要敲门?Y/N')
    if a=='Y' or a=='y':
        fangjian.category.roar()  #调用房间中的动物实例的叫的方法

    b=input('请问是否需要喂食Y/N')
    if b=='Y' or b=='y':
        food=input('请输入需要喂的食物meat/grass')
        if food=='meat' or food=='grass':
            fangjian.category.eat(food)  #调用房间中的动物实例的吃的方法
        else:
            print('食物种类不正确')
else:
    print('游戏时间到')
    for i in range(len(roomlist)):
        print(f'{i+1}号房间的动物是{roomlist[i].category.name},体重是{roomlist[i].category.weight}')

#思考题,打印所有200以内的质数
# ```

