# -*- coding: utf-8 -*-
# @Time     :  2021/1/9 13:21
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_search.py

from test_frame_0110_01.app import App

class TestSearch:

    def setup(self):
        self.app=App()

    def test_search(self):

        res = self.app.start().goto_main().goto_market().goto_search().search()
        assert res==True