# -*- coding: utf-8 -*-
# @Time     :  2020/12/20 14:42
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  test_add_member.py
import pytest

from test_selenium_1220_01.test_web_weixin.page.main_page import MainPage


class TestAddMember:

    def setup_class(self):
        self.main = MainPage()

    def teardown_class(self):
        self.main.quit()

    # 参数化使用
    def teardown(self):
        self.main.back_main()

    def test_add_member(self):

        '''添加成员测试用例'''

        member = self.main.goto_add_member().add_member().get_member()

        assert "赫敏4" in member

    @pytest.mark.parametrize("accid,phone,expect",[("xxx3","13112345612",'该帐号已被“admin231”占有'),("xx4","13112345622",'该手机已被“admin231”占有')])
    def test_add_member_fail(self,accid,phone,expect):

        member = self.main.goto_add_member().add_member_fail(accid,phone)
        assert expect in member


    # def test_add_member_by_contact(self):


    #     member = self.main.goto_contact().goto_add_member().add_member().get_member()
    #     assert "admin3" in member
    def test_add_member_by_contact(self):
        """通过通讯录页面添加成员
        :return:
        """
        res = self.main.goto_contact().goto_add_member().add_member().get_member()
        assert "赫敏4" in res
