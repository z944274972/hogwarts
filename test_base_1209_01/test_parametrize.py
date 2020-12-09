# -*- coding: utf-8 -*-
# @Time     :  2020/12/9 20:37
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_parametrize.py

import pytest


def add_function(a, b):
    return a + b


class Test_demo:

    # ids的意义为用例的别名
    @pytest.mark.parametrize("a,b,expected",[(1,2,3),(4,5,9),(1,3,4)],ids=("1","2","3"))
    def test_one(self,a,b,expected):

        assert add_function(a,b)==expected

    @pytest.mark.parametrize("b", [0,1,6])
    @pytest.mark.parametrize("a",[0,1,5])
    def test_add(self,a,b):
        print("测试数据组合：a->%s,b->%s" %(a,b))

if __name__ == '__main__':
    pytest.main(["-s","-q"])