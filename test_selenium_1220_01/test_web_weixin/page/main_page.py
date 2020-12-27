# -*- coding: utf-8 -*-
# @Time     :  2020/12/20 14:38
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  main_page.py
from selenium.webdriver.common.by import By

from test_selenium_1220_01.test_web_weixin.page.add_member_page import AddMember
from test_selenium_1220_01.test_web_weixin.page.base_page import BasePage
from test_selenium_1220_01.test_web_weixin.page.contact_page import ContactPage


class MainPage(BasePage):

    _location_add_member = (By.CSS_SELECTOR,".ww_indexImg_AddMember")
    _location_contact = (By.ID, "menu_contacts")
    def goto_add_member(self):
        '''跳转至添加成员界面'''

        self.find(*self._location_add_member).click()
        return AddMember(self.driver)

    def goto_contact(self):
        '''跳转到通讯录界面'''
        self.find(*self._location_contact).click()
        return ContactPage(self.driver)

    def back_main(self):

        self.find(By.ID, "menu_index").click()
        self.find(By.CSS_SELECTOR, "a[node-type='cancel'").click()