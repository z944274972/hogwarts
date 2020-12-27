# !/usr/bin/env python
# @Time    : 2020/12/21 16:10
# @Author  : zhang yu xin
# @Python  : 3.7.5
# @File    : test_add_party
# @Project : hogwarts
from test_selenium_1220_01.test_web_weixin.page.main_page import MainPage


class TestAddMember:

    def setup_class(self):
        self.main = MainPage()

    def teardown_class(self):
        self.main.quit()

    def test_add_party(self):

        '''添加部门测试用例'''

        party_list = self.main.goto_contact().add_party().add_party()

        assert "zhuolang" in party_list