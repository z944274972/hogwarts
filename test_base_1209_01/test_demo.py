# !/usr/bin/env python
# @Time    : 2021/2/5 09:43
# @Author  : zhang yu xin
# @Python  : 3.7.5
# @File    : test_demo
# @Project : hogwarts

import pytest
class TestDemo:

    def setup_class(self):
        print("计算开始")

    def teardown_class(self):
        print("计算结束")

    def test_add(self):
        assert 1 == 0

if __name__ == '__main__':
    pytest.main()