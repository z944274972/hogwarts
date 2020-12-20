# -*- coding: utf-8 -*-
# @Time     :  2020/12/20 14:27
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_index.py
from test_selenium_1220_01.po_object_demo.page.index_page import IndexPage


class TestIndex:

    def setup_class(self):
        self.index_page = IndexPage()

    def test_login(self):
        self.index_page.goto_login().login_scanf()

    def test_register(self):
        self.index_page.goto_register().register()