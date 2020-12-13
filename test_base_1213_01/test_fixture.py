# -*- coding: utf-8 -*-
# @Time     :  2020/12/13 15:22
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_fixture.py


import pytest




class Test_Demo():

    # 方法级别使用fixture，只需要把fixture方法名进行传参,fixture可以放入conftest下
    # 适用于return，获取返回参数直接使用方法名myfixture接收即可
    # def test_one(self,myfixture):
    #     print("执行test1")
    #     print(myfixture)
    #     assert 1+1==2

    # 适用于yield，可以使用参数名接收yield返回，如果无返回，可以使用下面test——three
    # def test_two(self,myfixture_yield):
    #     print(myfixture_yield)
    #     assert 1+1==2

    # 适用于yield无返回的
    # @pytest.mark.usefixtures("myfixture_None")
    # def test_three(self):
    #     print("执行test3")
    #     assert 1+1==2

    # 失败重跑
    @pytest.mark.flaky(reruns=2,delay=1)
    def test_four(self):
        # 断言失败继续执行
        pytest.assume(1==2)
        pytest.assume(2==2)


if __name__ == '__main__':
    pytest.main(["-sq"])