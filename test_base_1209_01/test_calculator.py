# -*- coding: utf-8 -*-
# @Time     :  2020/12/9 21:25
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_calculator.py

import pytest
import yaml
import allure
import os
from test_base_1209_01.pythoncode.calculator import  Calculator



class TestCalculator:

    def setup_class(self):
        self.cal = Calculator()
        print("计算开始")

    def teardown_class(self):
        print("计算结束")

    @allure.feature("加法")
    @allure.title("加法case")
    @pytest.mark.parametrize("a,b,expected",yaml.safe_load(open("./yaml/cal.yal"))["add"])
    def test_add(self,a,b,expected):
        with allure.step("进行加法计算"):
            assert expected ==self.cal.add(a,b)

    @allure.feature("减法")
    @allure.title("减法case")
    @pytest.mark.parametrize("a,b,expected", yaml.safe_load(open("./yaml/cal.yal"))["jian"])
    def test_jia(self, a, b, expected):
        with allure.step("进行减法计算"):
            assert expected == self.cal.jian(a, b)

    @allure.feature("乘法")
    @allure.title("乘法case")
    @pytest.mark.parametrize("a,b,expected", yaml.safe_load(open("./yaml/cal.yal"))["cheng"])
    def test_cheng(self,a,b,expected):
        with allure.step("进行乘法计算"):
            assert expected ==self.cal.cheng(a,b)

    @allure.feature("除法")
    @allure.title("除法case")
    @pytest.mark.parametrize("a,b,expected", yaml.safe_load(open("./yaml/cal.yal"))["chu"])
    def test_chu(self,a,b,expected):
        with allure.step("进行除法计算"):
            assert expected ==self.cal.chu(a,b)


if __name__ == '__main__':
    pytest.main(["-s","-q","--alluredir","./result"])
    os.system("allure generate ./result -o ./report --clean")
    os.system("allure open -h 127.0.0.1 -p 8883 ./report")