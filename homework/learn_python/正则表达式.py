#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 20:01
# @Author  : jingchen
# @File    : 正则表达式.py


import re
a = "123sdgkfuhkahg"
print(re.findall("s(.*)g", a))
