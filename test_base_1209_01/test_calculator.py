# -*- coding: utf-8 -*-
# @Time     :  2020/12/9 21:25
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_calculator.py

import pytest
from pythoncode.calculator import Calculator
import yaml

class TestCalculator:


    def setup_class(self):
        self.cal = Calculator()
        print("计算开始")

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,expected",yaml.safe_load(open("./yaml/cal.yal")))
    def test_add(self,a,b,expected):
        assert expected ==self.cal.add(a,b)

    @pytest.mark.parametrize("a,b,expected", [(1, 2, -1), (1, 3, -2)])
    def test_jia(self, a, b, expected):
        assert expected == self.cal.jian(a, b)

    @pytest.mark.parametrize("a,b,expected",[(1,2,2),(1,3,3)])
    def test_cheng(self,a,b,expected):
        assert expected ==self.cal.cheng(a,b)

    @pytest.mark.parametrize("a,b,expected",[(1,2,0.5),(1,4,0.25)])
    def test_chu(self,a,b,expected):
        assert expected ==self.cal.chu(a,b)


if __name__ == '__main__':
    pytest.main(["-sq"])