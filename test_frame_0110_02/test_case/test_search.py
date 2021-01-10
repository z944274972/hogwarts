# -*- coding: utf-8 -*-
# @Time     :  2021/1/9 13:21
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_search.py



from test_frame_0110_02.base_page import BasePage
from test_frame_0110_02.page.main import Main


class TestSearch:

    def setup(self):
        basepage = BasePage()
        self.app=Main(basepage)

    def test_search(self):

        res = self.app.goto_market().goto_search().search()
        assert res==True