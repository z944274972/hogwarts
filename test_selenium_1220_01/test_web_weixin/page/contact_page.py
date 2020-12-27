# -*- coding: utf-8 -*-
# @Time     :  2020/12/20 14:40
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  contact_page.py
import time

from selenium.webdriver.common.by import By

from test_selenium_1220_01.test_web_weixin.page.base_page import BasePage


class ContactPage(BasePage):
    _location_member_list = (By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
    _location_goto_add_member= (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _location_add = (By.CSS_SELECTOR,".member_colLeft_top_addBtnWrap")
    _location_add_party = (By.CSS_SELECTOR,".js_create_party")

    def goto_add_member(self):
        '''添加成员'''
        from test_selenium_1220_01.test_web_weixin.page.add_member_page import AddMember
        self.wait_click(self._location_goto_add_member)
        self.find(self._location_goto_add_member).click()
        return AddMember(self.driver)

    def get_member(self):
        '''获取成员列表'''
        time.sleep(1)
        elements = self.finds(*self._location_member_list)
        member_list = [i.get_attribute("title") for i in elements]
        return member_list


        # time.sleep(2)
        # member_list = self.finds(*self._location_member_list)
        # name_list = []
        # for vaule in member_list:
        #     name_list.append(vaule.get_attribute("title"))
        # return name_list

    def add_party(self):
        '''添加部门'''
        from test_selenium_1220_01.test_web_weixin.page.add_party_page import AddParty
        self.find(self._location_add).click()
        self.find(self._location_add_party).click()
        return AddParty(self.driver)





