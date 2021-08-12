# -*- coding:utf-8 -*-
"""
@author:jingchen.li
@file: 类和对象.py
@date: 2020/10/15 21:20
"""


class Car(object):

    def __init__(self, name, no, speed):
        self.name = name
        self.no = no
        self.speed = speed

    def show(self):
        """
        :return: 输出每一个属性的值
        """
        print(self.name)
        print(self.no)
        print(self.speed)

    def start(self, ):
        """
        启动，speed=100，输出车名，启动了
        :return:
        """
        if self.speed == 100:
            print("{}启动了".format(self.name))

    def run(self):
        """
        行驶，输出车名和当前速度
        :return:
        """
        print("{}行驶速度是{}".format(self.name, self.speed))

    def stop(self):
        """
        刹车，speed=0，输出车名，刹车当前速度
        :return:
        """
        if self.speed == 0:
            print('{}刹车了'.format(self.name))


if __name__ == '__main__':
    car = Car('宝马', 1, 0)
    car.show()
    car.start()
    car.run()
    car.stop()
