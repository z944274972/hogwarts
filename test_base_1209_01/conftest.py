# -*- coding: utf-8 -*-
# @Time     :  2020/12/13 15:28
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  conftest.py
import pytest

from test_base_1209_01.pythoncode.calculator import Calculator


@pytest.fixture(scope="module")
def myfixture():
    print("开始执行")
    cal = Calculator()
    yield cal
    print("结束执行")

