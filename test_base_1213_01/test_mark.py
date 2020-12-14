# -*- coding: utf-8 -*-
# @Time     :  2020/12/13 14:11
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_mark.py



import pytest

class Test_Demo:

    @pytest.mark.demo
    def test_demo(self):
        print("我的第一个测试用例")

    @pytest.mark.demo
    @pytest.mark.smoke
    def test_demo2(self):
        print("我的第二个测试用例")

if __name__ == '__main__':
    pytest.main()