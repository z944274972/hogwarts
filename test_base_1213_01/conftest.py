# -*- coding: utf-8 -*-
# @Time     :  2020/12/13 15:28
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  conftest.py
import pytest

# scope作用域，session，多文件共享，conftest只能存在于包下
# 参数使用params传入，传参必须使用request，使用参数必须使用request.param
# 适用于return
# @pytest.fixture(scope="session",params=[10,20])
# def myfixture(request):
#     print("执行我的fixture")
#     return request.param*2


# 适用于yield
# @pytest.fixture(scope="session",params=[10,20])
# def myfixture_yield(request):
#     print("执行我的fixture")
#     yield request.param*2
#     print("结束")

# autouse,不用调用也可使用，谨慎使用
# @pytest.fixture(scope="session",autouse=True)
# def myfixture_auto():
#     print("执行我的fixture")
#     yield
#     print("结束")

# yield无返回
@pytest.fixture(scope="module")
def myfixture_None():
    print("执行我的fixture")
    yield
    print("结束")



# pytest-rerunfailures  失败重试插件
# 执行方式 pytest --reruns  5 --reruns-delay 1  重试5次 延迟一秒
# 对单个用例执行的方法 @pytest.mark.flaky(reruns=5,reruns_delay=1)


# pytest-assume多重校验
#使用方法 pytest.assume(1==2)


# pytest-xdist  pytest -n 3 执行

# pytest,mark.run(order=1)  装饰器
# pytest-ording