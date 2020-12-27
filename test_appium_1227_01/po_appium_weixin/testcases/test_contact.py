# -*- coding: utf-8 -*-
# @Time     :  2020/12/27 19:52
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_contact.py
from test_appium_1227_01.po_appium_weixin.page.app import App



class TestAddMember:

    def test_add_member(self):
        app = App()
        app.start()
        res = app.goto_main().goto_contact().click_add_member().add_member_manual().add_contact()
        assert res==True