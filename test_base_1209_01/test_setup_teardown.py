# -*- coding: utf-8 -*-
# @Time     :  2020/12/9 21:02
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_setup_teardown.py




import pytest

# def setup_module():
#     print("module:整个test模块开始只执行 一次")
#
# def teardown_module():
#     print("module:整个test模块结束执行 一次")


class TestClass2():



    def test_one(self):
        print("class2------>one")

class TestClass():

    # 类级别
    def setup_class(self):
        print("setup_Class:类开始执行一次")

    def teardown_class(self):
        print("teardown_class:类结束执行一次")

    # 方法级别
    def setup_method(self):
        print("setup:每个用例开始执行")

    def teardown_method(self):
        print("teardown:每个用例结束执行")

    def test_one(self):
        print("one")

    def test_two(self):
        print("two")

if __name__ == '__main__':
    pytest.main(["-s"])