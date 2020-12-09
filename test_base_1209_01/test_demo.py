# -*- coding: utf-8 -*-
# @Time     :  2020/12/9 20:37
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_demo.py

import pytest
class Test_demo:
    def test_one(self):

        a = 5
        b =1
        assert a!=b
        print("第一个测试用例")


if __name__ == '__main__':
    pytest.main(["-s","-q"])