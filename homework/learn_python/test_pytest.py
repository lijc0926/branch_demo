#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 20:20
# @Author  : jingchen
# @File    : test_pytest.py

import pytest

class Test1(object):

    @pytest.fixture(scope='module', )
    def test_01(self):
        assert 1 == 2


# if __name__ == '__main__':
#     pytest.main(["D:\pythonfile\homework\test_pytest.py"])
