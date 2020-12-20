# -*- coding: utf-8 -*-
# @Time     :  2020/12/20 14:42
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_add_member.py
from test_selenium_1220_01.test_web_weixin.page.main_page import MainPage


class TestAddMember:

    def setup_class(self):
        self.main = MainPage()


    def test_add_member(self):

        '''添加成员测试用例'''

        member = self.main.goto_add_member().add_member().get_member()
        assert "admin231" in member

    def test_add_member_by_contact(self):

        self.main.goto_contact().add_member()