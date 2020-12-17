# -*- coding: utf-8 -*-
# @Time     :  2020/12/9 21:25
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_calculator.py

import pytest
import yaml
import os
import allure
from test_base_1209_01.pythoncode.calculator import  Calculator




def get_datas(path,data=None,ids=None):
    with open(path) as f:
        datas = yaml.safe_load(f)
        if ids == None:
            add_datas = datas[data]
            add_ids =None
        if data ==None:
            add_datas = None
            add_ids = datas[ids]
        return  [add_datas,add_ids]

class TestCalculator:

    def setup_class(self):
        self.cal = Calculator()
        print("计算开始")

    def teardown_class(self):
        print("计算结束")

    @allure.feature("加法")
    @allure.title("加法case")
    @pytest.mark.parametrize("a,b,expected", get_datas("yaml/cal.yml","add")[0],ids=get_datas("yaml/cal.yml",ids="myid")[1])
    def test_add(self,a,b,expected,myfixture):
        with allure.step("进行加法计算"):
            assert expected ==myfixture.add(a,b)

    @allure.feature("减法")
    @allure.title("减法case")
    @pytest.mark.parametrize("a,b,expected", get_datas("yaml/cal.yml","jian")[0],ids=get_datas("yaml/cal.yml",ids="myid_jian")[1])
    def test_jia(self, a, b, expected,myfixture):
        with allure.step("进行减法计算"):
            assert expected == myfixture.jian(a, b)

    @allure.feature("乘法")
    @allure.title("乘法case")
    @pytest.mark.parametrize("a,b,expected", get_datas("yaml/cal.yml","cheng")[0],ids=get_datas("yaml/cal.yml",ids="myid_cheng")[1])
    def test_cheng(self,a,b,expected,myfixture):
        with allure.step("进行乘法计算"):
            assert expected ==myfixture.cheng(a,b)

    @allure.feature("除法")
    @allure.title("除法case")
    @pytest.mark.parametrize("a,b,expected", get_datas("yaml/cal.yml","chu")[0],ids=get_datas("yaml/cal.yml",ids="myid_chu")[1])
    def test_chu(self,a,b,expected,myfixture):
        with allure.step("进行除法计算"):
            assert expected ==myfixture.chu(a,b)



if __name__ == '__main__':
    pytest.main(["-s","-q","--alluredir","./result"])
    os.system("allure generate ./result -o ./report --clean")
    os.system("allure open -h 127.0.0.1 -p 8883 ./report")
    # pytest.main(["-sq"])

